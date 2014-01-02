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

import time
import logging
import logging.config

from .daemon import Daemon
from paula import config as conf
from paula.scripts.script import ScriptController
from paula.core import outputs
from paula.core import schedule
from paula.core import system


class Paula(Daemon):
    def __init__(self):
        super(Paula, self).__init__(conf.PAULA_PID_FILE, std_out=conf.PAULA_OUT_FILE, std_err=conf.PAULA_ERR_FILE,
                                    started_error="PAULA is already running.", stopped_error="PAULA is not running.")

        # Logging
        self.log = logging.getLogger('PAULA')
        self.log.setLevel(logging.DEBUG)
        formatter = logging.Formatter(conf.LOG_FORMAT, datefmt=conf.LOG_DATEFORMAT)
        fileHandler = logging.handlers.RotatingFileHandler(conf.PAULA_LOG_FILE, mode='a', maxBytes=conf.LOG_MAXBYTES,
                                                           backupCount=conf.LOG_BACKUPCOUNT)
        fileHandler.setFormatter(formatter)
        self.log.addHandler(fileHandler)

    def info(self, text):
        self.log.info(text)

    def error(self, error_str):
        self.log.error(error_str)

    def debug(self, text):
        self.log.debug(text)

    def respond_to(self, string):
        self.debug("Deciding " + string)
        sc = ScriptController()
        sc.decide_and_run(string)
        self.debug("Done with " + string)

    def check(self):
        for e in schedule.get_overdue_events():
            debug("Found event to be overdue " + str(e))
            cmd = "urxvt -title PAULA -e bash -c \"" + conf.PAULA_EXECUTABLE + " " + e.command + " " + e.operand + "\""
            debug("executing " + cmd)
            system.call(cmd, sync=True)

            e.delete()

    def run(self):
        while True:
            self.info('Check start')
            self.check()
            self.info('Check done \n')
            time.sleep(conf.CHECK_TIMER)


def debug(string):
    if conf.DEBUG:
        outputs.print_debug(string)
        
