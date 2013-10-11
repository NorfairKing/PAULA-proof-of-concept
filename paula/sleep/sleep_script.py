from paula.paula import Paula
from paula.music import song
import sleep_conf as conf

def execute():
    p = Paula()

    p.say("How long would you like to sleep, Sir?")

    answer = p.get_input_str()
    chosen_option = int(conf.duration_options[answer])
    
    p.debug("answer = " + answer, conf.debug)
    p.debug("selected option = " + str(chosen_option) + " seconds", conf.debug)
        

    #Sleep
    p.go_to_sleep_mode(chosen_option)
    
    p.say("Good morning, Sir")
    
    song.play()
