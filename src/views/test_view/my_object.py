from src.screen_engine import Interactive
from src.utils.fraction import Fraction as Fr


class MyObject(Interactive):
    IMG_PATH = 'res/sprites/characters/snake.png'

    def __init__(self, x_fraction: Fr, y_fraction: Fr, width_fraction: Fr, height_fraction: Fr):
        super().__init__(x_fraction, y_fraction, width_fraction, height_fraction, self.IMG_PATH)

    def move_up(self):
        self.y_fraction.add(-5)

    def move_down(self):
        self.y_fraction.add(5)

    def move_left(self):
        self.x_fraction.add(-5)

    def move_right(self):
        self.x_fraction.add(5)

    def on_click(self):
        print("Psss")