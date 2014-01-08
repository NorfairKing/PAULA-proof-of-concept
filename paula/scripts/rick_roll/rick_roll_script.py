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

"""
The Rickroll script
"""

from paula.scripts.script import Script
from paula.music import song

class RickRollScript(Script):
    def execute(self, operand):
        rr = song.Song(self.get_resource_path('rick_roll.mp3'))
        rr.play()

