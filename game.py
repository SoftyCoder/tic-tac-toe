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
#loading x image
x_image = pygame.image.load('assets/x.png')
#loading x image
o_image = pygame.image.load('assets/o.png')
#load player O image
player_o_bg = pygame.image.load('assets/player_o_bg.png')
#player won
player_won_bg = pygame.image.load('assets/player_won_bg.png')
#computer won
computer_won_bg = pygame.image.load('assets/computer_won_bg.png')




n_moves_played = 0


# reference for symbols
empty= 0
x = 1
o = 2

# actual position of the game
grid  = [empty, empty, empty, 
         empty, empty, empty, 
         empty, empty, empty]

position = [(454, 250), (585, 250), (715, 250),
            (454, 385), (585, 385), (715, 385),
            (454, 520), (585, 520), (715, 520)]


#LOADING SYMBOLS:-
#empty     
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
x0 = x_image.get_rect()
x1 = x_image.get_rect()
x2 = x_image.get_rect()
x3 = x_image.get_rect()
x4 = x_image.get_rect()
x5 = x_image.get_rect()
x6 = x_image.get_rect()
x7 = x_image.get_rect()
x8 = x_image.get_rect()
#O
o0 = o_image.get_rect()
o1 = o_image.get_rect()
o2 = o_image.get_rect()
o3 = o_image.get_rect()
o4 = o_image.get_rect()
o5 = o_image.get_rect()
o6 = o_image.get_rect()
o7 = o_image.get_rect()
o8 = o_image.get_rect()







#generating symbol for player

player = random.randint(1, 2)
if player == o:
    computer = x
if player == x:
    computer = o


did_computer_play = False
did_player_play = True
did_game_end = False


player_o_bg_rect = player_o_bg.get_rect()
player_won_bg_rect = player_won_bg.get_rect()
computer_won_bg_rect = computer_won_bg.get_rect()

who_won = 'none'

def did_anyone_win():
    won = 0
    #vertical
    for j in range(3):
        if (grid[j] == grid[j+3]) and (grid[j]!=0):
            if grid[j+3] == grid[j+6]:
                won = grid[j]
                break
            
    i = 0
    while i <= 6:
        if (grid[i] == grid[i+1]) and (grid[i]!=0):
            if grid[i+1] == grid[i+2]:
                won = grid[i]
                break
        
        i += 3
    return won
            





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
        

        #POSITIONING SYMBOLS
        for i in range(9):
            vars()['empty' + str(i)].x,  vars()['empty' + str(i)].y = position[i]
            vars()['x' + str(i)].x,  vars()['x' + str(i)].y = position[i]
            vars()['o' + str(i)].x,  vars()['o' + str(i)].y = position[i]
        
        #render game bg image (with grid)
        screen.blit(bg_game, bg_game_rect)
        
        for event in pygame.event.get():
            #to quit the game when use clicks close button
            if event.type == pygame.QUIT:
                running = False
    

        #rendering symbols:
        for i in range(9):
            if grid[i] == empty:
                screen.blit(empty_image, vars()['empty' + str(i)])
            if grid[i] == x:
                screen.blit(x_image, vars()['x' + str(i)])
            if grid[i] == o:
                screen.blit(o_image, vars()['o' + str(i)])
        

        if player == x:
            #clicking empty to register clicks + randomly generating move
            if did_anyone_win() == player:
                state = 'player_won'
            if did_anyone_win() == computer:
                state = 'computer_won'
                
                
                
            for i in range(9):
                if vars()['empty' + str(i)].collidepoint(pygame.mouse.get_pos()):
                    if event.type == pygame.MOUSEBUTTONUP:
                        if grid[i] == empty:
                            # waits for 200ms and register click
                            
                            grid[i] = player
                            n_moves_played += 1
                            pygame.time.wait(200)
                            if n_moves_played == 9:
                                break
                            #generate a random move
                            while True:
                                rand = random.randint(0, 8)
                                if grid[rand] == empty:
                                    grid[rand] = computer
                                    n_moves_played += 1
                                    
                                    break

        if player == o:
            
            """
            #generate a random move
            if did_game_end == False:
                while (did_computer_play == False) and (did_player_play == True):
                    rand = random.randint(0, 8)
                    if grid[rand] == empty:
                        grid[rand] = computer
                        n_moves_played += 1
                        
                        pygame.time.wait(200)
                        did_computer_play = True
                        did_player_play = False
                        pygame.display.flip()
                        if n_moves_played == 9:
                            did_game_end = True
                        break
            """
            
            screen.blit(player_o_bg, player_o_bg_rect)

    if state == 'player_won':
        screen.blit(player_won_bg, player_won_bg_rect)
        player_won_bg_rect.x, player_won_bg_rect.y = 0, 0
        pygame.display.flip()
        pygame.time.wait(2000)
        pygame.quit()
    if state == 'computer_won':
        screen.blit(computer_won_bg, computer_won_bg_rect)
        computer_won_bg_rect.x, computer_won_bg_rect.y = 0, 0
        pygame.display.flip()
        pygame.time.wait(2000)
        pygame.quit()
            





    # update the game's frame
    pygame.display.flip()


    # limit framerate to 60fps
    clock.tick(60)

pygame.quit()