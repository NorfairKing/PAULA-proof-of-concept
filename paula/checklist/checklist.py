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
PAULA checklist
"""

import os
from . import checklist_config as conf

from paula.core import speech

class Checklist(object):
    def __init__(self, name):
        """
        Initialize this checklist with all its elements from a name
        @param path: The given path.
        """
        self.name = name
        self.source_path = os.path.join(conf.CHECKLISTS_DIR, name + conf.CHECKLIST_EXTENSION)
        #TODO some error if the path doesn't exist, is a directory, or doesn't exist.

        if not (os.path.exists(self.source_path) and os.path.isfile(self.source_path)):
            self.items = []
            return

        with open(self.source_path) as f:
            lines = f.readlines()

        #Leave the first line blank if you want the default options.
        self.options_str = lines[0]
        self.items = lines[1:]
        self.options = self.parse_options(self.options_str)

        #FIXME delete endlines
        self.items = (line.rstrip('\n') for line in self.items)

    def parse_options(self,options_str):
        selected_options = options_str.split(" ")
        current_options = conf.DEFAULT_OPTIONS
        for option in selected_options:
            if option in current_options.keys():
                current_options[option] = not current_options[option] #FIXME make this more general for defaults that aren't false
        return current_options


    def check(self):
        """
        Check every item on this checklist, according to the appropriate settings.
        """
        for item in self.items:
            speech.say(item, sync=True)