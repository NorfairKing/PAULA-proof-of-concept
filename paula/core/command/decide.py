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

import os
import re

# Returns command class for the command
from paula.core.command import command_config as conf

def decide_meaning(string):
    meanings = get_meanings_dict()
    meaning_found = "UNKNOWN"
    for path in meanings:
        if means(string, path):
            meaning_found = meanings[path]
            break
    if conf.DEBUG:
        print("decided  " + string + " to mean " + meaning_found + ".")
    return meaning_found


def means(string, path):
    meanings = get_meanings_dict()
    if not path in meanings:
        return False

    regexes = get_meaning_regexes(path)
    for reg_str in regexes:
        if conf.IGNORE_CASING:
            reg = re.compile("^" + reg_str + "$", re.IGNORECASE)
        else:
            reg = re.compile(reg_str)

        if reg.match(string):
            return True
    return False


def get_meanings_dict():
    dict = {}

    # Generic meanings
    for f in os.listdir(conf.MEANINGS_DIR):
        if os.path.isfile(os.path.join(conf.MEANINGS_DIR, f)):
            path = os.path.join(conf.MEANINGS_DIR, f)
            dict[path] = f

    return dict


def get_meaning_regexes(path):
    return [i.strip() for i in open(path).readlines()]

