from __future__ import annotations  # For typing the enclosing class

from .drawable import Drawable
from .interactive import Interactive
from src.utils.fraction import Fraction as Fr

from typing import Tuple, List, Union


class Layer:
    def __init__(self, x_fraction: Fr, y_fraction: Fr, width_fraction: Fr, height_fraction: Fr, parent):

        # TODO Delete saving fractions as attributes if not in used
        self.x_fraction = x_fraction
        self.y_fraction = y_fraction
        self.width_fraction = width_fraction
        self.height_fraction = height_fraction
        self.parent = parent  # TODO Create frame class which have x, y, height, width attributes

        # Absolute parameters
        self.x = int(parent.get_x() + parent.get_width() * x_fraction)
        self.y = int(parent.get_y() + parent.get_height() * y_fraction)
        self.width = int(parent.get_width() * width_fraction)
        self.height = int(parent.get_height() * height_fraction)

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

    def draw_object(self, drawable: Drawable, pygame_screen):
        x, y = self.calculate_object_absolute_position(drawable)
        self.check_position()

        width, height = self.calculate_object_absolute_size(drawable)
        scaled_img = drawable.scale(width, height)

        pygame_screen.blit(scaled_img, (x, y))

    def check_position(self):
        pass  # TODO Return position error when object point is outside the layer

    ##################
    # Finding object #
    ##################
    def find_object_on_layer(self, position) -> Tuple[int, Union[Interactive, None]]:
        """
        :param position: Tuple of x and y of mouse position # TODO Create point class
        :return: Tuple of return code and interactive object
                 Return code could be:
                    0 - Not found
                    1 - Found correct object
                    2 - Block by other object
        """
        for layer in self.get_layers():
            signal, found_object = layer.find_object_on_layer(position)
            if signal != 0:
                return signal, found_object

        for drawable in reversed(self.get_drawable_objects()):
            # TODO Create generic function for check if point is inside the square
            is_inside = self._if_point_is_inside_object(position, drawable)
            if is_inside:
                if isinstance(drawable, Interactive):
                    return 1, drawable
                if drawable.if_blocking():
                    return 2, None
        return 0, None

    def _if_point_is_inside_object(self, position, drawable: Drawable) -> bool:
        """
        :param position: Tuple of x and y of mouse position # TODO Create point class
        :return: True if point is inside given object image, false otherwise
        """
        object_x, object_y = self.calculate_object_absolute_position(drawable)
        if position[0] > object_x and position[1] > object_y:
            width, height = self.calculate_object_absolute_size(drawable)
            if position[0] < object_x + width and position[1] < object_y + height:
                return True
        return False

    #####################
    # Object parameters #
    #####################
    def calculate_object_absolute_position(self, drawable: Drawable) -> Tuple[int, int]:
        absolute_x = self.get_x() + (drawable.get_x_fraction() * self.width)
        absolute_y = self.get_y() + (drawable.get_y_fraction() * self.height)
        return int(absolute_x), int(absolute_y)

    def calculate_object_absolute_size(self, drawable: Drawable) -> Tuple[int, int]:
        absolute_width = drawable.get_width_fraction() * self.width
        absolute_height = drawable.get_height_fraction() * self.height
        return int(absolute_width), int(absolute_height)

    #######################
    # Add object to layer #
    #######################
    def add_drawable_object_to_front(self, drawable: Drawable):
        self.drawable_objects.append(drawable)

    def add_drawable_object_to_bottom(self, drawable: Drawable):
        self.drawable_objects.insert(0, drawable)

    #############
    # Add layer #
    #############
    def create_bottom_layer(self, x_fraction: Fr, y_fraction: Fr, width_fraction: Fr, height_fraction: Fr) -> Layer:
        new_layer = Layer(x_fraction, y_fraction, width_fraction, height_fraction, self)
        self.layers.insert(0, new_layer)
        return new_layer

    def create_top_layer(self, x_fraction: Fr, y_fraction: Fr, width_fraction: Fr, height_fraction: Fr) -> Layer:
        new_layer = Layer(x_fraction, y_fraction, width_fraction, height_fraction, self)
        self.layers.append(new_layer)
        return new_layer

    ###########
    # Getters #
    ###########
    def get_x(self) -> int:
        return self.x

    def get_y(self) -> int:
        return self.y

    def get_width(self) -> int:
        return self.width

    def get_height(self) -> int:
        return self.height

    def get_layers(self) -> List[Layer]:
        return self.layers

    def get_drawable_objects(self) -> List[Drawable]:
        return self.drawable_objects
