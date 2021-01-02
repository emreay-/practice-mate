from copy import deepcopy
from typing import List, Dict

from practice_mate.theory import Note, Interval, note_generator, ChromaticScale
from practice_mate.guitar import Tuning, EStandard


__all__ = ["Fretboard", "FretboardRangeError", "Fret", "String"]


Fret = int
String = int


class FretboardRangeError(Exception):
    pass


class Fretboard:
    def __init__(self, frets: int, tuning: Tuning = EStandard):
        self._frets = frets
        self._tuning = tuning
        self._fretboard_notes: Dict[int, List[Note]] = {}
        
        self._populate()

    def _populate(self):
        for string_number, open_string_note in zip(range(self.strings, 0, -1), self.tuning.open_string_notes_desc()):
            _string_notes = []
            note_generator = ChromaticScale(open_string_note).generator()

            for _ in range(self._frets + 1):
                _string_notes.append(next(note_generator))
            self._fretboard_notes[string_number] = _string_notes

    @property
    def tuning(self) -> Tuning:
        return self._tuning

    @property
    def strings(self) -> int:
        return self.tuning.strings

    @property
    def frets(self) -> int:
        return self._frets

    @property
    def all_notes(self) -> Dict[int, List[Note]]:
        return deepcopy(self._fretboard_notes)

    def get_note(self, string: String, fret: Fret) -> Note:
        if 0 < string <= self._tuning.strings and 0 <= fret <= self._frets:
            return self._fretboard_notes[string][fret]
        raise FretboardRangeError(f"For string {string} and fret {fret}")
