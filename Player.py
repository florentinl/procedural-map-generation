class Player:
    def __init__(self, speed: float, x: float = 0., y: float = 0.):
        self.x = x
        self.x_speed: float = 0.

        self.y = y
        self.y_speed: float = 0.

        self.max_speed = speed

    def set_speed(self, direction: str):
        if direction == 'up':
            self.y_speed = +self.max_speed
        elif direction == 'down':
            self.y_speed = -self.max_speed
        elif direction == 'left':
            self.x_speed = -self.max_speed
        elif direction == 'right':
            self.x_speed = +self.max_speed

    def reset_speed(self, direction: str):
        if direction in ['up', 'down']:
            self.y_speed = 0
        elif direction in ['left', 'right']:
            self.x_speed = 0

    def update_position(self, dT: float):
        self.x += self.x_speed * dT
        self.y += self.y_speed * dT
