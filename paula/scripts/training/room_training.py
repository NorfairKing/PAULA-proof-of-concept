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
    exercise = inputs.get_item_from_list(['push-ups','sit-ups'])
    week = inputs.get_item_from_list([1,2,3,4,5,6])
    day = inputs.get_item_from_list([1,2,3])
    difficulty_level = inputs.get_item_from_list(conf.DIFFICULTY_LEVELS)
    debug("scheme= " + str(get_training_scheme(exercise,week,day,difficulty_level)))




def get_training_scheme(exercise,week,day,difficulty_level):
    debug("Loading " + exercise + " script")
    week_module = "paula.scripts.training.resources." + exercise + ".week_" + str(week)
    try:
        module = importlib.import_module(week_module)
    except ImportError:
        outputs.print_error("TRAINING FILE MISSING")

    day = module.schemes[day-1] #-1 because arrays start at zero.
    rest, difficulties = day
    scheme = (rest, difficulties[difficulty_level])
    return scheme

def debug(string):
    if conf.DEBUG:
        outputs.print_debug(string)