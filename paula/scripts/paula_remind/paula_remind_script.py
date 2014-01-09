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
Documentation for this script.
"""

from paula.scripts.script import Script
from paula.core import outputs
from paula.core import speech
from paula.core import meaning
from paula.core import inputs
from paula.core import schedule
from paula.core import parse
from paula.core import exceptions


class PaulaRemindScript(Script):
    def execute(self, operand):
        self.debug("Reminding " + operand)

        speech.say("Sir, " + operand, sync=False)
        response = inputs.get_string_timeout(self.get_config('TIME_OUT'))
        if not response:
            self.reschedule(operand)

        if meaning.means(response, "okay"):
            return
        elif meaning.means(response, "not_okay"):
            self.debug("Reminding again in one day.")
            reschedule_str = inputs.get_string("Schedule again in: ")
            try:
                delta = parse.time_delta(reschedule_str)
            except exceptions.PAULAParseException as e:
                outputs.print_error(str(e.__class__))

            # fix bash issues again
            operand = operand.replace("\"", "\\\"")
            operand = operand.replace("\'", "\\\'")
            schedule.schedule_event_with_delta(delta, "paula_remind", operand)
        else:
            self.reschedule(operand)

    def reschedule(self, reminder):
        delta = parse.time_delta(self.get_config('AUTO_RESCHEDULE'))
        schedule.schedule_event_with_delta(delta, "paula_remind", reminder)
