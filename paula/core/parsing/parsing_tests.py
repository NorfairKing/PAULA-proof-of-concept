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
    TEN_SECONDS = timedelta(days=0, seconds=10, minutes=0, hours=0, weeks=0)
    TWO_MINUTES = timedelta(days=0, seconds=0, minutes=2, hours=0, weeks=0)
    SIX_HOURS = timedelta(days=0, seconds=0, minutes=0, hours=6, weeks=0)
    THREE_DAYS = timedelta(days=3, seconds=0, minutes=0, hours=0, weeks=0)
    FOUR_WEEKS = timedelta(days=0, seconds=0, minutes=0, hours=0, weeks=4)

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

    def ten_seconds_test(self):
        ten_seconds_strings = ["10", " 10 ", "ten", " ten ", "Ten", "TEN", "10 seconds", "10 second", "ten second",
                               "Ten Second", "10 sec ", "ten s", "TEN S"]
        for fss in ten_seconds_strings:
            self.failUnlessEqual(Parse_Time_Tests.TEN_SECONDS, parse_time.parse_delta(fss))

    def two_minutes_test(self):
        two_minutes_strings = ["2 min", "2 minutes", "two minutes", "Two Minute", "2 m ", "two m", "TWO M"]
        for oss in two_minutes_strings:
            self.failUnlessEqual(Parse_Time_Tests.TWO_MINUTES, parse_time.parse_delta(oss))

    def six_hours_test(self):
        six_hours_strings = ["6 h", "6 hours", "six hours", "Six Hour", "6 hour ", "six h", "SIX HOURS"]
        for oss in six_hours_strings:
            self.failUnlessEqual(Parse_Time_Tests.SIX_HOURS, parse_time.parse_delta(oss))

    def three_days_test(self):
        three_days_strings = ["3 d", "3 days", "three days", "Three Day", "3 D ", "three day", "THREE DAYS"]
        for oss in three_days_strings:
            self.failUnlessEqual(Parse_Time_Tests.THREE_DAYS, parse_time.parse_delta(oss))

    def four_weeks_test(self):
        four_weeks_strings = ["4 w", "4 weeks", "four weeks", " Four Week", "4 W ", " four week ", "FOUR WEEKS"]
        for oss in four_weeks_strings:
            self.failUnlessEqual(Parse_Time_Tests.FOUR_WEEKS, parse_time.parse_delta(oss))

    def fails_test(self):
        fails = ["xdmlk", "a", "zeros", "1a", "xdm lk", "a b", "zeros 5", "a b c d e ", "five something"]
        for f in fails:
            print(f)
            self.assertRaises(exceptions.PAULA_Parse_Exception, parse_time.parse_delta, f)
