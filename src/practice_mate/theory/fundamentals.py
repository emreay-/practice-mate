from enum import Enum


__all__ = ["SemiTone", "NoteName", "NoteIndex", "Modifier", "Spn"]


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
        if args[0] in range(0, 144):
            return super().__new__(cls, *args, **kwargs)
        raise ValueError(f"Invalid note index {args[0]}")


class NoteName(str, Enum):
    c = "C"
    d = "D"
    e = "E"
    f = "F"
    g = "G"
    a = "A"
    b = "B"


class Modifier(str, Enum):
    flat = "♭"
    sharp = "♯"
    natural = "♮"
    double_flat = "♭♭"
    double_sharp = "♯♯"
