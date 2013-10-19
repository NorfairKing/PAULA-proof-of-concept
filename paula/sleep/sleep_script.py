from paula.paula import Paula
from paula.music import song
from paula.music import system_volume
import sleep_conf as conf

def execute():
    p = Paula()

    p.say("How long would you like to sleep, Sir?")

    printOptions(conf.duration_options)
    answer = p.get_input_str().strip()
    chosen_option = int(conf.duration_options[answer])
    
    p.debug("answer = " + answer, conf.debug)
    p.debug("selected option = " + str(chosen_option) + " seconds", conf.debug)

    p.say("Sir, which song do you want to wake you up")
    answer = p.get_input_str()
    if answer == "select":
        song_name, song_path = song.select()
    else:
        song_name, song_path = song.select_random()
        
    p.say("You selected " + song_name)

    # Set volume to something pleasant
    system_volume.set(conf.pleasant_wake_up_volume)
    
    # Sleep
    p.go_to_sleep_mode(chosen_option)
    
    # Wake up
    p.say("Good morning, Sir")
    
    # Play random song
    print("C-c to stop playing ")
    song.play(song_path)
    
    p.say("Have a nice day, Sir")

def printOptions(dic):
    for key in dic.keys():
        spaces = (20-len(key)) * " "
        print("         " + key + spaces +" - " + str(dic[key]/60) + " min") 
    print
    
