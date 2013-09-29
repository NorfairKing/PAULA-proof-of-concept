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

class Paula(Daemon):
    pid_file = '/tmp/paula.pid'
    out_file = '/tmp/paula_out'
    err_file = '/tmp/paula_err'
    log_file = '/tmp/paula_log'

    def __init__(self):
        super(Paula, self).__init__(Paula.pid_file, stdout=Paula.out_file, stderr=Paula.err_file)
        
        # Logging
        self.log = logging.getLogger('PAULA')
        self.log.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',datefmt='%Y-%m-%d %H:%M:%S')
        fileHandler = logging.handlers.RotatingFileHandler(Paula.log_file, mode='a', maxBytes=10000, backupCount=5)      
        fileHandler.setFormatter(formatter)  
        self.log.addHandler(fileHandler)

    def check(self):
        pass

    def run(self):
        while True:
            self.log.info('Check start')
            self.check()
            self.log.info('Check done \n')
            time.sleep(60)
 
if __name__ == "__main__":
    paula = Paula()
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            paula.start()
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

