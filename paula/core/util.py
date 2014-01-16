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
import inspect

from . import core_config as conf
from paula.core import outputs

def make_dir_if_nonexistent(path):
    if not os.path.exists(path):
        os.mkdir(path)
        if conf.DEBUG:
            outputs.print_debug("Created " + path + " directory.")

def get_caller_module_name():
    # Get calling module
    frm = inspect.stack()[1]
    module = inspect.getmodule(frm[0])
    print(module.__name__)
    file = inspect.getfile(frm[0])
    print(file)