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

import os

debug = False

PAULA_DIR = os.path.dirname(os.path.realpath(__file__))

# Pid file
PAULA_PID_FILE = '/tmp/paula.pid'

#Std streams
PAULA_OUT_FILE = '/tmp/paula_out'
PAULA_ERR_FILE = '/tmp/paula_err'

# Logging config
PAULA_LOG_FILE = '/tmp/paula_log'
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
LOG_DATEFORMAT = '%Y-%m-%d %H:%M:%S'
LOG_MAXBYTES = 10000
LOG_BACKUPCOUNT = 5

# Seconds between check
CHECK_TIMER = 60
