from enum import Enum
from typing import Protocol, Optional

from practice_mate.theory.fundamentals import SemiTone, NoteName, cycle, NoteIndex

__all__ = ["Quality", "Quantity", "Interval", "get_note_name_for_quantity", "NoteProtocol"]


class NoteProtocol(Protocol):
    @property
    def index(self) -> Optional[NoteIndex]:
        raise NotImplementedError()

    @property
    def base_index(self) -> NoteIndex:
        raise NotImplementedError()


class Quality(str, Enum):
    minor = "Minor"
    major = "Major"
    perfect = "Perfect"
    augmented = "Augmented"
    diminished = "Diminished"
    doubly_augmented = "Doubly augmented"
    doubly_diminished = "Doubly diminished"


class Quantity(str, Enum):
    second = "2nd"
    third = "3rd"
    fourth = "4th"
    fifth = "5th"
    sixth = "6th"
    seventh = "7th"
    eighth = "8th"

    ninth = "9th"
    tenth = "10th"
    eleventh = "11th"
    twelfth = "12th"
    thirteenth = "13th"
    fourteenth = "14th"
    fifteenth = "15th"


QUANTITY_TO_SEMITONE_IN_MAJOR_SCALE = {
    Quantity.second: SemiTone(2),
    Quantity.third: SemiTone(4),
    Quantity.fourth: SemiTone(5),
    Quantity.fifth: SemiTone(7),
    Quantity.sixth: SemiTone(9),
    Quantity.seventh: SemiTone(11),
    Quantity.eighth: SemiTone(12),
    Quantity.ninth: SemiTone(14),
    Quantity.tenth: SemiTone(16),
    Quantity.eleventh: SemiTone(17),
    Quantity.twelfth: SemiTone(19),
    Quantity.thirteenth: SemiTone(21),
    Quantity.fourteenth: SemiTone(23),
    Quantity.fifteenth: SemiTone(24)
}


QUANTITY_TO_DEGREE = {
    Quantity.second: 2,
    Quantity.third: 3,
    Quantity.fourth: 4,
    Quantity.fifth: 5,
    Quantity.sixth: 6,
    Quantity.seventh: 7,
    Quantity.eighth: 8,
    Quantity.ninth: 9,
    Quantity.tenth: 10,
    Quantity.eleventh: 11,
    Quantity.twelfth: 12,
    Quantity.thirteenth: 13,
    Quantity.fourteenth: 14,
    Quantity.fifteenth: 15
}


def get_note_name_for_quantity(base_note: NoteName, quantity: Quantity) -> NoteName:
    degree = QUANTITY_TO_DEGREE.get(quantity)
    iterator = cycle(root=base_note)
    for _ in range(degree - 1):
        next(iterator)
    return next(iterator)


def is_perfect_quantity(quantity: Quantity) -> bool:
    return quantity in {Quantity.fourth, Quantity.fifth, Quantity.eighth,
                        Quantity.eleventh, Quantity.twelfth, Quantity.fifteenth}


class Interval:
    def __init__(self, quality: Quality, quantity: Quantity):
        self._quality = quality
        self._quantity = quantity
        self._is_perfect_quantity = is_perfect_quantity(self._quantity)
        self._validate()
        self._semitones = self._determine_semitones()

    @staticmethod
    def from_str(value: str) -> "Interval":
        tokens = value.strip().split(" ")
        try:
            return Interval(Quality(" ".join(tokens[:-1])), Quantity(tokens[-1]))
        except Exception:
            raise ValueError(f"Cannot create Interval from {value}")

    @property
    def quality(self) -> Quality:
        return self._quality

    @property
    def quantity(self) -> Quantity:
        return self._quantity

    @property
    def semitones(self) -> SemiTone:
        return self._semitones

    def _validate(self):
        if self._quality is Quality.perfect and not self._is_perfect_quantity:
            raise ValueError(f"Invalid perfect interval {self}")

        if self._quality in {Quality.major, Quality.minor} and self._is_perfect_quantity:
            raise ValueError(f"Invalid interval {self}")

    def _determine_semitones(self) -> SemiTone:
        semitones = QUANTITY_TO_SEMITONE_IN_MAJOR_SCALE[self._quantity]

        if self._quality in {Quality.major, Quality.perfect}:
            return semitones 

        if self._quality is Quality.minor:
            return semitones - SemiTone(1)

        if self._quality is Quality.diminished:
            if self._is_perfect_quantity:
                return semitones - SemiTone(1)
            else:
                return semitones - SemiTone(2)

        if self._quality is Quality.doubly_diminished:
            if self._is_perfect_quantity:
                return semitones - SemiTone(2)
            else:
                return semitones - SemiTone(3)

        if self._quality is Quality.augmented:
            return semitones + SemiTone(1)

        if self._quality is Quality.doubly_augmented:
            return semitones + SemiTone(2)

    def __str__(self) -> str:
        return f"{self._quality} {self._quantity}"

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {str(self)}>"

    def __eq__(self, other: "Interval") -> bool:
        return self.quality is other.quality and self.quantity is other.quantity
