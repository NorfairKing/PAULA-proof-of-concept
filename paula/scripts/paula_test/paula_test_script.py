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
from paula.core import outputs
from paula.core import inputs


from . import paula_test_script_config as conf
from paula.core import inputs


def execute(operand):
    if conf.DEBUG:
        outputs.print_debug("The arguments to execute this script were the following.")
        outputs.print_debug(str(sys.argv))

    # <Test here>
    dict = [val for val in range(100)]
    item = inputs.get_item_from_list(dict)
    print(item)
    # </Test here>