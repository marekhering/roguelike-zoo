from .drawable import Drawable
from src.utils import Fraction as Fr


class Interactive(Drawable):
    def __init__(self, x_fraction: Fr, y_fraction: Fr, width_fraction: Fr, height_fraction: Fr, img_path):
        super().__init__(x_fraction, y_fraction, width_fraction, height_fraction, img_path)

    def on_click(self):
        raise NotImplementedError
