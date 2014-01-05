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
Documentation for this script.
"""

from paula.scripts.script import Script

from paula.core import interaction


class PaulaWorkingScript(Script):
    def execute(self, operand):
        """
        Documentation for the execute function
        @param operand: the operand for this script
        """
        interaction.say("I'm working, Sir.", sync=True)
        print(operand)
