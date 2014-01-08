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
The Training script
"""

import importlib

from paula.scripts.script import Script
from paula.scripts.script_controller import ScriptController

from paula.core import inputs
from paula.core import outputs


class TrainingScript(Script):
    def execute(self, operand):
        sc = ScriptController(parent=".training")
        script, new_operand = sc.decide_meaning(operand)
        if script:
            sc.execute(script, new_operand)
        else:
            script = inputs.get_item_from_list(sc.scripts_dict.keys())
            script_module = self.load(script)
            if script_module:
                script_module.execute(new_operand)

    def load(self, script_name):
        try:
            module_name = "paula.scripts.training." + script_name + "." + script_name + "_script"
            self.debug("Importing module: " + module_name)
            module = importlib.import_module(module_name)
        except ImportError:
            outputs.print_error(
                "The " + script_name + " script is missing or does not exist. Either that or some import fails inside the script.")
            return
        return module
