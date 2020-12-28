from abc import ABC
from typing import Generator, ClassVar, List

from practice_mate.theory.interval import Interval
from practice_mate.theory.note import Note
from practice_mate.theory.note_generator import note_generator


__all__ = ["Scale", "MajorScale", "ChromaticScale"]


class Scale(ABC):
    def key(self) -> Note:
        pass

    def generator(self) -> Generator[Note, None, None]:
        pass



class MajorScale(Scale):
    _rules: ClassVar[List[Interval]] = [
        Interval.from_str("Major 2nd"),
        Interval.from_str("Major 2nd"),
        Interval.from_str("Minor 2nd"),
        Interval.from_str("Major 2nd"),
        Interval.from_str("Major 2nd"),
        Interval.from_str("Major 2nd"),
        Interval.from_str("Minor 2nd")
    ]

    def __init__(self, key: Note):
        self._key = key

    def generator(self) -> Generator[Note, None, None]:
        return note_generator(root=self._key, rules=self._rules)


class ChromaticScale(Scale):
    _rules: ClassVar[List[Interval]] = [Interval.from_str("Minor 2nd")]

    def __init__(self, key: Note):
        self._key = key

    def generator(self) -> Generator[Note, None, None]:
        return note_generator(root=self._key, rules=self._rules, try_quantitative_naming=False)
