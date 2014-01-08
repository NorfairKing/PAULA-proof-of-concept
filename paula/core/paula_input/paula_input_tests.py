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

import sys
import unittest

from paula.core import exceptions

from . import integer


class Integer_Tests(unittest.TestCase):
    def fails_test(self):
        for (x,y) in [(i,i*i+1) for i in range(10) ]:
            print( str(x), str(y))
            self.assertRaises(exceptions.PAULABrokenContractException,integer.prompt_for_input_int_in_range,y,x)

