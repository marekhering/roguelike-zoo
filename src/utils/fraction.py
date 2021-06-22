from src.setup import FRACTION_DIVIDER


class Fraction:
    DIVIDER = FRACTION_DIVIDER

    def __init__(self, value):
        self.value = value
        self.fraction = self.calculate_fraction()
        self._check_fraction()

    def calculate_fraction(self):
        return self.value / Fraction.DIVIDER

    def add(self, value):
        self.value += value
        self.fraction = self.calculate_fraction()
        self._check_fraction(set_values=True)

    def __mul__(self, other):
        return self.fraction * other

    def __rmul__(self, other):
        return self.fraction * other

    def _check_fraction(self, set_values=False):
        if set_values:
            if self.fraction < 0:
                self.value = 0
                self.fraction = 0
            elif self.fraction > 1:
                self.value = Fraction.DIVIDER
                self.fraction = 1
        else:
            if self.fraction < 0 or self.fraction > 1:
                raise ValueError

    def copy(self):
        return Fraction(self.get_value())

    def get_value(self):
        return self.value

    def get_fraction(self):
        return self.fraction

    @staticmethod
    def max():
        return Fraction(Fraction.DIVIDER)
