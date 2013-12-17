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

from paula.sleep import sleep
from paula.core import inputs
from paula.core import outputs
from paula.core import interaction
from . import goingout_script_config as conf


def execute(operand):
    interaction.say("How long do you think you will be gone, Sir?")

    SECONDS_IN_A_MINUTE = 60
    MINUTES_IN_AN_HOUR = 60

    answer = inputs.get_integer()
    if answer == None:
        outputs.print_error("ERROR: Not an Integer")
        return
    seconds = answer * SECONDS_IN_A_MINUTE * MINUTES_IN_AN_HOUR

    if conf.DEBUG:
        outputs.print_debug("answer = " + str(answer))
        outputs.print_debug("seconds = " + str(seconds))

    sleep.go_to_sleep_mode(seconds)

    answer = inputs.get_string_timeout(seconds)

    if answer != "":
        interaction.say("Welcome back, Sir")
    else:
        sleep.go_to_sleep_mode()
