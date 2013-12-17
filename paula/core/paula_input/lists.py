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


def prompt_for_list(possible_selections):
    tuples = [(index,value) for index, value in enumerate(possible_selections)]
    dict = { index:value for index,value in tuples}

    for (index,value) in tuples:
        key_str = "     "
        key_str += str(index)
        key_str += (5 - len(str(index))) * " "
        key_str += " - "
        key_str += str(value)
        print(key_str)

    while True:
        user_input = integer.prompt_for_input_int()
        if user_input in dict:
            return dict[user_input]
        else:
            print("That is an invalid selection, Sir.")

def prompt_for_dict(possible_selections, sort_alphabetically=True):
    str_tuples = [(str(key),possible_selections[key]) for key in possible_selections]
    str_dict = {str(key):possible_selections[key] for key in possible_selections}

    if sort_alphabetically:
        str_tuples = sorted(str_tuples)

    for (key, value) in str_tuples:
        key_str = "     "
        key_str += key
        key_str += (5 - len(key)) * " "
        key_str += " - "
        key_str += str(value)
        print(key_str)

    while True:
        user_input = string.prompt_for_input_string()
        if user_input in str_dict:
            return str_dict[user_input]
        else:
            print("That is an invalid selection, Sir.")