#!/usr/bin/env python
##
#      ____   _   _   _ _        _    
#     |  _ \ / \ | | | | |      / \   
#     | |_) / _ \| | | | |     / _ \  
#     |  __/ ___ \ |_| | |___ / ___ \ 
#     |_| /_/   \_\___/|_____/_/   \_\
#
#
# Personal
# Artificial
# Unintelligent
# Life
# Assistant
#
##

    
     
import sys, time
from daemon import Daemon
import logging
import logging.config
import config as conf
import voice
import decide

class Paula(Daemon):
    
    def __init__(self):
        super(Paula, self).__init__(conf.pid_file, stdout=conf.out_file, stderr=conf.err_file)
        
        # Logging
        self.log = logging.getLogger('PAULA')
        self.log.setLevel(logging.DEBUG)
        formatter = logging.Formatter(conf.log_format,datefmt=conf.log_dateFormat)
        fileHandler = logging.handlers.RotatingFileHandler(conf.log_file, mode='a', maxBytes=conf.log_maxBytes, backupCount=conf.log_backupCount)      
        fileHandler.setFormatter(formatter)  
        self.log.addHandler(fileHandler)
    
    def say(self, text):
        print("PAULA:   " + text)
        voice.say(text)    

    def decide_command(self, command):
        decide.command(command)

    def check(self):
        pass

    def run(self):
        while True:
            self.log.info('Check start')
            self.check()
            self.log.info('Check done \n')
            time.sleep(conf.check_timer) 

if __name__ == "__main__":
    paula = Paula()
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            paula.say("Started")
            paula.start()
            # Nothing can happen after this line.
        elif 'stop' == sys.argv[1]:
            paula.stop()
        elif 'restart' == sys.argv[1]:
            paula.restart()
        else:
            print "Unknown command"
            sys.exit(2)
        sys.exit(0)
    else:
        print "usage: %s start|stop|restart" % sys.argv[0]
        sys.exit(2)

