from .point import Point

class Snake:
    """
    Snake object for snake display, process in game
    """
    def __init__(self, startPos: list[Point], direction: Point) -> None:
        """
        initialize function for snake object

        @param startPos: list of start position of snake
        @param direction: default direction of snake moving
        """

        self.snakeLength = 3 #default snake length
        assert self.snakeLength == len(startPos)
        # x, y
        # 0, 1 -> down
        # 0,-1 -> up
        # 1, 0 -> right
        #-1, 0 -> left
        # current snake direction
        self.snakeDirection = direction

        # a vector storing list of postition
        # for a map with 20x20 head at position (x, y) = (0, 2)
        self.snakePosition = startPos

    def updateSnakeByDirection(self) -> None:
        """
        update snake by current snake direction
        """
        snakeHead = self.snakePosition[0]
        self.snakePosition.pop(-1)
        self.snakePosition.insert(0, snakeHead + self.snakeDirection)
