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

from paula.music import song
from paula.music import music_conf
import os

def execute(operand):
    if os.path.exists(music_conf.SONG_PID):
        print("Song: " + song.get_current_song())
        print("Artist: " + song.get_current_artist())
        print("Album: " + song.get_current_album())
    else:
        print("There is no song playing.")
