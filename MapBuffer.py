from PixelMap import PixelMap
import numpy


class MapBuffer:
    def __init__(self, map: PixelMap, x: float, y: float):
        self.pixel_map = map

        self.view_x = x
        self.view_y = y

        self.pixel_map.generate_view(round(self.view_x), 
                                     round(self.view_y))

    def get_view(self, x: float, y: float) -> numpy.ndarray:
        view = self.pixel_map.get_view(round(self.view_x),
                                       round(self.view_y),
                                       round(x),
                                       round(y))
        self.view_x = x
        self.view_y = y
        return view
