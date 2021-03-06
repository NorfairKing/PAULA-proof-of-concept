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
The configuration for the command package.
"""

import os

# Default = False
DEBUG = False

# Default = True
IGNORE_CASING = True

# Default = False
MATCH_WHOLE_STRING = True

# Default = os.path.join(os.path.dirname(os.path.realpath(__file__)),'commands')
MEANINGS_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'meanings')
