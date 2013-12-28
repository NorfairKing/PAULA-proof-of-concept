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

from . import training_script_config as conf

def execute(operand):
    answer = inputs.get_item_from_list(conf.TRAINING_OPTIONS)

    try:
        answer = "paula.scripts.training." + answer
        module = importlib.import_module(answer)
    except ImportError:
        outputs.print_error(
            "The " + module + " script is missing or does not exist. Either that or some import fails inside the script.")
        return
    outputs.clear()
    module.execute(operand)