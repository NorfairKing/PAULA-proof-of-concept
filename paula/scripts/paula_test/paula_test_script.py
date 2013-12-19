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

from paula.core import outputs

from . import paula_test_script_config as conf


def execute(operand):
    if conf.DEBUG:
        outputs.print_debug("The arguments to execute this script were the following.")
        outputs.print_debug(operand)

    # <Test here>

    import datetime
    from paula.core.scheduling import event

    now = datetime.datetime.now()

    year = now.year
    print(year)
    month = now.month
    print(month)
    day = now.day
    print(day)
    hours = now.hour
    print(hours)
    minutes = now.minute
    print(minutes)
    seconds = now.second
    print(seconds)

    dt = datetime.datetime(year, month, day, hours, minutes, seconds)
    print(str(dt))
    e = event.Event(dt, "paula_working", "Nothing")
    e.schedule()

    from paula.core.scheduling import scheduler

    scheduler.get_all_events()



    # </Test here>