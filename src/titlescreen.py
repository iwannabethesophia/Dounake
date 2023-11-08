import pygame, sys

from button import Button

pygame.init()
##display screen could be change later.
#200x200 should be for gameplay. the windown screen should be larger
SCREEN = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Dounake")

BG = pygame.image.load("src/assets/Background.png")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("src/assets/font.ttf", size)

def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        PLAY_BACK = Button(image=None, pos=(200, 200), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Red")

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
bgm_stat = True
sfx_stat = True
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        BOX = pygame.image.load("src/assets/unfilled box.png")

        SCREEN.blit(BG, (0, 0))

        OPTIONS_BACK = Button(image=None, pos=(60, 30), 
                             text_input="BACK", font=get_font(20), base_color="white", hovering_color="green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        OPTIONS_PLAYER_1 = Button(image=None, pos=(50, 100), 
                             text_input="P1", font=get_font(30), base_color="white", hovering_color="green")
        OPTIONS_PLAYER_1.update(SCREEN)
        SCREEN.blit(BOX, (100, 80))
        SCREEN.blit(BOX, (180, 80))
        SCREEN.blit(BOX, (260, 80))
        SCREEN.blit(BOX, (340, 80))
        P1_UP = Button(image=None, pos=(121, 102), 
                             text_input="W", font=get_font(20), base_color="white", hovering_color="green")
        P1_DOWN = Button(image=None, pos=(201, 102), 
                             text_input="S", font=get_font(20), base_color="white", hovering_color="green")
        P1_LEFT = Button(image=None, pos=(281, 102), 
                             text_input="A", font=get_font(20), base_color="white", hovering_color="green")
        P1_RIGHT = Button(image=None, pos=(361, 102), 
                             text_input="D", font=get_font(20), base_color="white", hovering_color="green")
        P1_UP.update(SCREEN)
        P1_DOWN.update(SCREEN)
        P1_LEFT.update(SCREEN)
        P1_RIGHT.update(SCREEN)

        OPTIONS_PLAYER_2 = Button(image=None, pos=(50, 200), 
                             text_input="P2", font=get_font(30), base_color="white", hovering_color="green")
        OPTIONS_PLAYER_2.update(SCREEN)
        SCREEN.blit(BOX, (100, 180))
        SCREEN.blit(BOX, (180, 180))
        SCREEN.blit(BOX, (260, 180))
        SCREEN.blit(BOX, (340, 180))
        P2_UP = Button(image=None, pos=(121.5, 210), 
                             text_input="^", font=get_font(30), base_color="white", hovering_color="green")
        P2_DOWN = Button(image=None, pos=(201, 202), 
                             text_input="v", font=get_font(20), base_color="white", hovering_color="green")
        P2_LEFT = Button(image=None, pos=(281, 202), 
                             text_input=">", font=get_font(20), base_color="white", hovering_color="green")
        P2_RIGHT = Button(image=None, pos=(361, 202), 
                             text_input="<", font=get_font(20), base_color="white", hovering_color="green")
        P2_UP.update(SCREEN)
        P2_DOWN.update(SCREEN)
        P2_LEFT.update(SCREEN)
        P2_RIGHT.update(SCREEN)
        
        OPTIONS_SFX = Button(image=None, pos=(100, 300), 
                             text_input="SFX", font=get_font(30), base_color="white", hovering_color="green")
        OPTIONS_SFX.update(SCREEN)
        OPTIONS_BGM = Button(image=None, pos=(100, 350), 
                             text_input="BGM", font=get_font(30), base_color="white", hovering_color="green")
        OPTIONS_BGM.update(SCREEN)
        global sfx_stat
        if (sfx_stat == True):
            SFX_STAT = Button(image=None, pos=(250, 300), 
                             text_input="ON", font=get_font(30), base_color="white", hovering_color="green")
        else:
            SFX_STAT = Button(image=None, pos=(250, 300), 
                             text_input="OFF", font=get_font(30), base_color="white", hovering_color="green")
        SFX_STAT.changeColor(OPTIONS_MOUSE_POS)
        SFX_STAT.update(SCREEN)
        
        global bgm_stat
        if (bgm_stat == True):
            BGM_STAT = Button(image=None, pos=(250, 350), 
                             text_input="ON", font=get_font(30), base_color="white", hovering_color="green")
        else:
            BGM_STAT = Button(image=None, pos=(250, 350), 
                             text_input="OFF", font=get_font(30), base_color="white", hovering_color="green")
        BGM_STAT.changeColor(OPTIONS_MOUSE_POS)
        BGM_STAT.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()
                if SFX_STAT.checkForInput(OPTIONS_MOUSE_POS):
                    if sfx_stat == True:
                        sfx_stat = False
                        SFX_STAT = Button(image=None, pos=(250, 300), 
                             text_input="OFF", font=get_font(30), base_color="white", hovering_color="green")
                        SFX_STAT.changeColor(OPTIONS_MOUSE_POS)
                        SFX_STAT.update(SCREEN)
                    else:
                        sfx_stat = True
                        SFX_STAT = Button(image=None, pos=(250, 300), 
                             text_input="ON", font=get_font(30), base_color="white", hovering_color="green")
                        SFX_STAT.changeColor(OPTIONS_MOUSE_POS)
                        SFX_STAT.update(SCREEN)
                if BGM_STAT.checkForInput(OPTIONS_MOUSE_POS):
                    if bgm_stat == True:
                        bgm_stat = False
                        BGM_STAT = Button(image=None, pos=(250, 350), 
                             text_input="OFF", font=get_font(30), base_color="white", hovering_color="green")
                        BGM_STAT.changeColor(OPTIONS_MOUSE_POS)
                        BGM_STAT.update(SCREEN)
                    else:
                        bgm_stat = True
                        BGM_STAT = Button(image=None, pos=(250, 350), 
                             text_input="ON", font=get_font(30), base_color="white", hovering_color="green")
                        BGM_STAT.changeColor(OPTIONS_MOUSE_POS)
                        BGM_STAT.update(SCREEN)
                        


        pygame.display.update()

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(40).render("DOUNAKE", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(200, 100))

        PLAY_BUTTON = Button(image=None, pos=(200, 200), 
                            text_input="PLAY", font=get_font(25), base_color="White", hovering_color="Green")
        OPTIONS_BUTTON = Button(image=None, pos=(200, 250), 
                            text_input="OPTION", font=get_font(25), base_color="White", hovering_color="Green")
        QUIT_BUTTON = Button(image=None, pos=(200, 300), 
                            text_input="QUIT", font=get_font(25), base_color="White", hovering_color="Green")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()