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

from . import paula_remind_script_config as conf


def execute(operand):
    if conf.DEBUG:
        outputs.print_debug("Reminding " + operand)

    interaction.say(operand, sync=True)

    response = inputs.get_string_timeout(conf.TIME_OUT)
    if interaction.means(response, "okay"):
        return
    elif interaction.means(response, "not_okay"):
        if conf.DEBUG:
            outputs.print_debug("Reminding again in one day.")
        # TODO make this pretty (rescheduling.)
        delta = datetime.timedelta(days=1, seconds=0, minutes=0, hours=0, weeks=0)
        schedule.schedule_event_with_delta(delta, "paula_remind", operand)
    else:
        pass