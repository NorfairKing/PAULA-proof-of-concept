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

SLEEP_SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
RESOURCES_DIR = os.path.join(SLEEP_SCRIPT_DIR, 'resources')
MORNING_FILE = os.path.join(RESOURCES_DIR, "morning.paula_says")
NIGHT_FILE = os.path.join(RESOURCES_DIR, "night.paula_says")
UP_FILE = os.path.join(RESOURCES_DIR, "up.paula_says")
ANNOYING_ALARM_TEXT = os.path.join(RESOURCES_DIR, 'annoying')

# A dictionary that maps strings (options) to integers (amounts of seconds)
DURATION_OPTIONS = {
    "short nap": 25 * 60
    , "long nap": 90 * 60
    , "short": 4.5 * 3600 + 5 * 60
    , "medium": 6 * 3600 + 5 * 60
    , "long": 7.5 * 3600 + 5 * 60
    , "very long": 9 * 3600 + 5 * 60
    , "crash": 12 * 3600
}

# Default = 60
PLEASANT_WAKE_UP_VOLUME = 60

# Default = 5 * 60
WAKE_UP_TIME = 5 * 60

# Default = True
ANNOYING = True

DAY_SUFFIXES = {
    1:"st",
    2:"nd",
    3:"rd",
    21:"st",
    22:"nd",
    23:"rd",
    31:"st",
    32:"nd",
    33:"rd",
}