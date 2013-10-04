import subprocess
import voice_config as conf

def say(text):
    bashCommand = conf.speak_script + " " + text
    subprocess.call(conf.speak_script + " " + text, shell=True)
    #process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    #output = process.communicate()
