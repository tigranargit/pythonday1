
import factorial
import list_of_squares
import vowels


def test_factorial():
    assert factorial.fact(4) == 24

def test_list_of_squares():
    assert list_of_squares.list_of_squares(2) == {1: 1, 2: 4}

def test_vowels():
    assert vowels.sounds("dream") == 2