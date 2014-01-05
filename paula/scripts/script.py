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

import importlib

from paula.core import outputs
from abc import ABCMeta, abstractmethod


class Script(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def execute(self, operand):
        pass

    def debug(self,string):
        if self.get_config_module().DEBUG:
            outputs.print_debug(string)
        pass

    def get_config_module(self):
        configfile = self.__module__ + "_config"
        print(configfile)
        return importlib.import_module(configfile)