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
import signal
from .paula_system import shell_command

def call(command_string, sync=True):
    return shell_command.call(command_string, sync)

def call_list(command_list, sync=True):
    return shell_command.call_list(command_list, sync)

def call_silently(command_string, sync=True):
    return shell_command.call_silently(command_string, sync)

def call_list_silently(command_list, sync=True):
    return shell_command.call_list_silently(command_list, sync)

def get_output_of(command_string):
    return shell_command.get_output_of(command_string, sync)

def kill_vlc():
    if os.path.isfile('/tmp/paula_song.pid'):
        songfile = open('/tmp/paula_song.pid', 'r');
        pid = songfile.read()
        #check if the process is still running
        if(os.path.exists("/proc/" + pid)):
            os.kill(int(pid), signal.SIGTERM)
        os.remove('/tmp/paula_song.pid')