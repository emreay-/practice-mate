from typing import Tuple

from practice_mate.ui_utility import *
from practice_mate.guitar.tuning import KNOWN_TUNINGS, Tuning
from practice_mate.practice import name_the_note


def main():
    frets, tuning = get_guitar_details()
    option = main_menu()
    print_border()

    if option == 1:
        name_the_note(frets, tuning)


def main_menu():
    while True:
        try:
            print("""Greetings fellow guitar player. Here's a mini tool to help you with your practice.
Please choose one from the below (the list will grow):\n
""")
            option = int(input(make_green("""1. NAME THE NOTE -- You will be ask to name the note at a string/fret combination
2. NAME THE NOTE [TIMED] -- Same as (1) except there will be an adjustable time out\n
""")))
        except ValueError:
            pass
        else:
            if 0 < option <= 2:
                return option


def get_guitar_details() -> Tuple[int, Tuning]:
    print("\n")

    frets = None
    for _ in range(3):
        try:
            frets = int(input(make_green("Number of frets on your guitar? ")))
        except ValueError:
            print("Invalid input, please enter an integer")
        else:
            if 0 < frets:
                break
            else:
                frets = None

    if frets is None:
        print("You seem to struggle, so for now let's set the frets as 24")
        frets = 24

    known_tunings = "\n".join([f"{i}.{t.name}" for i, t in enumerate(KNOWN_TUNINGS, 1)])
    tuning_index = None
    for _ in range(3):
        try:
            tuning_index = -1 + int(input(make_green(f"""\nChoose the tuning from the following:\n{known_tunings}\n\n""")))
        except ValueError:
            print("Invalid input, please enter an integer")
        else:
            if 0 <= tuning_index < len(KNOWN_TUNINGS):
                break
            else:
                tuning_index = None

    if tuning_index is None:
        print("You seem to struggle, so for now let's set the tuning as E Standard")
        tuning_index = 0

    print_border()

    return frets, KNOWN_TUNINGS[tuning_index]
