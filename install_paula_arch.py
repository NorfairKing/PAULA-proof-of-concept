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
import subprocess

from paula.core import system

PAULA_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'paula')
LIBS_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'libs')
FILENAME = "required_packages_arch"
SETUPFILE = "setup.py"

def get_required_packages():
    required_package_files = []
    for dirname, dirnames, filenames in os.walk(PAULA_DIR):
        for filename in filenames:
            if filename == FILENAME:
                required_package_files.append(os.path.join(dirname, filename))

    required_packages = []
    for file in required_package_files:
        for line in [i.strip() for i in open(file).readlines()]:
            required_packages.append(line)

    return required_packages


if __name__ == "__main__":
    for dirname, dirnames, filenames in os.walk(LIBS_DIR):
        for filename in filenames:
            if filename == SETUPFILE:
                system.call("cd " + dirname + " && python3 " + os.path.join(dirname, filename) + " build")
                system.call("cd " + dirname + " && sudo python3 " + os.path.join(dirname, filename) + " install")

    for package in get_required_packages():
        cmd = "packer -S " + package
        process = subprocess.Popen(cmd, shell=True)
        out, err = process.communicate()
