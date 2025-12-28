"""Demonstration of how StrEnums are used in Python."""

from enum import StrEnum


class Command(StrEnum):
    START = 'start'
    STOP = 'stop'
    STATUS = 'status'


def handle_command(cmd: Command) -> str:
    if cmd == Command.START:
        return 'Starting system...'
    elif cmd == Command.STOP:
        return 'Shutting down...'
    elif cmd == Command.STATUS:
        return 'All systems operational.'
    # Notice that there is no else statement needed for type checkers
    # Knows that all possibilities for type Command are exhausted

