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
The configurations for the training script.
"""

import os

DEBUG = False

ROOM_TRAINING_SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
RESOURCES_DIR = os.path.join(ROOM_TRAINING_SCRIPT_DIR, 'resources')
BREAK_FILE = os.path.join(RESOURCES_DIR, 'break.paula_says')
DONE_FILE = os.path.join(RESOURCES_DIR, 'done.paula_says')

ROOM_TRAINING_OPTIONS = [
    'push-ups',
    'sit-ups'
]

# TODO this should be a config, currently it isn't.
DIFFICULTY_LEVELS = [
    'easy',
    'medium',
    'hard'
]

WEEKS_PER_EXERCISE = 6
DAYS_PER_WEEK = 3

CLOCK_PADDING = 10
