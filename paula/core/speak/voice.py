import os
import subprocess
import speak_config as conf

def say(text):
    print("PAULA:   " + text + "\n")

    if conf.sound_on:
        bashCommand = conf.speak_script + ' "' + text  +'"'
        null = open(os.devnull, 'w')
        if (conf.debug):
            process = subprocess.Popen(bashCommand, shell=True)
            out,err = process.communicate()
        else:
            process = subprocess.Popen(bashCommand, shell=True, stdout=null, stderr = null)
            out,err = process.communicate()
