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
The configurations file for the configurations package... IKR!
"""

import os
from paula import config as conf

DEBUG = False

PAULA_CONFIG_DIR = os.path.dirname(os.path.realpath(__file__))
RESOURCES_DIR = os.path.join(PAULA_CONFIG_DIR, 'resources')

CONFIG_DIR_NAME = 'config'
PAULA_USER_CONFIG_DIR = os.path.join(conf.PAULA_STATE_DIR, CONFIG_DIR_NAME)

CONFIG_EXTENSION = '.cfg'

GLOBAL_CONFIG_NAME = 'global'
PAULA_GLOBAL_CONFIG_FILE = os.path.join(PAULA_USER_CONFIG_DIR, GLOBAL_CONFIG_NAME + CONFIG_EXTENSION)
PAULA_GLOBAL_CONFIG_FILE_TEMPLATE = os.path.join(conf.PAULA_DIR, 'global_config_template')

DEBUG_SECTION = 'Debug'
DEBUG_OPTION = 'debug'


