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
Any utilities the paula_config may require.
"""

import os
import shutil

from . import paula_config_config as conf


def init_default_config_file_if_nonexistent(package, default_config):
    """
    Initializes the default config file of a given package.
    @param package: The given package.
    @param default_config: The default config file.
    """
    config_file = os.path.join(conf.PAULA_USER_CONFIG_DIR, package + conf.CONFIG_EXTENSION)
    if not os.path.exists(config_file):
        shutil.copyfile(default_config, config_file)
