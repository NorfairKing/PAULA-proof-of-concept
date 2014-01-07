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
The youtube script.
"""

from paula.scripts.script import Script
from paula.external import youtube


class YoutubeScript(Script):
    def execute(self, operand):
        vid_id, name = youtube.search_first_hit(operand)
        youtube.play_video(vid_id)
