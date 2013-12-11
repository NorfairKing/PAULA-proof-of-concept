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
from . import paula_system_config as conf
from paula.core import outputs

def call(command_string, sync=True):
    if conf.DEBUG:
        outputs.print_debug("Executing: " + command_string)

    process = subprocess.Popen(command_string, shell=True)
    if sync:
        process.wait()
    else:
        return process

def call_list(command_list, sync=True):
    if conf.DEBUG:
        outputs.print_debug("Executing: " + str(command_list))

    process = subprocess.Popen(command_list, shell=False)
    if sync:
        process.wait()
    else:
        return process


def call_silently(command_string, sync=True):
    if conf.DEBUG:
        outputs.print_debug("Executing silently: " + command_string)

    null = open(os.devnull, 'w')
    process = subprocess.Popen(command_string, shell=True, stdout=null, stderr=null)
    if sync:
        process.wait()
    else:
        return process

def call_list_silently(command_list, sync=True):
    if conf.DEBUG:
        outputs.print_debug("Executing silently: " + str(command_list))

    null = open(os.devnull, 'w')
    process = subprocess.Popen(command_list, shell=False, stdout=null, stderr=null)
    if sync:
        process.wait()
    else:
        return process



def get_output_of(command_string):
    if conf.DEBUG:
        outputs.print_debug("Getting output of: " + command_string)
    process = subprocess.Popen(command_string, shell=True, stdout=subprocess.PIPE)
    out, err = process.communicate()
    return out