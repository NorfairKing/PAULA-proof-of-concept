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

import operator

def prompt_for_list(possible_selections, sortAlphabetically=True):
    if sortAlphabetically:
        sorted_dict = dict(zip(range(len(possible_selections)), sorted(possible_selections)))
        return prompt_for_dict(sorted_dict)
    else:
        return prompt_for_dict(dict(zip(range(len(possible_selections)), possible_selections)), sortAlphabetically=False)

def prompt_for_dict(possible_selections, sortAlphabetically=True):

    #sorted_dict = list(possible_selections.items(), key=operator.itemgetter(1))
    sorted_dict = list()
    if sortAlphabetically:
        sorted_dict = sorted(possible_selections.items(), key=operator.itemgetter(1))

    for key, value in sorted_dict:
        print(("     " + str(key) + ((5 - len(str(key))) * " ") + " - " + str(value)))
    print()

    while (True):
        userInput = input("Take your pick: ")

        try:
            key = str(userInput)
        except:
            print("That's not a valid input, Sir.")
            continue

        try:
            if int(key) in possible_selections.keys():
                return possible_selections[int(key)]
        except:
            pass
        
        if str(key) in possible_selections.keys():
            return possible_selections[str(key)]
        else:
            print("That is an invalid selection, Sir.")