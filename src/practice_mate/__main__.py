import pygame
import pygame_menu

from practice_mate.ui_utility import *
from practice_mate.guitar.tuning import KNOWN_TUNINGS, EStandard
from practice_mate.practice import name_the_note, name_the_note_timed

pygame.init()

FRETS = 24
TUNING = EStandard
DISPLAY_SURFACE = pygame.display.set_mode(DISPLAY_SIZE)


def main():
    menu = pygame_menu.Menu(*MENU_SIZE, "Practice Mate", theme=pygame_menu.themes.THEME_DARK)
    menu.add_text_input("Frets: ", default="24", onchange=set_frets)
    menu.add_selector("Tuning :", [(i.name, i) for i in KNOWN_TUNINGS], onchange=set_tuning)
    menu.add_button("Select Practice", select_practice)
    menu.add_button("Quit", pygame_menu.events.EXIT)

    menu.mainloop(DISPLAY_SURFACE)


def set_frets(value):
    try:
        FRETS = int(value)
    except ValueError:
        FRETS = 24


def set_tuning(_, value):
    try:
        TUNING = value
    except ValueError:
        TUNING = EStandard


def select_practice():
    menu = pygame_menu.Menu(*MENU_SIZE, "Select Practice", theme=pygame_menu.themes.THEME_DARK)
    menu.add_button("Name the Note", lambda: name_the_note(FRETS, TUNING, DISPLAY_SURFACE))
    menu.add_button("Name the Note [Timed]", lambda: name_the_note_timed(FRETS, TUNING, DISPLAY_SURFACE))
    menu.add_button("Name the Note [Quiz]", lambda: name_the_note(FRETS, TUNING, DISPLAY_SURFACE))
    menu.add_button("Quit", pygame_menu.events.EXIT)

    menu.mainloop(DISPLAY_SURFACE)
