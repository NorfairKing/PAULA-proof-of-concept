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

from paula import config

# Default = False
DEBUG = False

NEW_SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
RESOURCES_DIR = os.path.join(NEW_SCRIPT_DIR, 'resources')

OPTIONS = [
    "list"
]