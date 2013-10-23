import os
import subprocess
import speak_config as conf

def say(text):
    print("PAULA:   " + text + "\n")

    if conf.SOUND_ON:
        bashCommand = conf.SPEAK_SCRIPT + ' "' + text  +'"'
        null = open(os.devnull, 'w')
        if (conf.DEBUG):
            process = subprocess.Popen(bashCommand, shell=True)
            out,err = process.communicate()
        else:
            process = subprocess.Popen(bashCommand, shell=True, stdout=null, stderr = null)
            out,err = process.communicate()
