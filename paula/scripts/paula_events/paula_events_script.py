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

import importlib

from paula.core import outputs
from paula.scripts import script

from . import paula_events_script_config as conf

def execute(operand):
    script.decide_and_run(operand,'.paula_events')

def debug(string):
    if conf.DEBUG:
        outputs.print_debug(string)
