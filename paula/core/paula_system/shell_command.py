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

from paula.core.inputs import get_password
from paula.core.outputs import print_debug
from paula.core import config

from . import paula_system_config as conf


def call(command_string, sync, sudo):
    debug("Executing: " + command_string)

    if sudo:
        command_string = sudoify_command(command_string)

    process = subprocess.Popen(command_string, shell=True)
    if sync:
        process.wait()
    else:
        return process


def call_list(command_list, sync, sudo):
    return call(" ".join(command_list), sync, sudo)


def call_silently(command_string, sync, sudo):
    debug("Executing silently: " + command_string)

    if sudo:
        command_string = sudoify_command(command_string)

    null = open(os.devnull, 'w')
    process = subprocess.Popen(command_string, shell=True, stdout=null, stderr=null)
    if sync:
        process.wait()
    else:
        return process


def call_list_silently(command_list, sync, sudo):
    debug("calling list silently= "+ str(command_list))
    return call_silently(" ".join(command_list), sync, sudo)


def get_output_of(command_string):
    debug("Getting output of: " + command_string)
    process = subprocess.Popen(command_string, shell=True, stdout=subprocess.PIPE)
    out, err = process.communicate()
    return out


def sudoify_command(command_string):
    ask = config.get_global('Sudo', 'ask') == 'True'
    if ask:
        password = get_password()
    else:
        password = config.get_global('Sudo', 'password')
    command_string = ('echo %s | sudo -S %s' % (password, command_string))
    return command_string


def debug(string):
    if conf.DEBUG:
        print_debug(string)