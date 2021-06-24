import pygame

from src.mouse import Mouse
from src.screen_engine import Screen
from src.utils import Fraction as Fr
from src.characters import Character

from ..view import View
from .board import Board
from .character_icon import CharacterIcon


class RunView(View):
    def __init__(self, screen: Screen, character: Character):
        super().__init__(screen)

        self.character = character
        self.screen.set_background_color((144, 255, 160))

        # Layers
        self.base_layer = self.screen.get_base_layer()
        self.run_map_layer = self.base_layer.create_top_layer(Fr(0), Fr(100), Fr.max(), Fr(800))
        self.board_layer = self.run_map_layer.create_top_layer(Fr(100), Fr(100), Fr(700), Fr(800))

        # Board
        self.board = Board(10, 10)
        self.board.set_on_layer(self.board_layer)

        # Character Icon
        self.character_icon = CharacterIcon(self.board, self.character)
        self.board_layer.add_drawable_object_to_front(self.character_icon)

    def key_handler(self, keys, mouse: Mouse):

        if mouse.if_left_button_up():
            clicked_object = self.screen.find_object(mouse.get_position())
            if clicked_object:
                clicked_object.on_click()

        if keys[pygame.K_UP]:
            self.character_icon.move(-1, vertically=True)
        if keys[pygame.K_DOWN]:
            self.character_icon.move(1, vertically=True)
        if keys[pygame.K_LEFT]:
            self.character_icon.move(-1, horizontally=True)
        if keys[pygame.K_RIGHT]:
            self.character_icon.move(1, horizontally=True)



