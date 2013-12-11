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

        #Write pid and song info to temporary file
        songfile = open('/tmp/paula_song.pid', 'w+');
        songfile.write(str(process.pid) + "\n")
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
    if not os.path.exists('/tmp/paula_song.pid'):
        return None

    try:
        with open('/tmp/paula_song.pid', 'r') as f:
            lines = f.readlines()
            return lines[3]
    except IOError:
        outputs.print_error('Could not open paula_song.pid')

def get_current_song():
    if not os.path.exists('/tmp/paula_song.pid'):
        return None

    try:
        with open('/tmp/paula_song.pid', 'r') as f:
            lines = f.readlines()
            return lines[1]
    except IOError:
        outputs.print_error('Could not open paula_song.pid')

def get_current_album():
    if not os.path.exists('/tmp/paula_song.pid'):
        return None

    try:
        with open('/tmp/paula_song.pid', 'r') as f:
            lines = f.readlines()
            return lines[2]
    except IOError:
        outputs.print_error('Could not open paula_song.pid')


def stop_song():
    songfile = open('/tmp/paula_song.pid', 'r');
    lines = songfile.readlines()
    os.kill(int(lines[0]), signal.SIGTERM)
    os.remove('/tmp/paula_song.pid')

def play_random():
    files = [os.path.join(path, filename)
        for musicFolder in conf.MUSIC_DIRS
        for path, dirs, files in os.walk(musicFolder)
        for filename in files
        if not filename.endswith(".jpg") and not filename.endswith(".png")]
        
    song = Song(random.choice(files))
    process = song.play()
    return process

def choose():
    artists = get_artists_dict()
    artist_path = ask_selection(artists)

    songs = get_songs_dict(artist_path)
    song_path = ask_selection(songs)

    song = Song(song_path)
    return song


def ask_selection(possible_selections):
    sorted_keys = sorted(possible_selections.keys())

    print(("    " + str(-1) + ((6 - len(str(-1))) * " ") + " - " + "random song"))
    counter = 0
    for entry in sorted_keys:
        print(("     " + str(counter) + ((5 - len(str(counter))) * " ") + " - " + str(entry)))
        counter += 1
    print()

    ask = True
    while (ask):
        userInput = input("Take your pick: ")

        try:
            val = int(userInput)
        except ValueError:
            print("That's not a number, Sir.")
            continue

        if val < -1 or val >= len(sorted_keys):
            print("That is an invalid selection, Sir.")
            continue

        if val == -1:
            selected_song = select_random()
        else:
            selected_title = sorted_keys[val]
            selected_song = possible_selections[selected_title]
        ask = False

    return selected_song



def get_artists_dict():
    possible_selections = {}
    for path in conf.MUSIC_DIRS:
        for dirname in os.listdir(path):
            possible_selections[dirname] = os.path.join(path, dirname)
    return possible_selections

def get_songs_dict(dir):
    possible_selections = {}
    for path, names, files in os.walk(dir):
        for f in files:
            possible_selections[f] = os.path.join(path, f)
    return possible_selections
