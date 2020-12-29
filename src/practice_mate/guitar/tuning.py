from dataclasses import dataclass
from typing import List

from practice_mate.theory import Interval, Note


__all__ = ["Tuning", "EStandard", "BStandard", "DropD", "KNOWN_TUNINGS"]


@dataclass(frozen=True)
class Tuning:
    name: str
    strings: int
    lowest_note: Note
    rules: List[Interval]

    def open_string_notes_desc(self):
        open_string_notes = [self.lowest_note]
        if len(self.rules) + 1 == self.strings:
            for rule in self.rules:
                next_string = open_string_notes[-1].apply(rule)
                open_string_notes.append(next_string)
        else:
            raise ValueError(f"Invalid tuning rules as opposed to number of strings")
        return open_string_notes


EStandard = Tuning(
    name="E Standard", 
    strings=6,
    lowest_note=Note.from_str("E2"),
    rules=[
        Interval.from_str("Perfect 4th"),
        Interval.from_str("Perfect 4th"),
        Interval.from_str("Perfect 4th"),
        Interval.from_str("Major 3rd"),
        Interval.from_str("Perfect 4th")
    ]
)

BStandard = Tuning(
    name="B Standard", 
    strings=7,
    lowest_note=Note.from_str("B1"),
    rules=[
        Interval.from_str("Perfect 4th"),
        Interval.from_str("Perfect 4th"),
        Interval.from_str("Perfect 4th"),
        Interval.from_str("Perfect 4th"),
        Interval.from_str("Major 3rd"),
        Interval.from_str("Perfect 4th")
    ]
)

DropD = Tuning(
    name="Drop D", 
    strings=6, 
    lowest_note=Note.from_str("D2"),
    rules=[
        Interval.from_str("Perfect 5th"),
        Interval.from_str("Perfect 4th"),
        Interval.from_str("Perfect 4th"),
        Interval.from_str("Major 3rd"),
        Interval.from_str("Perfect 4th"),
    ]
)


KNOWN_TUNINGS = (EStandard, BStandard, DropD)
