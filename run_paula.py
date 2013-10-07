import sys, os

from paula.paula import Paula

if __name__ == "__main__":
    p = Paula()
    all_args = " ".join(sys.argv[1:])
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            p.say("Started")
            p.start()
            # Nothing can happen after this line.                                                        
        elif 'stop' == sys.argv[1]:
            p.stop()
        elif 'restart' == sys.argv[1]:
            p.restart()

    print ("deciding " + all_args)
    p.decide_command(all_args)
