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
    meaning_found = None
    for meaning in meanings:
        if means(string, meaning):
            meaning_found = meaning
            break
    if conf.DEBUG:
        if meaning_found:
            print("decided  " + string + " to mean " + meaning_found + ".")
        else:
            print("No meaning found.")
    return meaning_found


def means(string, meaning):
    meanings = get_meanings_dict()
    if not meaning in meanings.keys():
        return False

    regexes = get_meaning_regexes(meaning)
    for reg_str in regexes:
        if not conf.MATCH_WHOLE_STRING:
            reg_str += ".*"
        else:
            reg_str = "^" + reg_str + "$"
        if conf.IGNORE_CASING:
            reg = re.compile(reg_str, re.IGNORECASE)
        else:
            reg = re.compile(reg_str)
        if reg.match(string):
            return True
    return False


def get_meanings_dict():
    global meanings_dict
    meanings_dict = {}

    for f in os.listdir(conf.MEANINGS_DIR):
        if os.path.isfile(os.path.join(conf.MEANINGS_DIR, f)):
            path = os.path.join(conf.MEANINGS_DIR, f)
            meanings_dict[f] = path

    return meanings_dict


def get_meaning_regexes(meaning):
    return [i.strip() for i in open(meanings_dict[meaning]).readlines()]
