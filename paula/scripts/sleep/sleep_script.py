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

import datetime
from paula.sleep import sleep
from paula.core import inputs
from paula.core import interaction
from paula.music import song
from paula.music import system_volume
from paula.motivation import quote
from paula.agenda import agenda


"""
Goes through a sleep routine for the user..
"""

from paula.scripts.script import Script


class SleepScript(Script):
    def execute(self, operand):
        interaction.say("How long would you like to sleep, Sir?")

        option = inputs.get_item_from_dict(self.get_config('DURATION_OPTIONS'))

        # select song
        interaction.say("Please select which song you want to wake you up.")
        s = song.choose()

        interaction.say_from_file(self.get_resource_path('night.paula_says'), sync=True)

        # Set volume to something pleasant
        system_volume.set(self.get_config('PLEASANT_WAKE_UP_VOLUME'))

        # Sleep
        sleep.go_to_sleep_mode(int(option))

        # Alarm go off
        interaction.say_from_file(self.get_resource_path('morning.paula_says'), sync=True)
        now = datetime.datetime.now()
        hour_min = 'It is %H:%M'
        if now.hour < 9:
            hour_min += "in the morning."
        interaction.say(now.strftime(hour_min), sync=True)

        month_day = "We are the %-d"
        day = now.day
        if day in self.get_config('DAY_SUFFIXES').keys():
            month_day += self.get_config('DAY_SUFFIXES')[day]
        else:
            month_day += "th"
        month_day += ' %B %Y'
        interaction.say(now.strftime(month_day), sync=True)

        subp = s.play()
        answer = inputs.get_string_timeout(self.get_config('WAKE_UP_TIME'))

        if not answer:
            # Wait until the song has finished
            subp.wait()

        try:
            subp.kill()
        except ProcessLookupError:
            pass

        interaction.say_from_file(self.get_resource_path('up.paula_says'))

        # Show quote
        print((str(quote.get_random())))

        # Get agenda for next few days
        agenda.print_default()
