class Point:
    """
    Point class to storing axis of a position during the game
    """
    x = 0
    y = 0
    def __init__(self, x: int, y: int) -> None:
        """
        initialize function and index of point axis
        @param x: X axis
        @param y: Y axis
        """
        self.x = x
        self.y = y

    def axisToRect(self, rectSize: int) -> tuple:
        """
        axis to rect size tuple

        @param rectSize: rect size for specify rect object
        """
        return (self.x * rectSize, self.y * rectSize, rectSize, rectSize)

    def __add__(self, other):
        """
        add operator overloading

        @param other: another point to add

        @return: new Point object after add other point axis
        """
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """
        minus operator overloading

        @param other: another point to sub

        @return: new Point object after sub other point axis
        """
        return Point(self.x - other.x, self.y - other.y)
    
    def __eq__(self, other):
        """
        equal operator overloading

        @param other: another point

        @return: boolean value that self axis equal other axis
        """
        return bool(self.x == other.x and self.y == other.y)

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def __iter__(self):
        """
        iterator object overloading
        """
        yield Point(self.x , self.y)
