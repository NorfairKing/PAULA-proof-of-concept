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
import shutil
import configparser

from paula.core import outputs
from paula.core import exceptions
from paula.core import interaction

from . import paula_config_config as conf


def get_config(package, config_option):
    """
    Get's the value of a given config option in a given package.
    @param package: The name of the package.
    @param config_option: The name of the config option.
    """
    config_file = os.path.join(conf.PAULA_USER_CONFIG_DIR, package + conf.CONFIG_EXTENSION)

    if not os.path.exists(config_file):
        raise exceptions.PAULAMissingConfigFileException

    debug("Getting \"" + config_option + "\" in package \"" + config_file + "\".")

    config_parser = configparser.ConfigParser()
    config_parser.read(config_file)

    return config_parser.get('Configurations', config_option)


def get_global(section, config_option):
    """
    Get's the value of a given global config option.
    @param section: The section of the config file to look in
    @param config_option: The name of the config option.
    """

    if not os.path.exists(conf.PAULA_GLOBAL_CONFIG_FILE):
        debug('making: \"' + conf.PAULA_GLOBAL_CONFIG_FILE + '\"')
        shutil.copyfile(conf.PAULA_GLOBAL_CONFIG_FILE_TEMPLATE, conf.PAULA_GLOBAL_CONFIG_FILE)

    debug("Getting global option \"" + config_option + "\" in section \"" + section + "\".")

    config_parser = configparser.ConfigParser()
    config_parser.read(conf.PAULA_GLOBAL_CONFIG_FILE)

    return config_parser.get(section, config_option)


def get_global_debug():
    """
    Gets whether the global debug is toggled on.
    @return: True if it is toggled on, False if it is toggled off, None if it does not have any useful value.
    """
    debug_str = get_global(conf.DEBUG_SECTION, conf.DEBUG_OPTION)
    if interaction.means(debug_str, 'yes'):
        return True
    elif interaction.means(debug_str, 'no'):
        return False
    else:
        return None


def debug(string):
    """
    Prints a given debug string if debug is toggled on.
    @param string: The given debug string.
    """
    if conf.DEBUG:
        outputs.print_debug(string)