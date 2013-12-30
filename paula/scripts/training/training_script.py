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
The Training script
"""

import importlib

from paula.core import inputs
from paula.core import outputs

from . import training_script_config as conf


def execute(operand):
    answer = inputs.get_item_from_list(conf.TRAINING_OPTIONS)
    module = load_script(answer)

    outputs.print_PAULA()
    module.execute(operand)


def load_script(name):
    module_name = "paula.scripts.training." + name + "." + name + "_script"
    try:
        module = importlib.import_module(module_name)
    except ImportError:
        outputs.print_error(
            "The " + module_name + " script is missing or does not exist. Either that or some import fails inside the script.")
        return
    return module