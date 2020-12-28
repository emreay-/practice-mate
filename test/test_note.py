import pytest
from practice_mate.theory.fundamentals import *
from practice_mate.theory.interval import *
from practice_mate.theory.note import Note, determine_notes_from_index, NoteRangeException


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


def test_invalid_note():
    Note(NoteName.c, pitch=Spn(-1))
    Note(NoteName.c, pitch=Spn(-1), modifier=Modifier.sharp)
    Note(NoteName.b, pitch=Spn(10))
    Note(NoteName.b, pitch=Spn(10), modifier=Modifier.flat)

    with pytest.raises(NoteRangeException):
        Note(NoteName.c, pitch=Spn(-1), modifier=Modifier.flat)

    with pytest.raises(NoteRangeException):
        Note(NoteName.c, pitch=Spn(-1), modifier=Modifier.double_flat)

    with pytest.raises(NoteRangeException):
        Note(NoteName.b, pitch=Spn(10), modifier=Modifier.sharp)

    with pytest.raises(NoteRangeException):
        Note(NoteName.b, pitch=Spn(10), modifier=Modifier.double_sharp)


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


def test_inequality():
    assert Note(NoteName.c, pitch=Spn(4)) >= Note(NoteName.c, pitch=Spn(4))
    assert Note(NoteName.c, pitch=Spn(4)) >= Note(NoteName.c, pitch=Spn(3))
    assert Note(NoteName.c, pitch=Spn(4)) > Note(NoteName.c, pitch=Spn(3))
    assert Note(NoteName.c, pitch=Spn(2)) < Note(NoteName.c, pitch=Spn(3))
    assert Note(NoteName.c, pitch=Spn(2)) <= Note(NoteName.c, pitch=Spn(3))
    assert Note(NoteName.c, pitch=Spn(2)) <= Note(NoteName.c, pitch=Spn(2))


def _get_notes_for_pitch(pitch):
    return [
        (Note(NoteName.c, pitch=pitch),),
        (Note(NoteName.c, pitch=pitch, modifier=Modifier.sharp), Note(NoteName.d, pitch=pitch, modifier=Modifier.flat),),
        (Note(NoteName.d, pitch=pitch),),
        (Note(NoteName.d, pitch=pitch, modifier=Modifier.sharp), Note(NoteName.e, pitch=pitch, modifier=Modifier.flat),),
        (Note(NoteName.e, pitch=pitch),),
        (Note(NoteName.f, pitch=pitch),),
        (Note(NoteName.f, pitch=pitch, modifier=Modifier.sharp), Note(NoteName.g, pitch=pitch, modifier=Modifier.flat),),
        (Note(NoteName.g, pitch=pitch),),
        (Note(NoteName.g, pitch=pitch, modifier=Modifier.sharp), Note(NoteName.a, pitch=pitch, modifier=Modifier.flat),),
        (Note(NoteName.a, pitch=pitch),),
        (Note(NoteName.a, pitch=pitch, modifier=Modifier.sharp), Note(NoteName.b, pitch=pitch, modifier=Modifier.flat),),
        (Note(NoteName.b, pitch=pitch),),
    ]


def test_determine_notes_from_index():
    data = []
    for pitch in range(-1, 11, 1):
        data += _get_notes_for_pitch(Spn(pitch))

    for i in range(0, 144):
        assert data[i] == determine_notes_from_index(i)


def test_from_str():
    assert Note.from_str("E0") == Note(NoteName.e, pitch=Spn(0), modifier=None)
    assert Note.from_str("E#0") == Note(NoteName.e, pitch=Spn(0), modifier=Modifier.sharp)
    assert Note.from_str("E##0") == Note(NoteName.e, pitch=Spn(0), modifier=Modifier.double_sharp)
    assert Note.from_str("Eb0") == Note(NoteName.e, pitch=Spn(0), modifier=Modifier.flat)
    assert Note.from_str("Ebb0") == Note(NoteName.e, pitch=Spn(0), modifier=Modifier.double_flat)


def test_apply():
    doubly_augmented_second = Interval.from_str("Doubly augmented 2nd")
    perfect_fourth = Interval.from_str("Perfect 4th")
    perfect_fifth = Interval.from_str("Perfect 5th")
    minor_sixth = Interval.from_str("Minor 6th")
    diminished_sixth = Interval.from_str("Diminished 6th")
    doubly_diminished_sixth = Interval.from_str("Doubly diminished 6th")

    assert Note.from_str("A4").apply(doubly_augmented_second) == Note.from_str("B##4")

    assert Note.from_str("C4").apply(perfect_fifth) == Note.from_str("G4")
    assert Note.from_str("G4").apply(perfect_fifth) == Note.from_str("D5")
    assert Note.from_str("D5").apply(perfect_fifth) == Note.from_str("A5")
    assert Note.from_str("A5").apply(perfect_fifth) == Note.from_str("E6")
    assert Note.from_str("E6").apply(perfect_fifth) == Note.from_str("B6")
    assert Note.from_str("B6").apply(perfect_fifth) == Note.from_str("F#7")
    assert Note.from_str("F#7").apply(perfect_fifth) == Note.from_str("Db8")
    assert Note.from_str("Db8").apply(perfect_fifth) == Note.from_str("Ab8")
    assert Note.from_str("Ab8").apply(perfect_fifth) == Note.from_str("Eb9")
    assert Note.from_str("Eb9").apply(perfect_fifth) == Note.from_str("Bb9")
    assert Note.from_str("Bb9").apply(perfect_fifth) == Note.from_str("F10")
    assert Note.from_str("F9").apply(perfect_fifth) == Note.from_str("C10")

    assert Note.from_str("G2").apply(perfect_fourth) == Note.from_str("C3")
    assert Note.from_str("D2").apply(perfect_fourth) == Note.from_str("G2")
    assert Note.from_str("A2").apply(perfect_fourth) == Note.from_str("D3")
    assert Note.from_str("E2").apply(perfect_fourth) == Note.from_str("A2")
    assert Note.from_str("B2").apply(perfect_fourth) == Note.from_str("E3")
    assert Note.from_str("Db2").apply(perfect_fourth) == Note.from_str("F#2")
    assert Note.from_str("Ab3").apply(perfect_fourth) == Note.from_str("Db4")
    assert Note.from_str("Eb3").apply(perfect_fourth) == Note.from_str("Ab3")
    assert Note.from_str("Bb3").apply(perfect_fourth) == Note.from_str("Eb4")
    assert Note.from_str("F4").apply(perfect_fourth) == Note.from_str("Bb4")
    assert Note.from_str("C4").apply(perfect_fourth) == Note.from_str("F4")

    assert Note.from_str("C4").apply(minor_sixth) == Note.from_str("Ab4")
    assert Note.from_str("C4").apply(diminished_sixth) == Note.from_str("Abb4")
    assert Note.from_str("C4").apply(doubly_diminished_sixth) == Note.from_str("Abbb4")
