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
import importlib
from paula.core import interaction

def decide_and_run(string):
    meaning = interaction.decide_meaning(string)
    execute(meaning)

def execute(meaning):
    try:
        module_name = "paula.scripts." + meaning + "." + meaning + "_script"
        module = importlib.import_module(module_name)
        module.execute()
    except ImportError:
        print("ERROR: The " + meaning + " script is missing or does not exist")


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
                dict[commands] = script
    return dict