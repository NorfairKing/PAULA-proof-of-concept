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
import time
import datetime
import subprocess
from paula.sleep import sleep
from paula.core import inputs
from paula.core import outputs
from paula.core import interaction
from paula.music import song
from paula.music import system_volume
from paula.motivation import quote
from paula.agenda import agenda

from . import sleep_script_config as conf


def execute(operand):
    interaction.say("How long would you like to sleep, Sir?")

    option = inputs.get_item_from_dict(conf.DURATION_OPTIONS)

    # select song
    interaction.say("Please select which song you want to wake you up.")
    s = song.choose()

    interaction.say_from_file(conf.NIGHT_FILE, sync=True)

    # Set volume to something pleasant
    system_volume.set(conf.PLEASANT_WAKE_UP_VOLUME)

    # Sleep
    sleep.go_to_sleep_mode(int(option))

    # Alarm go off
    interaction.say_from_file(conf.MORNING_FILE, sync=True)
    now = datetime.datetime.now()
    hour_min = 'It is %H:%M'
    if now.hour < 9:
        hour_min += "in the morning."
    interaction.say(now.strftime(hour_min), sync=True)

    month_day = "We are the %d"
    day = now.day
    if day in conf.DAY_SUFFIXES.keys():
        month_day += conf.DAY_SUFFIXES[day]
    else:
        month_day += "th"
    month_day += ' %b %Y'
    interaction.say(now.strftime(month_day), sync=True)

    subp = s.play()
    answer = inputs.get_string_timeout(conf.WAKE_UP_TIME)

    if not answer:
    # Wait until the song has finished
        subp.wait()
        if conf.ANNOYING:
            try:
                def saynwait(text, delay):
                    outputs.say(text)
                    time.sleep(delay)

                while system_volume.get() < 95:
                    for sentence in [i.strip() for i in open(conf.ANNOYING_ALARM_TEXT).readlines()]:
                        saynwait(sentence, 1)
                    system_volume.set(system_volume.get() + 5)

                for filename in [f for f in os.listdir(conf.RESOURCES_DIR) if
                                 os.path.isfile(os.path.join(conf.RESOURCES_DIR, f))]:
                    if filename.endswith(".mp3"):
                        path = os.path.join(conf.RESOURCES_DIR, filename)
                        alarm_process = playalarm(path)
                        alarm_process.wait()

            except KeyboardInterrupt:
                time.sleep(1)

    back = True
    try:
        subp.kill()
    except ProcessLookupError:
        pass

    interaction.say_from_file(conf.UP_FILE)

    # Show quote
    print((str(quote.get_random())))

    # Get agenda for next few days
    agenda.print_default()


def playalarm(path):
    cmd = ['play', path]
    null = open(os.devnull, 'w')

    process = subprocess.Popen(cmd, shell=False, stdout=null, stderr=null)
    return process

def debug(string):
    if conf.DEBUG:
        outputs.print_debug(string)