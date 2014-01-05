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

from . import core_config as conf
from paula.core import outputs

def make_dir_if_nonexistent(path):
    if not os.path.exists(path):
        os.mkdir(path)
        if conf.DEBUG:
            outputs.print_debug("Created " + path + " directory.")