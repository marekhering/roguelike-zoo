from src.screen_engine.layer import Layer
from src.utils.fraction import Fraction as Fr

import pygame


class Screen:
    def __init__(self, width, height):
        self.x = 0
        self.y = 0
        self.width = width
        self.height = height
        self.pygame_screen = pygame.display.set_mode((width, height))
        self.layer = Layer(Fr(0), Fr(0), Fr(1000), Fr(1000), self)
        self.background_color = None

    def set_background_color(self, rgb_color):
        self.background_color = rgb_color

    def draw_screen(self):
        if self.background_color:
            self.pygame_screen.fill(self.background_color)

        self.layer.draw_layer(self.pygame_screen)

    def find_object(self, position):
        return self.layer.find_object_on_layer(position)

    def get_main_layer(self):
        return self.layer

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

