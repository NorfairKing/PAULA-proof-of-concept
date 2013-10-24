from .speak import voice
from .command import decide

def decide_command(cmd):
    return decide.decide_command(cmd)

def is_command_for(cmd, class_of_commands):
    return decide.is_command_for(cmd, class_of_commands)

def say(text):
    return voice.say(text)
