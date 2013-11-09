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
from . import command_config as conf
from paula.scripts import script as script

# Returns command class for the command
def decide_command(string):
    meanings = get_meanings_list()
    meaning_found = "UNKNOWN"
    for meaning in meanings:
        if means(string,meaning):
            meaning_found = meaning
            break
    if conf.DEBUG:
        print("decided  " + string + " to mean " + meaning_found + ".")
    
    print(meaning_found)
    exit()
    
    return meaning_found

def means(string, meaning):
    meanings = get_meanings_list()
    if not meaning in meanings:
        return False
    
    regexes = get_meaning_regexes(meaning)
    for reg_str in regexes:
        if conf.IGNORE_CASING:
            reg = re.compile("^" + reg_str + "$", re.IGNORECASE)
        else:
            reg = re.compile(reg_str)

        if reg.match(string):
            return True
    return False


def get_meanings_list():
    return [ f for f in os.listdir(conf.MEANINGS_DIR) if os.path.isfile(os.path.join(conf.MEANINGS_DIR,f)) ]

def get_meaning_regexes(meaning):
    return [i.strip() for i in open(os.path.join(conf.MEANINGS_DIR,meaning)).readlines()]
