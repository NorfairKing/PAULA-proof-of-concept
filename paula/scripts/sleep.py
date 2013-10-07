import os
import sys
from paula import Paula

p = Paula()
p.go_to_sleep_mode(16500)

p.say("Good morning, Sir")

from scripts import song
song.play()
