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

from paula.external import browser
from paula.core import outputs
from . import google_script_config as conf

def execute(operand):
    if conf.DEBUG:
        outputs.print_debug("Search terms: " + operand)
    browser.open("http://www.google.com/search?q="+operand)