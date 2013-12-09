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
import time
import importlib
from . import script_config as conf

def decide_and_run(string):
    meaning = decide_meaning(string)
    print_PAULA()
    execute(meaning)
    time.sleep(conf.WAITING_TIME)

def execute(meaning):
    try:
        module_name = "paula.scripts." + meaning + "." + meaning + "_script"
        module = importlib.import_module(module_name)
        module.execute()
    except ImportError:
        print("ERROR: The " + meaning + " script is missing or does not exist")

def decide_meaning(string):
    global meanings
    meanings = get_scripts_dict()
    meaning_found = "None"
    for name in meanings:
        if means(string, name):
            meaning_found = meanings[path]
            break
    if conf.DEBUG:
        print("decided  " + string + " to mean " + meaning_found + ".")
    return meaning_found

def get_meaning_regexes(meaning):
    return [i.strip() for i in open(meanings[meaning]).readlines()]

def means(string, meaning):
    if not meaning in meanings:
        return False

    regexes = get_meaning_regexes(meaning)

    print(regexes)

    for reg_str in regexes:

        if conf.IGNORE_CASING:
            reg = re.compile("^" + reg_str + "$", re.IGNORECASE)
        else:
            reg = re.compile(reg_str)

        if reg.match(string):
            return True
    return False

def get_scripts_dict():
    dict = {}

    import paula.scripts
    scripts_dir = os.path.dirname(os.path.abspath(paula.scripts.__file__))
    for script in os.listdir(scripts_dir):
        to_be_checked = os.path.join(scripts_dir,script)
        if os.path.isdir(to_be_checked) and not to_be_checked.__contains__("__pycache__"):
            script_dir = os.path.join(scripts_dir,script)
            commands = os.path.join(script_dir, "script_commands")
            if os.path.isfile(commands):
                dict[script] = commands

    return dict

def get_meaning_regexes(path):
    return [i.strip() for i in open(path).readlines()]

def print_PAULA():
    print("""
      ____   _   _   _ _        _
     |  _ \ / \ | | | | |      / \
     | |_) / _ \| | | | |     / _ \
     |  __/ ___ \ |_| | |___ / ___ \
     |_| /_/   \_\___/|_____/_/   \_\\


 Personal
 Artificial
 Unintelligent
 Life
 Assistant

""")