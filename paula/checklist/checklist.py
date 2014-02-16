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
        with open(self.source_path) as f:
            self.items = f.readlines()

        #FIXME delete endlines
        self.items = (line.rstrip('\n') for line in self.items)

    def check(self):
        """
        Check every item on this checklist, according to the appropriate settings.
        """
        for item in self.items:
            speech.say(item, sync=True)