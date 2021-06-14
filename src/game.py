from src.setup import *
from src.views import View, RunView

import pygame


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(GAME_NAME)
        pygame.display.set_icon(pygame.image.load(ICON_PATH))

        self.current_view = View()
        self.screen = None
        self.clock = None
        self.running = None

    def run(self):
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
        self.set_current_view(RunView())

        self.running = True
        self.mainloop()

    def mainloop(self):
        while self.running:
            self.clock.tick(FPS_LIMIT)
            self.event_handler()
            keys = pygame.key.get_pressed()
            self.current_view.key_handler(keys)
            self.current_view.draw_on_screen(self.screen)
            pygame.display.update()

    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def set_current_view(self, new_view: View):
        self.current_view = new_view
