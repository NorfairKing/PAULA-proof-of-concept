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
#5
##

"""
Goes through the goingout sequence.
"""

from paula.scripts.script import Script
from paula.sleep import sleep
from paula.core import inputs
from paula.core import parse
from paula.core import speech


class GoingOutScript(Script):
    def execute(self, operand):
        speech.say("How long do you think you will be gone, Sir?")

        answer = inputs.get_string()
        delta = parse.time_delta(answer)
        speech.say_all_from_file(self.get_resource_path('greetings.paula_says'), sync=True)

        sleep.go_to_sleep_mode(delta.seconds)

        answer = inputs.get_string_timeout(self.get_config('WAITING_TIME'))

        if not answer:
            sleep.go_to_sleep_mode(0)
        else:
            speech.say("Welcome back, Sir")
