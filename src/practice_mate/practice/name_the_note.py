from random import randint

import time
from tqdm import tqdm

from practice_mate.ui_utility import make_green
from practice_mate.guitar.tuning import Tuning
from practice_mate.guitar.fretboard import Fretboard


__all__ = ["name_the_note", "name_the_note_timed"]


def name_the_note(frets: int, tuning: Tuning):
    fretboard = Fretboard(frets=frets, tuning=tuning)

    while True:
        string_human_indexed = randint(1, fretboard.tuning.strings)
        string = string_human_indexed - 1
        fret = randint(0, fretboard.frets)

        input(make_green(f"String {string_human_indexed} at fret {fret}? "))
        print(fretboard.get_note(string, fret))
        print()


def name_the_note_timed(frets: int, tuning: Tuning):
    fretboard = Fretboard(frets=frets, tuning=tuning)
    timeout_seconds = get_timeout()

    while True:
        string_human_indexed = randint(1, fretboard.tuning.strings)
        string = string_human_indexed - 1
        fret = randint(0, fretboard.frets)

        timeout = tqdm(total=timeout_seconds, leave=False, bar_format="{bar}")
        print(make_green(f"String {string_human_indexed} at fret {fret}?"))
        for _ in range(timeout_seconds):
            time.sleep(1)
            timeout.update(1)
        tqdm._instances.clear()

        time.sleep(0.5)
        print(fretboard.get_note(string, fret))
        print("\n")


def get_timeout() -> int:
    seconds = None
    for _ in range(3):
        try:
            seconds = int(input(make_green("Number of seconds > 0 for timeout? ")))
        except ValueError:
            print("Invalid input, please enter an integer")
        else:
            if 0 < seconds:
                break
            else:
                seconds = None

    if seconds is None:
        print("You seem to struggle, so for now let's set the timeout as 20")
        seconds = 20

    return seconds
