import sys, os

from paula.paula import Paula

if __name__ == "__main__":
    p = Paula()
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            p.say("Started")
            p.start()
            # Nothing can happen after this line.                                                        
        elif 'stop' == sys.argv[1]:
            p.stop()
        elif 'restart' == sys.argv[1]:
            p.restart()
        else:
            print "Unknown command"
            sys.exit(2)
        sys.exit(0)
    else:
        print p.decide_command("test")
        sys.exit(2)
