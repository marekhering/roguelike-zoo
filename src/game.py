from src.setup import *
from src.views import View, RunView
from src.screen_engine.screen.screen import Screen
from src.characters import Snake
from .mouse import Mouse

import pygame


class Game:
    def __init__(self):
        self.current_view = None
        self.screen = None
        self.clock = None
        self.running = None

        # For tests
        self.character = None

    def run(self):
        pygame.init()
        pygame.display.set_caption(GAME_NAME)
        pygame.display.set_icon(pygame.image.load(ICON_PATH))

        self.clock = pygame.time.Clock()
        self.screen = Screen(GAME_WIDTH, GAME_HEIGHT)

        # For tests
        self.character = Snake()
        self.set_current_view(RunView(self.screen, self.character))

        self.running = True
        self.mainloop()

    def mainloop(self):
        while self.running:
            self.clock.tick(FPS_LIMIT)
            keys, mouse = self.event_handler()
            self.current_view.key_handler(keys, mouse)
            self.screen.draw_screen()
            pygame.display.update()

    def event_handler(self):
        mouse_down = False
        mouse_up = False

        keys = pygame.key.get_pressed()
        mouse_position = pygame.mouse.get_pos()  # TODO make it point not Tuple
        mouse_buttons = pygame.mouse.get_pressed(3)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_down = True
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_up = True

        mouse = Mouse(mouse_down, mouse_up, mouse_position, mouse_buttons)
        corrected_mouse_buttons = pygame.mouse.get_pressed(3)
        mouse.correct_event(corrected_mouse_buttons)

        return keys, mouse

    def set_current_view(self, new_view: View):
        self.current_view = new_view
