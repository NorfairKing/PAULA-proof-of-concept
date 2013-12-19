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
from paula.core import outputs
from . import script_config as conf


def decide_and_run(string):
    outputs.print_PAULA()
    meaning, operand = decide_meaning(string)
    try:
        execute(meaning, operand)
    except KeyboardInterrupt:
        if conf.DEBUG:
            outputs.print_debug("Exiting.")
    time.sleep(conf.WAITING_TIME)


def execute(meaning, operand):
    if not meaning:
        return

    try:
        module_name = "paula.scripts." + meaning + "." + meaning + "_script"
        if conf.DEBUG:
            outputs.print_debug("Importing module: " + module_name)
        module = importlib.import_module(module_name)
        module.execute(operand)
    except ImportError:
        outputs.print_error(
            "The " + meaning + " script is missing or does not exist. Either that or some import fails inside the script.")


def decide_meaning(string):
    global meanings
    meanings = get_scripts_dict()
    meaning_found = None
    for name in meanings:
        matched, operand = means(string, name)
        if matched:
            meaning_found = name
            break
    if conf.DEBUG:
        if meaning_found:
            outputs.print_debug("decided  " + string + " to mean " + meaning_found + ".")
        else:
            outputs.print_debug("No meaning found.")
    return meaning_found, operand


def get_meaning_regexes(meaning):
    return [i.strip() for i in open(meanings[meaning]).readlines()]


def means(string, meaning):
    if not meaning in meanings:
        return False, None

    regexes = get_meaning_regexes(meaning)

    matches = []

    for reg_str in regexes:

        reg = re.compile(reg_str, re.IGNORECASE)

        if reg.match(string):
            if conf.DEBUG:
                outputs.print_debug("Matched \"" + string + "\" with \"" + reg_str + "\"")
                #Got a match, now find the operand, remove the match_whole_string
            for i in reversed(range(len(string) + 1)):
                string_part = string[:i]
                if conf.DEBUG:
                    outputs.print_debug("string part=\"" + string_part + "\"")
                reg2 = re.compile("^" + reg_str + "$", re.IGNORECASE)
                if reg2.match(string_part):
                    if conf.DEBUG:
                        outputs.print_debug("Matched \"" + string_part + "\" with \"" + reg_str + "\"")
                        outputs.print_debug("string[i:]=\"" + string[i:] + "\"")
                    matches.append(string[i:].strip())

    if not matches:
        return False, None

    matches.sort(key=lambda t: len(t))
    return True, matches[0]


def get_scripts_dict():
    dict = {}

    import paula.scripts

    scripts_dir = os.path.dirname(os.path.abspath(paula.scripts.__file__))
    for script in os.listdir(scripts_dir):
        to_be_checked = os.path.join(scripts_dir, script)
        if os.path.isdir(to_be_checked) and not to_be_checked.__contains__("__pycache__"):
            script_dir = os.path.join(scripts_dir, script)
            commands = os.path.join(script_dir, "script_commands")
            if os.path.isfile(commands):
                dict[script] = commands

    return dict


