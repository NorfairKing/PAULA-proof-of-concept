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

import sys
import time
import importlib

from paula.core import inputs
from paula.core import outputs
from paula.core import interaction

from . import room_training_script_config as conf

"""
The roomtraining script.
"""

SECONDS_IN_A_MINUTE = 60


def execute(operand):
    """
    The master method for the roomtraining script
    @param operand:
    """
    exercise = inputs.get_item_from_list(conf.ROOM_TRAINING_OPTIONS)
    week = inputs.get_integer_in_range(1, conf.WEEKS_PER_EXERCISE, prompt="Week: ")
    day = inputs.get_integer_in_range(1, conf.DAYS_PER_WEEK, prompt="day: ")
    difficulty_level = inputs.get_item_from_list(conf.DIFFICULTY_LEVELS)
    rest, workout_list = get_training_scheme(exercise, week, day, difficulty_level)
    debug("scheme= " + str((rest, workout_list)))
    coach(exercise, rest, workout_list)


def get_training_scheme(exercise, week, day, difficulty_level):
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

    day = module.SCHEMES[day - 1] #-1 because arrays start at zero.
    rest, difficulties = day
    scheme = (rest, difficulties[difficulty_level])
    return scheme


def coach(exercise, rest_duration, workout_list):
    """
    Coaches the given scheme of the given exercise.
    @param exercise: The given exercise.
    @param rest_duration: The amount of rest between each set.
    @param workout_list: The list of reps in the sets.
    @return:
    """
    for w in workout_list[:-1]:
        interaction.say(str(w) + " " + exercise + ", Sir.")
        if not inputs.get_boolean():
            interaction.say("Done, Sir?")
            if inputs.get_boolean():
                debug("Exiting.")
                return
        if not conf.DEBUG:
            interaction.say_from_file(conf.BREAK_FILE)
            rest(rest_duration)

    interaction.say("For the last set, do at least " + str(workout_list[-1]) + " " + exercise + ", Sir.")
    if not inputs.get_boolean():
        interaction.say("Too bad, Sir.")
        return
    interaction.say_from_file(conf.DONE_FILE)


def rest(duration):
    minutes = duration / SECONDS_IN_A_MINUTE
    seconds = duration % SECONDS_IN_A_MINUTE

    def erase():
        sys.stdout.write('\x1b[1A' + '\x1b[2K') # Go to previous line and erase it.

    def print_time(minute, second):
        erase()
        minute_str = str(int(minute))
        second_str = str(int(second))
        if minute < 10:
            minute_str = "0" + minute_str
        if second < 10:
            second_str = "0" + second_str
        print(conf.CLOCK_PADDING * " " + minute_str + ":" + second_str)

    print_time(minutes,seconds)
    while minutes >= 0:
        while seconds >= 0:
            time.sleep(1)
            print_time(minutes, seconds)
            seconds -= 1
        seconds = SECONDS_IN_A_MINUTE -1
        minutes -= 1
    erase()


def debug(string):
    """
    Prints debug info if debug is toggled on.
    @param string: The info to print.
    """
    if conf.DEBUG:
        outputs.print_debug(string)