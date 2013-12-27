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
from .command import decide
from .speak import voice
from .outputs import string
from . import core_config as conf

def decide_meaning(string):
    return decide.decide_meaning(string)


def means(string, meaning):
    return decide.means(string, meaning)


def say(text, sync=False):
    string.print_paula(text)
    return voice.say(text, sync=sync)

def say_from_file(path, sync=False):
    with open(path, 'r') as speech_file:
        lines = speech_file.readlines()
        line = random.choice(lines)
        if conf.DEBUG:
            string.print_debug("Chosen line: " + line)
        say(line,sync=sync)

