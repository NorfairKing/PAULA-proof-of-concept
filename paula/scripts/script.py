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


def decide_and_run(string, parent=""):
    outputs.print_PAULA()
    debug("Trying to decide " + string + " with parent " + parent)
    meaning, operand = decide_meaning(string,parent=parent)
    try:
        execute(meaning, operand, parent=parent)
    except KeyboardInterrupt:
        outputs.print_PAULA()
        debug("Exiting.")
        return
    time.sleep(conf.WAITING_TIME)


def execute(meaning, operand, parent=""):
    if not meaning:
        return
    debug("Trying to execute " + meaning + " with \"" + operand + "\" as operand, a child of " + parent)

    try:
        module_name = "paula.scripts" + parent + "." +meaning + "." + meaning + "_script"
        debug("Importing module: " + module_name)
        module = importlib.import_module(module_name)
    except ImportError:
        outputs.print_error(
            "The " + meaning + " script is missing or does not exist. Either that or some import fails inside the script.")
        return
    module.execute(operand)


def decide_meaning(string, parent=""):
    global meanings
    meanings = get_scripts_dict(parent=parent)
    meaning_found = None
    for name in meanings:
        matched, operand = means(string, name, parent=parent)
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


def means(string, meaning, parent=""):
    if not meaning in meanings:
        return False, None

    regexes = get_meaning_regexes(meaning)

    matches = []

    for reg_str in regexes:
        reg = re.compile(reg_str, re.IGNORECASE)
        if reg.match(string):
            debug("Matched \"" + string + "\" with \"" + reg_str + "\"")
            #Got a match, now find the operand, remove the match_whole_string
            for i in reversed(range(len(string) + 1)):
                string_part = string[:i]
                debug("string part=\"" + string_part + "\"")
                reg2 = re.compile("^" + reg_str + "$", re.IGNORECASE)
                if reg2.match(string_part):
                    debug("Matched \"" + string_part + "\" with \"" + reg_str + "\"")
                    debug("string[i:]=\"" + string[i:] + "\"")
                    matches.append(string[i:].strip())

    if not matches:
        return False, None

    matches.sort(key=lambda t: len(t))
    return True, matches[0]


def get_scripts_dict(parent=""):
    dict = {}
    debug("scripts dir= " + conf.SCRIPTS_DIR)
    PARENT_DIR = os.path.join(conf.SCRIPTS_DIR, parent.replace(".", "/")[1:])
    debug("parent dir = " + PARENT_DIR)
    for script in os.listdir(PARENT_DIR):
        to_be_checked = os.path.join(PARENT_DIR, script)
        if os.path.isdir(to_be_checked) and not to_be_checked.__contains__("__pycache__"):
            script_dir = os.path.join(PARENT_DIR, script)
            commands = os.path.join(script_dir, "script_commands")
            if os.path.isfile(commands):
                dict[script] = commands

    return dict


def debug(string):
    if conf.DEBUG:
        outputs.print_debug(string)