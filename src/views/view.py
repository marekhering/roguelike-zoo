from src.screen_engine import Screen
from src import Mouse


class View:
    def __init__(self, screen: Screen):
        self.screen = screen

    def key_handler(self, keys, mouse: Mouse):
        return NotImplementedError
