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

    year=2013
    month=8
    day=4
    hours=12
    minutes=30
    seconds=45

    dt = datetime.datetime(year, month, day, hours, minutes, seconds)
    e = event.Event(dt, "paula_working", "Nothing")
    e.schedule()
    dt = datetime.datetime(year+1, month, day, hours, minutes, seconds)
    e = event.Event(dt, "paula_working", "NOthing2")
    e.schedule()

    print(e.has_passed())

    from paula.core.scheduling import scheduler
    scheduler.get_all_events()



    # </Test here>