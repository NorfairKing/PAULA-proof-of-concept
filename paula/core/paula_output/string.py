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
    "bright_black": 0,
    "bright_red": 1,
    "bright_green": 2,
    "bright_yellow": 3,
    "bright_blue": 4,
    "bright_magenta": 5,
    "bright_cyan": 6,
    "bright_white": 7,
}


def print_color(string, color_str):
    if color_str in COLOR_DICT:
        ANSI_color_value = str(COLOR_DICT[color_str])

        print("\033[1;" + ANSI_color_value + "m" + string + "\033[0m")
    else:
        print(string)