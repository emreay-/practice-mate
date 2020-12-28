import pytest

from practice_mate.theory import Note, ChromaticScale
from practice_mate.guitar.tuning import *
from practice_mate.guitar.fretboard import *


def test_fretboard_populate():
    tuning = EStandard
    frets = 24

    expected = {}
    for i, note in enumerate(tuning.open_string_notes_desc()[::-1]):
        _data = []
        _gen = ChromaticScale(note).generator()
        for _ in range(frets + 1):
            _data.append(next(_gen))
        expected[i] = _data
    
    assert expected == Fretboard(frets=frets, tuning=tuning).all_notes


def test_fretboard_get_note():
    fretboard = Fretboard(frets=24, tuning=EStandard)
    
    assert fretboard.get_note(5, 0) == Note.from_str("E2")
    assert fretboard.get_note(5, 12) == Note.from_str("E3")
    assert fretboard.get_note(5, 24) == Note.from_str("E4")
    assert fretboard.get_note(4, 7) == Note.from_str("E3")
    assert fretboard.get_note(4, 10) == Note.from_str("G3")
    assert fretboard.get_note(3, 8) == Note.from_str("A#3")
    assert fretboard.get_note(1, 7) == Note.from_str("F#4")

    with pytest.raises(FretboardRangeError):
        fretboard.get_note(7, 5) == Note.from_str("F#4")

    with pytest.raises(FretboardRangeError):
        fretboard.get_note(5, 25) == Note.from_str("F#4")
