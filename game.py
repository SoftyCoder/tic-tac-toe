import sys, pygame
import random

#loading symbols
def load_symbols():
    #empty 
    global empty0, empty1, empty2, empty3, empty4, empty5, empty6, empty7, empty8
    empty0 = empty_image.get_rect()
    empty1 = empty_image.get_rect()
    empty2 = empty_image.get_rect()
    empty3 = empty_image.get_rect()
    empty4 = empty_image.get_rect()
    empty5 = empty_image.get_rect()
    empty6 = empty_image.get_rect()
    empty7 = empty_image.get_rect()
    empty8 = empty_image.get_rect()
    #X


    #O

def position_symbols():
    for i in range(9):
        vars()['empty' + str(i)].centrex,  vars()['empty' + str(i)].centrey = position[i]





pygame.init()
# window manipulation
width = 1280
height = 720
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tic Tac Toe')

#clock (to track fps)
clock = pygame.time.Clock()

running = True

# color of the screen
screencolor = 108, 105, 141

# state of the game, i.e. if the game started or not
state = 'menu'



#loading menu bg image
bg_menu = pygame.image.load('assets/bg_menu.png')
bg_menu_rect = bg_menu.get_rect()

#loading game bg image
bg_game = pygame.image.load('assets/bg_game.png')
bg_game_rect = bg_game.get_rect()

#loading bg image
play_button = pygame.image.load('assets/play_button.png')
play_button_rect = play_button.get_rect()
#position of play_button
play_button_rect.centerx, play_button_rect.centery = (width/2), (height/2)

#loading empty image
empty_image = pygame.image.load('assets/empty.png')



load_symbols()


# reference for symbols
empty= 0
x = 1
o = 2

# actual position of the game
grid  = [[empty, empty, empty], 
         [empty, empty, empty], 
         [empty, empty, empty]]

position = [(100, 100), (0, 0), (0, 0),
            (0, 0), (0, 0), (0, 0),
            (0, 0), (0, 0), (0, 0)]



position_symbols()
#generating symbol for player
player = random.randint(1, 2)
if player == 1:
    player = 'x'
if player == 2:
    player = 'o'


while running:
    
    

    # fill the screen with a color
    screen.fill(screencolor)


    

    #WHEN STATE IS MAIN MENU
    if state == 'menu':
        
        #render menu bg image
        screen.blit(bg_menu, bg_menu_rect)

        #render play button
        screen.blit(play_button, play_button_rect)


        
        for event in pygame.event.get():
            #to quit the game when use clicks close button
            if event.type == pygame.QUIT:
                running = False
            
            
            
            # runs when user clicks the play button
            if play_button_rect.collidepoint(pygame.mouse.get_pos()):
                if event.type == pygame.MOUSEBUTTONUP:
                    # waits for 200ms and changes state to actual game
                    pygame.time.wait(200)
                    state = 'game'



    # THE ACTUAL GAME
    if state == 'game':
        
        #render game bg image (with grid)
        screen.blit(bg_game, bg_game_rect)
        
        for event in pygame.event.get():
            #to quit the game when use clicks close button
            if event.type == pygame.QUIT:
                running = False
    


    screen.blit(empty_image, empty0)


    # update the game's frame
    pygame.display.flip()


    # limit framerate to 60fps
    clock.tick(60)

pygame.quit()