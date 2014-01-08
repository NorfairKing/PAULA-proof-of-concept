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
# Artificial0
# Unintelligent
# Life
# Assistant
#
##

"""
The sexy vibe script.
"""

import os
import random

from paula.scripts.script import Script
from paula.music import song


class VibeScript(Script):
    def execute(self, operand):
        possible_selections = self.get_vibe_songs_dict() #TODO make this cleaner and more contained within PAULA instead of the script
        self.debug("Possible selections = " + str(possible_selections))
        try:
            selected_title = random.choice(list(possible_selections.keys()))
        except IndexError:
            return #TODO do something fitting when there are no vibe songs
        selected_song = possible_selections[selected_title]
        self.debug("Selected = " + str(selected_song))
        selected_song.play()


    def get_vibe_songs_dict(self):
        possible_selections = {}
        for path in self.get_config('VIBE_DIRS'):
            for dirname, dirnames, filenames in os.walk(path):
                for filename in filenames:
                    file_clean = os.path.splitext(filename)[0]
                    entire_path = os.path.join(dirname, filename)
                    possible_selections[file_clean] = song.Song(entire_path)
        return possible_selections
