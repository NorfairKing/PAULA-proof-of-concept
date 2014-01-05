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

import os

from paula.core import config

DEBUG = False

HERE = os.path.dirname(os.path.realpath(__file__))

PAULA_TEST_SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
RESOURCES_DIR = os.path.join(PAULA_TEST_SCRIPT_DIR, 'resources')
DEFAULT_CONFIG_FILE = os.path.join(RESOURCES_DIR,'default_config_file')

config.make_default_config_file_if_nonexistent(__package__, DEFAULT_CONFIG_FILE)
