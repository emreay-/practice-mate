from practice_mate.theory.interval import *
from practice_mate.theory.note import *
from practice_mate.theory.scales import *


def test_major_scale():
    major_scale_generator = MajorScale(Note.from_str("C4")).generator()
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


def test_chromatic_scale():
    chromatic_generator = ChromaticScale(Note.from_str("C4")).generator()
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
