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

from paula.core import schedule

def execute(operand):
    events = schedule.get_all_events()
    print()
    print()
    print("<==============================|Scheduled Events|==============================>")
    print()
    for e in events:
        print(str(e.date) + ": " + e.command + " | " + e.operand)
    print()
    print("<==============================|Scheduled Events|==============================>")
    print()
    print()