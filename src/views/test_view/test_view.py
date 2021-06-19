from src.views.view import View
from src.screen_engine import Screen, Layer
from src.utils.fraction import Fraction as Fr
from .my_object import MyObject
from .node import Node
from src import Mouse

import pygame


class TestView(View):
    def __init__(self, screen: Screen):
        super().__init__(screen)
        screen.set_background_color((255, 255, 255))

        # Objects
        my_object_pos = (Fr(100), Fr(200))
        my_object_scale = (Fr(100), Fr(150))

        self.my_object = MyObject(my_object_pos[0], my_object_pos[1], my_object_scale[0], my_object_scale[1])
        self.my2nd_object = MyObject(my_object_pos[0], my_object_pos[1], my_object_scale[0], my_object_scale[1])
        self.nodes = [Node(Fr(x * 100), Fr(500), Fr(100), Fr(100)) for x in range(1, 8)]

        # Layers
        main_layer = screen.get_main_layer()
        bottom_layer = main_layer.create_bottom_layer(Fr(500), Fr(200), Fr(400), Fr(200))

        # Insert
        main_layer.add_drawable_object_to_front(self.my_object)
        bottom_layer.add_drawable_object_to_front(self.my2nd_object)

        for node in self.nodes:
            bottom_layer.add_drawable_object_to_bottom(node)

    def key_handler(self, keys, mouse: Mouse):
        if keys[pygame.K_UP]:
            self.my_object.move_up()
        if keys[pygame.K_DOWN]:
            self.my_object.move_down()
        if keys[pygame.K_LEFT]:
            self.my_object.move_left()
        if keys[pygame.K_RIGHT]:
            self.my_object.move_right()

        if keys[pygame.K_w]:
            self.my2nd_object.move_up()
        if keys[pygame.K_s]:
            self.my2nd_object.move_down()
        if keys[pygame.K_a]:
            self.my2nd_object.move_left()
        if keys[pygame.K_d]:
            self.my2nd_object.move_right()

        if mouse.get_left_button_up():
            clicked_object = self.screen.find_object(mouse.get_position())


