import pytest
from practice_mate.theory.note import NoteName, Modifier, Note, NoteIndex, SemiTone, Spn


def test_spn():
    for i in range(-1, 11, 1):
        i == int(Spn(i))

    for i in range(11, 21, 1):
        with pytest.raises(ValueError):
            Spn(i)


def test_repr():
    pitch = Spn(2)
    for note_name in NoteName:
        for modifier in [None, Modifier.sharp, Modifier.flat, Modifier.double_sharp, Modifier.double_flat]:
            expected_repr = note_name.value
            if modifier:
                expected_repr += modifier.value
            expected_repr = f"<Note {expected_repr}{pitch}>"

            assert expected_repr == repr(Note(note_name, pitch, modifier))


def test_indices():
    assert Note(NoteName.c, pitch=Spn(-1), modifier=None).index == NoteIndex(0)
    assert Note(NoteName.c, pitch=Spn(-1), modifier=Modifier.natural).index == NoteIndex(0)
    assert Note(NoteName.c, pitch=Spn(-1), modifier=Modifier.sharp).index == NoteIndex(1)
    assert Note(NoteName.c, pitch=Spn(-1), modifier=Modifier.double_sharp).index == NoteIndex(2)

    assert Note(NoteName.d, pitch=Spn(-1), modifier=None).index == NoteIndex(2)
    assert Note(NoteName.d, pitch=Spn(-1), modifier=Modifier.natural).index == NoteIndex(2)
    assert Note(NoteName.d, pitch=Spn(-1), modifier=Modifier.sharp).index == NoteIndex(3)
    assert Note(NoteName.d, pitch=Spn(-1), modifier=Modifier.double_sharp).index == NoteIndex(4)
    assert Note(NoteName.d, pitch=Spn(-1), modifier=Modifier.flat).index == NoteIndex(1)
    assert Note(NoteName.d, pitch=Spn(-1), modifier=Modifier.double_flat).index == NoteIndex(0)

    assert Note(NoteName.e, pitch=Spn(-1), modifier=None).index == NoteIndex(4)
    assert Note(NoteName.e, pitch=Spn(-1), modifier=Modifier.natural).index == NoteIndex(4)
    assert Note(NoteName.e, pitch=Spn(-1), modifier=Modifier.sharp).index == NoteIndex(5)
    assert Note(NoteName.e, pitch=Spn(-1), modifier=Modifier.double_sharp).index == NoteIndex(6)
    assert Note(NoteName.e, pitch=Spn(-1), modifier=Modifier.flat).index == NoteIndex(3)
    assert Note(NoteName.e, pitch=Spn(-1), modifier=Modifier.double_flat).index == NoteIndex(2)

    assert Note(NoteName.f, pitch=Spn(-1), modifier=None).index == NoteIndex(5)
    assert Note(NoteName.f, pitch=Spn(-1), modifier=Modifier.natural).index == NoteIndex(5)
    assert Note(NoteName.f, pitch=Spn(-1), modifier=Modifier.sharp).index == NoteIndex(6)
    assert Note(NoteName.f, pitch=Spn(-1), modifier=Modifier.double_sharp).index == NoteIndex(7)
    assert Note(NoteName.f, pitch=Spn(-1), modifier=Modifier.flat).index == NoteIndex(4)
    assert Note(NoteName.f, pitch=Spn(-1), modifier=Modifier.double_flat).index == NoteIndex(3)

    assert Note(NoteName.g, pitch=Spn(-1), modifier=None).index == NoteIndex(7)
    assert Note(NoteName.g, pitch=Spn(-1), modifier=Modifier.natural).index == NoteIndex(7)
    assert Note(NoteName.g, pitch=Spn(-1), modifier=Modifier.sharp).index == NoteIndex(8)
    assert Note(NoteName.g, pitch=Spn(-1), modifier=Modifier.double_sharp).index == NoteIndex(9)
    assert Note(NoteName.g, pitch=Spn(-1), modifier=Modifier.flat).index == NoteIndex(6)
    assert Note(NoteName.g, pitch=Spn(-1), modifier=Modifier.double_flat).index == NoteIndex(5)

    assert Note(NoteName.a, pitch=Spn(-1), modifier=None).index == NoteIndex(9)
    assert Note(NoteName.a, pitch=Spn(-1), modifier=Modifier.natural).index == NoteIndex(9)
    assert Note(NoteName.a, pitch=Spn(-1), modifier=Modifier.sharp).index == NoteIndex(10)
    assert Note(NoteName.a, pitch=Spn(-1), modifier=Modifier.double_sharp).index == NoteIndex(11)
    assert Note(NoteName.a, pitch=Spn(-1), modifier=Modifier.flat).index == NoteIndex(8)
    assert Note(NoteName.a, pitch=Spn(-1), modifier=Modifier.double_flat).index == NoteIndex(7)

    assert Note(NoteName.b, pitch=Spn(-1), modifier=None).index == NoteIndex(11)
    assert Note(NoteName.b, pitch=Spn(-1), modifier=Modifier.natural).index == NoteIndex(11)
    assert Note(NoteName.b, pitch=Spn(-1), modifier=Modifier.sharp).index == NoteIndex(12)
    assert Note(NoteName.b, pitch=Spn(-1), modifier=Modifier.double_sharp).index == NoteIndex(13)


def test_equality():
    assert Note(NoteName.c) == Note(NoteName.c)
    assert Note(NoteName.c, pitch=Spn(4), modifier=Modifier.double_sharp) == Note(NoteName.d, pitch=Spn(4),)
    assert Note(NoteName.c, pitch=Spn(4), modifier=Modifier.double_flat) == Note(NoteName.b, pitch=Spn(3), modifier=Modifier.flat)
    assert Note(NoteName.e, pitch=Spn(4), modifier=Modifier.sharp) == Note(NoteName.f, pitch=Spn(4))
    assert Note(NoteName.f, pitch=Spn(4), modifier=Modifier.flat) == Note(NoteName.e, pitch=Spn(4))

    assert not Note(NoteName.c, pitch=Spn(4)) == Note(NoteName.c, pitch=Spn(5))
    assert not Note(NoteName.c, pitch=Spn(4), modifier=Modifier.double_sharp) == Note(NoteName.c, pitch=Spn(4))
    assert not Note(NoteName.c, pitch=Spn(4), modifier=Modifier.double_flat) == Note(NoteName.c, pitch=Spn(4))
    assert not Note(NoteName.c, pitch=Spn(4), modifier=Modifier.sharp) == Note(NoteName.c, pitch=Spn(4))
    assert not Note(NoteName.c, pitch=Spn(4), modifier=Modifier.flat) == Note(NoteName.c, pitch=Spn(4))
