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

from . import string

from paula.core import interaction
from paula.core import outputs

def prompt_for_input_string(prompt=""):
    while True:
        answer = string.prompt_for_input_string(prompt=prompt)
        if interaction.means(answer, "yes"):
            return True
        elif interaction.means(answer, "no"):
            return False
        else:
            outputs.print_error("Not a Boolean value.")