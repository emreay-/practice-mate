import pytest

from practice_mate.theory.fundamentals import SemiTone, NoteName
from practice_mate.theory.interval import Interval, Quality, Quantity, get_note_name_for_quantity


def test_invalid_intervals():
    invalid = {
        (Quality.perfect, Quantity.second),
        (Quality.perfect, Quantity.third),
        (Quality.perfect, Quantity.sixth),
        (Quality.perfect, Quantity.seventh),
        (Quality.major, Quantity.fourth),
        (Quality.major, Quantity.fifth),
        (Quality.major, Quantity.eighth),
        (Quality.minor, Quantity.fourth),
        (Quality.minor, Quantity.fifth),
        (Quality.minor, Quantity.eighth),
    }
    
    for (ql, qn) in invalid:
        with pytest.raises(ValueError):
            Interval(ql, qn)


def test_interval_semitones():
    assert Interval(Quality.doubly_diminished, Quantity.second).semitones == SemiTone(-1)
    assert Interval(Quality.diminished, Quantity.second).semitones == SemiTone(0)
    assert Interval(Quality.minor, Quantity.second).semitones == SemiTone(1)
    assert Interval(Quality.major, Quantity.second).semitones == SemiTone(2)
    assert Interval(Quality.augmented, Quantity.second).semitones == SemiTone(3)
    assert Interval(Quality.doubly_augmented, Quantity.second).semitones == SemiTone(4)

    assert Interval(Quality.doubly_diminished, Quantity.third).semitones == SemiTone(1)
    assert Interval(Quality.diminished, Quantity.third).semitones == SemiTone(2)
    assert Interval(Quality.minor, Quantity.third).semitones == SemiTone(3)
    assert Interval(Quality.major, Quantity.third).semitones == SemiTone(4)
    assert Interval(Quality.augmented, Quantity.third).semitones == SemiTone(5)
    assert Interval(Quality.doubly_augmented, Quantity.third).semitones == SemiTone(6)

    assert Interval(Quality.doubly_diminished, Quantity.fourth).semitones == SemiTone(3)
    assert Interval(Quality.diminished, Quantity.fourth).semitones == SemiTone(4)
    assert Interval(Quality.perfect, Quantity.fourth).semitones == SemiTone(5)
    assert Interval(Quality.augmented, Quantity.fourth).semitones == SemiTone(6)
    assert Interval(Quality.doubly_augmented, Quantity.fourth).semitones == SemiTone(7)

    assert Interval(Quality.doubly_diminished, Quantity.fifth).semitones == SemiTone(5)
    assert Interval(Quality.diminished, Quantity.fifth).semitones == SemiTone(6)
    assert Interval(Quality.perfect, Quantity.fifth).semitones == SemiTone(7)
    assert Interval(Quality.augmented, Quantity.fifth).semitones == SemiTone(8)
    assert Interval(Quality.doubly_augmented, Quantity.fifth).semitones == SemiTone(9)

    assert Interval(Quality.doubly_diminished, Quantity.sixth).semitones == SemiTone(6)
    assert Interval(Quality.diminished, Quantity.sixth).semitones == SemiTone(7)
    assert Interval(Quality.minor, Quantity.sixth).semitones == SemiTone(8)
    assert Interval(Quality.major, Quantity.sixth).semitones == SemiTone(9)
    assert Interval(Quality.augmented, Quantity.sixth).semitones == SemiTone(10)
    assert Interval(Quality.doubly_augmented, Quantity.sixth).semitones == SemiTone(11)

    assert Interval(Quality.doubly_diminished, Quantity.seventh).semitones == SemiTone(8)
    assert Interval(Quality.diminished, Quantity.seventh).semitones == SemiTone(9)
    assert Interval(Quality.minor, Quantity.seventh).semitones == SemiTone(10)
    assert Interval(Quality.major, Quantity.seventh).semitones == SemiTone(11)
    assert Interval(Quality.augmented, Quantity.seventh).semitones == SemiTone(12)
    assert Interval(Quality.doubly_augmented, Quantity.seventh).semitones == SemiTone(13)

    assert Interval(Quality.doubly_diminished, Quantity.eighth).semitones == SemiTone(10)
    assert Interval(Quality.diminished, Quantity.eighth).semitones == SemiTone(11)
    assert Interval(Quality.perfect, Quantity.eighth).semitones == SemiTone(12)
    assert Interval(Quality.augmented, Quantity.eighth).semitones == SemiTone(13)
    assert Interval(Quality.doubly_augmented, Quantity.eighth).semitones == SemiTone(14)


