import pygame


class Screen:
    def __init__(self, width, height):
        self.screen = pygame.display.set_mode((width, height))

