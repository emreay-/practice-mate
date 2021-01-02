import pygame
from pygame.locals import *

from practice_mate.theory import Note, Interval
from practice_mate.ui_utility import *

__all__ = ["interval_finder"]


def delete_char(user_text: str) -> str:
    if len(user_text) > 0:
        return user_text[:-1]
    return user_text


def interval_finder(surface: pygame.Surface):
    info_text = "Type the notes to get the interval, press TAB to select first/second note"
    info_font = pygame.font.SysFont(None, 28)
    info_text_surface = info_font.render(info_text, True, LIME)
    info_text_rectangle = info_text_surface.get_rect()
    info_text_rectangle.topleft = (20, 20)

    font = pygame.font.SysFont(None, 68)

    FIRST_CENTER = (300, 250)
    SECOND_CENTER = (600, 250)

    first_note_text = "Note 1"
    first_note_text_surface = font.render(first_note_text, True, LIME)
    first_note_text_rectangle = first_note_text_surface.get_rect()
    first_note_text_rectangle.center = FIRST_CENTER

    second_note_text = "Note 2"
    second_note_text_surface = font.render(second_note_text, True, WHITE)
    second_note_text_rectangle = second_note_text_surface.get_rect()
    second_note_text_rectangle.center = SECOND_CENTER

    result_text = ""
    result_text_surface = font.render(result_text, True, WHITE)
    result_text_rectangle = result_text_surface.get_rect()
    result_text_rectangle.center = CENTER

    background = DARK_GRAY

    running = True
    is_asking_turn = True
    is_first_note_frame_selected = True

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    if is_first_note_frame_selected:
                        first_note_text = delete_char(first_note_text)
                        first_note_text_surface = font.render(first_note_text.strip(), True, LIME)
                        first_note_text_rectangle.size = first_note_text_surface.get_size()
                    else:
                        second_note_text = delete_char(second_note_text)
                        second_note_text_surface = font.render(second_note_text.strip(), True, LIME)
                        second_note_text_rectangle.size = second_note_text_surface.get_size()
                else:
                    if is_first_note_frame_selected:
                        first_note_text += event.unicode
                        first_note_text_surface = font.render(first_note_text.strip(), True, LIME)
                        first_note_text_rectangle.size = first_note_text_surface.get_size()
                    else:
                        second_note_text += event.unicode
                        second_note_text_surface = font.render(second_note_text.strip(), True, LIME)
                        second_note_text_rectangle.size = second_note_text_surface.get_size()

                first_note_text_rectangle.center = FIRST_CENTER
                second_note_text_rectangle.center = SECOND_CENTER

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    running = False

                elif event.key == K_TAB:
                    is_first_note_frame_selected = not is_first_note_frame_selected

                    if is_first_note_frame_selected:
                        first_note_text = ""
                    else:
                        second_note_text = ""

                    first_note_text_surface = font.render(first_note_text.strip(), True,
                                                          LIME if is_first_note_frame_selected else WHITE)
                    first_note_text_rectangle.size = first_note_text_surface.get_size()
                    second_note_text_surface = font.render(second_note_text.strip(), True,
                                                           WHITE if is_first_note_frame_selected else LIME)
                    second_note_text_rectangle.size = second_note_text_surface.get_size()

                if event.key == pygame.K_RETURN:
                    is_asking_turn = not is_asking_turn
                    result_text = ""

                    if is_asking_turn:
                        is_first_note_frame_selected = True

                        first_note_text_surface = font.render(first_note_text.strip(), True, LIME)
                        first_note_text_rectangle = first_note_text_surface.get_rect()
                        first_note_text_rectangle.center = FIRST_CENTER

                        second_note_text_surface = font.render(second_note_text.strip(), True, WHITE)
                        second_note_text_rectangle = second_note_text_surface.get_rect()
                        second_note_text_rectangle.center = SECOND_CENTER
                    else:
                        try:
                            first_note = Note.from_str(first_note_text)
                            second_note = Note.from_str(second_note_text)
                            interval = Interval.between_notes(first_note, second_note)

                            result_text += str(interval)
                            result_text_surface = font.render(result_text, True, WHITE)
                            result_text_rectangle = result_text_surface.get_rect()
                            result_text_rectangle.center = CENTER

                            first_note_text = ""
                            second_note_text = ""
                        except Exception as e:
                            print(e)
                            is_asking_turn = True

        surface.fill(background)
        surface.blit(info_text_surface, info_text_rectangle)

        if is_asking_turn:
            surface.blit(first_note_text_surface, first_note_text_rectangle)
            pygame.draw.rect(
                surface, LIME if is_first_note_frame_selected else WHITE, first_note_text_rectangle.inflate(30, 30), 3)
            surface.blit(second_note_text_surface, second_note_text_rectangle)
            pygame.draw.rect(
                surface, WHITE if is_first_note_frame_selected else LIME, second_note_text_rectangle.inflate(30, 30), 3)
        else:
            surface.blit(result_text_surface, result_text_rectangle)

        pygame.display.update()
