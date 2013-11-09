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

# Returns the script for the command
def decide_command(command):
    This is to be changed heavily when command recognision is implemented
    if conf.DEBUG:
        print("decided  "+command + " to be the command for the "+ command + " script.")
    script.execute(command)
    return command

# Returns whether the given command refers to a specific class of commands.
# e.g.  is_command_for("YES", "yes") == True
#       is_command_for("NO" , "yes") == False
def is_command_for(command, class_of_commands):
    classes = get_classes_list()
    if not class_of_commands in classes:
        return False
    
    
    regexes = get_class_regexes(class_of_commands)
    for reg_str in regexes:
        if conf.IGNORE_CASING:
            reg = re.compile(reg_str, re.IGNORECASE)
        else:
            reg = re.compile(reg_str)

        if reg.match(command):
            return True
    return False


def get_classes_list():
    return [ f for f in os.listdir(conf.COMMANDS_DIR) if os.path.isfile(os.path.join(conf.COMMANDS_DIR,f)) ]

def get_class_regexes(class_name):
    return [i.strip() for i in open(os.path.join(conf.COMMANDS_DIR,class_name)).readlines()]
