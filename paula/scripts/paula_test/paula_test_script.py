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

from . import paula_test_script_config as conf

from paula.utils import external
from paula.music import system_volume
def execute():
    if conf.DEBUG:
        print("The arguments to execute this script were the following.")
        print(sys.argv)

    # Test stuff here
    print(system_volume.get())