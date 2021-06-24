from typing import Tuple

from .utils import Point


class Mouse:
    def __init__(self, button_down: bool, button_up: bool, position: Point, button_pressed: Tuple[bool, bool, bool]):
        """
        :param button_down: True, if any of the buttons on the mouse was clicked, False otherwise.
        :param button_up: True, if any of the buttons on the mouse was un-clicked, False otherwise.
        :param position: position of the mouse cursor as Point class.
        :param button_pressed: list of boolean.
            button_pressed[0]: True, if left button was clicked, False otherwise
            button_pressed[1]: True, if middle button was clicked, False otherwise
            button_pressed[2]: True, if right button was clicked, False otherwise
        """
        self.button_down = button_down
        self.button_up = button_up
        self.position = position
        self.left_button = button_pressed[0]
        self.middle_button = button_pressed[1]
        self.right_button = button_pressed[2]

    def correct_event(self, button_pressed: Tuple[bool, bool, bool]):
        """
        Function correct button_pressed list to match the button_down and button_up flags
        :param button_pressed: list of boolean.
            button_pressed[0]: True, if left button was clicked, False otherwise
            button_pressed[1]: True, if middle button was clicked, False otherwise
            button_pressed[2]: True, if right button was clicked, False otherwise
        """
        self.left_button = self.left_button or button_pressed[0]
        self.middle_button = self.middle_button or button_pressed[1]
        self.right_button = self.right_button or button_pressed[2]

    def if_left_button_up(self) -> bool:
        return self.left_button and self.button_up

    def get_position(self) -> Point:
        return self.position
