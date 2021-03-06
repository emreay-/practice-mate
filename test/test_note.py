import pytest
from practice_mate.theory.fundamentals import *
from practice_mate.theory.interval import *
from practice_mate.theory.note import Note, determine_notes_from_index, NoteRangeException, NotePitchAwarenessException


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
    assert Note(NoteName.c, modifier=None).index is None
    assert Note(NoteName.c, modifier=Modifier.natural).index is None
    assert Note(NoteName.c, modifier=Modifier.sharp).index is None
    assert Note(NoteName.c, modifier=Modifier.double_sharp).index is None

    assert Note(NoteName.c, pitch=Spn(4), modifier=None).index == NoteIndex(60)
    assert Note(NoteName.c, pitch=Spn(4), modifier=Modifier.natural).index == NoteIndex(60)
    assert Note(NoteName.c, pitch=Spn(4), modifier=Modifier.sharp).index == NoteIndex(61)
    assert Note(NoteName.c, pitch=Spn(4), modifier=Modifier.double_sharp).index == NoteIndex(62)

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


def test_base_indices():
    assert Note(NoteName.c, pitch=Spn(4), modifier=None).base_index == NoteIndex(0)
    assert Note(NoteName.c, pitch=Spn(4), modifier=Modifier.natural).base_index == NoteIndex(0)
    assert Note(NoteName.c, pitch=Spn(4), modifier=Modifier.sharp).base_index == NoteIndex(1)
    assert Note(NoteName.c, pitch=Spn(4), modifier=Modifier.double_sharp).base_index == NoteIndex(2)

    assert Note(NoteName.d, pitch=Spn(4), modifier=None).base_index == NoteIndex(2)
    assert Note(NoteName.d, pitch=Spn(4), modifier=Modifier.natural).base_index == NoteIndex(2)
    assert Note(NoteName.d, pitch=Spn(4), modifier=Modifier.sharp).base_index == NoteIndex(3)
    assert Note(NoteName.d, pitch=Spn(4), modifier=Modifier.double_sharp).base_index == NoteIndex(4)
    assert Note(NoteName.d, pitch=Spn(4), modifier=Modifier.flat).base_index == NoteIndex(1)
    assert Note(NoteName.d, pitch=Spn(4), modifier=Modifier.double_flat).base_index == NoteIndex(0)

    assert Note(NoteName.e, pitch=Spn(4), modifier=None).base_index == NoteIndex(4)
    assert Note(NoteName.e, pitch=Spn(4), modifier=Modifier.natural).base_index == NoteIndex(4)
    assert Note(NoteName.e, pitch=Spn(4), modifier=Modifier.sharp).base_index == NoteIndex(5)
    assert Note(NoteName.e, pitch=Spn(4), modifier=Modifier.double_sharp).base_index == NoteIndex(6)
    assert Note(NoteName.e, pitch=Spn(4), modifier=Modifier.flat).base_index == NoteIndex(3)
    assert Note(NoteName.e, pitch=Spn(4), modifier=Modifier.double_flat).base_index == NoteIndex(2)

    assert Note(NoteName.f, pitch=Spn(4), modifier=None).base_index == NoteIndex(5)
    assert Note(NoteName.f, pitch=Spn(4), modifier=Modifier.natural).base_index == NoteIndex(5)
    assert Note(NoteName.f, pitch=Spn(4), modifier=Modifier.sharp).base_index == NoteIndex(6)
    assert Note(NoteName.f, pitch=Spn(4), modifier=Modifier.double_sharp).base_index == NoteIndex(7)
    assert Note(NoteName.f, pitch=Spn(4), modifier=Modifier.flat).base_index == NoteIndex(4)
    assert Note(NoteName.f, pitch=Spn(4), modifier=Modifier.double_flat).base_index == NoteIndex(3)

    assert Note(NoteName.g, pitch=Spn(4), modifier=None).base_index == NoteIndex(7)
    assert Note(NoteName.g, pitch=Spn(4), modifier=Modifier.natural).base_index == NoteIndex(7)
    assert Note(NoteName.g, pitch=Spn(4), modifier=Modifier.sharp).base_index == NoteIndex(8)
    assert Note(NoteName.g, pitch=Spn(4), modifier=Modifier.double_sharp).base_index == NoteIndex(9)
    assert Note(NoteName.g, pitch=Spn(4), modifier=Modifier.flat).base_index == NoteIndex(6)
    assert Note(NoteName.g, pitch=Spn(4), modifier=Modifier.double_flat).base_index == NoteIndex(5)

    assert Note(NoteName.a, pitch=Spn(4), modifier=None).base_index == NoteIndex(9)
    assert Note(NoteName.a, pitch=Spn(4), modifier=Modifier.natural).base_index == NoteIndex(9)
    assert Note(NoteName.a, pitch=Spn(4), modifier=Modifier.sharp).base_index == NoteIndex(10)
    assert Note(NoteName.a, pitch=Spn(4), modifier=Modifier.double_sharp).base_index == NoteIndex(11)
    assert Note(NoteName.a, pitch=Spn(4), modifier=Modifier.flat).base_index == NoteIndex(8)
    assert Note(NoteName.a, pitch=Spn(4), modifier=Modifier.double_flat).base_index == NoteIndex(7)

    assert Note(NoteName.b, pitch=Spn(4), modifier=None).base_index == NoteIndex(11)
    assert Note(NoteName.b, pitch=Spn(4), modifier=Modifier.natural).base_index == NoteIndex(11)
    assert Note(NoteName.b, pitch=Spn(4), modifier=Modifier.sharp).base_index == NoteIndex(0)
    assert Note(NoteName.b, pitch=Spn(4), modifier=Modifier.double_sharp).base_index == NoteIndex(1)


