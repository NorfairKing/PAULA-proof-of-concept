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

from paula.core import exceptions
from . import parse_time


class Parse_Time_Tests(unittest.TestCase):
    ONE_SECOND = timedelta(days=0, seconds=1, minutes=0, hours=0, weeks=0)
    FIVE_SECONDS = timedelta(days=0, seconds=5, minutes=0, hours=0, weeks=0)

    def test_only_numeral(self):
        one_second_strings = ["1", "  1 ", "one", " one ", "One", "ONE"]
        for oss in one_second_strings:
            self.failUnlessEqual(Parse_Time_Tests.ONE_SECOND, parse_time.parse_delta(oss))

        five_seconds_strings = ["5", " 5 ", "five", " five ", "Five", "FIVE"]
        for fss in five_seconds_strings:
            self.failUnlessEqual(Parse_Time_Tests.FIVE_SECONDS, parse_time.parse_delta(fss))

        fails = ["xdmlk", "a", "zeros", "1a"]
        for f in fails:
            self.assertRaises(exceptions.PAULA_Not_An_Integer_Exception, parse_time.parse_delta, f)

    def test_numeral_and_quantifier(self):
        one_second_strings = ["1 second", "1 seconds", "one second", "One Second", "1 sec ", "one s", "ONE S"]
        for oss in one_second_strings:
            self.failUnlessEqual(Parse_Time_Tests.ONE_SECOND, parse_time.parse_delta(oss))

        five_seconds_strings = ["5 seconds", "5 second", "five second", "Five Second", "5 sec ", "five s", "FIVE S"]
        for fss in five_seconds_strings:
            self.failUnlessEqual(Parse_Time_Tests.FIVE_SECONDS, parse_time.parse_delta(fss))

        fails = ["xdm lk", "a b", "zeros 5"]
        for f in fails:
            self.assertRaises(exceptions.PAULA_Not_An_Integer_Exception, parse_time.parse_delta, f)

    def one_second_test(self):
        one_second_strings = ["1", "  1 ", "one", " one ", "One", "ONE", "1 second", "1 seconds", "one second",
                              "One Second", "1 sec ", "one s", "ONE S"]
        for oss in one_second_strings:
            self.failUnlessEqual(Parse_Time_Tests.ONE_SECOND, parse_time.parse_delta(oss))

    def five_seconds_test(self):
        five_seconds_strings = ["5", " 5 ", "five", " five ", "Five", "FIVE", "5 seconds", "5 second", "five second",
                                "Five Second", "5 sec ", "five s", "FIVE S"]
        for fss in five_seconds_strings:
            self.failUnlessEqual(Parse_Time_Tests.FIVE_SECONDS, parse_time.parse_delta(fss))

    def fails_test(self):
        fails = ["xdmlk", "a", "zeros", "1a","xdm lk", "a b", "zeros 5"]
        for f in fails:
            self.assertRaises(exceptions.PAULA_Parse_Exception, parse_time.parse_delta, f)