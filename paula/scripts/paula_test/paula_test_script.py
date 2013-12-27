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

import os
from paula.core import outputs
from paula.core import interaction

from . import paula_test_script_config as conf


def execute(operand):
    if conf.DEBUG:
        outputs.print_debug("The arguments to execute this script were the following.")
        outputs.print_debug(operand)

    if conf.UNIT_TESTS:
        unit_tests()


    # <Test here>

    # </Test here>


def unit_tests():
    if conf.TEST_CORE:
        if conf.TEST_PARSING:
            from paula.core.parsing import parsing_tests
            parsing_tests.test()