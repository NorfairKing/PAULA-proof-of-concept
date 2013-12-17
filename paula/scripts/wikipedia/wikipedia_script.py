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
from paula.external import wikipedia
from paula.core import outputs

from . import wikipedia_script_config as conf

def execute(operand):
    args = sys.argv[2:]
    if conf.DEBUG:
        outputs.print_debug(str(args))

    arg_string = " ".join(args)
    wikipedia.get_description(arg_string)
