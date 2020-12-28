from practice_mate.theory.note import NoteName, Modifier, Note, SemiTone


def test_repr():
    for note_name in NoteName:
        for modifications in [None, (Modifier.sharp,), (Modifier.flat,), 
                             (Modifier.sharp, Modifier.sharp), (Modifier.flat, Modifier.flat)]:
            expected_repr = note_name.value
            if modifications:
                for m in modifications:
                    expected_repr += m.value
            expected_repr = f"<Note {expected_repr}>"

            assert expected_repr == repr(Note(note_name, modifications))


def test_semitone_indices():
    data = {
        (NoteName.c, None): SemiTone(0),
        (NoteName.c, (Modifier.sharp,)): SemiTone(1),
        (NoteName.c, (Modifier.sharp, Modifier.sharp)): SemiTone(2),
        (NoteName.c, (Modifier.flat,)): SemiTone(11),
        (NoteName.c, (Modifier.flat, Modifier.flat)): SemiTone(10),
        
        (NoteName.d, None): SemiTone(2),
        (NoteName.d, (Modifier.sharp,)): SemiTone(3),
        (NoteName.d, (Modifier.sharp, Modifier.sharp)): SemiTone(4),
        (NoteName.d, (Modifier.flat,)): SemiTone(1),
        (NoteName.d, (Modifier.flat, Modifier.flat)): SemiTone(0),

        (NoteName.e, None): SemiTone(4),
        (NoteName.e, (Modifier.sharp,)): SemiTone(5),
        (NoteName.e, (Modifier.sharp, Modifier.sharp)): SemiTone(6),
        (NoteName.e, (Modifier.flat,)): SemiTone(3),
        (NoteName.e, (Modifier.flat, Modifier.flat)): SemiTone(2),

        (NoteName.f, None): SemiTone(5),
        (NoteName.f, (Modifier.sharp,)): SemiTone(6),
        (NoteName.f, (Modifier.sharp, Modifier.sharp)): SemiTone(7),
        (NoteName.f, (Modifier.flat,)): SemiTone(4),
        (NoteName.f, (Modifier.flat, Modifier.flat)): SemiTone(3),

        (NoteName.g, None): SemiTone(7),
        (NoteName.g, (Modifier.sharp,)): SemiTone(8),
        (NoteName.g, (Modifier.sharp, Modifier.sharp)): SemiTone(9),
        (NoteName.g, (Modifier.flat,)): SemiTone(6),
        (NoteName.g, (Modifier.flat, Modifier.flat)): SemiTone(5),

        (NoteName.a, None): SemiTone(9),
        (NoteName.a, (Modifier.sharp,)): SemiTone(10),
        (NoteName.a, (Modifier.sharp, Modifier.sharp)): SemiTone(11),
        (NoteName.a, (Modifier.flat,)): SemiTone(8),
        (NoteName.a, (Modifier.flat, Modifier.flat)): SemiTone(7),

        (NoteName.b, None): SemiTone(11),
        (NoteName.b, (Modifier.sharp,)): SemiTone(0),
        (NoteName.b, (Modifier.sharp, Modifier.sharp)): SemiTone(1),
        (NoteName.b, (Modifier.flat,)): SemiTone(10),
        (NoteName.b, (Modifier.flat, Modifier.flat)): SemiTone(9),
    }

    for (note_name, modifiers), expected_semitone_index in data.items():
        assert expected_semitone_index == Note(note_name, modifiers)._semitone_index