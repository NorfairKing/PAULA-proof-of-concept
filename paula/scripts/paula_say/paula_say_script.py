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
PAULA's plain say-script.
"""

from paula.scripts.script import Script
from paula.core import interaction


class PaulaSayScript(Script):
    def execute(self, operand):
        self.debug("Saying " + operand)
        interaction.say(operand, sync=True)