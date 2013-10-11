import os
import subprocess
import sleep_conf as conf
def go_to_sleep_mode(seconds):
    cmd = "rtcwake --mode mem "
    if conf.debug:
        cmd += "--dry-run "
    cmd += "--seconds " + str(seconds)
    
    null = open(os.devnull, 'w')
    process = subprocess.Popen(cmd, shell=True, stdout = null)
    out, err = process.communicate()
