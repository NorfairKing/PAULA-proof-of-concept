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
from . import integer
import math


def prompt_for_list(possible_selections):
    tuples = [(index,value) for index, value in enumerate(possible_selections)]
    dict = { index:value for index,value in tuples}

    m = 1
    for key in dict.keys():
        if len(str(key)) > m:
            m = len(str(key))
    spacing = m

    for (index,value) in tuples:
        key_str = "     "
        key_str += str(index)
        key_str += (int(spacing) - len(str(index))) * " "
        key_str += " - "
        key_str += str(value)
        print(key_str)

    while True:
        user_input = integer.prompt_for_input_int("Take your pick: ")
        if user_input in dict:
            return dict[user_input]
        else:
            print("That is an invalid selection, Sir.")

def prompt_for_dict(possible_selections, sort_alphabetically=True):
    str_tuples = [(str(key),possible_selections[key]) for key in possible_selections]
    str_dict = {str(key):possible_selections[key] for key in possible_selections}

    if sort_alphabetically:
        str_tuples = sorted(str_tuples)

    m = 1
    for key in str_dict.keys():
        if len(key) > m:
            m = len(key)
    spacing = m

    for (key, value) in str_tuples:
        key_str = "     "
        key_str += key
        key_str += (spacing - len(key)) * " "
        key_str += " - "
        key_str += str(value)
        print(key_str)

    while True:
        user_input = string.prompt_for_input_string("Take your pick: ")
        if user_input in str_dict:
            return str_dict[user_input]
        else:
            print("That is an invalid selection, Sir.")