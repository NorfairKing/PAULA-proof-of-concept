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
import speak.voice as voice
import command.decide as decide

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
        script = decide.decide_command(command)        
        print("running "+ script)    
        execfile(script)
        #subprocess.call(script, shell=True)
        print("script done")

    def go_to_sleep_mode(self, seconds):
        if conf.debug:
            cmd = "rtcwake --dry-run --mode mem --seconds " + str(seconds)
        else:    
            cmd = "rtcwake --mode mem --seconds " + str(seconds)
        process = subprocess.Popen(cmd, shell=True)
        out, err = process.communicate()
        print(out, err)

    def check(self):
        pass

    def run(self):
        while True:
            self.log.info('Check start')
            self.check()
            self.log.info('Check done \n')
            time.sleep(conf.check_timer) 
