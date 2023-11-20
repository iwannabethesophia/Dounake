import pygame
import sys
import dn_lib as switches

from button import Button
from screen import GameScreen

class TitleScreen():
    # The Title screen should follow the width and height window of gameplay.
    SCREEN_WIDTH = 650
    SCREEN_HEIGHT = 650

    # Color
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    RED = (255,0,0)
    GREEN = (0,128,0)
    MENU_TEXT_COLOR = (182,143,64)

    # Global variables for controlling music and sfx
    bgm_stat = True
    sfx_stat = True

    BG = pygame.image.load("src/assets/Background.png")
    
    def __init__(self):
        pygame.init()
        # Load and play loaded song indefinitely
        pygame.mixer.music.load("src/assets/bgm.mp3")
        pygame.mixer.music.play(-1)
        # Load menu's sfx
        self.sfx_confirm = pygame.mixer.Sound("src/assets/confirm.ogg")
        self.sfx_back = pygame.mixer.Sound("src/assets/back.ogg")
        self.SCREEN = pygame.display.set_mode((self.SCREEN_HEIGHT, self.SCREEN_WIDTH))
        pygame.display.set_caption("Dounake")

    def get_font(self, size): # Returns Press-Start-2P in the desired size
        return pygame.font.Font("src/assets/font.ttf", size)

    def play(self): 
        play_game = GameScreen("Dounake")
        play_game.gameLoop()

    def options(self):
        while True:
            OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
            BOX = pygame.image.load("src/assets/Unfilled_box.png")
            dp = 50
            self.SCREEN.blit(self.BG, (0, 0)) # Background

            # Back button
            OPTIONS_BACK = Button(image=None, pos=(110, 80), 
                                text_input="BACK", font=self.get_font(30), base_color=self.WHITE, hovering_color=self.GREEN)

            OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
            OPTIONS_BACK.update(self.SCREEN)

            # Player 1 show button
            OPTIONS_PLAYER_1 = Button(image=None, pos=(50+dp, 150+dp), 
                                text_input="P1", font=self.get_font(40), base_color=self.WHITE, hovering_color=self.GREEN)
            OPTIONS_PLAYER_1.update(self.SCREEN)
            self.SCREEN.blit(BOX, (120+dp, 120+dp))
            self.SCREEN.blit(BOX, (240+dp, 120+dp))
            self.SCREEN.blit(BOX, (360+dp, 120+dp))
            self.SCREEN.blit(BOX, (480+dp, 120+dp))
            P1_UP = Button(image=None, pos=(151+dp, 152+dp), 
                                text_input="W", font=self.get_font(30), base_color=self.WHITE, hovering_color=self.GREEN)
            P1_DOWN = Button(image=None, pos=(271+dp, 152+dp), 
                                text_input="S", font=self.get_font(30), base_color=self.WHITE, hovering_color=self.GREEN)
            P1_LEFT = Button(image=None, pos=(391+dp, 152+dp), 
                                text_input="A", font=self.get_font(30), base_color=self.WHITE, hovering_color=self.GREEN)
            P1_RIGHT = Button(image=None, pos=(511+dp, 152+dp), 
                                text_input="D", font=self.get_font(30), base_color=self.WHITE, hovering_color=self.GREEN)
            P1_UP.update(self.SCREEN)
            P1_DOWN.update(self.SCREEN)
            P1_LEFT.update(self.SCREEN)
            P1_RIGHT.update(self.SCREEN)

            # Player 2 show button
            OPTIONS_PLAYER_2 = Button(image=None, pos=(50+dp, 250+dp), 
                                text_input="P2", font=self.get_font(40), base_color=self.WHITE, hovering_color=self.GREEN)
            OPTIONS_PLAYER_2.update(self.SCREEN)
            self.SCREEN.blit(BOX, (120+dp, 220+dp))
            self.SCREEN.blit(BOX, (240+dp, 220+dp))
            self.SCREEN.blit(BOX, (360+dp, 220+dp))
            self.SCREEN.blit(BOX, (480+dp, 220+dp))
            P2_UP = Button(image=None, pos=(151.5+dp, 270+dp), 
                                text_input="^", font=self.get_font(60), base_color=self.WHITE, hovering_color=self.GREEN)
            P2_DOWN = Button(image=None, pos=(271+dp, 252+dp), 
                                text_input="v", font=self.get_font(30), base_color=self.WHITE, hovering_color=self.GREEN)
            P2_LEFT = Button(image=None, pos=(391+dp, 252+dp), 
                                text_input=">", font=self.get_font(30), base_color=self.WHITE, hovering_color=self.GREEN)
            P2_RIGHT = Button(image=None, pos=(511+dp, 252+dp), 
                                text_input="<", font=self.get_font(30), base_color=self.WHITE, hovering_color=self.GREEN)
            P2_UP.update(self.SCREEN)
            P2_DOWN.update(self.SCREEN)
            P2_LEFT.update(self.SCREEN)
            P2_RIGHT.update(self.SCREEN)
            
            OPTIONS_SFX = Button(image=None, pos=(100, 500-dp), 
                                text_input="SFX", font=self.get_font(40), base_color=self.WHITE, hovering_color=self.GREEN)
            OPTIONS_SFX.update(self.SCREEN)
            OPTIONS_BGM = Button(image=None, pos=(100, 575-dp), 
                                text_input="BGM", font=self.get_font(40), base_color=self.WHITE, hovering_color=self.GREEN)
            OPTIONS_BGM.update(self.SCREEN)
            
            # SFX changing button
            global sfx_stat
            if (switches.sfx_switch == True):
                SFX_STAT = Button(image=None, pos=(250, 500-dp), 
                                text_input="ON", font=self.get_font(40), base_color=self.WHITE, hovering_color=self.GREEN)
                self.sfx_confirm.set_volume(100)
                self.sfx_back.set_volume(100)
                
            else:
                SFX_STAT = Button(image=None, pos=(250, 500-dp), 
                                text_input="OFF", font=self.get_font(40), base_color=self.WHITE, hovering_color=self.GREEN)
                self.sfx_confirm.set_volume(0)
                self.sfx_back.set_volume(0)
            SFX_STAT.changeColor(OPTIONS_MOUSE_POS)
            SFX_STAT.update(self.SCREEN)
            
            # BGM changing button
            global bgm_stat
            if (switches.bgm_switch == True):
                pygame.mixer.music.set_volume(100)
                BGM_STAT = Button(image=None, pos=(250, 575-dp), 
                                text_input="ON", font=self.get_font(40), base_color=self.WHITE, hovering_color=self.GREEN)
            else:
                pygame.mixer.music.set_volume(0)
                BGM_STAT = Button(image=None, pos=(250, 575-dp), 
                                text_input="OFF", font=self.get_font(40), base_color=self.WHITE, hovering_color=self.GREEN)
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
                        if switches.sfx_switch == True:
                            switches.sfx_switch = False
                        else:
                            switches.sfx_switch = True
                    if BGM_STAT.checkForInput(OPTIONS_MOUSE_POS):
                        self.sfx_confirm.play()
                        if switches.bgm_switch == True:
                            switches.bgm_switch = False
                        else:
                            switches.bgm_switch = True
            pygame.display.update()

    def main_menu(self):
        while True:
            self.SCREEN.blit(self.BG, (0, 0))

            MENU_MOUSE_POS = pygame.mouse.get_pos()
            MENU_TEXT = Button(image=None, pos=(325, 200), 
                            text_input="DOUNAKE", font=self.get_font(60), base_color=self.MENU_TEXT_COLOR, hovering_color=self.GREEN)
            MENU_TEXT.update(self.SCREEN)
            PLAY_BUTTON = Button(image=None, pos=(325, 325), 
                                text_input="PLAY", font=self.get_font(45), base_color=self.WHITE, hovering_color=self.GREEN)
            OPTIONS_BUTTON = Button(image=None, pos=(325, 400), 
                                text_input="OPTION", font=self.get_font(45), base_color=self.WHITE, hovering_color=self.GREEN)
            QUIT_BUTTON = Button(image=None, pos=(325, 475), 
                                text_input="QUIT", font=self.get_font(45), base_color=self.WHITE, hovering_color=self.GREEN)


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