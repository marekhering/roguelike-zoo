from src.screen_engine import Interactive
from src.utils import Fraction as Fr


class Field(Interactive):
    IMG_PATH = 'res/sprites/run_view/node.png'

    def __init__(self, x_fraction: Fr, y_fraction: Fr,  width_fraction: Fr, height_fraction: Fr,
                 field_x: int, field_y: int):

        super().__init__(x_fraction, y_fraction, width_fraction, height_fraction, self.IMG_PATH)
        self.field_x = field_x
        self.field_y = field_y

    def on_click(self) -> None:
        print(self.field_x, self.field_y)

    def get_field_x(self) -> int:
        return self.field_x

    def get_field_y(self) -> int:
        return self.field_y