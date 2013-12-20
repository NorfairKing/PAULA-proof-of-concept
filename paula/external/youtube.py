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
from paula.core import system
from paula.core import inputs
from paula.music import music_conf
from paula.music import song
from mutagenx.easyid3 import EasyID3
from . import external_config as conf


def search_first_hit(arg_string):
    url = "https://gdata.youtube.com/feeds/api/videos?q="
    for a in arg_string.split():
        url += (str(a) + "+")
    url = url[0:-1]
    response = str(urllib.request.urlopen(url).read())
    vidid = response[response.find("<entry><id>http://gdata.youtube.com/feeds/api/videos/") + len(
        "<entry><id>http://gdata.youtube.com/feeds/api/videos/"): response.find("</id><published>")]
    name = response[response.find("<media:title type=\\\'plain\\\'>") + len(
        "<media:title type=\\\'plain\\\'>"): response.find("</media:title>")]
    return vidid, name


def download_song(vidid):
    download = system.call_silently(
        "youtube-dl --extract-audio --audio-format mp3 --id http://youtube.com/watch?v=" + vidid, sync=False)

    print("Please fill in some info: ")
    artist = inputs.get_string(prompt="Artist: ")
    album = inputs.get_string(prompt="Album: ")
    title = inputs.get_string(prompt="Title: ")

    #heel lelijk, moet veranderd worden
    musicdir = song.get_music_dirs()[0]
    if len(song.get_music_dirs()) > 1:
        musicdir = inputs.get_item_from_list(music_conf.MUSIC_DIRS)

    if not os.path.isdir(musicdir + "/" + artist):
        os.mkdir(musicdir + "/" + artist)
    if not os.path.isdir(musicdir + "/" + artist + "/" + album):
        os.mkdir(musicdir + "/" + artist + "/" + album)

    download.wait()

    file_path = musicdir + "/" + artist + "/" + album + "/" + title + ".mp3"
    os.rename(vidid + ".mp3", file_path)

    audio = EasyID3(file_path)
    audio["title"] = title
    audio["artist"] = artist
    audio["album"] = album
    audio.save()


def play_video(vidid):
    system.kill_vlc()

    if conf.CONTROLS:
        process = system.call_list_silently(["vlc", "-vvv", "http://youtube.com/watch?v=" + vidid], sync=False)
        songfile = open(music_conf.SONG_PID, 'w+')
        songfile.write(str(process.pid))
        return process
    else:
        process = system.call_list_silently(["vlc", '-Idummy', "-vvv", "http://youtube.com/watch?v=" + vidid],
                                            sync=False)
        songfile = open(music_conf.SONG_PID, 'w+')
        songfile.write(str(process.pid))
        return process


def play_song(vidid, name):
    system.kill_vlc()

    process = system.call_list_silently(
        ["vlc", '-Idummy', '-Vdummy', "--play-and-exit", "-vvv", "http://youtube.com/watch?v=" + vidid], sync=False)

    songfile = open(music_conf.SONG_PID, 'w+')
    songfile.write(str(process.pid))

    songfile = open(music_conf.SONG_INFO, 'w+')
    songfile.write(name + "\n")
    songfile.write("Unkown\n")
    songfile.write("YouTube")


    return process