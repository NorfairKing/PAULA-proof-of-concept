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
The config file for this new package
"""

import os

from paula.core import config

DEBUG = True

NEW_PACKAGE_DIR = os.path.dirname(os.path.realpath(__file__))
RESOURCES_DIR = os.path.join(NEW_PACKAGE_DIR, 'resources')
DEFAULT_CONFIG_FILE = os.path.join(RESOURCES_DIR,'default_config_file')
config.make_default_config_file_if_nonexistent(__package__, DEFAULT_CONFIG_FILE)

PAULA_TEXT_FILE = os.path.join(RESOURCES_DIR,'paula_text.paula_says')

CHECKLISTS_DIR = config.PAULA_STATE_CHECKLISTS_DIR