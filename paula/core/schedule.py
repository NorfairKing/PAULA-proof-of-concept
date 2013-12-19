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

from .scheduling import event
from .scheduling import scheduler


def create_event(datetime,command,operand):
    return event.Event(datetime, command, operand)

def schedule_event(datetime, command, operand):
    e = event.Event(datetime, command, operand)
    e.schedule()
    return e

def get_all_events():
    return scheduler.get_all_events()