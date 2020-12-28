from copy import deepcopy
from typing import Optional, Tuple
from practice_mate.theory.fundamentals import *
from practice_mate.theory.interval import Interval, get_note_name_for_quantity

__all__ = ["Note", "CannotDetermineRelatedNoteError"]


NOTENAME_TO_BASE_INDEX = {
    NoteName.c: NoteIndex(0),
    NoteName.d: NoteIndex(2),
    NoteName.e: NoteIndex(4),
    NoteName.f: NoteIndex(5),
    NoteName.g: NoteIndex(7),
    NoteName.a: NoteIndex(9),
    NoteName.b: NoteIndex(11),
}

BASE_INDEX_TO_NOTE_NAME = {
    NoteIndex(0): NoteName.c,
    NoteIndex(2): NoteName.d,
    NoteIndex(4): NoteName.e,
    NoteIndex(5): NoteName.f,
    NoteIndex(7): NoteName.g,
    NoteIndex(9): NoteName.a,
    NoteIndex(11): NoteName.b,
}

MODIFIER_TO_SEMITONE_OFFSET = {
    Modifier.natural: SemiTone(0),
    Modifier.flat: SemiTone(-1),
    Modifier.sharp: SemiTone(1),
    Modifier.double_flat: SemiTone(-2),
    Modifier.double_sharp: SemiTone(2),
    Modifier.triple_flat: SemiTone(-3),
    Modifier.triple_sharp: SemiTone(3)
}

SEMITONE_OFFSET_TO_MODIFIER = {
    SemiTone(0): None,
    SemiTone(-1): Modifier.flat,
    SemiTone(1): Modifier.sharp,
    SemiTone(-2): Modifier.double_flat,
    SemiTone(2): Modifier.double_sharp,
    SemiTone(-3): Modifier.triple_flat,
    SemiTone(3): Modifier.triple_sharp,
}

FLATTENING_MODIFIERS = {Modifier.flat, Modifier.double_flat, Modifier.triple_flat}
SHARPENING_MODIFIERS = {Modifier.sharp, Modifier.double_sharp, Modifier.triple_sharp}


class Note:
    def __init__(self, base: NoteName,
                 pitch: Optional[Spn] = Spn(4),
                 modifier: Optional[Modifier] = None
                ):
        self._base: NoteName = base
        self._pitch: Spn = pitch
        self._modifier: Modifier = modifier
        self._index: NoteIndex = determine_note_index(self._base, self._pitch, self._modifier)

    @staticmethod
    def from_str(value: str) -> "Note":
        value = value.strip()
        base = NoteName(value[0].upper())
        try:
            numerics = "".join([i for i in value if i.isnumeric()])
            value = value[:-len(numerics)]
            pitch = Spn(int(numerics))
        except ValueError:
            pitch = Spn(4)

        if len(value) > 1:
            modifier = value[1:].replace("#", Modifier.sharp.value).replace("b", Modifier.flat.value)
            modifier = Modifier(modifier)
        else:
            modifier = None
        try:
            return Note(base, pitch, modifier)
        except Exception:
            raise ValueError(f"Cannot create a Note from {value}")

    @property
    def base(self) -> NoteName:
        return self._base

    @property
    def pitch(self) -> Spn:
        return self._pitch

    @property
    def modifier(self) -> Modifier:
        return self._modifier

    @property
    def index(self) -> NoteIndex:
        return self._index

    def apply(self, interval: Interval) -> "Note":
        new_base = get_note_name_for_quantity(base_note=self._base, quantity=interval.quantity)
        new_index = self._index + interval.semitones
        return determine_related_note(new_base, new_index)

    def __ge__(self, other: "Note") -> bool:
        return self.index >= other.index

    def __gt__(self, other: "Note") -> bool:
        return self.index > other.index

    def __eq__(self, other: "Note") -> bool:
        return self.index == other.index

    def __str__(self) -> str:
        return f"{self._base}{self._modifier.value if self._modifier else ''}{self._pitch}"

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {str(self)}>"


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


def determine_notes_from_index(index: NoteIndex) -> Tuple[Note]:
    pitch = Spn((index // 12) - 1)
    base_index = NoteIndex(index % 12)

    if base_index in BASE_INDEX_TO_NOTE_NAME:
        return (Note(BASE_INDEX_TO_NOTE_NAME[base_index], pitch=pitch, modifier=None),)
    else:
        (note_to_sharpen,) = determine_notes_from_index(index - 1)
        (note_to_flatten,) = determine_notes_from_index(index + 1)
        return (
            Note(note_to_sharpen.base, note_to_sharpen.pitch, Modifier.sharp),
            Note(note_to_flatten.base, note_to_flatten.pitch, Modifier.flat),
        )


class CannotDetermineRelatedNoteError(Exception):
    pass


def determine_related_note(target_base: NoteName, index: NoteIndex) -> Note:
    for search_index in range(index - 3, index + 4, 1):
        notes = determine_notes_from_index(search_index)
        if len(notes) > 1:
            continue
        elif notes[0].base is target_base:
            related_note = Note(target_base, notes[0].pitch, SEMITONE_OFFSET_TO_MODIFIER[index - search_index])
            assert related_note.index == index
            return related_note
    raise CannotDetermineRelatedNoteError(f"For index {index} and target base {target_base}")
