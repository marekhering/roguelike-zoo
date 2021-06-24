from typing import Union

from src.setup import FRACTION_DIVIDER


class Fraction:
    DIVIDER = FRACTION_DIVIDER

    def __init__(self, value: Union[int, float]):
        if type(value) == int:
            self.int_value = value
            self.float_value = self.calculate_float_value()
        if type(value) == float:
            self.float_value = value
            self.int_value = self.calculate_int_value()

        self._check_fraction()

    def calculate_float_value(self) -> float:
        return float(self.int_value / Fraction.DIVIDER)

    def calculate_int_value(self) -> int:
        return int(self.float_value * Fraction.DIVIDER)

    def add(self, value: Union[int, float]):
        if type(value) == int:
            self.int_value += value
            self.float_value = self.calculate_float_value()
        if type(value) == float:
            self.float_value += value
            self.int_value = self.calculate_int_value()
        self._check_fraction(set_values=True)

    def __mul__(self, other):
        return self.float_value * other

    def __rmul__(self, other):
        return self.float_value * other

    def _check_fraction(self, set_values=False):
        if set_values:
            if self.float_value < 0:
                self.int_value = 0
                self.float_value = 0
            elif self.float_value > 1:
                self.int_value = Fraction.DIVIDER
                self.float_value = 1
        else:
            if self.float_value < 0 or self.float_value > 1:
                raise ValueError

    def copy(self):
        return Fraction(self.get_int_value())

    def get_int_value(self) -> int:
        return self.int_value

    def get_float_value(self) -> float:
        return self.float_value

    @staticmethod
    def max():
        return Fraction(Fraction.DIVIDER)

