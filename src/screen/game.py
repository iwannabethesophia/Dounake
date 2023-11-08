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
        self.snake1 = Snake([Point(2, 0), Point(1, 0), Point(0, 0)], Point(1, 0)) # snake 1
        self.snake2 = Snake([Point(17, 19), Point(18, 19), Point(19, 19)], Point(-1, 0)) # snake 2
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

                self.handlingDirectionEvent(event) # event for snake 1
                
            # handling fruit eat evenet
            if self.snake1.snakePosition[0] == self.fruit: # snake 1
                self.snake1.snakeLength += 1
                self.snake1.snakePosition.append(Point(-1, -1))
                self.fruit.nextFruitPoisiton()
                while (self.fruit in self.snake1.snakePosition):
                    self.fruit.nextFruitPoisiton()

            self.handlingCollision1(self.snake1)


            if self.snake2.snakePosition[0] == self.fruit: # snake 2
                self.snake2.snakeLength += 1
                self.snake2.snakePosition.append(Point(-1, -1))
                self.fruit.nextFruitPoisiton()
                while (self.fruit in self.snake2.snakePosition):
                    self.fruit.nextFruitPoisiton()

            self.handlingCollision2(self.snake2)

            self.screen.fill((0, 0, 0))
            
            self.drawBareboneSnake1(self.snake1) #draw snake 1
            self.drawBareboneSnake2(self.snake2) #draw snake 2
            
            self.snake1.updateSnakeByDirection()
            self.snake2.updateSnakeByDirection()
            self.clock.tick(144)
            pygame.display.update()

    def handlingCollision1(self, snake1): # collision for snake 1
        """
        handling collistion for snake
        """
        head = self.snake1.snakePosition[0]
        if head in self.snake1.snakePosition[1:] or head in self.snake2.snakePosition[:] or head.x == -1 or head.x == 20 or head.y == -1 or head.y == 20:
            self.gameRunning = False
    
    def handlingCollision2(self, snake2): # collision for snake 2
        """
        handling collistion for snake
        """
        head = self.snake2.snakePosition[0]
        if head in self.snake2.snakePosition[1:] or head in self.snake1.snakePosition[:] or head.x == -1 or head.x == 20 or head.y == -1 or head.y == 20:
            self.gameRunning = False

    def drawBareboneSnake1(self, snake: Snake) -> None:
        """
        draw barebone snake without any sprite and animation into the screen only rect usage

        @param snake: Snake object to draw
        """

        snakePositionVector = self.snake1.snakePosition
        pygame.draw.rect(self.screen, (200, 255, 0), snakePositionVector[0].axisToRect(20))
        for i in range(1, len(snakePositionVector)):
            pygame.draw.rect(self.screen, (0, 255, 0), snakePositionVector[i].axisToRect(20))

        pygame.draw.rect(self.screen, (255, 0, 0), self.fruit.axisToRect(20))

    def drawBareboneSnake2(self, snake: Snake) -> None:
        """
        draw barebone snake without any sprite and animation into the screen only rect usage

        @param snake: Snake object to draw
        """

        snakePositionVector = self.snake2.snakePosition
        pygame.draw.rect(self.screen, (200, 0, 255), snakePositionVector[0].axisToRect(20))
        for i in range(1, len(snakePositionVector)):
            pygame.draw.rect(self.screen, (0, 0, 255), snakePositionVector[i].axisToRect(20))

        pygame.draw.rect(self.screen, (255, 0, 0), self.fruit.axisToRect(20))

    def handlingDirectionEvent(self, event: pygame.event.Event) -> None:
        """
        handling event when WASD pressed(for snake 1)

        @param event: Event for handling
        """
        directionEvent = {
            pygame.K_w: Point(0, -1),
            pygame.K_s: Point(0, 1),
            pygame.K_a: Point(-1, 0),
            pygame.K_d: Point(1, 0)
        }

        # direction event for snake 2
        directionEvent2 = {
            pygame.K_UP: Point(0, -1),
            pygame.K_DOWN: Point(0, 1),
            pygame.K_LEFT: Point(-1, 0),
            pygame.K_RIGHT: Point(1, 0)
        }
        # if event key is direction key pressed on the keyboard
        if event.type == pygame.KEYDOWN:
            if event.key in directionEvent:
                curDirection, newDirection = self.snake1.snakeDirection, directionEvent[event.key]
                if abs(curDirection.x) != abs(newDirection.x) or abs(curDirection.y) != abs(newDirection.y):
                    self.snake1.snakeDirection = newDirection
            if event.key in directionEvent2:
                curDirection, newDirection = self.snake2.snakeDirection, directionEvent2[event.key]
                if abs(curDirection.x) != abs(newDirection.x) or abs(curDirection.y) != abs(newDirection.y):
                    self.snake2.snakeDirection = newDirection
