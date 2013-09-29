#!/bin/bash

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

soundfile="/tmp/paula_speaks.wav"
pico2wave -l=en-GB -w="$soundfile" "$1"
aplay "$soundfile" > /dev/null 2>&1
rm "$soundfile"
exit 0
