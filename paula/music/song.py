import os
import sys
import subprocess
import random
import time

#from paula.paula import Paula
import music_conf as conf

def select_and_play():
    song, path = select()
    play(path)

def play(song_path):
    cmd = "play  \""+ song_path + "\""
    if not conf.debug:
        cmd += " > /dev/null 2>&1"
    null = open(os.devnull, 'w')
    
    try:
        process = subprocess.Popen(cmd, shell=True, stdout=null)
        process.wait()
    except KeyboardInterrupt:
        process.terminate()

def play_random():
    (song, path) = select_random()
    if conf.debug:
        print("randomly selected: " + song + " at " + path)
    play(path)

def select_random():
    possible_selections = get_songs_dict()
    selected = random.choice(possible_selections.keys())
    selected_path = possible_selections[selected]
    return selected, selected_path

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
            
        selected = sorted_keys[val]
        selected_path = possible_selections[selected]
        ask = False

    return selected, selected_path


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
                        possible_selections[file_clean] = entire_path
    return possible_selections
