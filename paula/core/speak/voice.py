import subprocess
import voice_config as conf

def say(text):
    print("PAULA:   " + text + "\n")
    bashCommand = conf.speak_script + ' "' + text  +'"'
    if not conf.debug:
        bashCommand += ">/dev/null 2>&1"
    process = subprocess.Popen(bashCommand,shell=True)
    out,err = process.communicate()
