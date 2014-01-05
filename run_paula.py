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

"""
    PAULA's master run file.
"""

import sys

from paula.paula import Paula

START_COMMAND = 'start'
STOP_COMMAND = 'stop'
RESTART_COMMAND = 'restart'

if __name__ == "__main__":
    PAULA = Paula()
    ALL_ARGUMENTS = " ".join(sys.argv[1:])
    if len(sys.argv) == 2:
        ARGUMENT = sys.argv[1]
        if ARGUMENT == START_COMMAND:
            PAULA.start()
            exit(0)
        elif ARGUMENT == STOP_COMMAND:
            PAULA.stop()
            exit(0)
        elif ARGUMENT == RESTART_COMMAND:
            PAULA.restart()
            exit(0)

    PAULA.respond_to(ALL_ARGUMENTS)
