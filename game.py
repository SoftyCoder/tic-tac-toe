import sys, pygame
import random




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

#loading bg image
bg = pygame.image.load('assets/bg.png')
bg_rect = bg.get_rect()

#loading bg image
play_button = pygame.image.load('assets/play_button.png')
play_button_rect = play_button.get_rect()
#position of play_button
play_button_rect.centerx, play_button_rect.centery = (width/2), (height/2)



while running:
    
    # to quit the game when close button is clicked
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color
    screen.fill(screencolor)

    #WHEN STATE IS MAIN MENU
    if state == 'menu':
        
        #render bg image
        screen.blit(bg, bg_rect)
        #render play button
        screen.blit(play_button, play_button_rect)


        # runs when user clicks the play button
        for event in pygame.event.get():
            if play_button_rect.collidepoint(pygame.mouse.get_pos()):
                if event.type == pygame.MOUSEBUTTONUP:
                    # waits for 200ms and changes state to actual game
                    pygame.time.wait(200)
                    state = 'game'



    # THE ACTUAL GAME
    if state == 'game':
        x = 1
    





    # update the game's frame
    pygame.display.flip()


    # limit framerate to 60fps
    clock.tick(60)  

pygame.quit()