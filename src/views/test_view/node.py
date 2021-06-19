from src.screen_engine import Drawable
from src.utils import Fraction as Fr


class Node(Drawable):
    IMG_PATH = 'res/sprites/run_view/base_node.png'

    def __init__(self, x_fraction: Fr, y_fraction: Fr,  width_fraction: Fr, height_fraction: Fr):
        super().__init__(x_fraction, y_fraction, width_fraction, height_fraction, self.IMG_PATH)
