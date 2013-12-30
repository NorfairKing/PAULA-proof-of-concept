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

import sys
import os
import wave
import urllib
import pyaudio

from paula.core import system

import urllib.request
import urllib.error

def execute(operand):
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 16000
    RECORD_SECONDS = 4
    WAVE_OUTPUT_FILENAME = "/tmp/output.wav"

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("* recording")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

    with open("/tmp/output.wav") as f:
            system.call_silently("flac -f /tmp/output.wav")
            f = open('/tmp/output.flac','rb')
            flac_cont = f.read()
            result = speech_to_text(flac_cont)
            f.close()

    print("understood: " + result)

def speech_to_text(audio):
    req = urllib.request.Request('https://www.google.com/speech-api/v1/recognize?xjerr=1&client=chromium&lang=en-US', data=audio, headers={'Content-type': 'audio/x-flac; rate=16000'})

    try:
        ret = urllib.request.urlopen(req)
    except urllib.error.URLError:
        print("Error Transcribing Voicemail")
        sys.exit(1)
    answer = str(ret.read())
    result = answer[answer.find('utterance":"') + 12 : answer.find('","con')]
    return result