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
Any resource utility functions
"""

import os

from . import module_util
from . import paula_util_config as conf


def get_resource_directory():
    return os.path.join(module_util._get_directory(), conf.DEFAULT_RESOURCE_DIR_NAME)


def get_resource_path(file_name):
    resource_dir = os.path.join(module_util._get_directory(), conf.DEFAULT_RESOURCE_DIR_NAME)
    return os.path.join(resource_dir, file_name)

