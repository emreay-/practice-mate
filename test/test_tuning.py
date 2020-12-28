from practice_mate.theory import Note
from practice_mate.guitar.tuning import *


def test_e_standard():
    expected_notes = [
        Note.from_str("E2"),
        Note.from_str("A2"),
        Note.from_str("D3"),
        Note.from_str("G3"),
        Note.from_str("B3"),
        Note.from_str("E4"),
    ]

    assert expected_notes == EStandard.open_string_notes_desc()


def test_b_standard():
    expected_notes = [
        Note.from_str("B1"),
        Note.from_str("E2"),
        Note.from_str("A2"),
        Note.from_str("D3"),
        Note.from_str("G3"),
        Note.from_str("B3"),
        Note.from_str("E4"),
    ]

    assert expected_notes == BStandard.open_string_notes_desc()


def test_drop_d():
    expected_notes = [
        Note.from_str("D2"),
        Note.from_str("A2"),
        Note.from_str("D3"),
        Note.from_str("G3"),
        Note.from_str("B3"),
        Note.from_str("E4"),
    ]

    assert expected_notes == DropD.open_string_notes_desc()
