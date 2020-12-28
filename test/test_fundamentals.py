from practice_mate.theory.fundamentals import cycle, NoteName


def test_cycle():
    inclusive_iterator = cycle(root=NoteName.f, inclusive_start=True)
    exclusive_iterator = cycle(root=NoteName.f, inclusive_start=False)
    index_to_note = {
        0: NoteName.f,
        1: NoteName.g, 
        2: NoteName.a,
        3: NoteName.b,
        4: NoteName.c,
        5: NoteName.d,
        6: NoteName.e
    }
    
    for i in range(100):
        index_to_note[i % 7] == next(inclusive_iterator)
        index_to_note[(i + 1) % 7] == next(exclusive_iterator)
