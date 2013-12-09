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
from paula.music.song import Song
from . import vibe_script_config as conf


def execute():
    possible_selections = get_vibe_songs_dict()
    if conf.DEBUG:
        print("Possible selections = " + str(possible_selections))
    selected_title = random.choice(list(possible_selections.keys()))
    selected_song = possible_selections[selected_title]
    if conf.DEBUG:
        print("Selected = " + str(selected_song))
    try:
        subp = selected_song.play()
        subp.wait()
    except KeyboardInterrupt:
        subp.kill()


def get_vibe_songs_dict():
    possible_selections = {}
    for path in conf.VIBE_DIRS:
        for dirname, dirnames, filenames in os.walk(path):
            for filename in filenames:
                # Only select mp3 files
                for ext in conf.MUSIC_EXTENSIONS:
                    if filename.endswith(ext):
                        file_clean = os.path.splitext(filename)[0]
                        entire_path = os.path.join(dirname, filename)
                        possible_selections[file_clean] = Song(file_clean, entire_path)
    return possible_selections
