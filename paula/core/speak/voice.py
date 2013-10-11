import os
import subprocess
import voice_config as conf

def say(text):
    print("PAULA:   " + text + "\n")
    bashCommand = conf.speak_script + ' "' + text  +'"'
    null = open(os.devnull, 'w')
    process = subprocess.Popen(bashCommand, shell=True, stdout=null, stderr = null)
    out,err = process.communicate()
