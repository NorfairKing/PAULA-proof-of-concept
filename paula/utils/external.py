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
from . import utils_config as conf

def call(command_string, sync=True):
    if conf.DEBUG:
        print("Executing: " + command_string)

    process = subprocess.Popen(command_string, shell=True)
    if sync:
        process.wait()
    else:
        return process

def call_list(command_list, sync=True):
    if conf.DEBUG:
        print("Executing: " + str(command_list))

    process = subprocess.Popen(command_list, shell=False)
    if sync:
        process.wait()
    else:
        return process


def call_silently(command_string, sync=True):
    if conf.DEBUG:
        print("Executing silently: " + command_string)

    null = open(os.devnull, 'w')
    process = subprocess.Popen(command_string, shell=True, stdout=null, stderr=null)
    if sync:
        process.wait()
    else:
        return process

def call_list_silently(command_list, sync=True):
    if conf.DEBUG:
        print("Executing silently: " + str(command_list))

    null = open(os.devnull, 'w')
    process = subprocess.Popen(command_list, shell=False, stdout=null, stderr=null)
    if sync:
        process.wait()
    else:
        return process



def get_output_of(command_string):
    if conf.DEBUG:
        print("Getting output of: " + command_string)
    process = subprocess.Popen(command_string, shell=True, stdout=subprocess.PIPE)
    out, err = process.communicate()
    return out