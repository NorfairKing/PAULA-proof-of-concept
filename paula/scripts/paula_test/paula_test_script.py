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
from paula.music import song
from paula.core import inputs
from paula.core import outputs
from paula.core import system
import signal

from . import paula_test_script_config as conf


def execute():
    if conf.DEBUG:
        outputs.print_debug("The arguments to execute this script were the following.")
        outputs.print_debug(sys.argv)


    #Write test code here

    song.play_random()

    print(song.get_current_artist())
    print(song.get_current_album())
    print(song.get_current_song())

    outputs.print_error("this is an error message")
    outputs.print_debug("this is a debug message")
    outputs.print_color("YAY","green")

    inputs.get_string()

    song.stop_song()