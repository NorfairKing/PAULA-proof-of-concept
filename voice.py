import subprocess
import voice_config as conf

def say(text):
    bashCommand = conf.speak_script + " " + text
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output = process.communicate()
