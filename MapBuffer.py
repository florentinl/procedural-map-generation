from PixelMap import PixelMap
import pygame


class MapBuffer:
    def __init__(self, map: PixelMap, x: float, y: float):
        self.pixel_map = map

        self.view_x = x
        self.view_y = y

        self.pixel_map.generate_view(round(self.view_x), 
                                     round(self.view_y))

    def get_surface(self, x: float, y: float) -> pygame.Surface:
        view = self.pixel_map.get_view(round(self.view_x),
                                       round(self.view_y),
                                       round(x),
                                       round(y))
        self.view_x = x
        self.view_y = y
        return pygame.surfarray.make_surface(view)
