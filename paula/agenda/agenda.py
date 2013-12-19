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

from paula.core import system


def print_default():
    print_agenda_for_next_five_days()


def print_agenda_for_next_five_days():
    call_agenda("agenda")


def print_week():
    call_agenda("calw", options_str="--width 23")


def print_month():
    call_agenda("calm", options_str="--width 23")


def call_agenda(command, options_str=""):
    process = system.call("gcalcli" + " " + options_str + " " + command, sync=True)

