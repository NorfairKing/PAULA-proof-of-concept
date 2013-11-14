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

import subprocess


def get_default():
    get_agenda_for_next_five_days()


def get_agenda_for_next_five_days():
    call_agenda("agenda")


def get_week():
    call_agenda("calw", options_str="--width 23")


def get_month():
    call_agenda("calm", options_str="--width 23")


def call_agenda(command, options_str=""):
    cmd = "gcalcli" + " " + options_str + " " + command
    process = subprocess.Popen(cmd, shell=True)
    out, err = process.communicate()

