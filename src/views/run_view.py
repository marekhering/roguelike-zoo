from .view import View

import pygame


class RunView(View):
    def __init__(self):
        super().__init__()

    def key_handler(self, keys):
        if keys[pygame.K_UP]:
            print("UP Key")
        if keys[pygame.K_DOWN]:
            print("Down Key")

