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
Mocks the user.
"""

from paula.scripts.script import Script
from paula.core import system


class MockScript(Script):
    def execute(self, operand):
        cmd = ['vlc', '-Idummy', '--play-and-exit', '-vvv', self.get_resource_path('haha.mp3')]
        process = system.call_list_silently(cmd, sync=False)