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
The play song script
"""

from paula.scripts.script import Script
from paula.core import inputs
from paula.core import interaction
from paula.music import song
from paula.external import youtube

class PlaySongScript(Script):
    def execute(self, operand):
        search_string = operand
        self.debug("The search string: " + search_string)
        local_song = song.find_song(search_string)

        if local_song:
            self.debug("Found local song!")
            local_song.play()
            return

        #We didn't find it locally; check youtube!
        vid_id, name = youtube.search_first_hit(search_string)
        youtube.play_song(vid_id, name)

        if self.get_config('ASK_DOWNLOAD'):
            interaction.say("Do you want to download this song?")
            answer = inputs.get_string()
            if interaction.means(answer, "yes"):
                youtube.download_song(vid_id)
