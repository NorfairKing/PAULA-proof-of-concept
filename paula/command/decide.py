import decide_config as conf

# Returns the script for the command
def decide_command(command):
    if command == "sleep":
        print "decided  "+command + " to be " + conf.sleep_script
        return conf.sleep_script
    return None

# Returns whether the given command refers to a specific class of commands.
# e.g.  isCommandFor("YES", "yes") == True
#       isCommandFor("NO" , "yes") == False
def isCommandFor(command, class_of_commands):
    if command == "sleep" and class_of_commands == "sleep":
        return true
    else:
        return false
