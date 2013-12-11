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

import sys
from paula.external import youtube
from paula.core import inputs
from paula.core import outputs
from paula.core import interaction
from . import youtube_script_config as conf

def execute():
    if conf.DEBUG:
        outputs.print_debug(" ".join(sys.argv[2:]))

    result = youtube.search(" ".join(sys.argv[2:]))

    youtube.play_video(result)