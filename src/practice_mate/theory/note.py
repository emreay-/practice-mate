from enum import Enum
from copy import deepcopy
from typing import NewType, Sequence, Optional


__all__ = ["SemiTone", "NoteName", "Modifier", "Note"]


SemiTone = NewType("SemiTone", int)


class NoteName(str, Enum):
    c = "C"
    d = "D"
    e = "E"
    f = "F"
    g = "G"
    a = "A"
    b = "B"



class Modifier(str, Enum):
    flat = "b"
    sharp = "#"


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
    Modifier.flat: SemiTone(-1), 
    Modifier.sharp: SemiTone(1)
}

def determine_note_semitone_index(base: NoteName, modifiers: Optional[Sequence[Modifier]] = None) -> SemiTone:
    i = deepcopy(NOTENAME_TO_SEMITONE_INDEX[base])
    if modifiers:
        for m in modifiers:
            i += MODIFIER_TO_SEMITONE_OFFSET[m]
    return i % 12


class Note:
    def __init__(self, base: NoteName, modifiers: Optional[Sequence[Modifier]] = None):
        self._base = base
        self._modifiers = modifiers if modifiers else []
        self._semitone_index = determine_note_semitone_index(self._base, self._modifiers)

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {self._base}{''.join([i.value for i in self._modifiers])}>"
    