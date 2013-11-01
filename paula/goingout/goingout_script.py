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

import time
from paula.paula import Paula
from . import goingout_config as conf

def execute():
    p = Paula()
    
    p.say("How long do you think you will be gone, Sir?")

    SECONDS_IN_A_MINUTE = 60
    MINUTES_IN_AN_HOUR = 60    

    answer = int(p.get_input_str())
    seconds = answer * SECONDS_IN_A_MINUTE * MINUTES_IN_AN_HOUR
    
    if conf.DEBUG:
        print("answer = " + str(answer))
        print("seconds = " + str(seconds))
 
    p.go_to_sleep_mode(seconds)

    back = False
    TIMEOUT = 5
    signal.signal(signal.SIGALRM, get_response)
    signal.alarm(TIMEOUT)
    def get_response():
        try:
            response = input()
            back = True
            return response
        except:
            return None

    if not back:
        p.go_to_sleep_mode()
