import sys
import pytest

sys.path.append("../")

from exercice1 import Calculator

calculator = Calculator()

def test_add():
    result = calculator.add(2, 2)
    assert result == 4
    assert calculator.get_memory() == 4

def test_subtract():
    result = calculator.subtract(2, 2)
    assert result == 0
    assert calculator.get_memory() == 0

def test_multiply():
    result = calculator.multiply(6, 3)
    assert result == 18
    assert calculator.get_memory() == 18

def test_divide():
    result = calculator.divide(4, 2)
    assert result == 2
    assert calculator.get_memory() == 2

    with pytest.raises(ValueError):
        calculator.divide(4, 0)

def test_power():
    result = calculator.power(2, 2)
    assert result == 4
    assert calculator.get_memory() == 4

def test_sqrt():
    result = calculator.sqrt(16)
    assert result == 4
    assert calculator.get_memory() == 4

    with pytest.raises(ValueError):
        calculator.sqrt(-1)

def test_clear_memory():
    calculator.add(2, 3)
    calculator.clear_memory()
    assert calculator.get_memory() == 0
