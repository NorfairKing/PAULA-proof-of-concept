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

from paula.scripts.script import Script
from paula.scripts.script_controller import ScriptController

from paula.core import inputs


class TrainingScript(Script):
    def execute(self, operand):
        sc = ScriptController(parent=".training")
        script, new_operand = sc.decide_meaning(operand)
        if script:
            sc.execute(script, new_operand)
        else:
            script = inputs.get_item_from_list(sc.scripts_dict.keys())
            sc.execute(script, new_operand)
