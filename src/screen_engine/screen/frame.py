from src.utils import Point


class Frame:
    def __init__(self, corner_point: Point, width: int, height: int):
        if corner_point.get_value_type() != int:
            raise ValueError

        self.corner_point = corner_point
        self.width = width
        self.height = height

    def get_corner_point(self) -> Point:
        return self.corner_point

    def get_x(self) -> int:
        return self.corner_point.get_x()

    def get_y(self) -> int:
        return self.corner_point.get_y()

    def get_width(self) -> int:
        return self.width

    def get_height(self) -> int:
        return self.height
