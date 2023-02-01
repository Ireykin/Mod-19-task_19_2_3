import pytest
from app.calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

# тест умножения
    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 2, 2) == 4
        
# тест умножения
    def test_division_calculate_correctly(self):
        assert self.calc.division(self, 4, 2) == 2
        
# тест умножения
    def test_subtraction_calculate_correctly(self):
        assert self.calc.subtraction(self, 5, 2) == 3
        
# тест умножения
    def test_adding_calculate_correctly(self):
        assert self.calc.adding(self, 5, 2) == 7

