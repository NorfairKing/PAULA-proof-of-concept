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

import urllib.request
import urllib.error
import os
import signal
from paula.core import system
from . import external_config as conf

def search(arg_string):
    url = "https://gdata.youtube.com/feeds/api/videos?q="
    for a in arg_string.split():
        url += (str(a) + "+")
    url = url[0:-1]
    response = str(urllib.request.urlopen(url).read())
    vidid = response[response.find("<entry><id>http://gdata.youtube.com/feeds/api/videos/") + len("<entry><id>http://gdata.youtube.com/feeds/api/videos/"): response.find("</id><published>")]

    return vidid

def play_video(vidid):
    system.kill_vlc()

    if conf.CONTROLS:
        process = system.call_list_silently(["vlc", "-vvv", "http://youtube.com/watch?v="+vidid], sync=False)
        songfile = open('/tmp/paula_song.pid', 'w+');
        songfile.write(str(process.pid))
        return process
    else:
        process = system.call_list_silently(["vlc", '-Idummy', "-vvv", "http://youtube.com/watch?v="+vidid], sync=False)
        songfile = open('/tmp/paula_song.pid', 'w+');
        songfile.write(str(process.pid))
        return process


def play_song(vidid):
    system.kill_vlc()

    process = system.call_list_silently(["vlc", '-Idummy' , '-Vdummy' , "--play-and-exit", "-vvv", "http://youtube.com/watch?v="+vidid], sync=False)

    songfile = open('/tmp/paula_song.pid', 'w+');
    songfile.write(str(process.pid))

    return process