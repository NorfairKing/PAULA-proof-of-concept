import os
import subprocess
from . import volume_conf as conf

def get():
    cmd = "amixer get Master | grep 'Mono:' | sed -e 's/^[^\[]*//' -e 's/^.//' -e 's/%.*$//'"
    
    null = open(os.devnull, 'w')
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    out, err = process.communicate()

    vol = int(out)
    return vol

def set(percent):
    cmd = "amixer set Master " + str(percent) + "%"

    null = open(os.devnull, 'w')
    if not conf.DEBUG:
        process = subprocess.Popen(cmd, shell=True, stdout = null, stderr = null)
    else:
        process = subprocess.Popen(cmd, shell=True)
    out, err = process.communicate()
    
def mute():
    set(0)
