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

from paula.core import system
from paula.core import outputs

from . import sleep_conf as conf


def go_to_sleep_mode(seconds):
    if seconds == 0:
        if not conf.DEBUG:
            cmd = "pm-suspend"
            system.call_silently(cmd, sudo=True)
        else:
            outputs.print_debug("going to sleep indefinitely")
    else:
        cmd = "sudo rtcwake --mode mem "
        if conf.DEBUG:
            cmd += "--dry-run "
        cmd += "--seconds " + str(seconds)

        if not conf.DEBUG:
            system.call_silently(cmd, sudo=True)
        else:
            system.call(cmd, sudo=True)