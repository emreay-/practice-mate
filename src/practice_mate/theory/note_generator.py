from typing import Sequence, Generator, Optional

from practice_mate.theory.interval import Interval
from practice_mate.theory.note import Note, NoteRangeException

__all__ = ["note_generator"]


def note_generator(root: Note, rules: Sequence[Interval], 
                   try_quantitative_naming: bool = True) -> Generator[Note, None, None]:
    note = root
    stop = False
    
    yield note

    while rules and not stop:
        for interval in rules:
            try:
                note = note.apply(interval, try_quantitative_naming=try_quantitative_naming)
            except NoteRangeException:
                stop = True
                break
            yield note