def test_equality():
    assert Note(NoteName.c) == Note(NoteName.c)
    assert Note.from_str("C") == Note.from_str("C")
    assert Note.from_str("C4") == Note.from_str("C4")

    with pytest.raises(NotePitchAwarenessException):
        assert Note.from_str("C") == Note.from_str("C4")

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

    assert Note(NoteName.c) <= Note(NoteName.c)
    assert Note(NoteName.c) <= Note(NoteName.d)
    assert Note(NoteName.c) < Note(NoteName.e)
    assert Note(NoteName.e) > Note(NoteName.d)

    with pytest.raises(NotePitchAwarenessException):
        assert Note.from_str("C") < Note.from_str("D4")


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
        assert data[i] == determine_notes_from_index(NoteIndex(i))


def test_from_str():
    assert Note.from_str("E") == Note(NoteName.e, pitch=None, modifier=None)
    assert Note.from_str("E#") == Note(NoteName.e, pitch=None, modifier=Modifier.sharp)
    assert Note.from_str("E##") == Note(NoteName.e, pitch=None, modifier=Modifier.double_sharp)
    assert Note.from_str("E###") == Note(NoteName.e, pitch=None, modifier=Modifier.triple_sharp)
    assert Note.from_str("Eb") == Note(NoteName.e, pitch=None, modifier=Modifier.flat)
    assert Note.from_str("Ebb") == Note(NoteName.e, pitch=None, modifier=Modifier.double_flat)
    assert Note.from_str("Ebbb") == Note(NoteName.e, pitch=None, modifier=Modifier.triple_flat)
    assert Note.from_str("E-1") == Note(NoteName.e, pitch=Spn(-1), modifier=None)
    assert Note.from_str("E0") == Note(NoteName.e, pitch=Spn(0), modifier=None)
    assert Note.from_str("E#0") == Note(NoteName.e, pitch=Spn(0), modifier=Modifier.sharp)
    assert Note.from_str("E##0") == Note(NoteName.e, pitch=Spn(0), modifier=Modifier.double_sharp)
    assert Note.from_str("Eb0") == Note(NoteName.e, pitch=Spn(0), modifier=Modifier.flat)
    assert Note.from_str("Ebb0") == Note(NoteName.e, pitch=Spn(0), modifier=Modifier.double_flat)


