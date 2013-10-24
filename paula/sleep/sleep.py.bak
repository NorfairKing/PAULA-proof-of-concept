import os
import subprocess
import sleep_conf as conf
def go_to_sleep_mode(seconds):
    cmd = "rtcwake --mode mem "
    if conf.DEBUG:
        cmd += "--dry-run "
    cmd += "--seconds " + str(seconds)
    
    null = open(os.devnull, 'w')
    if not conf.DEBUG:
        process = subprocess.Popen(cmd, shell=True, stdout = null, stderr = null)
        out, err = process.communicate()
    else:
        process = subprocess.Popen(cmd, shell=True)
        out, err = process.communicate()
    
