from paula.paula import Paula
from paula.music import song
from paula.music import system_volume
from paula.motivation import quote
import sleep_conf as conf

def execute():
    p = Paula()

    p.say("How long would you like to sleep, Sir?")

    printOptions(conf.DURATION_OPTIONS)
    answer = p.get_input_str().strip()
    chosen_option = int(conf.DURATION_OPTIONS[answer])
    
    p.debug("answer = " + answer, conf.DEBUG)
    p.debug("selected option = " + str(chosen_option) + " seconds", conf.DEBUG)
    
    # select song
    p.say("Please select which song you want to wake you up.")
    s = song.choose()

    # Set volume to something pleasant
    system_volume.set(conf.PLEASANT_WAKE_UP_VOLUME)
    
    # Sleep
    p.go_to_sleep_mode(chosen_option)
    
    # Wake up
    p.say("Good morning, Sir")
    
    # Play random song
    print("(C-c to stop playing)")
    s.play()
    
    p.say("Have a nice day, Sir")
    
    print str(quote.get_random())

def printOptions(dic):
    for key in dic.keys():
        spaces = (20-len(key)) * " "
        print("         " + key + spaces +" - " + str(dic[key]/60) + " min") 
    print
    
