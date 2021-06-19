import pygame

from src.utils.fraction import Fraction as Fr


class Drawable:
    def __init__(self, x_fraction, y_fraction: Fr, img_path):
        """
        :param x_fraction: per mille of the width of the layer on which the object will be located (0, 1000)
        :param y_fraction: per mille of the width of the layer on which the object will be located (0, 1000)
        :param img_path: path to image file
        """
        self.x_fraction = x_fraction
        self.y_fraction = y_fraction
        self.img_path = img_path
        self.img = pygame.image.load(img_path)

    def scale(self, width_fraction: Fr, height_fraction: Fr, layer):
        width = int(layer.get_width() * width_fraction)
        height = int(layer.get_height() * height_fraction)
        self.img = pygame.transform.scale(self.img, (width, height))

    def get_img(self):
        return self.img

    def get_x_fraction(self):
        return self.x_fraction

    def get_y_fraction(self):
        return self.y_fraction

