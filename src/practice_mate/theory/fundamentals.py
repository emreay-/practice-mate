from enum import Enum, unique
from typing import Generator


__all__ = ["SemiTone", "NoteName", "NoteIndex", "Modifier", "Spn", "cycle"]


class SemiTone(int):
    pass


class Spn(int):
    # See https://en.wikipedia.org/wiki/Scientific_pitch_notation
    def __new__(cls, *args, **kwargs):
        if -1 <= args[0] <= 10:
            return super().__new__(cls, *args, **kwargs)
        raise ValueError(f"Invalid scientific pitch notation {args[0]}")


class NoteIndex(int):
    def __new__(cls, *args, **kwargs):
        if args[0] in range(cls.min_int(), cls.max_int() + 1):
            return super().__new__(cls, *args, **kwargs)
        raise ValueError(f"Invalid note index {args[0]}")

    @staticmethod
    def min_int() -> int:
        return 0

    @staticmethod
    def max_int() -> int:
        return 143

    @staticmethod
    def bounded(value: int) -> "NoteIndex":
        return NoteIndex(max(NoteIndex.min_int(), min(NoteIndex.max_int(), value)))


@unique
class NoteName(str, Enum):
    c = "C"
    d = "D"
    e = "E"
    f = "F"
    g = "G"
    a = "A"
    b = "B"


@unique
class Modifier(str, Enum):
    flat = "b"  # "♭"
    sharp = "#"  # "♯"
    natural = "natural"  # "♮"
    double_flat = "bb"  # "♭♭"
    double_sharp = "##"  # "♯♯"
    triple_flat = "bbb"  # "♭♭♭"
    triple_sharp = "###"  # "♯♯♯"


_NOTE_NAMES_LIST = [i for i in NoteName]
_NOTE_NAME_TO_LIST_INDEX = {n: i for i, n in enumerate(NoteName)}


def cycle(root: NoteName, inclusive_start: bool = True) -> Generator[NoteName, None, None]:
    index = _NOTE_NAME_TO_LIST_INDEX[root]
    if not inclusive_start:
        index += 1
        index %= len(NoteName)

    while True:
        yield _NOTE_NAMES_LIST[index]
        index += 1
        index %= len(NoteName)
