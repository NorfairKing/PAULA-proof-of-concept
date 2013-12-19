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

from paula.core import outputs

from . import paula_test_script_config as conf


def execute(operand):
    if conf.DEBUG:
        outputs.print_debug("The arguments to execute this script were the following.")
        outputs.print_debug(operand)

    # <Test here>

    # </Test here>