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
The config handling module
"""

import os
import sys
import shutil
import configparser

from . import paula_config_config as conf

from paula.core import outputs


def get_config(package, config_option, default=None):
    """
    Get's the value of a given config option in a given package.
    @param package: The name of the package.
    @param config_option: The name of the config option.
    """
    debug("Getting \"" + config_option + "\" in package \"" + package + "\".")

    config_file = os.path.join(conf.PAULA_USER_CONFIG_DIR, package + conf.CONFIG_EXTENSION)
    debug('config_file= ' + config_file)
    config_parser = configparser.ConfigParser()
    config_parser.read(config_file)

    return config_parser.get(package, config_option)


def get_string_config():
    return "test"


def make_default_config_file_if_nonexistent(package, default_config):
    config_file = os.path.join(conf.PAULA_USER_CONFIG_DIR, package + conf.CONFIG_EXTENSION)
    if not os.path.exists(config_file):
        shutil.copyfile(default_config, config_file)


def this_module():
    modname = globals()['__name__']
    return sys.modules[modname]


def debug(string):
    if conf.DEBUG:
        outputs.print_debug(string)