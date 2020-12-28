from practice_mate.theory.interval import *
from practice_mate.theory.note import *
from practice_mate.theory.note_generator import *


def test_note_generator():
    major_scale_rules = [
        Interval.from_str("Major 2nd"),
        Interval.from_str("Major 2nd"),
        Interval.from_str("Minor 2nd"),
        Interval.from_str("Major 2nd"),
        Interval.from_str("Major 2nd"),
        Interval.from_str("Major 2nd"),
        Interval.from_str("Minor 2nd")
    ]
    major_scale_generator = note_generator(Note.from_str("C4"), major_scale_rules)
    assert Note.from_str("C4") == next(major_scale_generator)
    assert Note.from_str("D4") == next(major_scale_generator)
    assert Note.from_str("E4") == next(major_scale_generator)
    assert Note.from_str("F4") == next(major_scale_generator)
    assert Note.from_str("G4") == next(major_scale_generator)
    assert Note.from_str("A4") == next(major_scale_generator)
    assert Note.from_str("B4") == next(major_scale_generator)
    assert Note.from_str("C5") == next(major_scale_generator)
    assert Note.from_str("D5") == next(major_scale_generator)
    assert Note.from_str("E5") == next(major_scale_generator)
    assert Note.from_str("F5") == next(major_scale_generator)
    assert Note.from_str("G5") == next(major_scale_generator)
    assert Note.from_str("A5") == next(major_scale_generator)
    assert Note.from_str("B5") == next(major_scale_generator)

    chromatic_rules = [Interval.from_str("Minor 2nd")]
    chromatic_generator = note_generator(Note.from_str("C4"), chromatic_rules)
    assert Note.from_str("C4") == next(chromatic_generator)
    assert Note.from_str("C#4") == next(chromatic_generator)
    assert Note.from_str("D4") == next(chromatic_generator)
    assert Note.from_str("D#4") == next(chromatic_generator)
    assert Note.from_str("E4") == next(chromatic_generator)
    assert Note.from_str("F4") == next(chromatic_generator)
    assert Note.from_str("F#4") == next(chromatic_generator)
    assert Note.from_str("G4") == next(chromatic_generator)
    assert Note.from_str("G#4") == next(chromatic_generator)
    assert Note.from_str("A4") == next(chromatic_generator)
    assert Note.from_str("A#4") == next(chromatic_generator)
    assert Note.from_str("B4") == next(chromatic_generator)
    assert Note.from_str("C5") == next(chromatic_generator)
    assert Note.from_str("C#5") == next(chromatic_generator)
    assert Note.from_str("D5") == next(chromatic_generator)
    assert Note.from_str("D#5") == next(chromatic_generator)
    assert Note.from_str("E5") == next(chromatic_generator)
    assert Note.from_str("F5") == next(chromatic_generator)
    assert Note.from_str("F#5") == next(chromatic_generator)
    assert Note.from_str("G5") == next(chromatic_generator)
    assert Note.from_str("G#5") == next(chromatic_generator)
    assert Note.from_str("A5") == next(chromatic_generator)
    assert Note.from_str("A#5") == next(chromatic_generator)
