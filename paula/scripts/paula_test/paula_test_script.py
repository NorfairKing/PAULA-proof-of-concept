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

from paula.scripts.script import Script

from paula.core import outputs
from paula.core import interaction

from . import paula_test_script_config as conf


class PaulaTestScript(Script):
    def execute(self,operand):
        if conf.DEBUG:
            self.debug("The arguments to execute this script were the following.")
            self.debug(operand)


        # <Test here>
            
        # </Test here>
