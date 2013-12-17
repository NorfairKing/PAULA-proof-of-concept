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
from . import external_config as conf

def open(url):
    if conf.DEBUG:
        outputs.print_debug("Opening URL in browser: " + url)
    system.call_silently("xdg-open \"" + url + "\"", sync=False)