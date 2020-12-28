from enum import Enum
from copy import deepcopy
from typing import NewType, Optional


__all__ = ["SemiTone", "NoteName", "Modifier", "ScientificPitchNotation", "Note"]


class SemiTone(int):
    pass


class ScientificPitchNotation(int):
    # See https://en.wikipedia.org/wiki/Scientific_pitch_notation
    def __new__(cls, *args, **kwargs):
        if -1 <= args[0] <= 10:
            return super().__new__(cls, *args, **kwargs)
        raise ValueError(f"Invalid scientific pitch notation {args[0]}")



class NoteName(str, Enum):
    c = "C"
    d = "D"
    e = "E"
    f = "F"
    g = "G"
    a = "A"
    b = "B"



class Modifier(str, Enum):
    none = ""
    natural = "♮"
    flat = "♭"
    double_flat = "♭♭"
    sharp = "♯"
    double_sharp = "♯"


NOTENAME_TO_SEMITONE_INDEX = {
    NoteName.c: SemiTone(0),
    NoteName.d: SemiTone(2),
    NoteName.e: SemiTone(4),
    NoteName.f: SemiTone(5),
    NoteName.g: SemiTone(7),
    NoteName.a: SemiTone(9),
    NoteName.b: SemiTone(11),
}

MODIFIER_TO_SEMITONE_OFFSET = {
    Modifier.none: SemiTone(0),
    Modifier.natural: SemiTone(0),
    Modifier.flat: SemiTone(-1),
    Modifier.double_flat: SemiTone(-2),
    Modifier.sharp: SemiTone(1),
    Modifier.double_sharp: SemiTone(2)
}

def determine_note_semitone_index(base: NoteName, modifier: Optional[Modifier] = None) -> SemiTone:
    i = deepcopy(NOTENAME_TO_SEMITONE_INDEX[base])
    if modifier:
        i += MODIFIER_TO_SEMITONE_OFFSET[modifier]
    return i % SemiTone(12)


class Note:
    def __init__(self, base: NoteName, modifier: Optional[Modifier] = None):
        self._base = base
        self._modifier = modifier if modifier else Modifier.none
        self._semitone_index = determine_note_semitone_index(self._base, self._modifier)

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {self._base}{self._modifier}>"
    