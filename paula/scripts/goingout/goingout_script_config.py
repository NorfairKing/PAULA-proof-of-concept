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

# Default = False
DEBUG = False

GOING_OUT_SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
RESOURCES_DIR = os.path.join(GOING_OUT_SCRIPT_DIR, 'resources')
GREETINGS_FILE = os.path.join(RESOURCES_DIR, "greetings.paula_says")

# DEFAULT = 2 * 60 * 60
WAITING_TIME = 2 * 60 * 60
