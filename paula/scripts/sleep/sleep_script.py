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
from paula.sleep import sleep
from paula.core import inputs
from paula.core import interaction
from paula.music import song
from paula.music import system_volume
from paula.motivation import quote
from paula.agenda import agenda
from . import sleep_script_config as conf

def execute():
    interaction.say("How long would you like to sleep, Sir?")

    printOptions(conf.DURATION_OPTIONS)
    answer = inputs.get_string().strip()
    
    if not answer in conf.DURATION_OPTIONS:
        print("ERROR: Unknown option")
        return
    chosen_option = int(conf.DURATION_OPTIONS[answer])
    
    if conf.DEBUG:
        print("answer = " + answer)
        print("selected option = " + str(chosen_option) + " seconds")
    
    # select song
    interaction.say("Please select which song you want to wake you up.")
    s = song.choose()

    # Set volume to something pleasant
    system_volume.set(conf.PLEASANT_WAKE_UP_VOLUME)
    
    # Sleep
    sleep.go_to_sleep_mode(chosen_option)
    
    # Alarm go off
    interaction.say("Good Morning, Sir")
    
    subp = s.play()
    answer = inputs.get_string_timeout(conf.WAKE_UP_TIME)

    if answer != "":
        subp.kill()
    
    interaction.say("Have a nice day, Sir")
    
    # Show quote
    print((str(quote.get_random())))

    # Get agenda for next few days
    agenda.get_default()

    # Wait until the song has finished
    subp.wait()

    if conf.ANNOYING:
        interaction.say("Sir, You should really get up now!")
        time.sleep(1)
        interaction.say("Don't think you can go back to sleep!")
        time.sleep(1)
        interaction.say("You want to get up")
        interaction.say("You need to get up!")
    

def printOptions(dic):
    SECONDS_IN_A_MINUTE = 60
    for key in list(dic.keys()):
        spaces = (20-len(key)) * " "
        print(("         " + key + spaces +" - " + str(dic[key] // SECONDS_IN_A_MINUTE) + " min")) 
    print()
