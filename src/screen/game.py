import pygame
import sys
import os
import dn_lib as switches

from snake import *

class GameScreen:
    """
    Game screen class to handling screen during game operation
    """
    SCREEN_HEIGHT = 650 # Game screen height size 31x31
    SCREEN_WIDTH = 650 # Game screen width size 31x31
    
    FPS = 14 # Speed of Snake
    
    # Color
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    GREEN = (0,255,0)
    YELLOW = (255,255,0)
    RED = (255,0,0)
    CYAN = (2,243,229)
    FONT_COLOR = (239,84,85)
    HEAD_SNAKE1_COLOR = (120,0,0)
    BODY_SNAKE1_COLOR = (193,18,31)
    FRUIT_COLOR = (0,255,0)
    GOLDEN_FRUIT_COLOR = (255,215,0)
    HEAD_SNAKE2_COLOR = (26,83,92)
    BODY_SNAKE2_COLOR = (102,155,188)
    
    # Collision status
    COLLISION_STAT = -1 # 0 = Tie, 1 = P1 win, 2 = P2 win
    
    # Game status
    STAT_SIZE = 30
    STAT_COLOR = (255, 255, 255)
    STAT_BORDER_COLOR = (255, 0, 0)
    STAT_POS = (235, 295)
    STAT_GAME = False # True: Game Over

    def __init__(self, gameTitle: str):
        """
        Initialize game screen

        @param game_title: Window display title
        """
        pygame.init() # Initialize pygame
        
        #SFX when End game
        self.SFX_EAT = pygame.mixer.Sound(os.path.join('src','assets', 'eat.ogg'))
        self.SFX_WIN = pygame.mixer.Sound(os.path.join('src','assets', 'win.ogg'))
        self.SFX_TIE = pygame.mixer.Sound(os.path.join('src','assets', 'tie.ogg'))
        self.sfx_play = False
        self.screen = pygame.display.set_mode((self.SCREEN_HEIGHT, self.SCREEN_WIDTH)) # Set mode for game window
        pygame.display.set_caption(gameTitle) # Set caption and title for game's window

    def gameLoop(self) -> None:
        """
        Perform game loop operation for handling event during window game running
        """

        # Create snake on the screen
        self.snake1 = Snake([Point(3, 2), Point(2, 2), Point(1, 2)], Point(1, 0)) 
        self.snake2 = Snake([Point(28, 29), Point(29, 29), Point(30, 29)], Point(-1, 0)) 
        self.fps = pygame.time.Clock()
        self.fruit = [Fruit() for i in range(5)]
        # When apple counting == 3 -> 1 golden apple
        self.apple_cnt = 0

        self.obstacle_list = []

        # Handler variable for game window running
        self.gameRunning = True

        while self.gameRunning:
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)

                self.handlingDirectionEvent(event) # Event for snake 1

            # Handling fruit eat event
            for kF, vF in enumerate(self.fruit):
                if self.snake1.snakePosition[0] == vF: # Snake 1
                    if vF.is_golden:
                        self.snake1.snakeLength += 3
                        self.snake1.snakePoint += 3
                        if switches.sfx_switch == True:
                            self.SFX_EAT.play()
                        for i in range(3):
                            self.snake1.snakePosition.append(Point(-1, -1))
                    else:
                        self.snake1.snakeLength += 1
                        self.snake1.snakePoint += 1
                        if switches.sfx_switch == True:
                            self.SFX_EAT.play()
                        self.snake1.snakePosition.append(Point(-1, -1))
                        self.fruit[kF].nextFruitPosition()
                    while (self.fruit[kF] in self.snake1.snakePosition):
                        self.fruit[kF].nextFruitPosition()
                    self.fruit[kF].is_golden = False
                    self.apple_cnt += 1

            self.handlingCollision1(self.snake1)

            for kF, vF in enumerate(self.fruit):
                if self.snake2.snakePosition[0] == vF: # Snake 2
                    if vF.is_golden:
                        self.snake2.snakeLength += 3
                        self.snake2.snakePoint += 3
                        if switches.sfx_switch == True:
                            self.SFX_EAT.play()
                        for i in range(3):
                            self.snake2.snakePosition.append(Point(-1, -1))
                    else:
                        self.snake2.snakeLength += 1
                        self.snake2.snakePoint += 1
                        if switches.sfx_switch == True:
                            self.SFX_EAT.play()
                        self.snake2.snakePosition.append(Point(-1, -1))
                    self.fruit[kF].nextFruitPosition()
                    while (self.fruit[kF] in self.snake1.snakePosition):
                        self.fruit[kF].nextFruitPosition()
                    self.fruit[kF].is_golden = False
                    self.apple_cnt += 1

            self.handlingCollision2(self.snake2)
            # Handle for apple counting is count to 3
            # When apple counting is 3 generate obstacle
            if self.apple_cnt == 3:
                i = random.randint(0, 4)
                # Set a random apple to golden apple
                self.fruit[i].is_golden = True
                self.apple_cnt = 0

                self.generate_obstacle()

            self.screen.fill(self.BLACK) # Background
            pygame.draw.rect(self.screen,self.YELLOW,(0,0,650,24))   # Top Border
            pygame.draw.rect(self.screen,self.YELLOW,(0,0,22.5,650)) # Left Border
            pygame.draw.rect(self.screen,self.YELLOW,(0,620,650,30)) # Bot Border
            pygame.draw.rect(self.screen,self.YELLOW,(620,0,30,650)) # Right Border


            # Draw score
            score_font = pygame.font.Font(os.path.join('src','assets', 'font.ttf'), 15)
            score_text = score_font.render('Score:', False, self.FONT_COLOR)
            p1_score = score_font.render(str(self.snake1.snakePoint), False, self.RED)
            p2_score = score_font.render(str(self.snake2.snakePoint), False, self.CYAN)
            # Draw if not game over
            if not self.STAT_GAME:
                # Draw player 1 score
                self.screen.blit(score_text, (15, 10))
                self.screen.blit(p1_score, (105, 10))
                # Draw player 2 score
                self.screen.blit(score_text, (535, 10))
                self.screen.blit(p2_score, (625, 10))
                # Else draw if game over
                # Draw both players's score
            
            # Game over
            if self.COLLISION_STAT != -1:
                get_font = pygame.font.Font(os.path.join('src','assets', 'font.ttf'), self.STAT_SIZE)
                if self.COLLISION_STAT == 0:
                    text = get_font.render('TIE', True, self.STAT_COLOR, self.STAT_BORDER_COLOR)
                    sfx_get = self.SFX_TIE
                elif self.COLLISION_STAT == 1:
                    text = get_font.render('P1 Win', True, self.STAT_COLOR, self.STAT_BORDER_COLOR)
                    sfx_get = self.SFX_WIN
                elif self.COLLISION_STAT == 2:
                    text = get_font.render('P2 Win', True, self.STAT_COLOR, self.STAT_BORDER_COLOR)
                    sfx_get = self.SFX_WIN
                if self.sfx_play == False:
                    if switches.sfx_switch == True:
                        sfx_get.play()
                        pygame.mixer.music.stop()
                    self.sfx_play = True


                self.screen.blit(text, self.STAT_POS)
                events = pygame.event.get()
                for event in events:
                    if event.type == pygame.K_SPACE:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN and event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit() 

            if (self.STAT_GAME == False):
                self.drawBareboneSnake1(self.snake1) # Draw snake 1
                self.drawBareboneSnake2(self.snake2) # Draw snake 2
                self.draw_obstacle()

                self.snake1.updateSnakeByDirection()
                self.snake2.updateSnakeByDirection()


            pygame.display.update() 
            self.fps.tick(self.FPS)  # Speed of Snake

    def handlingCollision1(self, snake1): # Collision for snake 1
        """
        handling collision for snake
        """
        head = self.snake1.snakePosition[0]
        if head in self.snake1.snakePosition[1:] or head in self.snake2.snakePosition[:] or head.x == 0 or head.x == 31 or head.y == 0 or head.y == 31 or head in self.obstacle_list:
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
        if head in self.snake2.snakePosition[1:] or head in self.snake1.snakePosition[:] or head.x == 0 or head.x == 31 or head.y == 0 or head.y == 31 or head in self.obstacle_list:
            if head == self.snake1.snakePosition[0]:
                self.COLLISION_STAT = 0
            else:
                self.COLLISION_STAT = 1
            self.STAT_GAME = True
            return

    def generate_obstacle(self):
        self.obstacle_list.append(Obstacle())
        while self.obstacle_list[-1] in self.snake1.snakePosition or self.obstacle_list[-1] in self.snake2.snakePosition:
            self.obstacle_list[-1].nextPosition()

    def draw_obstacle(self):
        for k, v in enumerate(self.obstacle_list):
            pygame.draw.rect(self.screen, self.WHITE, v.axisToRect(20))

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

        for kF, vF in enumerate(self.fruit):
            if not vF.is_golden:
                pygame.draw.rect(self.screen, self.FRUIT_COLOR, vF.axisToRect(20))
            else:
                pygame.draw.rect(self.screen, self.GOLDEN_FRUIT_COLOR, vF.axisToRect(20))

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

        for kF, vF in enumerate(self.fruit):
            if not vF.is_golden:
                pygame.draw.rect(self.screen, self.FRUIT_COLOR, vF.axisToRect(20))
            else:
                pygame.draw.rect(self.screen, self.GOLDEN_FRUIT_COLOR, vF.axisToRect(20))

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