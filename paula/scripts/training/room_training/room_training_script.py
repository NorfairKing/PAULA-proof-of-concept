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


from . import room_training_script_config as conf

"""
The roomtraining script.
"""

def execute(operand):
    """
    The master method for the roomtraining script
    @param operand:
    """
    exercise = inputs.get_item_from_list(conf.ROOM_TRAINING_OPTIONS)
    week = inputs.get_integer_in_range(1,conf.WEEKS_PER_EXERCISE,prompt="Week: ")
    day = inputs.get_integer_in_range(1,conf.DAYS_PER_WEEK,prompt="day: ")
    difficulty_level = inputs.get_item_from_list(conf.DIFFICULTY_LEVELS)
    rest, workout_list = get_training_scheme(exercise,week,day,difficulty_level)
    debug("scheme= " + str((rest,workout_list)))
    coach(rest,workout_list)


def get_training_scheme(exercise,week,day,difficulty_level):
    """
    Get's the training scheme for a given exercise, week, day and difficulty level
    @param exercise: A string representing an exercise.
    @param week: An integer representing a week in the training.
    @param day: An integer representing the day of the week.
    @param difficulty_level: A string representing a difficulty level.
    @return: A tuple with the amount of rest between each set, and a list of reps in the sets.
    """
    debug("Loading " + exercise + " script")
    week_module = "paula.scripts.training.room_training.resources." + exercise + ".week_" + str(week)
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
    """
    Coaches the given scheme.
    @param rest: The amount of rest between each set.
    @param workout_list: The list of reps in the sets.
    @return:
    """
    for w in workout_list:
        interaction.say(str(w) + " repetitions, Sir.",sync=True)
        interaction.say("Let me know when you are done, Sir")
        if not inputs.get_boolean():
            interaction.say("Done, Sir?")
            if inputs.get_boolean():
                debug("Exiting.")
                return
        if not conf.DEBUG:
            interaction.say("Take a Break, Sir.")
            time.sleep(rest)
    interaction.say("Well done, Sir.")


def debug(string):
    """
    Prints debug info if debug is toggled on.
    @param string: The info to print.
    """
    if conf.DEBUG:
        outputs.print_debug(string)