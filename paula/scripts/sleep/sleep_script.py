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

import signal
from paula.paula import Paula
from paula.music import song
from paula.music import system_volume
from paula.motivation import quote
from paula.agenda import agenda
from . import sleep_script_config as conf

def execute():
    p = Paula()

    p.say("How long would you like to sleep, Sir?")

    printOptions(conf.DURATION_OPTIONS)
    answer = p.get_input_str().strip()
    chosen_option = int(conf.DURATION_OPTIONS[answer])
    
    p.debug("answer = " + answer, conf.DEBUG)
    p.debug("selected option = " + str(chosen_option) + " seconds", conf.DEBUG)
    
    # select song
    p.say("Please select which song you want to wake you up.")
    s = song.choose()

    # Set volume to something pleasant
    system_volume.set(conf.PLEASANT_WAKE_UP_VOLUME)
    
    # Sleep
    p.go_to_sleep_mode(chosen_option)
    
    # Alarm go off
    go_off(p, s)

    p.say("Have a nice day, Sir")
    
    # Show quote
    print((str(quote.get_random())))

    # Get agenda for next few days
    agenda.get_default()

def go_off(p, s):
    subp = s.play()

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

    @timeout(conf.WAKE_UP_TIME, False)
    def get_response():
        ans = p.get_input_str()
        return True
    # </unknown code>

    back = get_response()

    if back:
        subp.kill()

    # Wake up
    p.say("Good morning, Sir")

def printOptions(dic):
    SECONDS_IN_A_MINUTE = 60
    for key in list(dic.keys()):
        spaces = (20-len(key)) * " "
        print(("         " + key + spaces +" - " + str(dic[key] // SECONDS_IN_A_MINUTE) + " min")) 
    print()
    
