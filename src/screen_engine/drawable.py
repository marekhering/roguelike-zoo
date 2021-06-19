import pygame

from src.utils.fraction import Fraction as Fr


class Drawable:
    def __init__(self, x_fraction: Fr, y_fraction: Fr, width_fraction: Fr, height_fraction: Fr, img_path):
        """
        :param x_fraction: per mille of the width of the layer on which the object will be located (0, 1000)
        :param y_fraction: per mille of the width of the layer on which the object will be located (0, 1000)
        :param img_path: path to image file
        """
        self.x_fraction = x_fraction.copy()
        self.y_fraction = y_fraction.copy()
        self.width_fraction = width_fraction.copy()
        self.height_fraction = height_fraction.copy()

        self.img_path = img_path
        self.img = pygame.image.load(img_path)
        self._last_scaled_img = self.img

    def scale(self, new_width: int, new_height: int):
        last_scaled_width = self._last_scaled_img.get_width()
        last_scaled_height = self._last_scaled_img.get_height()
        if last_scaled_width != new_width or last_scaled_height != new_height:
            self._last_scaled_img = pygame.transform.scale(self.img, (new_width, new_height))
        return self._last_scaled_img

    def get_img(self):
        return self.img

    def get_x_fraction(self):
        return self.x_fraction

    def get_y_fraction(self):
        return self.y_fraction

    def get_width_fraction(self):
        return self.width_fraction

    def get_height_fraction(self):
        return self.height_fraction