def test_get_note_name_for_quantity():
    assert NoteName.b is get_note_name_for_quantity(NoteName.a, Quantity.second)
    assert NoteName.c is get_note_name_for_quantity(NoteName.b, Quantity.second)
    assert NoteName.d is get_note_name_for_quantity(NoteName.c, Quantity.second)
    assert NoteName.e is get_note_name_for_quantity(NoteName.d, Quantity.second)
    assert NoteName.f is get_note_name_for_quantity(NoteName.e, Quantity.second)
    assert NoteName.g is get_note_name_for_quantity(NoteName.f, Quantity.second)
    assert NoteName.a is get_note_name_for_quantity(NoteName.g, Quantity.second)

    assert NoteName.c is get_note_name_for_quantity(NoteName.a, Quantity.third)
    assert NoteName.d is get_note_name_for_quantity(NoteName.b, Quantity.third)
    assert NoteName.e is get_note_name_for_quantity(NoteName.c, Quantity.third)
    assert NoteName.f is get_note_name_for_quantity(NoteName.d, Quantity.third)
    assert NoteName.g is get_note_name_for_quantity(NoteName.e, Quantity.third)
    assert NoteName.a is get_note_name_for_quantity(NoteName.f, Quantity.third)
    assert NoteName.b is get_note_name_for_quantity(NoteName.g, Quantity.third)

    assert NoteName.d is get_note_name_for_quantity(NoteName.a, Quantity.fourth)
    assert NoteName.e is get_note_name_for_quantity(NoteName.b, Quantity.fourth)
    assert NoteName.f is get_note_name_for_quantity(NoteName.c, Quantity.fourth)
    assert NoteName.g is get_note_name_for_quantity(NoteName.d, Quantity.fourth)
    assert NoteName.a is get_note_name_for_quantity(NoteName.e, Quantity.fourth)
    assert NoteName.b is get_note_name_for_quantity(NoteName.f, Quantity.fourth)
    assert NoteName.c is get_note_name_for_quantity(NoteName.g, Quantity.fourth)

    assert NoteName.e is get_note_name_for_quantity(NoteName.a, Quantity.fifth)
    assert NoteName.f is get_note_name_for_quantity(NoteName.b, Quantity.fifth)
    assert NoteName.g is get_note_name_for_quantity(NoteName.c, Quantity.fifth)
    assert NoteName.a is get_note_name_for_quantity(NoteName.d, Quantity.fifth)
    assert NoteName.b is get_note_name_for_quantity(NoteName.e, Quantity.fifth)
    assert NoteName.c is get_note_name_for_quantity(NoteName.f, Quantity.fifth)
    assert NoteName.d is get_note_name_for_quantity(NoteName.g, Quantity.fifth)

    assert NoteName.f is get_note_name_for_quantity(NoteName.a, Quantity.sixth)
    assert NoteName.g is get_note_name_for_quantity(NoteName.b, Quantity.sixth)
    assert NoteName.a is get_note_name_for_quantity(NoteName.c, Quantity.sixth)
    assert NoteName.b is get_note_name_for_quantity(NoteName.d, Quantity.sixth)
    assert NoteName.c is get_note_name_for_quantity(NoteName.e, Quantity.sixth)
    assert NoteName.d is get_note_name_for_quantity(NoteName.f, Quantity.sixth)
    assert NoteName.e is get_note_name_for_quantity(NoteName.g, Quantity.sixth)

    assert NoteName.g is get_note_name_for_quantity(NoteName.a, Quantity.seventh)
    assert NoteName.a is get_note_name_for_quantity(NoteName.b, Quantity.seventh)
    assert NoteName.b is get_note_name_for_quantity(NoteName.c, Quantity.seventh)
    assert NoteName.c is get_note_name_for_quantity(NoteName.d, Quantity.seventh)
    assert NoteName.d is get_note_name_for_quantity(NoteName.e, Quantity.seventh)
    assert NoteName.e is get_note_name_for_quantity(NoteName.f, Quantity.seventh)
    assert NoteName.f is get_note_name_for_quantity(NoteName.g, Quantity.seventh)

    assert NoteName.a is get_note_name_for_quantity(NoteName.a, Quantity.eighth)
    assert NoteName.b is get_note_name_for_quantity(NoteName.b, Quantity.eighth)
    assert NoteName.c is get_note_name_for_quantity(NoteName.c, Quantity.eighth)
    assert NoteName.d is get_note_name_for_quantity(NoteName.d, Quantity.eighth)
    assert NoteName.e is get_note_name_for_quantity(NoteName.e, Quantity.eighth)
    assert NoteName.f is get_note_name_for_quantity(NoteName.f, Quantity.eighth)
    assert NoteName.g is get_note_name_for_quantity(NoteName.g, Quantity.eighth)


def test_from_str():
    assert Interval.from_str("Minor 3rd") == Interval(Quality.minor, Quantity.third)
    assert Interval.from_str("Major 3rd") == Interval(Quality.major, Quantity.third)
    assert Interval.from_str("Perfect 4th") == Interval(Quality.perfect, Quantity.fourth)
    assert Interval.from_str("Augmented 5th") == Interval(Quality.augmented, Quantity.fifth)
    assert Interval.from_str("Diminished 6th") == Interval(Quality.diminished, Quantity.sixth)
    assert Interval.from_str("Doubly augmented 5th") == Interval(Quality.doubly_augmented, Quantity.fifth)
    assert Interval.from_str("Doubly diminished 4th") == Interval(Quality.doubly_diminished, Quantity.fourth)
