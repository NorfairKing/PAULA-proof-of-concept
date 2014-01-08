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
Goes through the goingout sequence.
"""

from paula.scripts.script import Script
from paula.sleep import sleep
from paula.core import inputs
from paula.core import parse
from paula.core import interaction

class GoingOutScript(Script):
    def execute(self, operand):
        interaction.say("How long do you think you will be gone, Sir?")

        answer = inputs.get_string()
        delta = parse.time_delta(answer)
        interaction.say_from_file(self.get_resource_path('greetings.paula_says'))

        sleep.go_to_sleep_mode(delta.seconds)

        answer = inputs.get_string_timeout(self.get_config('WAITING_TIME'))

        if not answer:
            sleep.go_to_sleep_mode(0)
        else:
            interaction.say("Welcome back, Sir")
