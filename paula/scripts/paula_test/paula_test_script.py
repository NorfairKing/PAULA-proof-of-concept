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


class PaulaTestScript(Script):
    def execute(self, operand):
        self.debug("The arguments to execute this script were the following.")
        self.debug(operand)


        # <Test here>
        from paula.core import util

        print(util.get_this_module())
        print(util.get_config_module())
        print(util.get_debug())
        print(util.get_this_file())
        print(util.get_this_directory())
        print(util.get_resource_directory())
        print(util.get_resource_path('some_resource.txt'))
        # </Test here>


