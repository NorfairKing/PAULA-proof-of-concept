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

import sys
import os
import time
import atexit
from signal import SIGTERM

PANIC_MESSAGE = "PAULA PANIC: "
FORK_1_FAILED_ERROR = PANIC_MESSAGE + "FORK 1 FAILED"
FORK_2_FAILED_ERROR = PANIC_MESSAGE + "FORK 2 FAILED"


class Daemon(object):
    def __init__(self, pid_file, std_in='/dev/null', std_out='/dev/null', std_err='/dev/null',
                 started_error="DAEMON ALREADY RUNNING", stopped_error="DAEMON NOT RUNNING"):
        self.std_in = std_in
        self.std_out = std_out
        self.std_err = std_err
        self.pid_file = pid_file
        self.started_error = started_error
        self.stopped_error = stopped_error

    def daemonize(self):
        # Unix double fork magic
        try:
            pid = os.fork()
            if pid > 0:
                # exit first parent
                sys.exit(0)
        except OSError as e:
            sys.stderr.write(FORK_1_FAILED_ERROR)
            sys.exit(1)

        # decouple from parent environment
        os.chdir("/")
        os.setsid()
        os.umask(0)

        # do second fork
        try:
            pid = os.fork()
            if pid > 0:
                # exit from second parent
                sys.exit(0)
        except OSError as e:
            sys.stderr.write(FORK_2_FAILED_ERROR)
            sys.exit(1)

            # redirect standard file descriptors
        sys.stdout.flush()
        sys.stderr.flush()
        si = open(self.std_in, 'r')
        so = open(self.std_out, 'a')
        se = open(self.std_err, 'a')
        os.dup2(si.fileno(), sys.stdin.fileno())
        os.dup2(so.fileno(), sys.stdout.fileno())
        os.dup2(se.fileno(), sys.stderr.fileno())

        # write pidfile
        atexit.register(self.delpid)
        pid = str(os.getpid())
        open(self.pid_file, 'w+').write("%s\n" % pid)

    def delpid(self):
        os.remove(self.pid_file)

    def start(self):
        # Check for a pidfile to see if the daemon already runs
        try:
            pf = open(self.pid_file, 'r')
            pid = int(pf.read().strip())
            pf.close()
        except IOError:
            pid = None

        if pid:
            sys.stderr.write(self.started_error)
            sys.exit(1)


        # Start the daemon
        self.daemonize()
        self.run()

    def stop(self):
        # Get the pid from the pidfile
        try:
            pf = open(self.pid_file, 'r')
            pid = int(pf.read().strip())
            pf.close()
        except IOError:
            pid = None

        if not pid:
            sys.stderr.write(self.stopped_error)
            return # not an error in a restart

        # Try killing the daemon process    
        try:
            while 1:
                os.kill(pid, SIGTERM)
                time.sleep(0.1)
        except OSError as err:
            err = str(err)
            if err.find("No such process") > 0:
                if os.path.exists(self.pid_file):
                    os.remove(self.pid_file)
                if os.path.exists(self.std_out):
                    os.remove(self.std_out)
                if os.path.exists(self.std_err):
                    os.remove(self.std_err)
            else:
                print((str(err)))
                sys.exit(1)

    def restart(self):
        self.stop()
        self.start()

    def run(self):
        pass