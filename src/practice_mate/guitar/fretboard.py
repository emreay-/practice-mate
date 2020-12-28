from copy import deepcopy
from typing import List, Dict

from practice_mate.theory import Note, Interval, note_generator, ChromaticScale
from practice_mate.guitar import Tuning, EStandard


__all__ = ["Fretboard", "FretboardRangeError"]


class FretboardRangeError(Exception):
    pass


class Fretboard:
    def __init__(self, frets: int, tuning: Tuning = EStandard):
        self._frets = frets
        self._tuning = tuning
        self._fretboard_notes: Dict[int, List[Note]] = {}
        
        self._populate()

    def _populate(self):
        for string_number, open_string_note in zip(range(self._tuning.strings - 1, -1, -1), 
                                                   self._tuning.open_string_notes_desc()):
            _string_notes = []
            note_generator = ChromaticScale(open_string_note).generator()

            for _ in range(self._frets + 1):
                _string_notes.append(next(note_generator))
            self._fretboard_notes[string_number] = _string_notes

    @property
    def all_notes(self) -> Dict[int, List[Note]]:
        return deepcopy(self._fretboard_notes)

    def get_note(self, string: int, fret: int) -> Note:
        if 0 <= string < self._tuning.strings and 0 <= fret <= self._frets:
            return self._fretboard_notes[string][fret]
        raise FretboardRangeError(f"For string {string} and fret {fret}")
