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

HERE="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

sudo apt-get install gcalcli

# Install sub modules
for dir in $(find "$HERE/" -mindepth 1 -maxdepth 1 -type d)
do 
    install_script="$dir/install.sh"
    if [ -f "$install_script" ]
    then
        echo "installing $(basename $dir)" 
        $install_script
    fi
done
