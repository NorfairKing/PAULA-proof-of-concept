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

SECONDS_IN_A_MINUTE = 60

"""
Roomtraining script.
"""

import sys
import time
import importlib

from paula.scripts.script import Script
from paula.core import inputs
from paula.core import outputs
from paula.core import interaction


class RoomTrainingScript(Script):
    def execute(self, operand):
        """
        The master method for the roomtraining script
        @param operand:
        """
        exercise = inputs.get_item_from_list(self.get_config('ROOM_TRAINING_OPTIONS'))
        week = inputs.get_integer_in_range(1, self.get_config('WEEKS_PER_EXERCISE'), prompt="Week: ")
        day = inputs.get_integer_in_range(1, self.get_config('DAYS_PER_WEEK'), prompt="day: ")
        difficulty_level = inputs.get_item_from_list(self.get_config('DIFFICULTY_LEVELS'))
        rest, workout_list = self.get_training_scheme(exercise, week, day, difficulty_level)
        self.debug("scheme= " + str((rest, workout_list)))
        self.coach(exercise, rest, workout_list)

    def get_training_scheme(self, exercise, week, day, difficulty_level):
        """
        Get's the training scheme for a given exercise, week, day and difficulty level
        @param exercise: A string representing an exercise.
        @param week: An integer representing a week in the training.
        @param day: An integer representing the day of the week.
        @param difficulty_level: A string representing a difficulty level.
        @return: A tuple with the amount of rest between each set, and a list of reps in the sets.
        """
        self.debug("Loading " + exercise + " script")
        week_module = "paula.scripts.training.room_training.resources." + exercise + ".week_" + str(week)
        self.debug("importing " + week_module)
        try:
            module = importlib.import_module(week_module)
        except ImportError:
            outputs.print_error("TRAINING FILE MISSING")

        day = module.SCHEMES[day - 1] #-1 because arrays start at zero.
        rest, difficulties = day
        scheme = (rest, difficulties[difficulty_level])
        return scheme

    def coach(self, exercise, rest_duration, workout_list):
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
                    self.debug("Exiting.")
                    return
            if not self.get_debug():
                interaction.say_from_file(self.get_resource_path('break.paula_says'))
                self.rest(rest_duration)

        interaction.say("For the last set, do at least " + str(workout_list[-1]) + " " + exercise + ", Sir.")
        if not inputs.get_boolean():
            interaction.say("Too bad, Sir.")
            return
        interaction.say_from_file(self.get_resource_path('done.paula_says'))

    def rest(self, duration):
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
            print(self.get_config('CLOCK_PADDING') * " " + minute_str + ":" + second_str)

        print_time(minutes, seconds)
        while minutes >= 0:
            while seconds >= 0:
                time.sleep(1)
                print_time(minutes, seconds)
                seconds -= 1
            seconds = SECONDS_IN_A_MINUTE - 1
            minutes -= 1
        erase()