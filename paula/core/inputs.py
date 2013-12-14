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

from .paula_input import string
from .paula_input import integer
from .paula_input import lists


def get_string():
    return string.prompt_for_input_string()


def get_integer():
    return integer.prompt_for_input_int()


def get_string_timeout(timeout):
    return string.prompt_with_timeout(timeout)


def get_integer_timeout(timeout):
    return integer.prompt_with_timeout(timeout)

def get_item_from_list(possible_selections, sortAlphabetically=True):
    return lists.prompt_for_list(possible_selections, sortAlphabetically)

def get_item_from_dict(possible_selections, sortAlphabetically=True):
    return lists.prompt_for_dict(possible_selections, sortAlphabetically)