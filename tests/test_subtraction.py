"""Unit tests for subtraction."""
from app.calculator import Calculator

def test_subtract():
    """Test subtraction of two numbers."""
    calc = Calculator()
    assert calc.subtract(5, 2) == 3
    assert calc.subtract(0, 3) == -3
    assert calc.subtract(-2, -2) == 0
