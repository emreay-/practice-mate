import pygame
import pygame_menu

from practice_mate.tools import *
from practice_mate.practice import *
from practice_mate.ui_utility import *
from practice_mate.guitar.tuning import KNOWN_TUNINGS, EStandard

pygame.init()

FRETS = 24
TUNING = EStandard
IS_PITCH_AWARE = True
DISPLAY_SURFACE = pygame.display.set_mode(DISPLAY_SIZE)


def main():
    menu = pygame_menu.Menu(*MENU_SIZE, "Practice Mate", theme=pygame_menu.themes.THEME_DARK)
    menu.add_text_input("Frets: ", default="24", onchange=set_frets)
    menu.add_selector("Tuning :", [(i.name, i) for i in KNOWN_TUNINGS], onchange=set_tuning)
    menu.add_selector("Pitch Awareness :", [("On", True), ("Off", False)], onchange=set_pitch_awareness)
    menu.add_button("Select Practice", select_practice)
    menu.add_button("Select Tool", select_tool)
    menu.add_button("Quit", pygame_menu.events.EXIT)

    menu.mainloop(DISPLAY_SURFACE)


def set_frets(value):
    global FRETS
    try:
        FRETS = int(value)
    except ValueError:
        FRETS = 24


def set_tuning(_, value):
    global TUNING
    TUNING = value


def set_pitch_awareness(_, value):
    global IS_PITCH_AWARE
    IS_PITCH_AWARE &= value


def select_practice():
    menu = pygame_menu.Menu(*MENU_SIZE, "Select Practice", theme=pygame_menu.themes.THEME_DARK)
    menu.add_button(
        "Name the Note", lambda: name_the_note(FRETS, TUNING, DISPLAY_SURFACE))
    menu.add_button(
        "Name the Note [Timed]", lambda: name_the_note_timed(FRETS, TUNING, DISPLAY_SURFACE))
    menu.add_button(
        "Name the Note [Quiz]", lambda: name_the_note_quiz(FRETS, TUNING, IS_PITCH_AWARE, DISPLAY_SURFACE))
    menu.add_button(
        "Quit", pygame_menu.events.EXIT)

    menu.mainloop(DISPLAY_SURFACE)


def select_tool():
    menu = pygame_menu.Menu(*MENU_SIZE, "Select Tool", theme=pygame_menu.themes.THEME_DARK)
    menu.add_button(
        "Interval Finder", lambda: interval_finder(DISPLAY_SURFACE))
    menu.add_button(
        "Quit", pygame_menu.events.EXIT)

    menu.mainloop(DISPLAY_SURFACE)
