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


import importlib
import paula.scripts

def execute(class_name):
    module_name = "paula.scripts." + class_name + "." + class_name + "_script"
    module = importlib.import_module(module_name)
    module.execute()
