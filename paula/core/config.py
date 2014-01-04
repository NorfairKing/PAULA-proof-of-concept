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
The module responsible for interaction with user configuration options.
"""

from .paula_config import user_configs


def get_config(package, config_option):
    return user_configs.get_config(package, config_option)


def make_default_config_file_if_nonexistent(package, default):
    return user_configs.make_default_config_file_if_nonexistent(package, default)