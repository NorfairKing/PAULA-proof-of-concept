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

from .scheduling import event
from .scheduling import scheduler


def create_event(datetime, command, operand):
    return event.Event(datetime, command, operand)


def create_event_with_delta(timedelta, command, operand):
    create_event(get_rounded_now() + timedelta, command, operand)


def schedule_event(datetime, command, operand):
    e = event.Event(datetime, command, operand)
    e.schedule()
    return e


def schedule_event_with_delta(timedelta, command, operand):
    schedule_event(get_rounded_now() + timedelta, command, operand)


def get_all_events():
    return scheduler.get_all_events()


def get_overdue_events():
    return scheduler.get_overdue_events()


def get_rounded_now():
    now = datetime.datetime.now()
    moment_year = now.year
    moment_month = now.month
    moment_day = now.day
    moment_hour = now.hour
    moment_minute = now.minute
    moment_second = now.second
    now_rounded = datetime.datetime(year=moment_year, month=moment_month, day=moment_day, hour=moment_hour,
                                    minute=moment_minute, second=moment_second)
    return now_rounded