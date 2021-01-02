from typing import Type, Generator
from enum import Enum


__all__ = ["cycle_enum"]


def cycle_enum(enum_type: Type[Enum]) -> Generator[Enum, None, None]:
    i = 0
    elements = [i for i in enum_type]

    while True:
        yield elements[i]
        i += 1
        i %= len(elements)
