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


class Checklist(object):
    def __init__(self, path):
        """
        Initialize this checklist with all its elements from a given path.
        @param path: The given path.
        """
        self.source_path = path
        with open(path) as f:
            self.items = f.readlines()

    def check(self):
        for item in self.items:
            print(item)