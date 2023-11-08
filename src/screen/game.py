import pygame
import sys

from snake import *

class GameScreen:
    """
    Game screen class to handling screen during game operation
    """
    scr_height = 400 # game screen height size
    scr_weight = 400 # game screen width size
    
    FPS = 60
    
    VELOCITY = 100
    
    # Color
    BLACK = (0,0,0)
    HEAD_SNAKE1_COLOR = (120, 0, 0)
    BODY_SNAKE1_COLOR = (193, 18, 31)
    FRUIT_COLOR = (253, 240, 213)
    HEAD_SNAKE2_COLOR = (26, 83, 92)
    BODY_SNAKE2_COLOR = (102, 155, 188)
    
    
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
        self.snake1 = Snake([Point(2, 0), Point(1, 0), Point(0, 0)], Point(1, 0)) # snake1 wasd
        self.snake2 = Snake([Point(17, 19), Point(18, 19), Point(19, 19)], Point(-1, 0)) # snake2 
        self.clock = pygame.time.Clock()
        self.fruit = Fruit()

        # handler variable for game window running
        self.gameRunning = True

        while self.gameRunning:
            pygame.time.delay(self.VELOCITY) # Speed of snakes

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)

                self.handlingDirectionEvent(event) # event for snake 1
                
            # handling fruit eat event
            if self.snake1.snakePosition[0] == self.fruit: # snake 1
                self.snake1.snakeLength += 1
                self.snake1.snakePosition.append(Point(-1, -1))
                self.fruit.nextFruitPosition()
                while (self.fruit in self.snake1.snakePosition):
                    self.fruit.nextFruitPosition()

            self.handlingCollision1(self.snake1)


            if self.snake2.snakePosition[0] == self.fruit: # snake 2
                self.snake2.snakeLength += 1
                self.snake2.snakePosition.append(Point(-1, -1))
                self.fruit.nextFruitPosition()
                while (self.fruit in self.snake2.snakePosition):
                    self.fruit.nextFruitPosition()

            self.handlingCollision2(self.snake2)

            self.screen.fill(self.BLACK) # Background
            
            self.drawBareboneSnake1(self.snake1) #draw snake 1
            self.drawBareboneSnake2(self.snake2) #draw snake 2
            
            self.snake1.updateSnakeByDirection()
            self.snake2.updateSnakeByDirection()
            self.clock.tick(self.FPS)  # FPS
            pygame.display.update()

    def handlingCollision1(self, snake1): # collision for snake 1
        """
        handling collision for snake
        """
        head = self.snake1.snakePosition[0]
        if head in self.snake1.snakePosition[1:] or head in self.snake2.snakePosition[:] or head.x == -1 or head.x == 20 or head.y == -1 or head.y == 20:
            self.gameRunning = False
    
    def handlingCollision2(self, snake2): # collision for snake 2
        """
        handling collision for snake
        """
        head = self.snake2.snakePosition[0]
        if head in self.snake2.snakePosition[1:] or head in self.snake1.snakePosition[:] or head.x == -1 or head.x == 20 or head.y == -1 or head.y == 20:
            self.gameRunning = False

    def drawBareboneSnake1(self, snake: Snake) -> None:
        """
        draw barebone snake without any sprite and animation into the screen only rect usage

        @param snake: Snake object to draw
        """

        # Draw Snake 1
        snakePositionVector = self.snake1.snakePosition
        pygame.draw.rect(self.screen, self.HEAD_SNAKE1_COLOR, snakePositionVector[0].axisToRect(20))
        
        for i in range(1, len(snakePositionVector)):
            pygame.draw.rect(self.screen, self.BODY_SNAKE1_COLOR, snakePositionVector[i].axisToRect(20))

        pygame.draw.rect(self.screen, self.FRUIT_COLOR, self.fruit.axisToRect(20))

    def drawBareboneSnake2(self, snake: Snake) -> None:
        """
        draw barebone snake without any sprite and animation into the screen only rect usage

        @param snake: Snake object to draw
        """

        # Draw Snake 2
        snakePositionVector = self.snake2.snakePosition
        pygame.draw.rect(self.screen, self.HEAD_SNAKE2_COLOR, snakePositionVector[0].axisToRect(20))
        
        for i in range(1, len(snakePositionVector)):
            pygame.draw.rect(self.screen, self.BODY_SNAKE2_COLOR, snakePositionVector[i].axisToRect(20))

        pygame.draw.rect(self.screen, self.FRUIT_COLOR, self.fruit.axisToRect(20))

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
