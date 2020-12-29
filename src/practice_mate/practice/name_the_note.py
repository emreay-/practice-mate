from random import randint

from practice_mate.ui_utility import make_green
from practice_mate.guitar.tuning import Tuning
from practice_mate.guitar.fretboard import Fretboard


__all__ = ["name_the_note"]


def name_the_note(frets: int, tuning: Tuning):
    fretboard = Fretboard(frets=frets, tuning=tuning)

    while True:
        string_human_indexed = randint(1, fretboard.tuning.strings)
        string = string_human_indexed - 1
        fret = randint(0, fretboard.frets)

        input(make_green(f"String {string_human_indexed} at fret {fret}? "))
        print(fretboard.get_note(string, fret))
        print()
