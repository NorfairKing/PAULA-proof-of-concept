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
Googles something for the user.
"""

from paula.scripts.script import Script
from paula.external import browser


class GoogleScript(Script):
    def execute(self, operand):
        self.debug("Search terms: " + operand)
        browser.open("http://www.google.com/search?q=" + operand)