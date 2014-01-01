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
Documentation for the config file.
"""

import os

DEBUG = True

NEW_SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
RESOURCES_DIR = os.path.join(NEW_SCRIPT_DIR, 'resources')
PAULA_TEXT_FILE = os.path.join(RESOURCES_DIR,'paula_text.paula_says')