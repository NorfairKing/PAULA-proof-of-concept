import decide_config as conf

# Returns the script for the command
def decide_command(command):
    if command == "sleep":
        if conf.debug:
            print "decided  "+command + " to be the command for the sleep script."
        from paula.sleep import sleep_script
        sleep_script.execute()
        return "sleep"
    return "Nothing"

# Returns whether the given command refers to a specific class of commands.
# e.g.  isCommandFor("YES", "yes") == True
#       isCommandFor("NO" , "yes") == False
def isCommandFor(command, class_of_commands):
    if command == "sleep" and class_of_commands == "sleep":
        return true
    else:
        return false
