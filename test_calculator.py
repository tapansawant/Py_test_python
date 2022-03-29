import Calculator
import pytest


@pytest.mark.parametrize("a,b,c", [(3, 2, 5), (5, 7, 12), (10, 54, 64), (7, 8, 15)])
def test_add(a, b, c):
    result = Calculator.add(a, b)
    assert c == result


@pytest.mark.parametrize("a,b,c", [(3, 2, 1), (5, 7, -2), (10, 5, 5), (7, 8, -1)])
def test_sub(a, b, c):
    result = Calculator.sub(a, b)
    assert c == result


@pytest.mark.parametrize("a,b,c", [(3, 2, 6), (5, 7, 35), (10, 54, 540), (7, 8, 56)])
def test_mult(a, b, c):
    result = Calculator.mult(a, b)
    assert c == result


@pytest.mark.parametrize("a,b,c", [(4, 2, 2), (14, 7, 2), (10, 5, 2), (24, 8, 3)])
def test_div(a, b, c):
    result = Calculator.div(a, b)
    assert c == result
