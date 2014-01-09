#!/usr/bin/env python
##
#      ____   _   _   _ _        _
#     |  _ \ / \ | | | | |      / \
#     | |_) / _ \| | | | |     / _ \
#     |  __/ ___ \ |_| | |___ / ___ \
#     |_| /_/   \_\___/|_____/_/   \_\
#
#
# Personal
# Artificial
# Unintelligent
# Life
# Assistant
#
##

"""
The script class. Every one of PAULA's scripts will be a subclass of this class?
"""

import os
import importlib
from abc import ABCMeta, abstractmethod

from paula.core import outputs
from paula.core import config
from paula.core.exceptions import PAULAUnknownConfigException
from . import scripts_config as conf


class Script(object):
    """
    A class of scripts to be run from a script controller.
    """
    __metaclass__ = ABCMeta

    def __init__(self):
        """
        Initializes all values of this script.
        """
        self.module_name = self.__module__
        rest, self.name = self.module_name.rsplit('.', 1)
        rest, self.package_name = rest.rsplit('.', 1)
        self.relative_package = '.'.join(self.module_name[len(conf.DEFAULT_PARENT):].rsplit('.')[:-1])
        self.directory = os.path.join(conf.DEFAULT_SCRIPTS_DIR,
                                      self.relative_package.replace(".", "/")) #TODO this is pretty hard coded.
        configfile = self.__module__ + conf.CONFIG_SUFFIX
        self.config_module = importlib.import_module(configfile)
        self.resources_dir = os.path.join(self.directory, conf.DEFAULT_RESOURCE_DIR_NAME)

        self.check_config()

    @abstractmethod
    def execute(self, operand):
        """
        Execute this script with a given operand.
        @param operand: The given operand.
        """

    def debug(self, string):
        """
        Print a given string if DEBUG is toggled on, either in this script, or globally.
        @param string: The given string.
        """
        if self.get_debug():
            outputs.print_debug(string)

    def get_config(self, config_option):
        """
        Get a value from the configuration file of this script.
        @param config_option: The name of the config option to search for.
        @return The value of the given config option. This doesn't have to be a string.
        @raise PAULAUnknownConfigException: If there doesn't exist a config option with the given file.
        """
        try:
            value = getattr(self.config_module, config_option)
        except AttributeError:
            raise PAULAUnknownConfigException
        return value

    def get_debug(self):
        """
        Returns whether debug is toggled on or off.
        @return: True if debug is toggled on.
        """
        return conf.GLOBAL_SCRIPT_DEBUG or self.config_module.DEBUG

    def get_user_config(self, config_option):
        """
        Get a user configuration option with a given name.
        @param config_option: The name of the given configuration option.
        @return: The value of the given configuration option. This is always a string.
        """
        return config.get_config(self.name, config_option)

    def get_global_config(self, section, config_option):
        """
        Get a user configuration that is global for PAULA.
        @param section: The section of the config file to look in.
        @param config_option: The name of the config option
        @return: The value of the given configuration option. This is always a string.
        """
        return config.get_global(section, config_option)

    def get_resource_path(self, resource):
        """
        Get's a given resource from the resources folder of this script.
        @param resource: The name of the given resource
        @return: An absolute path to the given resource in string format.
        """
        return os.path.join(self.resources_dir, resource)

    def check_config(self):
        """
        Check if a config file exists, if not, check if one has to be made, if so, do so.
        """
        default_config_file = os.path.join(self.resources_dir, conf.DEFAULT_CONFIG_FILE_NAME)
        if os.path.exists(default_config_file):
            config.make_default_config_file_if_nonexistent(self.name, default_config_file)