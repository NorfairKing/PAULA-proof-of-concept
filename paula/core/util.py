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

import os
import inspect
import importlib

from . import core_config as conf
from . import outputs
from . import config


def make_dir_if_nonexistent(path):
    if not os.path.exists(path):
        os.mkdir(path)
        if conf.DEBUG:
            outputs.print_debug("Created " + path + " directory.")


def _get_module():
    frm = inspect.stack()[2]
    module = inspect.getmodule(frm[0])
    return module


def _get_file():
    """
    Get the file for the second to last caller.
    @return: The name of the file of the second to last calling method.
    """
    frm = inspect.stack()[2]
    file = inspect.getfile(frm[0])
    return file


def _get_directory():
    frm = inspect.stack()[2]
    file = inspect.getfile(frm[0])
    return os.path.dirname(file)


def _get_config_module():
    frm = inspect.stack()[2]
    module = inspect.getmodule(frm[0]).__name__
    parent, name = module.rsplit(conf.PACKAGE_DELIMITER, 1)
    config_module = parent + conf.PACKAGE_DELIMITER + name + conf.DEFAULT_CONFIG_FILE_SUFFIX
    return importlib.import_module(config_module)


def get_this_module():
    return _get_module().__name__


def get_config_module():
    return _get_config_module()


def get_debug():
    return _get_config_module().DEBUG or config.get_global_debug()


def debug(string):
    if _get_config_module().DEBUG or config.get_global_debug():
        outputs.print_debug(string)


def get_this_file():
    return _get_file()


def get_this_directory():
    return _get_directory()


def get_resource_directory():
    return os.path.join(_get_directory(), conf.DEFAULT_RESOURCE_DIR_NAME)


def get_resource_path(file_name):
    resource_dir = os.path.join(_get_directory(), conf.DEFAULT_RESOURCE_DIR_NAME)
    return os.path.join(resource_dir, file_name)

