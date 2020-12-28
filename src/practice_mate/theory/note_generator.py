from typing import Sequence, Iterator, Optional

from practice_mate.theory.interval import Interval
from practice_mate.theory.note import Note, NoteRangeException

__all__ = ["note_generator"]


def note_generator(root: Note, rules: Sequence[Interval]) -> Iterator[Note]:
    note = root
    stop = False
    
    yield note

    while rules and not stop:
        for interval in rules:
            try:
                note = note.apply(interval)
            except NoteRangeException:
                stop = True
                break
            yield note
