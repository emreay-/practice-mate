from copy import deepcopy
from typing import Optional, Tuple
from practice_mate.theory.fundamentals import *
from practice_mate.theory.interval import Interval, get_note_name_for_quantity

__all__ = ["Note", "CannotDetermineRelatedNoteError", "NoteRangeException", "NotePitchAwarenessException"]


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


class NoteRangeException(Exception):
    pass


class NotePitchAwarenessException(Exception):
    pass


class Note:
    def __init__(self, base: NoteName,
                 pitch: Optional[Spn] = None,
                 modifier: Optional[Modifier] = None):
        self._base: NoteName = base
        self._pitch: Optional[Spn] = pitch
        self._modifier: Optional[Modifier] = modifier
        self._index, self._base_index = determine_note_and_base_indices(
            self._base, self._pitch or Spn(4), self._modifier)
        if self._pitch is None:
            self._index = None

    @staticmethod
    def from_str(value: str) -> "Note":
        value = value.strip()
        if not value:
            raise ValueError("Empty string cannot be parsed")

        base = NoteName(value[0].upper())
        try:
            numerics = "".join([i for i in value if i.isnumeric()])
            pitch = Spn(int(numerics))
            value = value[:-len(numerics)]
        except ValueError:
            pitch = None

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
    def pitch(self) -> Optional[Spn]:
        return self._pitch

    @property
    def modifier(self) -> Modifier:
        return self._modifier

    @property
    def index(self) -> Optional[NoteIndex]:
        return self._index

    @property
    def base_index(self) -> NoteIndex:
        return self._base_index

    def apply(self, interval: Interval, try_quantitative_naming: bool = True) -> "Note":
        try:
            new_index = NoteIndex(self._index + interval.semitones)
        except ValueError as e:
            raise NoteRangeException(e)

        if not try_quantitative_naming:
            return determine_notes_from_index(new_index)[0]

        try:
            new_base = get_note_name_for_quantity(base_note=self._base, quantity=interval.quantity)
            return determine_related_note(new_base, new_index)
        except CannotDetermineRelatedNoteError:
            return determine_notes_from_index(new_index)[0]

    def __ge__(self, other: "Note") -> bool:
        if (self.pitch is None) ^ (other.pitch is None):
            raise NotePitchAwarenessException(f"Cannot compare pitch-naive and pitch-aware notes {self}, {other}")
        elif (self.pitch is None) and (other.pitch is None):
            return self.base_index >= other.base_index
        else:
            return self.index >= other.index

    def __gt__(self, other: "Note") -> bool:
        if (self.pitch is None) ^ (other.pitch is None):
            raise NotePitchAwarenessException(f"Cannot compare pitch-naive and pitch-aware notes {self}, {other}")
        elif (self.pitch is None) and (other.pitch is None):
            return self.base_index > other.base_index
        else:
            return self.index > other.index

    def __eq__(self, other: "Note") -> bool:
        if (self.pitch is None) ^ (other.pitch is None):
            raise NotePitchAwarenessException(f"Cannot compare pitch-naive and pitch-aware notes {self}, {other}")
        elif (self.pitch is None) and (other.pitch is None):
            return self.base_index == other.base_index
        else:
            return self.index == other.index

    def __str__(self) -> str:
        _pitch = str(self.pitch) if self.pitch else ""
        return f"{self._base}{self._modifier.value if self._modifier else ''}{_pitch}"

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {str(self)}>"


def determine_note_and_base_indices(base: NoteName, pitch: Spn, modifier: Optional[Modifier] = None
                                    ) -> Tuple[NoteIndex, NoteIndex]:
    if pitch == Spn(-1) and base is NoteName.c and modifier in FLATTENING_MODIFIERS:
        raise NoteRangeException(f"Cannot go flatter than C-1")
    if pitch == Spn(10) and base is NoteName.b and modifier in SHARPENING_MODIFIERS:
        raise NoteRangeException(f"Cannot go sharper than B10")

    base_index = deepcopy(NOTENAME_TO_BASE_INDEX[base])
    if modifier:
        base_index += MODIFIER_TO_SEMITONE_OFFSET[modifier]
    note_index = base_index + (pitch + Spn(1)) * SemiTone(12)
    return NoteIndex(note_index), NoteIndex(base_index % 12)


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
