from calc import add


def test_calc_add__add_positives():
    assert add(1, 2) == 3, 'Return value shall be 3'


def test_calc_add__add_negatives():
    assert add(-1, -2) == -3, 'Return value shall be -3'


def test_calc_add__add_mixed():
    assert add(-1, 3) == 2, 'Return value shall be 2'
