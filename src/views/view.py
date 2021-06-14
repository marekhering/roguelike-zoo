
class View:
    def __init__(self):
        pass

    def key_handler(self, keys):
        return NotImplementedError

    def draw_on_screen(self, screen):
        return NotImplementedError
