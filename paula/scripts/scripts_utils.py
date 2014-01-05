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
Any utilisation methods for the scripts package.
"""

from paula.core import outputs
from . import scripts_config as conf

def package_to_class_name(package):
    package_parts = package.split("_")
    package_parts = [ p.capitalize() for p in package_parts]
    result = ''.join(package_parts) + "Script"
    debug("Class name for package \"" + package + "\" is \"" + result + "\"")
    return result

def debug(string):
    """
    Shows the given string as debug info if debug is toggled on.
    @param string: The given string.
    """
    if conf.DEBUG:
        outputs.print_debug(string)