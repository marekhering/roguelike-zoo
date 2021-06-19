from .drawable import Drawable
from src.utils.fraction import Fraction as Fr


class Layer:
    def __init__(self, x_fraction: Fr, y_fraction: Fr, width_fraction: Fr, height_fraction: Fr, parent):

        # TODO Delete fractions if not in used
        self.x_fraction = x_fraction
        self.y_fraction = y_fraction
        self.width_fraction = width_fraction
        self.height_fraction = height_fraction
        self.parent = parent

        # Absolute parameters
        self.x = parent.get_x() + parent.get_width() * x_fraction
        self.y = parent.get_y() + parent.get_height() * y_fraction
        self.width = parent.get_width() * width_fraction
        self.height = parent.get_height() * height_fraction

        self.layers = []
        self.drawable_objects = []

    #####################
    # Drawing functions #
    #####################
    def draw_layer(self, pygame_screen):
        for drawable_object in self.drawable_objects:
            self.draw_object(drawable_object, pygame_screen)

        for layer in self.layers:
            layer.draw_layer(pygame_screen)

    def draw_object(self, drawable_object, pygame_screen):
        img = drawable_object.get_img()
        x, y = self.calculate_object_absolute_position(drawable_object)
        pygame_screen.blit(img, (x, y))

    def calculate_object_absolute_position(self, drawable_object: Drawable):
        absolute_x = self.get_x() + (drawable_object.get_x_fraction() * self.width)
        absolute_y = self.get_y() + (drawable_object.get_y_fraction() * self.height)
        return absolute_x, absolute_y

    ##################
    # Finding object #
    ##################
    def find_object_on_layer(self, position):
        pass

    #######################
    # Add object to layer #
    #######################
    def add_drawable_object_to_front(self, drawable_object: Drawable, scale=None):
        if scale is not None and isinstance(scale, tuple):
            drawable_object.scale(scale[0], scale[1], self)
        self.check_position()
        self.drawable_objects.append(drawable_object)

    def add_drawable_object_to_bottom(self, drawable_object: Drawable):
        self.drawable_objects.insert(0, drawable_object)

    def check_position(self):
        pass  # TODO Return position error when object point is outside the layer

    #############
    # Add layer #
    #############
    def create_bottom_layer(self, x_fraction: Fr, y_fraction: Fr, width_fraction: Fr, height_fraction: Fr):
        new_layer = Layer(x_fraction, y_fraction, width_fraction, height_fraction, self)
        self.layers.insert(0, new_layer)
        return new_layer

    def create_top_layer(self, x_fraction: Fr, y_fraction: Fr, width_fraction: Fr, height_fraction: Fr):
        new_layer = Layer(x_fraction, y_fraction, width_fraction, height_fraction, self)
        self.layers.append(new_layer)
        return new_layer

    ###########
    # Getters #
    ###########
    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height
