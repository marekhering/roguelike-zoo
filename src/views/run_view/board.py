from typing import List, Union
import random

from src.screen_engine import Layer
from .field import Field
from src.utils import Fraction as Fr


class Board:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.field_width = Fr(1 / self.width)
        self.field_height = Fr(1 / self.height)

        self.fields = self.create_blank_board()
        self.starting_field = self.add_start_field()

    def create_blank_board(self) -> List[List[Field]]:
        fields = list()
        for y in range(self.height):
            y_fraction = Fr(y / self.height)
            fields_row = list()
            for x in range(self.width):
                x_fraction = Fr(x / self.width)
                fields_row.append(Field(x_fraction, y_fraction, self.field_width, self.field_height, x, y))
            fields.append(fields_row)
        return fields

    def if_field_open(self, field_x: int, field_y: int) -> bool:
        if not (0 <= field_x < self.width):
            return False

        if not (0 <= field_y < self.height):
            return False

        return True

    def add_start_field(self):
        start_x = random.randint(0, self.width - 1)
        start_y = random.randint(0, self.height - 1)
        return self.fields[start_y][start_x]

    def set_on_layer(self, layer: Layer):
        for field in self.get_fields():
            layer.add_drawable_object_to_front(field)

    def get_field_width(self) -> Fr:
        return self.field_width

    def get_field_height(self) -> Fr:
        return self.field_height

    def get_field_offset(self, param_1: Union[int, Field], param_2: int = None):
        if type(param_1) == Field and param_2 is None:
            x = param_1.get_field_x()
            y = param_1.get_field_y()
            return Fr(self.get_field_width() * x), Fr(self.get_field_height() * y)
        elif type(param_1) == int and type(param_2) == int:
            return Fr(self.get_field_width() * param_1), Fr(self.get_field_height() * param_2)
        else:
            raise TypeError

    def get_starting_field(self):
        return self.starting_field

    def get_field(self, field_x: int, field_y: int) -> Field:
        return self.fields[field_y][field_x]

    def get_fields(self):
        flat_fields = []
        [flat_fields.extend(field_row) for field_row in self.fields]
        return flat_fields
