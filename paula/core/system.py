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
import subprocess
from .system import shell_command

def call(command_string, sync=True):
    return shell_command.call(command_string, sync)

def call_list(command_list, sync=True):
    return shell_command.call_list(command_list, sync)

def call_silently(command_string, sync=True):
    return shell_command.call_silently(command_string, sync)

def call_list_silently(command_list, sync=True):
    return shell_command.call_list_silently(command_list, sync)

def get_output_of(command_string):
    return shell_command.get_output_of(command_string, sync)