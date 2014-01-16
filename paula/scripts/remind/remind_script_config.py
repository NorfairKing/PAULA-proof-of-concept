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

"""
The configurations for the remind script.
"""

DEBUG = False

REPLACEMENTS = {
    "I": "you",
    "I'm": "you're",
    "Im": "you're",
    "my": "your",
    "me": "you",
    "myself": "yourself",
    "mine": "yours",
    "you": "me",
    "your": "my",
    "you're": "I'm",
    "youre": "I'm",
    "yours": "mine",
    "yourself": "myself",
    "then": "now",
}

REMIND_SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
RESOURCES_DIR = os.path.join(REMIND_SCRIPT_DIR, 'resources')
CONFIRMATION_FILE = os.path.join(RESOURCES_DIR, 'confirmation.paula_says')
