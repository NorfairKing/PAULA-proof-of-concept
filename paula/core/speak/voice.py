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

from paula.utils import external

from . import speak_config as conf


def say(text):
    print(("PAULA:   " + text + "\n"))

    if conf.SOUND_ON:
        bash_command = conf.SPEAK_SCRIPT + ' "' + text + '"'
        if conf.DEBUG:
            external.call(bash_command)
        else:
            external.call_silently(bash_command)