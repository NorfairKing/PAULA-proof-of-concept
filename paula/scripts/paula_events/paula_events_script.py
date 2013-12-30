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
from paula.core import exceptions
from paula.scripts.script import decide_and_run

from . import paula_events_script_config as conf

def execute(operand):
    decide_and_run(operand,'.paula_events')
    """
    if not operand:
        debug("Empty operand.")
        subscript = inputs.get_item_from_list(conf.OPTIONS)
    else:
        subscript = operand.split()[0]
        if not subscript in conf.OPTIONS:
            return

    try:
        module = load_script(subscript)
    except exceptions.PAULA_Import_Exception as e:
        debug("Unable to load script: " + subscript)
        return

    debug("executing" + str(module) + " with \""+  operand + "\" as operand.")
    module.execute(operand)

def load_script(name):
    debug("Loading " + name + "script")
    script = "paula.scripts.paula_events." + name
    try:
        module = importlib.import_module(script)
    except ImportError:
        raise exceptions.PAULA_Missing_Script_Exception

    outputs.print_PAULA()
    return module
"""

def debug(string):
    if conf.DEBUG:
        outputs.print_debug(string)