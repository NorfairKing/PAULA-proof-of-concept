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

import sys

def print_error(error_string):
    print("\033[1;31m" + "ERROR: " + error_string + " \033[0m")


def print_debug(debug_string):
    print("\033[1;36m" + "DEBUG: " + debug_string + " \033[0m")


COLOR_DICT = {
    "black": 0,
    "red": 1,
    "green": 2,
    "yellow": 3,
    "blue": 4,
    "magenta": 5,
    "cyan": 6,
    "white": 7,
    "default":9
}

def print_color(text, foreground, background="default", bold=False, newline=True):
    if not foreground in COLOR_DICT or not background in COLOR_DICT:
        result = text
        if newline: result += "\n"
    else:
        result = "\033["
        boldstr = "1" if bold else "0"
        result += boldstr
        result += ";"
        foreground_string = "3" + str(COLOR_DICT[foreground]) + "m"
        result += foreground_string

        result += "\033["
        background_string = "4" + str(COLOR_DICT[background]) + "m"
        result += background_string

        result += text

        result += "\033[0m"

        newlinestr = "\n" if newline else ""
        result += newlinestr
    sys.stdout.write(result)