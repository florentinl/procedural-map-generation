import numpy as np
import noise


class PixelMap:
    def __init__(self, map_size: int, view_radius: int, seed: int = np.random.randint(100)):

        self.view_radius = view_radius
        self.seed = seed

        self.world = np.zeros((map_size, map_size), dtype=np.uint8)
        self.x_center = map_size // 2
        self.y_center = map_size // 2

    def noise(self, i: int, j: int) -> float:
        scale = 1000.0
        octaves = 6
        persistence = 0.5
        lacunarity = 2.0
        return 255 * noise.pnoise2(i/scale,
                                   j/scale,
                                   octaves=octaves,
                                   persistence=persistence,
                                   lacunarity=lacunarity,
                                   repeatx=1024,
                                   repeaty=1024,
                                   base=self.seed)

    def generate_view(self, x: int, y: int):
        for i in range(x - self.view_radius, x + self.view_radius + 1):
            for j in range(y - self.view_radius, y + self.view_radius + 1):
                if self.world[i + self.x_center, j + self.y_center] == 0.:
                    self.world[i + self.x_center, j +
                               self.y_center] = self.noise(i, j)

    def __extract_view(self, x: int, y: int) -> np.ndarray:
        return self.world[x + self.x_center - self.view_radius:
                          x + self.x_center + self.view_radius + 1,
                          y + self.y_center - self.view_radius:
                          y + self.y_center + self.view_radius + 1]

    def get_view(self, old_x: int, old_y: int, x: int, y: int) -> np.ndarray:
        if x == old_x:
            if y == old_y:
                return self.__extract_view(x, y)
            elif y > old_y:
                for i in range(x - self.view_radius, x + self.view_radius + 1):
                    for j in range(self.view_radius + 1 + old_y, y + self.view_radius + 1):
                        if self.world[i + self.x_center, j + self.y_center] == 0.:
                            self.world[i + self.x_center,
                                       j + self.y_center] = self.noise(i, j)

            else:
                for i in range(x - self.view_radius, x + self.view_radius + 1):
                    for j in range(y - self.view_radius, old_y - self.view_radius + 1):
                        if self.world[i + self.x_center, j + self.y_center] == 0.:
                            self.world[i + self.x_center, j +
                                       self.y_center] = self.noise(i, j)

        elif y == old_y:
            if x > old_x:
                for i in range(old_x + self.view_radius + 1, x + self.view_radius + 1):
                    for j in range(y - self.view_radius, y + self.view_radius + 1):
                        if self.world[i + self.x_center, j + self.y_center] == 0.:
                            self.world[i + self.x_center,
                                       j + self.y_center] = self.noise(i, j)

            elif x < old_x:
                for i in range(x - self.view_radius, old_x - self.view_radius + 1):
                    for j in range(y - self.view_radius, y + self.view_radius + 1):
                        if self.world[i + self.x_center, j + self.y_center] == 0.:
                            self.world[i + self.x_center,
                                       j + self.y_center] = self.noise(i, j)

        else:
            self.view = self.generate_view(x, y)
        old_x = x
        old_y = y
        return self.__extract_view(x, y)
