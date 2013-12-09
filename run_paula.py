import sys

from paula.paula import Paula
START_COMMAND   = 'start'
STOP_COMMAND    = 'stop'
RESTART_COMMAND = 'restart'


if __name__ == "__main__":
    paula = Paula()
    all_arguments = " ".join(sys.argv[1:])
    if len(sys.argv) == 2:
        argument = sys.argv[1]
        if argument == START_COMMAND:
            paula.start()
            exit(0)
        elif argument == STOP_COMMAND:
            paula.stop()
            exit(0)
        elif argument == RESTART_COMMAND:
            paula.restart()
            exit(0)

    paula.respond_to(all_arguments)
