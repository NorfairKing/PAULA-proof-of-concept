import os
import sys
import subprocess

#from paula.paula import Paula
import music_conf as conf

def play_random():
    pass

def select():
    #p = Paula()
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

    return selected, path

def play(song_path):
    try:
        bashCommand = "play  \""+ song_path + "\"" + " > /dev/null 2>&1"
        null = open(os.devnull, 'w')
        process = subprocess.Popen(bashCommand, shell=True, stdout=null)
        out,err = process.communicate()
    except:
        process.kill()