def test_apply():
    doubly_augmented_second = Interval.from_str("Doubly augmented 2nd")
    perfect_fourth = Interval.from_str("Perfect 4th")
    perfect_fifth = Interval.from_str("Perfect 5th")
    perfect_unison = Interval.from_str("Perfect unison")
    perfect_twelfth = Interval.from_str("Perfect 12th")
    minor_sixth = Interval.from_str("Minor 6th")
    diminished_sixth = Interval.from_str("Diminished 6th")
    doubly_diminished_sixth = Interval.from_str("Doubly diminished 6th")

    assert Note.from_str("C-1").apply(perfect_fifth) == Note.from_str("G-1")
    assert Note.from_str("A").apply(perfect_unison) == Note.from_str("A")
    assert Note.from_str("A4").apply(perfect_unison) == Note.from_str("A4")
    assert Note.from_str("A").apply(doubly_augmented_second) == Note.from_str("B##")
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

    assert Note.from_str("C").apply(perfect_fifth) == Note.from_str("G")
    assert Note.from_str("G").apply(perfect_fifth) == Note.from_str("D")
    assert Note.from_str("D").apply(perfect_fifth) == Note.from_str("A")
    assert Note.from_str("A").apply(perfect_fifth) == Note.from_str("E")
    assert Note.from_str("E").apply(perfect_fifth) == Note.from_str("B")
    assert Note.from_str("B").apply(perfect_fifth) == Note.from_str("F#")
    assert Note.from_str("F#").apply(perfect_fifth) == Note.from_str("Db")
    assert Note.from_str("Db").apply(perfect_fifth) == Note.from_str("Ab")
    assert Note.from_str("Ab").apply(perfect_fifth) == Note.from_str("Eb")
    assert Note.from_str("Eb").apply(perfect_fifth) == Note.from_str("Bb")
    assert Note.from_str("Bb").apply(perfect_fifth) == Note.from_str("F")
    assert Note.from_str("F").apply(perfect_fifth) == Note.from_str("C")

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

    assert Note.from_str("G").apply(perfect_fourth) == Note.from_str("C")
    assert Note.from_str("D").apply(perfect_fourth) == Note.from_str("G")
    assert Note.from_str("A").apply(perfect_fourth) == Note.from_str("D")
    assert Note.from_str("E").apply(perfect_fourth) == Note.from_str("A")
    assert Note.from_str("B").apply(perfect_fourth) == Note.from_str("E")
    assert Note.from_str("Db").apply(perfect_fourth) == Note.from_str("F#")
    assert Note.from_str("Ab").apply(perfect_fourth) == Note.from_str("Db")
    assert Note.from_str("Eb").apply(perfect_fourth) == Note.from_str("Ab")
    assert Note.from_str("Bb").apply(perfect_fourth) == Note.from_str("Eb")
    assert Note.from_str("F").apply(perfect_fourth) == Note.from_str("Bb")
    assert Note.from_str("C").apply(perfect_fourth) == Note.from_str("F")

    assert Note.from_str("C4").apply(minor_sixth) == Note.from_str("Ab4")
    assert Note.from_str("C4").apply(diminished_sixth) == Note.from_str("Abb4")
    assert Note.from_str("C4").apply(doubly_diminished_sixth) == Note.from_str("Abbb4")

    assert Note.from_str("C").apply(minor_sixth) == Note.from_str("Ab")
    assert Note.from_str("C").apply(diminished_sixth) == Note.from_str("Abb")
    assert Note.from_str("C").apply(doubly_diminished_sixth) == Note.from_str("Abbb")

    # Compound
    assert Note.from_str("C4").apply(perfect_twelfth) == Note.from_str("G5")
    assert Note.from_str("G4").apply(perfect_twelfth) == Note.from_str("D6")
    assert Note.from_str("D5").apply(perfect_twelfth) == Note.from_str("A6")
    assert Note.from_str("A5").apply(perfect_twelfth) == Note.from_str("E7")
    assert Note.from_str("E6").apply(perfect_twelfth) == Note.from_str("B7")
