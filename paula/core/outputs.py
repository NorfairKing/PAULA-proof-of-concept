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


def print_error(error_string):
    string.print_error("ERROR: " + error_string)


def print_debug(debug_string):
    string.print_debug("DEBUG: " + debug_string)


def print_color(text, foreground, background="default", bold=False, newline=True):
    string.print_color(text, foreground, background=background, bold=bold, newline=newline)
