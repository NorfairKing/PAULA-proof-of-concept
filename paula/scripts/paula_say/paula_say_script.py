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
from paula.core import interaction

from . import paula_say_script_config as conf

def execute(operand):
    if conf.DEBUG:
        outputs.print_debug("Saying " + operand)
    interaction.say(operand,sync=True)
    import time
    time.sleep(5)