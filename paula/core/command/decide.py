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

# Returns command class for the command
def decide_meaning(string):
    for path in get_meanings_dict():
        print(path," -> ",  get_meaning_regexes(path))
    exit(0)

    meanings = get_meanings_list()
    meaning_found = "UNKNOWN"
    for meaning in meanings:
        if means(string, meaning):
            meaning_found = meaning
            break
    if conf.DEBUG:
        print("decided  " + string + " to mean " + meaning_found + ".")

    return meaning_found


def means(string, meaning):
    meanings = get_meanings_dict()
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


def get_meanings_dict():
    dict = {}

    # Generic meanings
    for f in os.listdir(conf.MEANINGS_DIR):
        if os.path.isfile(os.path.join(conf.MEANINGS_DIR, f)):
            path = os.path.join(conf.MEANINGS_DIR, f)
            dict[path] = f

    # Script commands
    import paula.scripts
    scripts_dir = os.path.dirname(os.path.abspath(paula.scripts.__file__))
    scripts = []
    for f in os.listdir(scripts_dir):
        to_be_checked = os.path.join(scripts_dir,f)
        if os.path.isdir(to_be_checked) and not to_be_checked.__contains__("pycache"):
            scripts.append(f)


    for script in scripts:
        script_dir = os.path.join(scripts_dir,script)
        commands = os.path.join(script_dir, "script_commands")
        if os.path.isfile(commands):
            dict[commands] = script

    return dict


def get_meaning_regexes(path):
    return [i.strip() for i in open(path).readlines()]

