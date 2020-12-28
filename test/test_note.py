import pytest
from practice_mate.theory.note import NoteName, Modifier, Note, SemiTone, ScientificPitchNotation


def test_spn():
    for i in range(-1, 11, 1):
        i == int(ScientificPitchNotation(i))

    for i in range(11, 21, 1):
        with pytest.raises(ValueError):
            ScientificPitchNotation(i)


def test_repr():
    pitch = ScientificPitchNotation(2)
    for note_name in NoteName:
        for modifier in [None, Modifier.sharp, Modifier.flat, Modifier.double_sharp, Modifier.double_flat]:
            expected_repr = note_name.value
            if modifier:
                expected_repr += modifier.value
            expected_repr = f"<Note {expected_repr}{pitch}>"

            assert expected_repr == repr(Note(note_name, modifier, pitch))


def test_semitone_indices():
    data = {
        (NoteName.c, None): SemiTone(0),
        (NoteName.c, Modifier.natural): SemiTone(0),
        (NoteName.c, Modifier.sharp): SemiTone(1),
        (NoteName.c, Modifier.double_sharp): SemiTone(2),
        (NoteName.c, Modifier.flat): SemiTone(11),
        (NoteName.c, Modifier.double_flat): SemiTone(10),
        
        (NoteName.d, None): SemiTone(2),
        (NoteName.d, Modifier.natural): SemiTone(2),
        (NoteName.d, Modifier.sharp): SemiTone(3),
        (NoteName.d, Modifier.double_sharp): SemiTone(4),
        (NoteName.d, Modifier.flat): SemiTone(1),
        (NoteName.d, Modifier.double_flat): SemiTone(0),

        (NoteName.e, None): SemiTone(4),
        (NoteName.e, Modifier.natural): SemiTone(4),
        (NoteName.e, Modifier.sharp): SemiTone(5),
        (NoteName.e, Modifier.double_sharp): SemiTone(6),
        (NoteName.e, Modifier.flat): SemiTone(3),
        (NoteName.e, Modifier.double_flat): SemiTone(2),

        (NoteName.f, None): SemiTone(5),
        (NoteName.f, Modifier.natural): SemiTone(5),
        (NoteName.f, Modifier.sharp): SemiTone(6),
        (NoteName.f, Modifier.double_sharp): SemiTone(7),
        (NoteName.f, Modifier.flat): SemiTone(4),
        (NoteName.f, Modifier.double_flat): SemiTone(3),

        (NoteName.g, None): SemiTone(7),
        (NoteName.g, Modifier.natural): SemiTone(7),
        (NoteName.g, Modifier.sharp): SemiTone(8),
        (NoteName.g, Modifier.double_sharp): SemiTone(9),
        (NoteName.g, Modifier.flat): SemiTone(6),
        (NoteName.g, Modifier.double_flat): SemiTone(5),

        (NoteName.a, None): SemiTone(9),
        (NoteName.a, Modifier.natural): SemiTone(9),
        (NoteName.a, Modifier.sharp): SemiTone(10),
        (NoteName.a, Modifier.double_sharp): SemiTone(11),
        (NoteName.a, Modifier.flat): SemiTone(8),
        (NoteName.a, Modifier.double_flat): SemiTone(7),

        (NoteName.b, None): SemiTone(11),
        (NoteName.b, Modifier.natural): SemiTone(11),
        (NoteName.b, Modifier.sharp): SemiTone(0),
        (NoteName.b, Modifier.double_sharp): SemiTone(1),
        (NoteName.b, Modifier.flat): SemiTone(10),
        (NoteName.b, Modifier.double_flat): SemiTone(9),
    }

    for (note_name, modifier), expected_semitone_index in data.items():
        assert expected_semitone_index == Note(note_name, modifier)._semitone_index
