import pygame
import sys

from snake import *

class GameScreen:
    """
    Game screen class to handling screen during game operation
    """
    scr_height = 400 # game screen height size
    scr_weight = 400 # game screen width size
    def __init__(self, gameTitle: str):
        """
        Initialize game screen

        @param game_title: Window display title
        """
        pygame.init() # initialize pygame

        self.screen = pygame.display.set_mode((self.scr_height, self.scr_weight)) # set mode for game window
        pygame.display.set_caption(gameTitle) # set caption and title for game's window

    def gameLoop(self) -> None:
        """
        Perform game loop operation for handling event during window game running
        """

        # create snake on the screen
        self.snake = Snake1()
        self.clock = pygame.time.Clock()
        self.fruit = Fruit()

        # handler variable for game window running
        self.gameRunning = True

        while self.gameRunning:
            pygame.time.delay(100)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)

                self.handlingDirectionEvent(event)

            # handling fruit eat evenet
            if self.snake.snakePosition[0] == self.fruit:
                self.snake.snakeLength += 1
                self.snake.snakePosition.append(Point(-1, -1))
                self.fruit.nextFruitPoisiton()
                while (self.fruit in self.snake.snakePosition):
                    self.fruit.nextFruitPoisiton()

            self.handlingCollision(self.snake)

            self.screen.fill((0, 0, 0))
            self.drawBareboneSnake(self.snake)
            self.snake.updateSnakeByDirection()
            self.clock.tick(144)
            pygame.display.update()

    def handlingCollision(self, snake1):
        """
        handling collistion for snake
        """
        head = self.snake.snakePosition[0]
        if head in self.snake.snakePosition[1:] or head.x == -1 or head.x == 20 or head.y == -1 or head.y == 20:
            self.gameRunning = False

    def drawBareboneSnake(self, snake: Snake1) -> None:
        """
        draw barebone snake without any sprite and animation into the screen only rect usage

        @param snake: Snake object to draw
        """

        snakePositionVector = self.snake.snakePosition
        pygame.draw.rect(self.screen, (200, 255, 0), snakePositionVector[0].axisToRect(20))
        for i in range(1, len(snakePositionVector)):
            pygame.draw.rect(self.screen, (0, 255, 0), snakePositionVector[i].axisToRect(20))

        pygame.draw.rect(self.screen, (255, 0, 0), self.fruit.axisToRect(20))

    def handlingDirectionEvent(self, event: pygame.event.Event) -> None:
        """
        handling event when direction key or WASD pressed

        @param event: Event for handling
        """
        directionEvent = {
            pygame.K_w: Point(0, -1),
            pygame.K_s: Point(0, 1),
            pygame.K_a: Point(-1, 0),
            pygame.K_d: Point(1, 0)
        }
        # if event key is direction key pressed on the keyboard
        if event.type == pygame.KEYDOWN:
            if event.key in directionEvent:
                curDirection, newDirection = self.snake.snakeDirection, directionEvent[event.key]
                if abs(curDirection.x) != abs(newDirection.x) or abs(curDirection.y) != abs(newDirection.y):
                    self.snake.snakeDirection = newDirection
