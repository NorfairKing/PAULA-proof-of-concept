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
DEBUG = True

# Default = True
IGNORE_CASING = True

# Default = False
MATCH_WHOLE_STRING = False

# Default = os.path.join(os.path.dirname(os.path.realpath(__file__)),'commands')
MEANINGS_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'meanings')
