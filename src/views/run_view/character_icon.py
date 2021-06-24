
from src.utils import Fraction as Fr
from src.characters import Character
from src.screen_engine import Drawable
from .board import Board


class CharacterIcon(Drawable):
    def __init__(self,  board: Board, character: Character):
        self.board = board
        self.character = character
        self.current_field = board.get_starting_field()

        start_x_offset, start_y_offset = self.board.get_field_offset(self.current_field)
        icon_width = self.board.get_field_width()
        icon_height = self.board.get_field_height()
        super().__init__(start_x_offset, start_y_offset, icon_width, icon_height, character.get_icon_path())

    def move(self, value: int, horizontally=False, vertically=False):
        if vertically == horizontally:
            raise ValueError

        new_field_x = self.current_field.get_field_x()
        new_field_y = self.current_field.get_field_y()

        if horizontally:
            new_field_x += value
        if vertically:
            new_field_y += value

        if self.board.if_field_open(new_field_x, new_field_y):
            self.change_current_field(new_field_x, new_field_y)

    def change_current_field(self, new_field_x, new_field_y):
        self.current_field = self.board.get_field(new_field_x, new_field_y)
        start_x_offset, start_y_offset = self.board.get_field_offset(self.current_field)
        self.x_fraction = start_x_offset
        self.y_fraction = start_y_offset

