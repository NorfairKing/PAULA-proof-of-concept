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

from .paula_output import string

from . import  core_config

def print_error(error_string):
    string.print_error(error_string)

def print_debug(debug_string):
    string.print_debug(debug_string)

def print_color(print_string, color_string):
    string.print_color(print_string, color_string)