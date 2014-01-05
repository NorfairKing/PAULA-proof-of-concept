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

from paula.core import system

from . import mock_script_config as conf


def execute(operand):
    cmd = ['vlc', '-Idummy', '--play-and-exit', '-vvv', conf.HAHA_FILE]
    process = system.call_list_silently(cmd, sync=False)
