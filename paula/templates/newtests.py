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

import unittest

def boolean_test_method(args):
    return False

# Here's our "unit tests".
class testCase(unittest.TestCase):

    def testOne(self):
        self.failUnless(boolean_test_method(1))

    def testTwo(self):
        self.failIf(boolean_test_method(2))

def test():
    unittest.main()