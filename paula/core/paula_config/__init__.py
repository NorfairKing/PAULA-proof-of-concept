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
The user configurations module for PAULA
"""

import os

from . import paula_config_config as conf

if not os.path.exists(conf.PAULA_USER_CONFIG_DIR):
    os.mkdir(conf.PAULA_USER_CONFIG_DIR)