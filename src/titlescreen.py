import pygame
import sys
import os

from button import Button
from screen import GameScreen

class TitleScreen:
    # Display screen could be change later.
    # 400x400 should be for gameplay. The window screen should be larger
    # The Title screen should follow the width and height window of gameplay.
    SCREEN_WIDTH = 400
    SCREEN_HEIGHT = 400

    # Color
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    RED = (255,0,0)
    GREEN = (0,128,0)
    MENU_TEXT_COLOR = (182,143,64)

    # Global variables for controlling music and sfx
    bgm_stat = True
    sfx_stat = True

    BG = pygame.transform.scale(pygame.image.load(
        os.path.join('src', 'assets', 'Background.png')),(SCREEN_HEIGHT,SCREEN_WIDTH))
    
    def __init__(self):
        pygame.init()
        # Load and play loaded song indefinitely
        pygame.mixer.music.load(os.path.join('src', 'assets', 'bgm.mp3'))
        pygame.mixer.music.play(-1)
        # Load menu's sfx
        self.sfx_confirm = pygame.mixer.Sound(os.path.join('src', 'assets', 'confirm.ogg'))
        self.sfx_back = pygame.mixer.Sound(os.path.join('src', 'assets', 'back.ogg'))

        self.SCREEN = pygame.display.set_mode((self.SCREEN_HEIGHT, self.SCREEN_WIDTH))
        pygame.display.set_caption("Dounake")

    def get_font(self, size): # Returns Press-Start-2P in the desired size
        return pygame.font.Font(os.path.join('src','assets', 'font.ttf'), size)

    def play(self): 
        # The play button (on maintain :<).  Need to connect to the main.py
        # print("Hello, this is play button")
        play_game = GameScreen("Dounake")
        play_game.gameLoop()

    def options(self): # Recommend define all the button outside then connect them into options!!!
        while True:
            OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
            BOX = pygame.image.load(os.path.join('src','assets', 'Unfilled_box.png'))

            self.SCREEN.blit(self.BG, (0, 0)) # Background

            # Back button
            OPTIONS_BACK = Button(image=None, pos=(60, 30), 
                                text_input="BACK", font=self.get_font(20), base_color=self.WHITE, hovering_color=self.GREEN)

            OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
            OPTIONS_BACK.update(self.SCREEN)

            # Player 1 changing button
            OPTIONS_PLAYER_1 = Button(image=None, pos=(50, 100), 
                                text_input="P1", font=self.get_font(30), base_color=self.WHITE, hovering_color=self.GREEN)
            OPTIONS_PLAYER_1.update(self.SCREEN)
            self.SCREEN.blit(BOX, (100, 80))
            self.SCREEN.blit(BOX, (180, 80))
            self.SCREEN.blit(BOX, (260, 80))
            self.SCREEN.blit(BOX, (340, 80))
            P1_UP = Button(image=None, pos=(121, 102), 
                                text_input="W", font=self.get_font(20), base_color=self.WHITE, hovering_color=self.GREEN)
            P1_DOWN = Button(image=None, pos=(201, 102), 
                                text_input="S", font=self.get_font(20), base_color=self.WHITE, hovering_color=self.GREEN)
            P1_LEFT = Button(image=None, pos=(281, 102), 
                                text_input="A", font=self.get_font(20), base_color=self.WHITE, hovering_color=self.GREEN)
            P1_RIGHT = Button(image=None, pos=(361, 102), 
                                text_input="D", font=self.get_font(20), base_color=self.WHITE, hovering_color=self.GREEN)
            P1_UP.update(self.SCREEN)
            P1_DOWN.update(self.SCREEN)
            P1_LEFT.update(self.SCREEN)
            P1_RIGHT.update(self.SCREEN)

            # Player 2 changing button
            OPTIONS_PLAYER_2 = Button(image=None, pos=(50, 200), 
                                text_input="P2", font=self.get_font(30), base_color=self.WHITE, hovering_color=self.GREEN)
            OPTIONS_PLAYER_2.update(self.SCREEN)
            self.SCREEN.blit(BOX, (100, 180))
            self.SCREEN.blit(BOX, (180, 180))
            self.SCREEN.blit(BOX, (260, 180))
            self.SCREEN.blit(BOX, (340, 180))
            P2_UP = Button(image=None, pos=(121.5, 210), 
                                text_input="^", font=self.get_font(30), base_color=self.WHITE, hovering_color=self.GREEN)
            P2_DOWN = Button(image=None, pos=(201, 202), 
                                text_input="v", font=self.get_font(20), base_color=self.WHITE, hovering_color=self.GREEN)
            P2_LEFT = Button(image=None, pos=(281, 202), 
                                text_input=">", font=self.get_font(20), base_color=self.WHITE, hovering_color=self.GREEN)
            P2_RIGHT = Button(image=None, pos=(361, 202), 
                                text_input="<", font=self.get_font(20), base_color=self.WHITE, hovering_color=self.GREEN)
            P2_UP.update(self.SCREEN)
            P2_DOWN.update(self.SCREEN)
            P2_LEFT.update(self.SCREEN)
            P2_RIGHT.update(self.SCREEN)
            
            OPTIONS_SFX = Button(image=None, pos=(100, 300), 
                                text_input="SFX", font=self.get_font(30), base_color=self.WHITE, hovering_color=self.GREEN)
            OPTIONS_SFX.update(self.SCREEN)
            OPTIONS_BGM = Button(image=None, pos=(100, 350), 
                                text_input="BGM", font=self.get_font(30), base_color=self.WHITE, hovering_color=self.GREEN)
            OPTIONS_BGM.update(self.SCREEN)
            
            # SFX changing button
            global sfx_stat
            if (self.sfx_stat == True):
                SFX_STAT = Button(image=None, pos=(250, 300), 
                                text_input="ON", font=self.get_font(30), base_color=self.WHITE, hovering_color=self.GREEN)
                #turned on sfx
                self.sfx_confirm.set_volume(100)
                self.sfx_back.set_volume(100)
                
            else:
                SFX_STAT = Button(image=None, pos=(250, 300), 
                                text_input="OFF", font=self.get_font(30), base_color=self.WHITE, hovering_color=self.GREEN)
                #turned off sfx
                self.sfx_confirm.set_volume(0)
                self.sfx_back.set_volume(0)
            SFX_STAT.changeColor(OPTIONS_MOUSE_POS)
            SFX_STAT.update(self.SCREEN)
            
            # BGM changing button
            global bgm_stat
            if (self.bgm_stat == True):
                pygame.mixer.music.set_volume(100)
                BGM_STAT = Button(image=None, pos=(250, 350), 
                                text_input="ON", font=self.get_font(30), base_color=self.WHITE, hovering_color=self.GREEN)
            else:
                pygame.mixer.music.set_volume(0)
                BGM_STAT = Button(image=None, pos=(250, 350), 
                                text_input="OFF", font=self.get_font(30), base_color=self.WHITE, hovering_color=self.GREEN)
            BGM_STAT.changeColor(OPTIONS_MOUSE_POS)
            BGM_STAT.update(self.SCREEN)
            
            # User click on things in option menu
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                        self.sfx_back.play()
                        self.main_menu()
                    if SFX_STAT.checkForInput(OPTIONS_MOUSE_POS):
                        self.sfx_confirm.play()
                        if self.sfx_stat == True:
                            self.sfx_stat = False
                        else:
                            self.sfx_stat = True
                    if BGM_STAT.checkForInput(OPTIONS_MOUSE_POS):
                        self.sfx_confirm.play()
                        if self.bgm_stat == True:
                            self.bgm_stat = False
                        else:
                            self.bgm_stat = True
            pygame.display.update()

    def main_menu(self):
        while True:
            self.SCREEN.blit(self.BG, (0, 0))

            MENU_MOUSE_POS = pygame.mouse.get_pos()
            MENU_TEXT = Button(image=None, pos=(200, 100), 
                            text_input="DOUNAKE", font=self.get_font(40), base_color=self.MENU_TEXT_COLOR, hovering_color=self.GREEN)
            MENU_TEXT.update(self.SCREEN)
            PLAY_BUTTON = Button(image=None, pos=(200, 200), 
                                text_input="PLAY", font=self.get_font(25), base_color=self.WHITE, hovering_color=self.GREEN)
            OPTIONS_BUTTON = Button(image=None, pos=(200, 250), 
                                text_input="OPTION", font=self.get_font(25), base_color=self.WHITE, hovering_color=self.GREEN)
            QUIT_BUTTON = Button(image=None, pos=(200, 300), 
                                text_input="QUIT", font=self.get_font(25), base_color=self.WHITE, hovering_color=self.GREEN)


            for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(self.SCREEN)
            
            
            # User click on the menu
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.sfx_confirm.play()
                        self.play()
                    if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.sfx_confirm.play()
                        self.options()
                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.sfx_confirm.play()
                        pygame.quit()
                        sys.exit()

            pygame.display.update()

game = TitleScreen()
game.main_menu()