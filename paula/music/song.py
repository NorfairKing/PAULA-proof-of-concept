import os
import sys
import subprocess

def play():
    try:
        song = "/home/syd/Music/music/avicii-wake_me_up.mp3"
        bashCommand = "play  \""+ song + "\"" + " > /dev/null 2>&1"
        null = open(os.devnull, 'w')
        process = subprocess.Popen(bashCommand, shell=True, stdout=null)
        out,err = process.communicate()
    except:
        pass
