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

from datetime import timedelta

from paula.core import outputs
from paula.core import exceptions
from paula.core import interaction
from . import parsing_config as conf


def parse_datetime(string):
    raise exceptions.PAULAUnimplementedFeatureException


def parse_delta(string):
    string = string.strip()

    while string.endswith("."):
        string = string.rstrip(".")

    if not " " in string:
        debug("No space in string")
        return only_numeral(string)
    else:
        return numeral_and_quantifier(string)


def only_numeral(string):
    numeral = get_numeral_int(string)
    return timedelta(seconds=numeral)


def numeral_and_quantifier(string):
    if len(string.split()) != 2: #TODO is this too hard coded?
        raise exceptions.PAULAParseException("Too many spaces to parse:  \"" + string + "\"")
    numeral, quantifier = string.split()
    num = get_numeral_int(numeral)
    delta_seconds = 0
    delta_minutes = 0
    delta_hours = 0
    delta_days = 0
    delta_weeks = 0

    if interaction.means(quantifier, "seconds"):
        delta_seconds = num
    elif interaction.means(quantifier, "minutes"):
        delta_minutes = num
    elif interaction.means(quantifier, "hours"):
        delta_hours = num
    elif interaction.means(quantifier, "days"):
        delta_days = num
    elif interaction.means(quantifier, "weeks"):
        delta_weeks = num
    else:
        raise exceptions.PAULAUnknownQuantifierException

    delta = timedelta(days=delta_days, seconds=delta_seconds, minutes=delta_minutes, hours=delta_hours,
                      weeks=delta_weeks)
    return delta


def get_numeral_int(string):
    lowered = string.strip().lower()
    if lowered in conf.DIGITS:
        return conf.DIGITS[lowered]

    try:
        numeral_int = int(string)
    except ValueError:
        raise exceptions.PAULANotAnIntegerException
    return numeral_int


def debug(string):
    if conf.DEBUG:
        outputs.print_debug(string)
