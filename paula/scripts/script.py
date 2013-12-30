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
The script recognition module.
"""

import os
import re
import time
import importlib

from paula.core import outputs
from . import script_config as conf


class ScriptController:
    def __init__(self, parent=""):
        self.parent = parent
        self.scripts_dict = self._calculate_scripts_dict()

    def decide_and_run(self, string):
        """
        Decides which script the given string represents and executes that script.
        @param string: A given string.
        @param parent: The parent package under which to look for the scripts.
        @return: Nothing whatsoever
        """
        outputs.print_PAULA()
        debug("Trying to decide " + string + " with parent " + self.parent)
        meaning, operand = self.decide_meaning(string)
        try:
            self.execute(meaning, operand)
        except KeyboardInterrupt:
            outputs.print_PAULA()
            debug("Exiting.")
            return
        time.sleep(conf.WAITING_TIME)

    def execute(self, script_name, operand):
        """
        Execute the given script with given operand under given parent.
        @param script_name: The name of the script to execute.
        @param operand: The given operand to the script.
        @param parent: The given parent.
        @return: Nothing.
        """
        if not script_name:
            return
        debug("Trying to execute " + script_name + " with \"" + operand + "\" as operand, a child of " + self.parent)

        try:
            module_name = "paula.scripts" + self.parent + "." + script_name + "." + script_name + "_script"
            debug("Importing module: " + module_name)
            module = importlib.import_module(module_name)
        except ImportError:
            outputs.print_error(
                "The " + script_name + " script is missing or does not exist. Either that or some import fails inside the script.")
            return
        module.execute(operand)


    def decide_meaning(self, string):
        """
        Decides to which script the given string belongs under a given parent.
        @param string: The given string.
        @param parent: The given parent.
        @return: Nothing.
        """
        meaning_found = None
        for name in self.scripts_dict:
            matched, operand = self.means(string, name)
            if matched:
                meaning_found = name
                break
        if conf.DEBUG:
            if meaning_found:
                outputs.print_debug("decided  " + string + " to mean " + meaning_found + ".")
            else:
                outputs.print_debug("No meaning found.")
        return meaning_found, operand


    def get_meaning_regexes(self, script):
        """
        Gets all the regexes that correspond to the given script
        @param script: The given script.
        @return: A list of regexes in string format corresponding to the given script.
        """
        return [i.strip() for i in open(self.scripts_dict[script]).readlines()]


    def means(self, string, script):
        """
        Decides whether a given string corresponds to a given script.
        @param string: The given string.
        @param script: The given script.
        @return: A tuple of a Boolean and the shortest possible operand.
        """
        if not script in self.scripts_dict:
            return False, None

        regexes = self.get_meaning_regexes(script)

        possible_operands = []

        for reg_str in regexes:
            reg = re.compile(reg_str, re.IGNORECASE)
            if reg.match(string):
                debug("Matched \"" + string + "\" with \"" + reg_str + "\"")
                #Got a match, now find the operand, remove the match_whole_string
                for i in reversed(range(len(string) + 1)):
                    string_part = string[:i]
                    debug("string part=\"" + string_part + "\"")
                    reg2 = re.compile("^" + reg_str + "$", re.IGNORECASE)
                    if reg2.match(string_part):
                        debug("Matched \"" + string_part + "\" with \"" + reg_str + "\"")
                        debug("string[i:]=\"" + string[i:] + "\"")
                        possible_operands.append(string[i:].strip())

        if not possible_operands:
            return False, None
        debug("matches= " + str(possible_operands))

        possible_operands.sort(key=lambda t: len(t))
        return True, possible_operands[0]


    def _calculate_scripts_dict(self):
        """
        Gets a dictionary mapping the script to the commands corresponding to them.
        @return: The described dictionary.
        """
        dict = {}
        debug("scripts dir= " + conf.DEFAULT_SCRIPTS_DIR)
        PARENT_DIR = os.path.join(conf.DEFAULT_SCRIPTS_DIR, self.parent.replace(".", "/")[1:])
        debug("parent dir = " + PARENT_DIR)
        for script in os.listdir(PARENT_DIR):
            to_be_checked = os.path.join(PARENT_DIR, script)
            if os.path.isdir(to_be_checked) and not to_be_checked.__contains__("__pycache__"):
                script_dir = os.path.join(PARENT_DIR, script)
                commands = os.path.join(script_dir, "script_commands")
                if os.path.isfile(commands):
                    dict[script] = commands
        return dict

def debug(string):
    """
    Shows the given string as debug info if debug is toggled on.
    @param string: The given string.
    """
    if conf.DEBUG:
        outputs.print_debug(string)
