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

import sys
from paula.external import youtube
from paula.core import inputs
from paula.core import interaction

def execute():
    interaction.say("Which song would you like to play?")
    arg = inputs.get_string()

    result = youtube.search(arg)

    youtube.play_video(result)