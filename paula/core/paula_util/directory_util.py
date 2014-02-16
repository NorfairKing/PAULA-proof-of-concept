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
The util functions for directories
"""

import os

from paula.core import outputs

from . import paula_util_config as conf


def make_if_nonexistent(path):
    if not os.path.exists(path):
        os.mkdir(path)
        if conf.DEBUG:
            outputs.print_debug("Created " + path + " directory.")