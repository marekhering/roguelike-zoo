from .layer import Layer
from .frame import Frame

from src.utils import Point, Fraction as Fr

import pygame


class Screen(Frame):
    def __init__(self, width: int, height: int):
        super(Screen, self).__init__(Point(0, 0), width, height)

        self.pygame_screen = pygame.display.set_mode((width, height))
        self.base_layer = Layer(Fr(0), Fr(0), Fr.max(), Fr.max(), self)
        self.background_color = None

    def set_background_color(self, rgb_color):
        self.background_color = rgb_color

    def draw_screen(self):
        if self.background_color:
            self.pygame_screen.fill(self.background_color)

        self.base_layer.draw_layer(self.pygame_screen)

    def find_object(self, position):
        signal, found_object = self.base_layer.find_object_on_layer(position)
        if signal == 1:
            return found_object

    def get_base_layer(self):
        return self.base_layer


