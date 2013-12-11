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

from paula.core import shell_command

from . import sleep_conf as conf


def go_to_sleep_mode(seconds):
    if seconds == 0:
        if not conf.DEBUG:
            cmd = "sudo pm-suspend"
            shell_command.call_silently(cmd)
        else:
            print("going to sleep indefinitly")
    else:
        cmd = "sudo rtcwake --mode mem "
        if conf.DEBUG:
            cmd += "--dry-run "
        cmd += "--seconds " + str(seconds)

        if not conf.DEBUG:
            shell_command.call_silently(cmd)
        else:
            shell_command.call(cmd)