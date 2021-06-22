from typing import Union, Tuple

from .fraction import Fraction as Fr


class Point(list):
    def __init__(self, x: Union[Fr, int], y: Union[Fr, int]):
        if type(x) != type(y):
            raise ValueError
        super().__init__([x, y])
        self.x = x
        self.y = y

    def get_value_type(self) -> type:
        return type(self.x)

    def get_x(self) -> Union[Fr, int]:
        return self.x

    def get_y(self) -> Union[Fr, int]:
        return self.y

    def as_tuple(self) -> Tuple[Union[Fr, int], Union[Fr, int]]:
        return self.x, self.y
