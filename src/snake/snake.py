from .point import Point

class Snake1:
    """
    Snake object for snake display, process in game
    """
    def __init__(self) -> None:
        """
        initialize function for snake object
        """

        self.snakeLength = 3 #default snake length

        # x, y
        # 0, 1 -> down
        # 0,-1 -> up
        # 1, 0 -> right
        #-1, 0 -> left
        # current snake direction
        self.snakeDirection = Point(1, 0)

        # a vector storing list of postition
        # for a map with 20x20 head at position (x, y) = (0, 2)
        self.snakePosition = [Point(2, 0), Point(1, 0), Point(0, 0)]

    def updateSnakeByDirection(self) -> None:
        """
        update snake by current snake direction
        """
        snakeHead = self.snakePosition[0]
        self.snakePosition.pop(-1)
        self.snakePosition.insert(0, snakeHead + self.snakeDirection)

# Snake 2nd:
class Snake2:
    """
    Snake object for snake display, process in game
    """
    def __init__(self) -> None:
        """
        initialize function for snake object
        """

        self.snakeLength = 3 #default snake length

        # x, y
        # 0, 1 -> down
        # 0,-1 -> up
        # 1, 0 -> right
        #-1, 0 -> left
        # current snake direction
        self.snakeDirection = Point(-1, 0)

        # a vector storing list of postition
        # for a map with 20x20 head at position (x, y) = (0, 2)
        self.snakePosition = [Point(17, 19), Point(18, 19), Point(19, 19)]

    def updateSnakeByDirection(self) -> None:
        """
        update snake by current snake direction
        """
        snakeHead = self.snakePosition[0]
        self.snakePosition.pop(-1)
        self.snakePosition.insert(0, snakeHead + self.snakeDirection)

    
