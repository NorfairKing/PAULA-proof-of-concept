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

import os
import platform
from os.path import expanduser
from paula.core import outputs
from paula.core import system

PAULA_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'paula')
LIBS_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'libs')


def get_required_packages(distribution):
    FILE_NAME = "required_packages_" + distribution
    required_package_files = []
    for dirname, dirnames, filenames in os.walk(PAULA_DIR):
        for filename in filenames:
            if filename == FILE_NAME:
                required_package_files.append(os.path.join(dirname, filename))

    required_packages = []
    for file in required_package_files:
        for line in [i.strip() for i in open(file).readlines()]:
            required_packages.append(line)

    return required_packages


def install_libraries():
    SETUP_FILE = "setup.py"
    for dirname, dirnames, filenames in os.walk(LIBS_DIR):
        for filename in filenames:
            if filename == SETUP_FILE:
                system.call("cd " + dirname + " && python3 " + os.path.join(dirname, filename) + " build")
                system.call("cd " + dirname + " && sudo python3 " + os.path.join(dirname, filename) + " install")


if __name__ == "__main__":
    outputs.print_PAULA()
    outputs.print_color("INSTALLING PAULA", "red")

    (dist1, dist2, dist3) = platform.linux_distribution()

    if dist1 == "arch":
        cmd = "packer -S " + " ".join(get_required_packages("arch"))
        system.call(cmd)

    elif dist1 == "LinuxMint" or dist1 == "Ubuntu":
        cmd = "sudo apt-get install -y " + " ".join(get_required_packages("ubuntu"))
        system.call(cmd)

    else:
        print("ERROR: Your platform is not supported")
        exit(1)

    DOT_PAULA_DIR = expanduser("~/.PAULA")
    if not os.path.isdir(DOT_PAULA_DIR):
        os.mkdir(DOT_PAULA_DIR)

    outputs.print_color("INSTALLING PAULA DONE", "red")

