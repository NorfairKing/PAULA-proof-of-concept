def execute():
    #import os
    #import sys
    from paula.paula import Paula

    p = Paula()
    # 16500 = 4.5 hours
    # 27300 = 7.5 hours
    p.go_to_sleep_mode(21900)
    
    p.say("Good morning, Sir")
    
    from paula.music import song
    song.play()
