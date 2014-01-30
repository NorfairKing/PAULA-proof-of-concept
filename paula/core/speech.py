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

import random
from .speak import voice
from .outputs import string
from . import core_config as conf


def say(text, sync=False):
    string.print_paula(text)
    return voice.say(text, sync=sync)


def say_all_from_file(path, ordered=True, sync=False):
    with open(path, 'r') as speech_file:
        lines = speech_file.readlines()
    if not ordered:
        random.shuffle(lines)
    for line in lines[:-1]:
        say(line, sync=True)
    say(lines[-1], sync=sync)


def say_random_from_file(path, sync=False):
    with open(path, 'r') as speech_file:
        lines = speech_file.readlines()
        line = random.choice(lines)
        if conf.DEBUG:
            string.print_debug("Chosen line: " + line)
        say(line, sync=sync)

