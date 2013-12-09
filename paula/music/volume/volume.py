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

from paula.utils import external

from . import volume_conf as conf


def get():
    cmd = "amixer get Master | grep 'Mono:' | sed -e 's/^[^\[]*//' -e 's/^.//' -e 's/%.*$//'"
    out = external.get_output_of(cmd)
    vol = int(out)
    return vol


def set(percent):
    cmd = "amixer set Master " + str(percent) + "%"
    if not conf.DEBUG:
        external.call_silently(cmd)
    else:
        external.call(cmd)


def mute():
    set(0)
