import os
import sys
import subprocess
import random
import time

#from paula.paula import Paula
from . import music_conf as conf

class Song:
    def __init__(self, title, path):
        self.title = title
        self.path = path
        self.title_pronouncable = self.make_pronouncable(title)
    
    def make_pronouncable(self, title):
        split = title.split(conf.TITLE_ARTIST_DELIMITER)
        artist = split[0]
        title = split[1]
        partist = artist.replace(conf.SONG_PATH_SPACE_SYNONYM,' ')
        ptitle = title.replace(conf.SONG_PATH_SPACE_SYNONYM,' ')
        return ptitle + " by " + partist

    def play(self):
        cmd = "play  \""+ self.path + "\""
        if not conf.DEBUG:
            cmd += " > /dev/null 2>&1"
        null = open(os.devnull, 'w')
    
        try:
            process = subprocess.Popen(cmd, shell=True, stdout=null)
            process.wait()
        except KeyboardInterrupt:
            process.terminate()

    def __str__(self):
        return self.title + "  at: " + self.path + "  pronounced: " + self.title_pronouncable 

    
def choose_and_play():
    song = choose()
    song.play()

def select_and_play():
    song = select()
    song.play()

def play_random():
    song = select_random()
    if conf.DEBUG:
        print(("randomly selected: " + str(song)))
    song.play()

def select_random():
    possible_selections = get_songs_dict()
    selected_title = random.choice(list(possible_selections.keys()))
    selected_song = possible_selections[selected_title]
    return selected_song

def choose():
    possible_selections = get_songs_dict()
                 
    sorted_keys = sorted(possible_selections.keys())
    
    print(("    " + str(-1) +  ((6-len(str(-1))) * " ") +" - " + "random song"))
    counter = 0
    for entry in sorted_keys:
        print(("     " + str(counter) +  ((5-len(str(counter))) * " ") +" - " + str(entry)))
        counter += 1
    print()

    ask = True
    while(ask):
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
def select():
    possible_selections = get_songs_dict()
                 
    sorted_keys = sorted(possible_selections.keys())
    counter = 0
    for entry in sorted_keys:
        print(("     " + str(counter) +  ((5-len(str(counter))) * " ") +" - " + str(entry)))
        counter += 1
    print()

    ask = True
    while(ask):
        userInput = input("Take your pick: ")

        try:
            val = int(userInput)
        except ValueError:
            print("That's not a number, Sir.")        
            continue

        if val < 0 or val >= len(sorted_keys):
            print("That is invalid selection, Sir.")
            continue
            
        selected_title = sorted_keys[val]
        selected_song = possible_selections[selected_title]
        ask = False

    return selected_song


def get_songs_dict():
    possible_selections = {}
    for path in conf.MUSIC_DIRS:    
        for dirname, dirnames, filenames in os.walk(path):
            for filename in filenames:
                # Only select mp3 files
                for ext in conf.MUSIC_EXTENSIONS:
                    if filename.endswith(ext):
                        file_clean = os.path.splitext(filename)[0]
                        entire_path = os.path.join(dirname, filename)
                        possible_selections[file_clean] = Song(file_clean, entire_path)
    return possible_selections

