from copy import deepcopy
from typing import Optional
from practice_mate.theory.fundamentals import *

__all__ = ["Note"]


NOTENAME_TO_BASE_INDEX = {
    NoteName.c: NoteIndex(0),
    NoteName.d: NoteIndex(2),
    NoteName.e: NoteIndex(4),
    NoteName.f: NoteIndex(5),
    NoteName.g: NoteIndex(7),
    NoteName.a: NoteIndex(9),
    NoteName.b: NoteIndex(11),
}

MODIFIER_TO_SEMITONE_OFFSET = {
    Modifier.natural: SemiTone(0),
    Modifier.flat: SemiTone(-1),
    Modifier.double_flat: SemiTone(-2),
    Modifier.sharp: SemiTone(1),
    Modifier.double_sharp: SemiTone(2)
}

FLATTENING_MODIFIERS = {Modifier.flat, Modifier.double_flat}
SHARPENING_MODIFIERS = {Modifier.sharp, Modifier.double_sharp}


def determine_note_index(base: NoteName, pitch: Spn, modifier: Optional[Modifier] = None) -> NoteIndex:
    if pitch == Spn(-1) and base is NoteName.c and modifier in FLATTENING_MODIFIERS:
        raise ValueError(f"Cannot go flatter than C-1")
    if pitch == Spn(10) and base is NoteName.b and modifier in SHARPENING_MODIFIERS:
        raise ValueError(f"Cannot go sharper than B10")

    i = deepcopy(NOTENAME_TO_BASE_INDEX[base])
    i += (pitch + Spn(1)) * SemiTone(12)
    if modifier:
        i += MODIFIER_TO_SEMITONE_OFFSET[modifier]
    return NoteIndex(i)


class Note:
    def __init__(self, base: NoteName,
                 pitch: Optional[Spn] = Spn(4),
                 modifier: Optional[Modifier] = None
                ):
        self._base: NoteName = base
        self._pitch: Spn = pitch
        self._modifier: Modifier = modifier
        self._index: NoteIndex = determine_note_index(self._base, self._pitch, self._modifier)

    @property
    def index(self) -> NoteIndex:
        return self._index

    def __eq__(self, other: "Note") -> bool:
        return self._index == other._index

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {self._base}"\
            f"{self._modifier.value if self._modifier else ''}{self._pitch}>"
