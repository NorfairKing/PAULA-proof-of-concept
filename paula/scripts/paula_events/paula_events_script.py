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

from paula.core import inputs
from paula.core import outputs
from paula.core import interaction

from . import paula_events_script_config as conf

def execute(operand):
    if not operand:
        debug("Empty operand.")
        subscript = inputs.get_item_from_list(conf.OPTIONS)
    else:
        subscript = operand.split()[0]
    module = load_script(subscript)
    debug("executing" + str(module) + " with \""+  operand + "\" as operand.")
    module.execute(operand)

def load_script(name):
    debug("Loading " + name + "script")
    script = "paula.scripts.paula_events." + name
    try:
        module = importlib.import_module(script)
    except ImportError:
        outputs.print_error(
            "The " + script + " script is missing or does not exist. Either that or some import fails inside the script.")
        return

    outputs.clear()
    return module


def debug(string):
    if conf.DEBUG:
        outputs.print_debug(string)