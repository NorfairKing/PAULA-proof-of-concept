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

# Default = os.path.join(os.path.dirname(os.path.realpath(__file__)),'resources')
RESOURCES_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'resources')

# Default = True
ANNOYING = True
