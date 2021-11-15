from calc import multiply


def test_calc_multiply__multiply_positives():
    assert multiply(2, 2) == 4, 'Return value shall be 4'


def test_calc_multiply__multiply_negatives():
    assert multiply(-3, -2) == 'fail', 'Return value shall be 6'


def test_calc_multiply__multiply_mixed():
    assert multiply(3, -2) == -6, 'Return value shall be -6'
