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

from . import music_conf as conf


class Song:
    def __init__(self, path):
        foldernames = path.split('/')
        self.title = foldernames[-1]
        self.artist = foldernames[-3]
        self.album = foldernames[-2]
        if conf.DEBUG:
            print("Title: " + self.title)
            print("Artist " + self.artist)
            print("Album: " + self.album)
        self.path = path
        self.playing = False

    def play(self):
        cmd = ['vlc', '-Idummy' , '--play-and-exit','-vvv', self.path]
        null = open(os.devnull, 'w')

        self.process = subprocess.Popen(cmd, shell=False, stdout=null, stderr=null)
        print(self.process.pid)
        self.playing = True
        songfile = open('/tmp/paula_song.pid', 'w+');
        songfile.write(str(self.process.pid))
        return self.process

    def __str__(self):
        return "Artist: " + self.artist + ", Song: "+self.title


def choose_and_play():
    song = choose()
    song.play()

def stop_song():
    songfile = open('/tmp/paula_song.pid', 'r');
    pid = songfile.read()
    os.kill(int(pid), signal.SIGTERM)

def play_random():


def select_random():


def choose():
    artists = get_artists_dict()
    artist_path = ask_selection(artists)

    songs = get_songs_dict(artist_path)
    song_path = ask_selection(songs)

    song = Song(song_path)
    song.play()


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
            print("That is invalid selection, Sir.")
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
