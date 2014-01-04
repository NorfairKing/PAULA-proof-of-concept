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

# Default = False
DEBUG = True

EMAIL_DIR = os.path.dirname(os.path.realpath(__file__))
RESOURCES_DIR = os.path.join(EMAIL_DIR, 'resources')
DEFAULT_CONFIG_FILE = os.path.join(RESOURCES_DIR, 'default_config_file')

config.make_default_config_file_if_nonexistent(__package__, DEFAULT_CONFIG_FILE)

FROM = config.get_config(__package__, 'from')

LOGIN = config.get_config(__package__, 'login')
PASSWORD = config.get_config(__package__, 'password')

SMTP_SERVER = 'smtp.gmail.com:587'

