from .point import Point

import random

class Obstacle(Point):
    def __init__(self, x = None, y = None):
        super().__init__(random.randint(1, 30), random.randint(2, 30))

    def nextPosition(self):
        self.x = random.randint(1, 30)
        self.y = random.randint(2, 30)
