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
from . import scripts_config as conf


class Script(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        self.module_name = self.__module__
        rest, self.name = self.module_name.rsplit('.', 1)
        rest, self.package_name = rest.rsplit('.', 1)
        self.relative_package = self.module_name[len(conf.DEFAULT_PARENT):].rsplit('.')[0]
        self.directory = os.path.join(conf.DEFAULT_SCRIPTS_DIR, self.relative_package.replace(".", "/")) #TODO this is pretty hard coded.
        configfile = self.__module__ + conf.CONFIG_SUFFIX
        self.config_module = importlib.import_module(configfile)

        self.check_config()

    @abstractmethod
    def execute(self, operand):
        pass

    def debug(self, string):
        if self.config_module.DEBUG:
            outputs.print_debug(string)
        pass

    def get_user_config(self, config_option):
        return config.get_config(self.name, config_option)

    def check_config(self):
        resource_dir = os.path.join(self.directory, conf.DEFAULT_RESOURCE_DIR_NAME)
        default_config_file = os.path.join(resource_dir, conf.DEFAULT_CONFIG_FILE_NAME)
        if os.path.exists(default_config_file):
            config.make_default_config_file_if_nonexistent(self.name, default_config_file)