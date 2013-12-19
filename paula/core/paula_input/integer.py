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
from paula.core import outputs


def prompt_for_input_int(prompt=""):
    value = None
    while not value:
        answer = input(prompt)
        try:
            value = int(answer)
        except ValueError:
            outputs.print_error("Not an Integer")
            value = None
    return value


def prompt_with_timeout(timeout, prompt=""):
    #This is an "Error" thrown when it times out
    class Timeout(IOError):
        pass

    def handler(signum, frame):
        #Cause an error
        raise Timeout()

    try:
        #Set the alarm
        signal.signal(signal.SIGALRM, handler)
        signal.alarm(timeout)

        #Wait for input
        line = prompt_for_input_int(prompt=prompt)

        #If typed before timed out, disable alarm
        signal.alarm(0)
    except Timeout:
        line = None
    return line
