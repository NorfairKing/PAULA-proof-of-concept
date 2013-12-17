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
import signal
import subprocess
import random
import os.path
from paula.core import outputs
from paula.core import inputs
from paula.core import system

from . import music_conf as conf


class Song:
    def __init__(self, path):
        foldernames = path.split('/')
        self.title = foldernames[-1]
        self.artist = foldernames[-3]
        self.album = foldernames[-2]
        if conf.DEBUG:
            outputs.print_debug("Title: " + self.title)
            outputs.print_debug("Artist " + self.artist)
            outputs.print_debug("Album: " + self.album)
        self.path = path

    def play(self):
        cmd = ['vlc', '-Idummy' , '--play-and-exit','-vvv', self.path]

        process = system.call_list_silently(cmd, sync=False)

        stop_song()

        #Write pid and song info to temporary file
        pidfile = open('/tmp/paula_song.pid', 'w+');
        pidfile.write(str(process.pid))

        songfile = open('/tmp/paula_song.info', 'w+');
        songfile.write(self.title + "\n")
        songfile.write(self.album + "\n")
        songfile.write(self.artist)
        return process

    def __str__(self):
        return "Artist: " + self.artist + ", Song: "+self.title


def choose_and_play():
    song = choose()
    song.play()

def get_current_artist():
    if not os.path.exists('/tmp/paula_song.info'):
        return None

    try:
        with open('/tmp/paula_song.info', 'r') as f:
            lines = f.readlines()
            return lines[2]
    except IOError:
        outputs.print_error('Could not open paula_song.info')

def get_current_song():
    if not os.path.exists('/tmp/paula_song.info'):
        return None

    try:
        with open('/tmp/paula_song.info', 'r') as f:
            lines = f.readlines()
            return lines[0]
    except IOError:
        outputs.print_error('Could not open paula_song.info')

def get_current_album():
    if not os.path.exists('/tmp/paula_song.info'):
        return None

    try:
        with open('/tmp/paula_song.info', 'r') as f:
            lines = f.readlines()
            return lines[1]
    except IOError:
        outputs.print_error('Could not open paula_song.info')

def find_song(search_string):
    #get all files
    files = [os.path.join(path, filename)
        for musicFolder in conf.MUSIC_DIRS
        for path, dirs, files in os.walk(musicFolder, followlinks=True)
        for filename in files]

    matches = []

    #Check for search string
    for fil in files:
        allMatched = True
        for substr in search_string.split():
            if fil.lower().find(substr.lower()) == -1:
                allMatched = False
        if allMatched:
            matches.append(Song(fil))

    if not matches:
        return None

    return random.choice(matches)

def stop_song():
    system.kill_vlc()

def select_random():
    files = [os.path.join(path, filename)
        for musicFolder in conf.MUSIC_DIRS if os.path.isdir(musicFolder)
        for path, dirs, files in os.walk(musicFolder)
        for filename in files
        if not filename.endswith(".jpg") and not filename.endswith(".png")]

    song = Song(random.choice(files))
    return song

def play_random():
    song = select_random()
    process = song.play()
    return process

def choose():
    artists = get_artists_dict()
    artistkey = inputs.get_item_from_list(artists.keys())
    artist_path = artists[artistkey]

    songs = get_songs_dict(artist_path)
    songkey = inputs.get_item_from_list(songs.keys())
    song_path = songs[songkey]

    song = Song(song_path)
    return song

def get_artists_dict():
    possible_selections = {}
    for path in conf.MUSIC_DIRS:
        if os.path.isdir(path):
            for dirname in os.listdir(path):
                possible_selections[dirname] = os.path.join(path, dirname)
    return possible_selections

def get_songs_dict(dir):
    possible_selections = {}
    for path, names, files in os.walk(dir):
        for f in files:
            possible_selections[f] = os.path.join(path, f)
    return possible_selections
