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
The Boolean input module.
"""

from . import string

from paula.core import interaction
from paula.core import outputs


def prompt_for_input_boolean(prompt=""):
    """
    Prompt the user for a boolean, optionally given a specific prompt.
    @param prompt: A given prompt string
    @return: A boolean of the user's choice.
    """
    while True:
        answer = string.prompt_for_input_string(prompt=prompt)
        if interaction.means(answer, "yes"):
            return True
        elif interaction.means(answer, "no"):
            return False
        else:
            outputs.print_error("Not a Boolean value.")
