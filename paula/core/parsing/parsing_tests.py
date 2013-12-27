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
from datetime import timedelta
from datetime import datetime

from . import parse_time


class Parse_Time_Tests(unittest.TestCase):
    def test_one_second(self):
        one_second = timedelta(days=0, seconds=1, minutes=0, hours=0, weeks=0)
        one_second_strings = ["1 second", "1 seconds", "one second"]
        for oss in one_second_strings:
            self.failUnlessEqual(one_second,parse_time.parse_delta(oss))

    #def test_one_minute(self):
    #    pass
