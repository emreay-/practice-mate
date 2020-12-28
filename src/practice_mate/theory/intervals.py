from enum import Enum

from practice_mate.theory.fundamentals import SemiTone

__all__ = ["Quality", "Quantity", "Interval"]


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


QUANTITY_TO_SEMITONE_IN_MAJOR_SCALE = {
    Quantity.second: SemiTone(2),
    Quantity.third: SemiTone(4),
    Quantity.fourth: SemiTone(5),
    Quantity.fifth: SemiTone(7),
    Quantity.sixth: SemiTone(9),
    Quantity.seventh: SemiTone(11),
    Quantity.eighth: SemiTone(12)
}


class Interval:
    def __init__(self, quality: Quality, quantity: Quantity):
        self._quality = quality
        self._quantity = quantity
        self._is_perfect_quantity = quantity in {Quantity.fourth, Quantity.fifth, Quantity.eighth}
        self._validate()
        self._semitones = self._determine_semitones()
    
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
    

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {self._quality} {self._quantity}>"
