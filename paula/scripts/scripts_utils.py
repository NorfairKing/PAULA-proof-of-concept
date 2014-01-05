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

import re
from paula.core import outputs
from . import scripts_config as conf

def package_to_class_name(package):
    package_parts = package.split("_")
    package_parts = [ p.capitalize() for p in package_parts]
    result = ''.join(package_parts) + "Script"
    debug("Class name for package name \"" + package + "\" is \"" + result + "\"")
    return result

def class_name_to_package(class_name):
    regex = '[A-Z][^A-Z]*'
    class_name_parts = re.findall(regex , class_name)
    lowered = [c.lower() for c in class_name_parts]
    result = "_".join(lowered)
    debug("package name for package name \"" + class_name + "\" is \"" + result + "\"")
    return result

def debug(string):
    """
    Shows the given string as debug info if debug is toggled on.
    @param string: The given string.
    """
    if conf.DEBUG:
        outputs.print_debug(string)