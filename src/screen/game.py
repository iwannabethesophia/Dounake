import pygame
import sys
import os

from snake import *


class GameScreen:
    """
    Game screen class to handling screen during game operation
    """
    scr_height = 500 # Game screen height size
    scr_weight = 500 # Game screen width size
    
    FPS = 10 # Speed of Snake
    
    # Color
    BLACK = (0,0,0)
    WHITE = (255, 255, 255)
    HEAD_SNAKE1_COLOR = (120, 0, 0)
    BODY_SNAKE1_COLOR = (193, 18, 31)
    FRUIT_COLOR = (253, 240, 213)
    HEAD_SNAKE2_COLOR = (26, 83, 92)
    BODY_SNAKE2_COLOR = (102, 155, 188)
    
    #collision status
    COLLISION_STAT = -1 #0 = Tie, 1 = P1 win, 2 = P2 win
    #game status
    STAT_SIZE = 20
    STAT_COLOR = (255, 255, 255)
    STAT_BORDER_COLOR = (255, 0, 0)
    STAT_POS = (145, 190)
    STAT_GAME = False #True: Game Over


    def __init__(self, gameTitle: str):
        """
        Initialize game screen

        @param game_title: Window display title
        """
        pygame.init() # Initialize pygame

        self.screen = pygame.display.set_mode((self.scr_height, self.scr_weight)) # Set mode for game window
        pygame.display.set_caption(gameTitle) # Set caption and title for game's window

    def gameLoop(self) -> None:
        """
        Perform game loop operation for handling event during window game running
        """

        # Create snake on the screen
        self.snake1 = Snake([Point(2, 0), Point(1, 0), Point(0, 0)], Point(1, 0)) 
        self.snake2 = Snake([Point(17, 19), Point(18, 19), Point(19, 19)], Point(-1, 0)) 
        self.fps = pygame.time.Clock()
        self.fruit = Fruit()

        # Handler variable for game window running
        self.gameRunning = True

        while self.gameRunning:
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)

                self.handlingDirectionEvent(event) # Event for snake 1
            
            # handling fruit eat event
            if self.snake1.snakePosition[0] == self.fruit: # Snake 1
                self.snake1.snakeLength += 1
                self.snake1.snakePoint +=1
                self.snake1.snakePosition.append(Point(-1, -1))
                self.fruit.nextFruitPosition()
                while (self.fruit in self.snake1.snakePosition):
                    self.fruit.nextFruitPosition()

            self.handlingCollision1(self.snake1)


            if self.snake2.snakePosition[0] == self.fruit: # Snake 2
                self.snake2.snakeLength += 1
                self.snake2.snakePoint += 1
                self.snake2.snakePosition.append(Point(-1, -1))
                self.fruit.nextFruitPosition()
                while (self.fruit in self.snake2.snakePosition):
                    if not self.STAT_GAME:
                        self.fruit.nextFruitPosition()

            self.handlingCollision2(self.snake2)

            self.screen.fill(self.BLACK) # Background


            #draw score
            score_font = pygame.font.Font(os.path.join('src','assets', 'font.ttf'), 15)
            score_text = score_font.render('Score:', False, self.WHITE)
            p1_score = score_font.render(str(self.snake1.snakePoint), False, self.WHITE)
            p2_score = score_font.render(str(self.snake2.snakePoint), False, self.WHITE)
            #draw if not game over
            if not self.STAT_GAME:
                #draw player 1 score
                self.screen.blit(score_text, (15, 10))
                self.screen.blit(p1_score, (105, 10))
                #draw player 2 score
                self.screen.blit(score_text, (385, 10))
                self.screen.blit(p2_score, (475, 10))
                #else draw if game over
                #draw both players's score
            
            #game over
            if self.COLLISION_STAT != -1:
                get_font = pygame.font.Font(os.path.join('src','assets', 'font.ttf'), self.STAT_SIZE)
                if self.COLLISION_STAT == 0:
                    text = get_font.render('TIE', True, self.STAT_COLOR, self.STAT_BORDER_COLOR)
                elif self.COLLISION_STAT == 1:
                    text = get_font.render('P1 Win', True, self.STAT_COLOR, self.STAT_BORDER_COLOR)
                elif self.COLLISION_STAT == 2:
                    text = get_font.render('P2 Win', True, self.STAT_COLOR, self.STAT_BORDER_COLOR)
                self.screen.blit(text, self.STAT_POS)
                events = pygame.event.get()
                for event in events:
                    if event.type == pygame.K_SPACE:
                        #return to titlescreen, but will be done later
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN and event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit() 
            if (self.STAT_GAME == False):
                self.drawBareboneSnake1(self.snake1) # Draw snake 1
                self.drawBareboneSnake2(self.snake2) # Draw snake 2

                self.snake1.updateSnakeByDirection()
                self.snake2.updateSnakeByDirection()


            pygame.display.update() 
            self.fps.tick(self.FPS)  # Speed of Snake

    def handlingCollision1(self, snake1): # Collision for snake 1
        """
        handling collision for snake
        """
        head = self.snake1.snakePosition[0]
        if head in self.snake1.snakePosition[1:] or head in self.snake2.snakePosition[:] or head.x == -1 or head.x == 20 or head.y == -1 or head.y == 20:
            if head == self.snake2.snakePosition[0]:
                self.COLLISION_STAT = 0
            else:
                self.COLLISION_STAT = 2
            self.STAT_GAME = True
            return
    
    def handlingCollision2(self, snake2): # Collision for snake 2
        """
        handling collision for snake
        """
        head = self.snake2.snakePosition[0]
        if head in self.snake2.snakePosition[1:] or head in self.snake1.snakePosition[:] or head.x == -1 or head.x == 20 or head.y == -1 or head.y == 20:
            if head == self.snake1.snakePosition[0]:
                self.COLLISION_STAT = 0
            else:
                self.COLLISION_STAT = 1
            self.STAT_GAME = True
            return

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

        # Direction event for snake 2
        directionEvent2 = {
            pygame.K_UP: Point(0, -1),
            pygame.K_DOWN: Point(0, 1),
            pygame.K_LEFT: Point(-1, 0),
            pygame.K_RIGHT: Point(1, 0)
        }
        # If event key is direction key pressed on the keyboard
        if event.type == pygame.KEYDOWN:
            if event.key in directionEvent:
                curDirection, newDirection = self.snake1.snakeDirection, directionEvent[event.key]
                if abs(curDirection.x) != abs(newDirection.x) or abs(curDirection.y) != abs(newDirection.y):
                    self.snake1.snakeDirection = newDirection
            if event.key in directionEvent2:
                curDirection, newDirection = self.snake2.snakeDirection, directionEvent2[event.key]
                if abs(curDirection.x) != abs(newDirection.x) or abs(curDirection.y) != abs(newDirection.y):
                    self.snake2.snakeDirection = newDirection