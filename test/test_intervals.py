import pytest

from practice_mate.theory.fundamentals import SemiTone
from practice_mate.theory.intervals import Interval, Quality, Quantity


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
