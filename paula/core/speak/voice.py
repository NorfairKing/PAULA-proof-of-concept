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

from paula.core import system

from . import speak_config as conf


def say(text):
    print(("PAULA:   " + text + "\n"))

    if conf.SOUND_ON:
        bash_command = conf.SPEAK_SCRIPT + ' "' + text + '"'
        if conf.DEBUG:
            system.call(bash_command)
        else:
            system.call_silently(bash_command)