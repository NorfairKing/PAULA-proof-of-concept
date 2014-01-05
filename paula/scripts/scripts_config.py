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
The configurations for the scripts package.
"""

import os

DEBUG = True

# How long PAULA waits after a script is done.
WAITING_TIME = 1

# The default package where the scripts are housed (this package)
DEFAULT_PARENT = "paula.scripts."
# The directory where the scripts are housed (this directory)
DEFAULT_SCRIPTS_DIR = os.path.dirname(os.path.realpath(__file__))

DEFAULT_RESOURCE_DIR_NAME = 'resources'
DEFAULT_CONFIG_FILE_NAME = 'default_config_file'
CONFIG_SUFFIX = "_config"