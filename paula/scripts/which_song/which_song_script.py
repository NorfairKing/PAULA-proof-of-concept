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
Prints information about the song that is currently playing.
"""

from paula.scripts.script import Script
from paula.music import song


class WhichSongScript(Script):
    def execute(self, operand):
        if song.is_song_playing():
            print("Song: " + song.get_current_song())
            print("Artist: " + song.get_current_artist())
            print("Album: " + song.get_current_album())
        else:
            print("There is no song playing.")