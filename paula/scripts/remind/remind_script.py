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
from paula.core import schedule
from . import remind_script_config as conf

def execute(operand):
    # Parsing
    if conf.DEBUG:
        outputs.print_debug("OPERAND = " + operand)

    if not "in" in operand:
        outputs.print_debug("no \"in\", exiting")
        return

    content , moment = operand.split(" in ")

    now = datetime.datetime.now()
    year = now.year
    month = now.month
    day = now.day
    hour = now.hour
    minute = now.minute
    second = now.second
    event_moment = datetime.datetime(year, month, day, hour, minute, second)
    schedule.schedule_event(event_moment,"paula_say", content)