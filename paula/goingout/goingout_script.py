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
import signal
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

    
    # <unknown code>
    class TimeoutException(Exception): 
        pass 
 
    def timeout(timeout_time, default):
        def timeout_function(f):
            def f2(*args):
                def timeout_handler(signum, frame):
                    raise TimeoutException()
 
                old_handler = signal.signal(signal.SIGALRM, timeout_handler) 
                signal.alarm(timeout_time) # triger alarm in timeout_time seconds
                try: 
                    retval = f()
                except TimeoutException:
                    return default
                finally:
                    signal.signal(signal.SIGALRM, old_handler) 
                signal.alarm(0)
                return retval
            return f2
        return timeout_function
 
    @timeout(conf.WAITING_TIME, False)
    def get_response():
        ans = p.get_input_str()
        return True 
    # </unknown code>

    back = get_response()
    
    if not back:
        p.go_to_sleep_mode()
