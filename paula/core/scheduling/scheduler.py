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
from . import event
from . import scheduling_config as conf

def get_all_events():
    for path, dirs, files in os.walk(conf.SCHEDULING_DIR):
        return [event.get_event_from_file(os.path.join(conf.SCHEDULING_DIR,f)) for f in files]

def get_overdue_events():
    return [e for e in get_all_events() if e.is_overdue()]