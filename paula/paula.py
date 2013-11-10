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
import subprocess
from .daemon import Daemon

import logging
import logging.config
import paula.config as conf
import paula.core.interaction as interaction
import paula.scripts.script as script

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
    
    def info(self,text):
        self.log.info(text)
    
    def error(self, error_str):
        self.log.error(error_str)

    def debug(self, text):
        self.log.debug(text)
    
    def respond_to(self, string):
        self.debug("Deciding " + string)
        meaning = interaction.decide_meaning(string)
        if meaning == "UNKNOWN":
            self.error("Meaning not recognised")
        else:
            script.execute(meaning)        
        self.debug("Done with " + string)

    def check(self):
        pass

    def run(self):
        while True:
            self.info('Check start')
            self.check()
            self.info('Check done \n')
            time.sleep(conf.check_timer) 
