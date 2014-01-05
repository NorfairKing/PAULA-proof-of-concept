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
import random
from paula.core import outputs
from paula.music import song
from . import vibe_script_config as conf


def execute(operand):
    possible_selections = get_vibe_songs_dict()
    debug("Possible selections = " + str(possible_selections))
    try:
        selected_title = random.choice(list(possible_selections.keys()))
    except IndexError:
        return #TODO do something fitting when there are no vibe songs
    selected_song = possible_selections[selected_title]
    debug("Selected = " + str(selected_song))
    selected_song.play()


def get_vibe_songs_dict():
    possible_selections = {}
    for path in conf.VIBE_DIRS:
        for dirname, dirnames, filenames in os.walk(path):
            for filename in filenames:
                file_clean = os.path.splitext(filename)[0]
                entire_path = os.path.join(dirname, filename)
                possible_selections[file_clean] = song.Song(entire_path)
    return possible_selections


def debug(string):
    if conf.DEBUG:
        outputs.print_debug(string)
