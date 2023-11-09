import pygame
import sys
import os

from button import Button

pygame.init()
# Display screen could be change later.
# 400x400 should be for gameplay. The window screen should be larger
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400

#load and play loaded song indefinitely
pygame.mixer.music.load('src/assets/bgm.mp3')
pygame.mixer.music.play(-1)

#load menu's sfx
sfx_confirm = pygame.mixer.Sound('src/assets/confirm.ogg')
sfx_back = pygame.mixer.Sound('src/assets/back.ogg')

#Color
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,128,0)
MENU_TEXT_COLOR = (182,143,64)

#global variables for controlling music and sfx
bgm_stat = True
sfx_stat = True


SCREEN = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
pygame.display.set_caption("Dounake")

BG = pygame.transform.scale(pygame.image.load(
    os.path.join('src','assets', 'Background.png')),(SCREEN_HEIGHT,SCREEN_WIDTH))

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font(os.path.join('src','assets', 'font.ttf'), size)

def play(): # The play button (on maintain :<).  Need to connect to the main.py
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill(BLACK)

        PLAY_BACK = Button(image=None, pos=(200, 200), 
                            text_input="BACK", font=get_font(75), base_color=WHITE, hovering_color=RED)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def options(): # Recommend define all the button outside then connect them into options!!!
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        BOX = pygame.image.load(os.path.join('src','assets', 'Unfilled_box.png'))

        SCREEN.blit(BG, (0, 0)) # Background

        # Back button
        OPTIONS_BACK = Button(image=None, pos=(60, 30), 
                            text_input="BACK", font=get_font(20), base_color=WHITE, hovering_color=GREEN)

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        # Player 1 changing button
        OPTIONS_PLAYER_1 = Button(image=None, pos=(50, 100), 
                            text_input="P1", font=get_font(30), base_color=WHITE, hovering_color=GREEN)
        OPTIONS_PLAYER_1.update(SCREEN)
        SCREEN.blit(BOX, (100, 80))
        SCREEN.blit(BOX, (180, 80))
        SCREEN.blit(BOX, (260, 80))
        SCREEN.blit(BOX, (340, 80))
        P1_UP = Button(image=None, pos=(121, 102), 
                            text_input="W", font=get_font(20), base_color=WHITE, hovering_color=GREEN)
        P1_DOWN = Button(image=None, pos=(201, 102), 
                            text_input="S", font=get_font(20), base_color=WHITE, hovering_color=GREEN)
        P1_LEFT = Button(image=None, pos=(281, 102), 
                            text_input="A", font=get_font(20), base_color=WHITE, hovering_color=GREEN)
        P1_RIGHT = Button(image=None, pos=(361, 102), 
                            text_input="D", font=get_font(20), base_color=WHITE, hovering_color=GREEN)
        P1_UP.update(SCREEN)
        P1_DOWN.update(SCREEN)
        P1_LEFT.update(SCREEN)
        P1_RIGHT.update(SCREEN)

        # Player 2 changing button
        OPTIONS_PLAYER_2 = Button(image=None, pos=(50, 200), 
                            text_input="P2", font=get_font(30), base_color=WHITE, hovering_color=GREEN)
        OPTIONS_PLAYER_2.update(SCREEN)
        SCREEN.blit(BOX, (100, 180))
        SCREEN.blit(BOX, (180, 180))
        SCREEN.blit(BOX, (260, 180))
        SCREEN.blit(BOX, (340, 180))
        P2_UP = Button(image=None, pos=(121.5, 210), 
                            text_input="^", font=get_font(30), base_color=WHITE, hovering_color=GREEN)
        P2_DOWN = Button(image=None, pos=(201, 202), 
                            text_input="v", font=get_font(20), base_color=WHITE, hovering_color=GREEN)
        P2_LEFT = Button(image=None, pos=(281, 202), 
                            text_input=">", font=get_font(20), base_color=WHITE, hovering_color=GREEN)
        P2_RIGHT = Button(image=None, pos=(361, 202), 
                            text_input="<", font=get_font(20), base_color=WHITE, hovering_color=GREEN)
        P2_UP.update(SCREEN)
        P2_DOWN.update(SCREEN)
        P2_LEFT.update(SCREEN)
        P2_RIGHT.update(SCREEN)
        
        OPTIONS_SFX = Button(image=None, pos=(100, 300), 
                            text_input="SFX", font=get_font(30), base_color=WHITE, hovering_color=GREEN)
        OPTIONS_SFX.update(SCREEN)
        OPTIONS_BGM = Button(image=None, pos=(100, 350), 
                            text_input="BGM", font=get_font(30), base_color=WHITE, hovering_color=GREEN)
        OPTIONS_BGM.update(SCREEN)
        
        # SFX changing button
        global sfx_stat
        if (sfx_stat == True):
            SFX_STAT = Button(image=None, pos=(250, 300), 
                            text_input="ON", font=get_font(30), base_color=WHITE, hovering_color=GREEN)
            #turned on sfx
            sfx_confirm.set_volume(100)
            sfx_back.set_volume(100)
            
        else:
            SFX_STAT = Button(image=None, pos=(250, 300), 
                            text_input="OFF", font=get_font(30), base_color=WHITE, hovering_color=GREEN)
            #turned off sfx
            sfx_confirm.set_volume(0)
            sfx_back.set_volume(0)
        SFX_STAT.changeColor(OPTIONS_MOUSE_POS)
        SFX_STAT.update(SCREEN)
        
        # BGM changing button
        global bgm_stat
        if (bgm_stat == True):
            pygame.mixer.music.unpause()
            BGM_STAT = Button(image=None, pos=(250, 350), 
                            text_input="ON", font=get_font(30), base_color=WHITE, hovering_color=GREEN)
        else:
            pygame.mixer.music.pause()
            BGM_STAT = Button(image=None, pos=(250, 350), 
                            text_input="OFF", font=get_font(30), base_color=WHITE, hovering_color=GREEN)
        BGM_STAT.changeColor(OPTIONS_MOUSE_POS)
        BGM_STAT.update(SCREEN)
        
        # User click on things in option menu
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    sfx_back.play()
                    main_menu()
                if SFX_STAT.checkForInput(OPTIONS_MOUSE_POS):
                    sfx_confirm.play()
                    if sfx_stat == True:
                        sfx_stat = False
                    else:
                        sfx_stat = True
                if BGM_STAT.checkForInput(OPTIONS_MOUSE_POS):
                    sfx_confirm.play()
                    if bgm_stat == True:
                        bgm_stat = False
                    else:
                        bgm_stat = True
        pygame.display.update()

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(40).render("DOUNAKE", True, MENU_TEXT_COLOR)
        MENU_RECT = MENU_TEXT.get_rect(center=(200, 100))

        PLAY_BUTTON = Button(image=None, pos=(200, 200), 
                            text_input="PLAY", font=get_font(25), base_color=WHITE, hovering_color=GREEN)
        OPTIONS_BUTTON = Button(image=None, pos=(200, 250), 
                            text_input="OPTION", font=get_font(25), base_color=WHITE, hovering_color=GREEN)
        QUIT_BUTTON = Button(image=None, pos=(200, 300), 
                            text_input="QUIT", font=get_font(25), base_color=WHITE, hovering_color=GREEN)

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        # User click on the menu
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    sfx_confirm.play()
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    sfx_confirm.play()
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    sfx_confirm.play()
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()