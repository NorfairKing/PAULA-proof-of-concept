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
from daemon import Daemon

import logging
import logging.config
import config as conf
import core.speak.voice as voice
import core.command.decide as decide
import sleep.sleep as sleep

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
    
    def log_i(self,text):
        self.log.info(text)
    
    def debug(self, text, option=conf.debug):
        if option:
            self.log.debug(text)
            print
            print(text)
            print
    
    def say(self, text):
        self.log_i("PAULA:   " + text)
        voice.say(text)    
    
    def get_input_str(self):
        answer = raw_input("YOU:     ")
        print
        return answer
    
    def get_input_int(self):
        return int(self.get_input_str())

    def decide_command(self, command):
        self.debug("Deciding " + command)
        script = decide.decide_command(command)        
        self.debug("Done with " + script)

    def go_to_sleep_mode(self, seconds):
        self.debug("Going to sleep mode for " + str(seconds) + " seconds.")
        sleep.go_to_sleep_mode(seconds)
        self.debug("Woke up")

    def check(self):
        pass

    def run(self):
        while True:
            self.log.info('Check start')
            self.check()
            self.log.info('Check done \n')
            time.sleep(conf.check_timer) 
