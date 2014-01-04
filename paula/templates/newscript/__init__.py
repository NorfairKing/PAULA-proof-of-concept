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
The Top-level documentation for this new script.
"""

from paula.core import config

from . import newscript_script_config as conf

config.make_default_config_file_if_nonexistent(__package__, conf.DEFAULT_CONFIG_FILE)