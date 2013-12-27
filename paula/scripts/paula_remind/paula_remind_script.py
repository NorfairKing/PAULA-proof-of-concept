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

from paula.core import outputs
from paula.core import interaction
from paula.core import inputs
from paula.core import schedule
from paula.core import parse
from paula.core import exceptions

from . import paula_remind_script_config as conf


def execute(operand):
    debug("Reminding " + operand)

    interaction.say("Sir, " + operand, sync=True)

    response = inputs.get_string_timeout(conf.TIME_OUT)
    if not response:
        reschedule(operand)

    if interaction.means(response, "okay"):
        return
    elif interaction.means(response, "not_okay"):
        debug("Reminding again in one day.")
        reschedule_str = inputs.get_string("Schedule again in: ")
        try:
            delta = parse.time_delta(reschedule_str)
        except exceptions.PAULA_Parse_Exception as e:
            outputs.print_error(str(e.__class__))
        schedule.schedule_event_with_delta(delta, "paula_remind", operand)
    else:
        reschedule(operand)

def debug(string):
    if conf.DEBUG:
        outputs.print_debug(string)

def reschedule(reminder):
    delta = parse.time_delta(conf.AUTO_RESCHEDULE)
    schedule.schedule_event_with_delta(delta,"paula_remind",reminder)
    return