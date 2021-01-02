from collections import defaultdict
from random import randint
from typing import Tuple, Dict, List

import pygame
import pygame_menu
from pygame.locals import *

from practice_mate.theory import Note
from practice_mate.guitar.fretboard import Fretboard, Fret, String
from practice_mate.guitar.tuning import Tuning
from practice_mate.ui_utility import *

__all__ = ["name_the_note", "name_the_note_timed", "name_the_note_quiz"]


def random_fretboard_position(fretboard: Fretboard) -> Tuple[String, Fret]:
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


def name_the_note_quiz(frets: int, tuning: Tuning, surface: pygame.Surface):
    fretboard = Fretboard(frets=frets, tuning=tuning)

    total = 0
    correct = 0
    question_pool: List[Tuple[String, Fret]] = []
    positions_to_answer_times: Dict[Tuple[String, Fret], List[float]] = defaultdict(list)
    positions_to_number_of_failures: Dict[Tuple[String, Fret], int] = defaultdict(lambda: 0)

    string, fret = random_fretboard_position(fretboard)
    text = f"String {string} at fret {fret}? "

    font = pygame.font.SysFont(None, 68)
    text_surface = font.render(text, True, LIME)
    text_rectangle = text_surface.get_rect()
    text_rectangle.topleft = CENTER_RECT_TOP_LEFT

    answer_font = pygame.font.SysFont(None, 38)
    user_text_prefix = "Type Answer: "
    user_text = ""
    user_input_surface = answer_font.render(user_text_prefix + user_text, True, WHITE)
    user_input_rectangle = user_input_surface.get_rect()
    user_input_rectangle.topleft = (340, 400)

    running = True
    is_question_turn = False
    background = DARK_GRAY

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    if len(user_text) > 0:
                        user_text = user_text[:-1]
                else:
                    user_text += event.unicode

                user_input_surface = answer_font.render(user_text_prefix + user_text, True, WHITE)
                user_input_rectangle.size = user_input_surface.get_size()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN:
                    is_question_turn = not is_question_turn

                    if is_question_turn:
                        user_text = ""
                        user_input_surface = answer_font.render(user_text_prefix + user_text, True, WHITE)
                        user_input_rectangle.size = user_input_surface.get_size()

                        string, fret = random_fretboard_position(fretboard)
                        text = f"String {string} at fret {fret}? "
                        text_surface = font.render(text, True, LIME)
                        text_rectangle = text_surface.get_rect()
                        text_rectangle.topleft = CENTER_RECT_TOP_LEFT
                    else:
                        expected_answer = fretboard.get_note(string, fret)
                        try:
                            user_answer = Note.from_str(user_text)
                        except ValueError:
                            user_answer = None

                        if user_answer is not None and user_answer == expected_answer:
                            text = "Correct"
                            topleft = (380, CENTER_RECT_TOP_LEFT[1])
                        else:
                            text = f"Incorrect, the answer is {expected_answer}"
                            topleft = (150, CENTER_RECT_TOP_LEFT[1])

                        text_surface = font.render(text, True, WHITE)
                        text_rectangle = text_surface.get_rect()
                        text_rectangle.topleft = topleft

                    text_rectangle.size = text_surface.get_size()

        surface.fill(background)
        surface.blit(text_surface, text_rectangle)
        surface.blit(user_input_surface, user_input_rectangle)
        pygame.display.update()

    pygame.quit()
