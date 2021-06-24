
from .character import Character


class Snake(Character):
    def __init__(self):
        icon_path = 'res/sprites/characters/snake.png'
        super().__init__(icon_path)

