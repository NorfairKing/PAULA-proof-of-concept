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

import time
import importlib

from paula.core import inputs
from paula.core import outputs
from paula.core import interaction


from . import training_script_config as conf


def execute(operand):
    exercise = inputs.get_item_from_list(conf.ROOM_TRAINING_OPTIONS)
    week = inputs.get_integer_in_range(1,conf.WEEKS_PER_EXERCISE,prompt="Week: ")
    day = inputs.get_integer_in_range(1,conf.DAYS_PER_WEEK,prompt="day: ")
    difficulty_level = inputs.get_item_from_list(conf.DIFFICULTY_LEVELS)
    rest, workout_list = get_training_scheme(exercise,week,day,difficulty_level)
    debug("scheme= " + str((rest,workout_list)))
    coach(rest,workout_list)


def get_training_scheme(exercise,week,day,difficulty_level):
    debug("Loading " + exercise + " script")
    week_module = "paula.scripts.training.resources." + exercise + ".week_" + str(week)
    debug("importing " + week_module)
    try:
        module = importlib.import_module(week_module)
    except ImportError:
        outputs.print_error("TRAINING FILE MISSING")

    day = module.schemes[day-1] #-1 because arrays start at zero.
    rest, difficulties = day
    scheme = (rest, difficulties[difficulty_level])
    return scheme

def coach(rest, workout_list):
    for w in workout_list:
        interaction.say(str(w) + " repetitions, Sir.")
        answer =  inputs.get_string()
        if interaction.means(answer,"okay"):
            pass
        else:
            interaction.say("Done, Sir?")
            # TODO something in here, this isn't finished yet.
            return
        if not conf.DEBUG:
            interaction.say("Take a Break, Sir.")
            time.sleep(rest)
    interaction.say("Well done, Sir.")


def debug(string):
    if conf.DEBUG:
        outputs.print_debug(string)