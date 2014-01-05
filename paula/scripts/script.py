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
The script class. Every one of PAULA's scripts will be a subclass of this class?
"""

from abc import ABCMeta, abstractmethod


class Script(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def execute(self, operand):
        pass

    @abstractmethod
    def debug(self):
        pass