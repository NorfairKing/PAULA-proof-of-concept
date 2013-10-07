import subprocess
from .. import config as conf

# Returns the script for the command
def decide_command(command):
    if command == "sleep":
        return conf.sleep_script
    return " "

# Returns whether the given command refers to a specific class of commands.
# e.g.  isCommandFor("YES", "yes") == True
#       isCommandFor("NO" , "yes") == False
def isCommandFor(command, class_of_commands):
    if command == "sleep" and class_of_commands == "sleep":
        return true
    else:
        return false
