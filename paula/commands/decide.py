import subprocess
from .. import config as conf

# Returns the script for the command
def decide_command(command):
    return "Nothing"

# Returns whether the given command refers to a specific class of commands.
# e.g.  isCommandFor("YES", "yes") == True
#       isCommandFor("NO" , "yes") == False
def isCommandFor(command, class_ofCommands):
    return True;
