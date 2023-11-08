from .point import Point

import random

class Fruit(Point):
    def __init__(self, x = None, y = None):
        super().__init__(random.randint(0, 19), random.randint(0, 19))

    def nextFruitPosition(self):
        self.x = random.randint(0, 19)
        self.y = random.randint(0, 19)
