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

from paula.checklist.checklist import Checklist

class ChecklistScript(Script):
    def execute(self, operand):
        """
        Run the checklist of which the name is given by the operand for this script.
        @param operand: The operand for this script.
        """
        checklist_name = operand
        self.debug("Looking for a checklist with name: " + checklist_name)
        c = Checklist(checklist_name)
        c.check()