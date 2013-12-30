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
The Decide module.

This module contains functionality to decide the meaning of a string.
"""

import os
import re

from . import command_config as conf
from paula.core import outputs


def decide_meaning(string):
    """
    Decides which meaning the given string has.
    @param string: A given string
    @return: A string, representing the meaning of the given string.
    """

    meaning_found = None
    for meaning in MEANINGS_DICT:
        if means(string, meaning):
            meaning_found = meaning
            break
    if conf.DEBUG:
        if meaning_found:
            outputs.print_debug("decided  " + string + " to mean " + meaning_found + ".")
        else:
            outputs.print_debug("No meaning found.")
    return meaning_found


def means(string, meaning):
    """
    Decides whether the given string has the given meaning.
    @param string: A given string.
    @param meaning: A string representing a meaning.
    @return: A boolean value indicating whether the given string has the given meaning as its meaning.
    """
    if not meaning in MEANINGS_DICT.keys():
        return None

    regexes = get_meaning_regexes(meaning)
    for reg_str in regexes:
        reg_str = make_regex_string(reg_str)
        if conf.IGNORE_CASING:
            reg = re.compile(reg_str, re.IGNORECASE)
        else:
            reg = re.compile(reg_str)
        if reg.match(string):
            return True
    return False


def make_regex_string(reg_str):
    """
    Makes a regex string of the given string.
    @param reg_str: A given string.
    @return: A regex in string form.
    """
    if not conf.MATCH_WHOLE_STRING:
        reg_str += ".*"
    else:
        reg_str = "^" + reg_str + "$"
    return reg_str


def calculate_meanings_dict():
    """
    Gets a dictionary mapping meanings to the path of the file containing their regexes.
    @return: The described dictionary
    """
    for f in os.listdir(conf.MEANINGS_DIR):
        if os.path.isfile(os.path.join(conf.MEANINGS_DIR, f)):
            path = os.path.join(conf.MEANINGS_DIR, f)
            MEANINGS_DICT[f] = path

    return MEANINGS_DICT


def get_meaning_regexes(meaning):
    """
    .Returns all regexes for the given meaning
    @param meaning: A string representing a given meaning.
    @return: A list of regexes in string format corresponding to the given meaning.
    """
    return [i.strip() for i in open(MEANINGS_DICT[meaning]).readlines()]


MEANINGS_DICT = {}
calculate_meanings_dict()
