import os
import sys
import subprocess
import random
import time

#from paula.paula import Paula
import music_conf as conf

class Song:
    def __init__(self, title, path):
        self.title = title
        self.path = path
        self.title_pronouncable = self.make_pronouncable(title)
    
    def make_pronouncable(self, title):
        split = title.split(conf.title_artist_delimiter)
        artist = split[0]
        title = split[1]
        partist = artist.replace(conf.song_path_space_synonym,' ')
        ptitle = title.replace(conf.song_path_space_synonym,' ')
        return ptitle + " by " + partist

    def __str__(self):
        return self.title + "  at: " + self.path + "  pronounced: " + self.title_pronouncable 

def select_and_play():
    song = select()
    play(song)

def play(song):
    cmd = "play  \""+ song.path + "\""
    if not conf.debug:
        cmd += " > /dev/null 2>&1"
    null = open(os.devnull, 'w')
    
    try:
        process = subprocess.Popen(cmd, shell=True, stdout=null)
        process.wait()
    except KeyboardInterrupt:
        process.terminate()

def play_random():
    song = select_random()
    if conf.debug:
        print("randomly selected: " + song.title + " at " + song.path)
    play(song)

def select_random():
    possible_selections = get_songs_dict()
    selected_title = random.choice(possible_selections.keys())
    selected_song = possible_selections[selected_title]
    return selected_song

def select():
    #p = Paula()
    possible_selections = get_songs_dict()
                 
    sorted_keys = sorted(possible_selections.keys())
    counter = 0
    for entry in sorted_keys:
        print str(counter) + ": " + entry    
        counter += 1

    ask = True
    while(ask):
        userInput = raw_input("Take your pick: ")

        try:
            val = int(userInput)
        except ValueError:
            print "That's not a number, Sir."        
            continue

        if val < 0 or val >= len(sorted_keys):
            print "That is invalid selection, Sir."
            continue
            
        selected_title = sorted_keys[val]
        selected_song = possible_selections[selected_title]
        ask = False

    return selected_song


def get_songs_dict():
    possible_selections = {}
    for path in conf.music_dirs:    
        for dirname, dirnames, filenames in os.walk(path):
            for filename in filenames:
                # Only select mp3 files
                for ext in conf.music_extensions:
                    if filename.endswith(ext):
                        file_clean = os.path.splitext(filename)[0]
                        entire_path = os.path.join(dirname, filename)
                        possible_selections[file_clean] = Song(file_clean, entire_path)
    return possible_selections
