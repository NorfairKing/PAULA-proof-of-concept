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

from . import command_config as conf
from paula.scripts import script as script

# Returns the script for the command
def decide_command(command):
    # This is to be changed heavily when command recognision is implemented
    if conf.DEBUG:
        print("decided  "+command + " to be the command for the "+ command + " script.")
    script.execute(command)
    return command

# Returns whether the given command refers to a specific class of commands.
# e.g.  is_command_for("YES", "yes") == True
#       is_command_for("NO" , "yes") == False
def is_command_for(command, class_of_commands):
    if command == "sleep" and class_of_commands == "sleep":
        return true
    elif command == "goingout" and class_of_commands == "goingout":
        return false
