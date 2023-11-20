from .point import Point

import random

class Fruit(Point):
    # Variable for handling the golden apple
    is_golden = False

    def __init__(self, x = None, y = None):
        super().__init__(random.randint(1, 30), random.randint(2, 30))
        self.is_golden = False

    def nextFruitPosition(self):
        self.x = random.randint(1, 30)
        self.y = random.randint(2, 30)
