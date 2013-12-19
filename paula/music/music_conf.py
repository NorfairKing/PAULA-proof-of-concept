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

from os.path import expanduser

# Default = False
DEBUG = False

# Default = [".mp3"]
MUSIC_EXTENSIONS = [".mp3"]

# Default = ["/home/syd/music"]
EXTRA_MUSIC_DIRS = []

STANDARD_MUSIC_DIRS = [
    expanduser("~/music"),
    expanduser("~/Music"),
    expanduser("~/music/music"),
    expanduser("~/music/Music"),
    expanduser("~/Music/music"),
    expanduser("~/Music/Music")
]
