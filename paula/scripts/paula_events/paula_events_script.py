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
Everything that PAULA can do with its events internally
"""

from paula.scripts.script_controller import ScriptController
from paula.scripts.script import Script

class PaulaEventsScript(Script):
    def execute(self, operand):
        sc = ScriptController(parent=".paula_events")
        sc.decide_and_run(operand)
