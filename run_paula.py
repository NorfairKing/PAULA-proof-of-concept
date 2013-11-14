import sys

from paula.paula import Paula
from paula.core import interaction

if __name__ == "__main__":
    p = Paula()
    all_args = " ".join(sys.argv[1:])
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            p.say("Started")
            p.start()
        elif 'stop' == sys.argv[1]:
            p.stop()
        elif 'restart' == sys.argv[1]:
            p.restart()
    interaction.say("Hello, Sir")
    p.respond_to(all_args)
