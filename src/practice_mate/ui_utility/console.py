import os

__all__ = ["make_red", "make_green", "line_width", "print_border"]


def make_red(msg: str):
    return f"\033[0;91m{msg}\033[0;0m"


def make_green(msg: str):
    return f"\033[0;92m{msg}\033[0;0m"


def line_width() -> int:
    try:
        line_width = os.get_terminal_size().columns
    except OSError:
        line_width = 100
    return line_width


def print_border():
    print("=" * line_width() + "\n")
