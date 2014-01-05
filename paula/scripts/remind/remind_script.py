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

from paula.core import outputs
from paula.core import interaction
from paula.core import schedule
from paula.core import parse
from paula.core import exceptions
from . import remind_script_config as conf


def execute(operand):
    debug("OPERAND = " + operand)

    if operand.strip() == "":
        outputs.print_error("Nothing to remind you of.")
        return

    if not "in" in operand: #TODO too hard coded?
        debug("no \"in\", Exiting.")
        return

    operand_parts = operand.split(" in ")
    content = " in ".join(operand_parts[:-1])
    moment = operand_parts[-1]

    if not " " in moment:
        debug("No space in moment, Exiting.")
        return

    try:
        delta = parse.time_delta(moment)
    except exceptions.PAULAParseException as e:
        outputs.print_error("An error occured while parsing the time delta.", error=e)
        return
    treated_content = treat_content(content)
    schedule.schedule_event_with_delta(delta, "paula_remind", treated_content)
    interaction.say_from_file(conf.CONFIRMATION_FILE)


def treat_content(content):
    content = ' ' + content + ' '
    treated = content.lower()

    for replace_str in conf.REPLACEMENTS:
        treated = treated.replace(" " + replace_str.lower() + " ", " " + conf.REPLACEMENTS[replace_str] + " ")

    treated = treated.replace("\"", "\\\"")
    treated = treated.replace("\'", "\\\'")

    debug("Replaced \"" + content + "\" with \"" + treated + "\".")
    return treated.strip()


def debug(string):
    if conf.DEBUG:
        outputs.print_debug(string)
