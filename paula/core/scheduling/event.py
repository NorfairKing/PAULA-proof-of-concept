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

import os
import datetime

from paula.core import outputs

from . import scheduling_config as conf


class Event:
    def __init__(self, date, command, operand):
        if not isinstance(date, datetime.datetime):
            outputs.print_error("class mismatch: date argument is not a datetime object.")
            exit(1)
        self.date = date
        self.command = command
        self.operand = operand
        self.file = os.path.join(conf.SCHEDULING_DIR, str(self.date))
        if conf.DEBUG:
            outputs.print_debug("Constructed event " + str(self))

    def schedule(self):
        if not os.path.exists(conf.SCHEDULING_DIR):
            os.mkdir(conf.SCHEDULING_DIR)
            if conf.DEBUG:
                outputs.print_debug("Created event directory.")

        event_file = open(self.file, 'w')
        event_file.write(self.command + "\n")
        event_file.write(self.operand)
        event_file.close()
        if conf.DEBUG:
            outputs.print_debug("Scheduled " + self.command + " at " + str(self.date))

    def delete(self):
        if os.path.exists(self.file):
            os.remove(self.file)
            if conf.DEBUG:
                outputs.print_debug("Removed event file " + self.file)

    def is_overdue(self):
        return self.date < datetime.datetime.now()

    def __str__(self):
        return "EVENT: " + str(self.date) + "  COMMAND = " + self.command + "  OPERAND = " + self.operand

    def __lt__(self, other):
        return self.date < other.date


def get_event_from_file(path):
    date = datetime.datetime.strptime(os.path.basename(path), '%Y-%m-%d %H:%M:%S')
    event_file = open(os.path.join(conf.SCHEDULING_DIR, path))
    lines = event_file.readlines()
    cmd = lines[0].strip()
    operand = lines[1].strip()

    e = Event(date, cmd, operand)
    if conf.DEBUG:
        outputs.print_debug("Got event from file " + path + " : " + str(e))

    return e
