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

        self.snakeLength = 3 # Default snake length
        self.snakePoint = 0
        assert self.snakeLength == len(startPos)
        # x, y
        # 0, 1 -> down
        # 0,-1 -> up
        # 1, 0 -> right
        #-1, 0 -> left
        # Current snake direction
        self.snakeDirection = direction

        # A vector storing list of position
        self.snakePosition = startPos

    def updateSnakeByDirection(self) -> None:
        """
        update snake by current snake direction
        """
        snakeHead = self.snakePosition[0]
        self.snakePosition.pop(-1)
        self.snakePosition.insert(0, snakeHead + self.snakeDirection)
