from enum import Enum
from typing import Protocol, Optional, cast

from practice_mate.utility import cycle_enum
from practice_mate.theory.fundamentals import SemiTone, NoteName, cycle, NoteIndex

__all__ = ["Quality", "Quantity", "Interval", "get_note_name_for_quantity", "get_quantity_between_notes",
           "NoteProtocol", "CannotFindIntervalException", "NotesUnsuitableForFindingIntervalException"]


class NoteProtocol(Protocol):
    @property
    def base(self) -> NoteName:
        raise NotImplementedError()

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
    unison = "unison"
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
    Quantity.unison: SemiTone(0),
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

SEMITONE_IN_MAJOR_SCALE_TO_QUANTITY = {v: k for k, v in QUANTITY_TO_SEMITONE_IN_MAJOR_SCALE.items()}


QUANTITY_TO_DEGREE = {
    Quantity.unison: 1,
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


def get_quantity_between_notes(first: NoteName, second: NoteName) -> Quantity:
    note_generator = cycle(root=first)
    quantity_generator = cycle_enum(Quantity)

    while True:
        _note = next(note_generator)
        _quantity = cast(Quantity, next(quantity_generator))
        if _note is second:
            return _quantity


def is_perfect_quantity(quantity: Quantity) -> bool:
    return quantity in {Quantity.unison, Quantity.fourth, Quantity.fifth, Quantity.eighth,
                        Quantity.eleventh, Quantity.twelfth, Quantity.fifteenth}


class CannotFindIntervalException(Exception):
    pass


class NotesUnsuitableForFindingIntervalException(Exception):
    pass


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
            return Interval(Quality(" ".join(tokens[:-1]).capitalize()), Quantity(tokens[-1].lower()))
        except Exception:
            raise ValueError(f"Cannot create Interval from {value}")

    @staticmethod
    def between_notes(first: NoteProtocol, second: NoteProtocol) -> "Interval":
        quantity = get_quantity_between_notes(first.base, second.base)

        if first.index is None and second.index is None:
            if first > second:
                semitones = SemiTone(second.base_index + 12 - first.base_index)
            else:
                semitones = SemiTone(second.base_index - first.base_index)
        elif first.index is not None and second.index is not None:
            if first > second:
                raise NotesUnsuitableForFindingIntervalException(
                    f"For the pitch aware notes, first <= second should be true, {first} and {second}")
            semitones = SemiTone(second.index - first.index)
        else:
            raise NotesUnsuitableForFindingIntervalException(f"{first} and {second}")

        try:
            return Interval._determine_interval(quantity, semitones)
        except CannotFindIntervalException:
            raise NotesUnsuitableForFindingIntervalException(f"{first} and {second}")

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

    @staticmethod
    def _determine_interval(quantity: Quantity, semitones: SemiTone) -> "Interval":
        # Do not support compound intervals larger than an octave,
        # any such interval will be treated to be in the same octave
        if semitones > QUANTITY_TO_SEMITONE_IN_MAJOR_SCALE[Quantity.fifteenth]:
            semitones %= QUANTITY_TO_SEMITONE_IN_MAJOR_SCALE[Quantity.eighth]

        # Adjusting quantity for compound intervals
        _multiplier = semitones // QUANTITY_TO_SEMITONE_IN_MAJOR_SCALE[Quantity.eighth]
        _semitone_for_quantity = QUANTITY_TO_SEMITONE_IN_MAJOR_SCALE[quantity] + (
                _multiplier * QUANTITY_TO_SEMITONE_IN_MAJOR_SCALE[Quantity.eighth])
        quantity = SEMITONE_IN_MAJOR_SCALE_TO_QUANTITY[_semitone_for_quantity]

        expected_semitones = QUANTITY_TO_SEMITONE_IN_MAJOR_SCALE[quantity]
        difference_in_semitones = semitones - expected_semitones
        is_perfect = is_perfect_quantity(quantity)

        if is_perfect:
            if difference_in_semitones == SemiTone(-2):
                return Interval(quality=Quality.doubly_diminished, quantity=quantity)
            elif difference_in_semitones == SemiTone(-1):
                return Interval(quality=Quality.diminished, quantity=quantity)
            elif difference_in_semitones == SemiTone(0):
                return Interval(quality=Quality.perfect, quantity=quantity)
            elif difference_in_semitones == SemiTone(1):
                return Interval(quality=Quality.augmented, quantity=quantity)
            elif difference_in_semitones == SemiTone(2):
                return Interval(quality=Quality.doubly_augmented, quantity=quantity)
        else:
            if difference_in_semitones == SemiTone(-3):
                return Interval(quality=Quality.doubly_diminished, quantity=quantity)
            elif difference_in_semitones == SemiTone(-2):
                return Interval(quality=Quality.diminished, quantity=quantity)
            elif difference_in_semitones == SemiTone(-1):
                return Interval(quality=Quality.minor, quantity=quantity)
            elif difference_in_semitones == SemiTone(0):
                return Interval(quality=Quality.major, quantity=quantity)
            elif difference_in_semitones == SemiTone(1):
                return Interval(quality=Quality.augmented, quantity=quantity)
            elif difference_in_semitones == SemiTone(2):
                return Interval(quality=Quality.doubly_augmented, quantity=quantity)
        raise CannotFindIntervalException(f"Given quantity={quantity} and semitones={semitones} with "
                                          f"{difference_in_semitones} difference")

    def __str__(self) -> str:
        return f"{self._quality} {self._quantity}"

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {str(self)}>"

    def __eq__(self, other: "Interval") -> bool:
        return self.quality is other.quality and self.quantity is other.quantity
