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
paula_test: The developers test package.
Here, developers test their newly implemented features, or part of them.
"""

from paula.core import config

from . import paula_test_script_config as conf

config.make_default_config_file_if_nonexistent(__package__, conf.DEFAULT_CONFIG_FILE)