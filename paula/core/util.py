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
This might be the ugliest code ever, but it works, be weary when cleaning!
"""

from .paula_util import directory_util
from .paula_util import module_util
from .paula_util import resource_util

# directory utils
def make_dir_if_nonexistent(path):
    directory_util.make_if_nonexistent(path)


# module utils
def get_this_module():
    return module_util.get_this_module()


def get_config_module():
    return module_util.get_config_module()


def get_debug():
    return module_util.get_debug()


def debug(string):
    return module_util.debug(string)


def get_this_file():
    return module_util.get_this_file()


def get_this_directory():
    return module_util.get_this_directory()


# resource utils
def get_resource_directory():
    return resource_util.get_resource_directory()


def get_resource_path(file_name):
    return resource_util.get_resource_path(file_name)

