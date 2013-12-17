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

import sys

from paula.core import inputs
from paula.core import outputs
from paula.core import interaction
from paula.music import song
from paula.external import youtube

from . import play_song_script_config as conf

def execute(operand):
    search_string = " ".join(sys.argv[2:])
    if conf.DEBUG:
        outputs.print_debug("The search string: " + search_string)
    local_song = song.find_song(search_string)

    if local_song:
        if conf.DEBUG:
            outputs.print_debug("Found local song!")
        local_song.play()
        return

    #We didn't find it locally; check youtube!
    vidid = youtube.search(search_string)
    youtube.play_song(vidid)

    interaction.say("Do you want to download this song?")
    answer = inputs.get_string()
    if interaction.means(answer, "yes"):
        print("Please fill in some info: ")
        print("Artist: ")
        artist = inputs.get_string()
        print("Album: ")
        album = inputs.get_string()
        print("Title: ")
        title = inputs.get_string()
        youtube.download_song(vidid, title, artist, album)