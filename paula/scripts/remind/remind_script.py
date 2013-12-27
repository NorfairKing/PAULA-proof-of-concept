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

import datetime

from paula.core import outputs
from paula.core import schedule
from paula.core import interaction
from . import remind_script_config as conf


def execute(operand):
    if conf.DEBUG:
        outputs.print_debug("OPERAND = " + operand)

    if not "in" in operand:
        if conf.DEBUG:
            outputs.print_debug("no \"in\", Exiting.")
        return

    content, moment = operand.split(" in ")

    if not " " in moment:
        if conf.DEBUG:
            outputs.print_debug("No space in moment, Exiting.")
        return

    delta = parse_delta(moment)
    treated_content = treat_content(content)
    schedule.schedule_event_with_delta(delta, "paula_remind", treated_content)


def parse_delta(moment):
    numeral, quantifier = moment.split()
    num = int(numeral)
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

    delta = datetime.timedelta(days=delta_days, seconds=delta_seconds, minutes=delta_minutes, hours=delta_hours,
                               weeks=delta_weeks)
    return delta


def treat_content(content):
    content = ' ' + content + ' '
    treated = content

    for replace_str in conf.REPLACEMENTS:
        treated = treated.replace(replace_str, conf.REPLACEMENTS[replace_str])

    if conf.DEBUG:
        outputs.print_debug("Replaced \"" + content + "\" with \"" + treated + "\".")
    return treated