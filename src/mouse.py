

class Mouse:
    def __init__(self, button_down, button_up, position, button_pressed):
        self.button_down = button_down
        self.button_up = button_up
        self.position_x = position[0]
        self.position_y = position[1]
        self.left_button = button_pressed[0]
        self.middle_button = button_pressed[1]
        self.right_button = button_pressed[2]

    def get_left_button_up(self):
        return self.left_button and self.button_up

    def correct_event(self, button_pressed):
        self.left_button = self.left_button or button_pressed[0]
        self.middle_button = self.middle_button or button_pressed[1]
        self.right_button = self.right_button or button_pressed[2]

    def get_position(self):
        return self.position_x, self.position_y
