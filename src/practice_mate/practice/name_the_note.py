import time
from random import randint
from typing import Tuple, Dict
from collections import defaultdict

import pygame
import pygame_menu
from pygame.locals import *

from practice_mate.theory import Note
from practice_mate.ui_utility import *
from practice_mate.guitar.tuning import Tuning
from practice_mate.guitar.fretboard import Fretboard


__all__ = ["name_the_note", "name_the_note_timed"]


def random_fretboard_position(fretboard: Fretboard) -> Tuple[int, int]:
    string = randint(1, fretboard.strings)
    fret = randint(0, fretboard.frets)
    return string, fret


def name_the_note(frets: int, tuning: Tuning, surface: pygame.Surface):
    fretboard = Fretboard(frets=frets, tuning=tuning)
    string, fret = random_fretboard_position(fretboard)
    text = f"String {string} at fret {fret}? "

    font = pygame.font.SysFont(None, 68)
    text_surface = font.render(text, True, LIME)

    text_rectangle = text_surface.get_rect()
    text_rectangle.topleft = CENTER_RECT_TOP_LEFT

    running = True
    is_question_turn = False
    background = DARK_GRAY

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN:
                    is_question_turn = not is_question_turn

                    if is_question_turn:
                        string, fret = random_fretboard_position(fretboard)
                        text = f"String {string} at fret {fret}? "
                        text_surface = font.render(text, True, LIME)
                        text_rectangle = text_surface.get_rect()
                        text_rectangle.topleft = CENTER_RECT_TOP_LEFT
                    else:
                        text = f"{fretboard.get_note(string, fret)}"
                        text_surface = font.render(text, True, WHITE)
                        text_rectangle = text_surface.get_rect()
                        text_rectangle.topleft = (425, CENTER_RECT_TOP_LEFT[1])

                    text_rectangle.size = text_surface.get_size()

        surface.fill(background)
        surface.blit(text_surface, text_rectangle)
        pygame.display.update()

    pygame.quit()


def name_the_note_timed(frets: int, tuning: Tuning, surface: pygame.Surface):
    def _set(value):
        try:
            timeout = int(value)
        except ValueError:
            timeout = 20
        _name_the_note_timed(frets, tuning, timeout, surface)

    menu = pygame_menu.Menu(*MENU_SIZE, "Name the Note [TIMED]", theme=pygame_menu.themes.THEME_DARK)
    menu.add_text_input("Timeout in seconds: ", default="20", onreturn=_set)
    menu.mainloop(surface)


def _name_the_note_timed(frets: int, tuning: Tuning, timeout: int, surface: pygame.Surface):
    fretboard = Fretboard(frets=frets, tuning=tuning)
    string, fret = random_fretboard_position(fretboard)

    font = pygame.font.SysFont(None, 68)

    clock = pygame.time.Clock()
    pygame.time.set_timer(pygame.USEREVENT, 1000)

    text = f"Press ENTER to start"
    text_surface = font.render(text, True, LIME)
    text_rectangle = text_surface.get_rect()
    text_rectangle.topleft = CENTER_RECT_TOP_LEFT

    counter, counter_text = timeout, f"{timeout}".rjust(3)
    counter_surface = font.render(counter_text, True, LIME)
    counter_rectangle = counter_surface.get_rect()
    counter_rectangle.topleft = (425, 150)

    running = True
    is_question_turn = False
    background = DARK_GRAY

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN:
                    is_question_turn = not is_question_turn

                    if is_question_turn:
                        string, fret = random_fretboard_position(fretboard)
                        text = f"String {string} at fret {fret}? "
                        text_surface = font.render(text, True, LIME)
                        text_rectangle = text_surface.get_rect()
                        text_rectangle.topleft = CENTER_RECT_TOP_LEFT
                        text_rectangle.size = text_surface.get_size()

                        counter = timeout
                        counter_text = str(counter).rjust(3) if counter > 0 else ""
                        counter_surface = font.render(counter_text, True, LIME)
                        counter_rectangle = counter_surface.get_rect()
                        counter_rectangle.topleft = (425, 150)
                        counter_rectangle.size = counter_surface.get_size()
                    else:
                        text = f"{fretboard.get_note(string, fret)}"
                        text_surface = font.render(text, True, WHITE)
                        text_rectangle = text_surface.get_rect()
                        text_rectangle.topleft = (425, CENTER_RECT_TOP_LEFT[1])
                        text_rectangle.size = text_surface.get_size()

                        counter = timeout
                        counter_text = ""
                        counter_surface = font.render(counter_text, True, LIME)
                        counter_rectangle.size = counter_surface.get_size()

            if event.type == pygame.USEREVENT:
                if is_question_turn:
                    counter -= 1
                    counter_text = str(counter).rjust(3) if counter > 0 else ""

                    if counter == 0:
                        is_question_turn = False
                        text = f"{fretboard.get_note(string, fret)}"
                        text_surface = font.render(text, True, WHITE)
                        text_rectangle = text_surface.get_rect()
                        text_rectangle.topleft = (425, CENTER_RECT_TOP_LEFT[1])
                        text_rectangle.size = text_surface.get_size()

                        counter = timeout
                        counter_text = ""

                    counter_surface = font.render(counter_text, True, LIME)
                    counter_rectangle.size = counter_surface.get_size()

        surface.fill(background)
        surface.blit(text_surface, text_rectangle)
        surface.blit(counter_surface, counter_rectangle)
        pygame.display.update()
        clock.tick(60)

    pygame.quit()
