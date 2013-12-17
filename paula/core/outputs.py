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

import subprocess
from .paula_output import string


def print_error(error_string):
    string.print_error(error_string)


def print_debug(debug_string):
    string.print_debug(debug_string)


def print_color(text, foreground, background="default", bold=False, newline=True):
    string.print_color(text, foreground, background=background, bold=bold, newline=newline)

def print_PAULA():
    cmd = "clear"
    process = subprocess.Popen(cmd, shell=True)
    out, err = process.communicate()

    print("""
      ____   _   _   _ _        _
     |  _ \ / \ | | | | |      / \ \n\
     | |_) / _ \| | | | |     / _ \ \n\
     |  __/ ___ \ |_| | |___ / ___ \ \n\
     |_| /_/   \_\___/|_____/_/   \_\ \n\


 Personal
 Artificial
 Unintelligent
 Life
 Assistant

""")