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
PAULA's random song script
"""

from paula.scripts.script import Script
from paula.music import song

class RandomSongScript(Script):
    def execute(self, operand):
        self.debug("Playing a random song")
        song.play_random()

        print("Song: " + song.get_current_song())
        print("Artist: " + song.get_current_artist())
        print("Album: " + song.get_current_album())