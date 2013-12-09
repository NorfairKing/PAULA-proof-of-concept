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

import os
import subprocess


def call(command_string, sync=True):
    process = subprocess.Popen(command_string, shell=True)
    if sync:
        process.wait()


def call_silently(command_string, sync=True):
    null = open(os.devnull, 'w')
    process = subprocess.Popen(command_string, shell=True, stdout=null, stderr=null)
    if sync:
        process.wait()


def get_output_of(command_string):
    process = subprocess.Popen(command_string, shell=True, stdout=subprocess.PIPE)
    out, err = process.communicate()
    return out