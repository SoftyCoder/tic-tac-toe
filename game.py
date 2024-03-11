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

#FONTS:
winstreak_font = pygame.font.Font('assets/comic.ttf', 42)
player_info_font = pygame.font.Font('assets/comic.ttf', 42)


#music and sounds
start_sound = pygame.mixer.Sound('assets/start.wav')
click_sound = pygame.mixer.Sound('assets/click.wav')
player_win_sound = pygame.mixer.Sound('assets/player_win.wav')
computer_win_sound = pygame.mixer.Sound('assets/computer_win.wav')

pygame.mixer.music.load('assets/music_peach.mp3')
pygame.mixer.music.play(-1)

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


is_timer_first_time = True
is_gameover_timer_first_time = True


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


    #diagonal
    if (grid[0] == grid[4]) and (grid[0]!=0):
        if grid[4] == grid[8]:
            won = grid[0]
    if (grid[2] == grid[4]) and (grid[2]!=0):
        if grid[4] == grid[6]:
            won = grid[2]
            
    return won
            



#winstreak counter
current_winstreak = 0

while running:
    
    #winstreak
    winstreak_text = winstreak_font.render('Winstreak = ' + str(current_winstreak), True, (241, 242, 238))
    

    player_info = 'idk smthn random'
    #Player info
    if player == o:
        player_info = 'O'
    elif player == x:
        player_info = 'X'
    
    player_info_text = player_info_font.render('Player = ' + player_info, True, (241, 242, 238))
    # fill the screen with a color
    screen.fill(screencolor)


    

    #WHEN STATE IS MAIN MENU
    if state == 'menu':
        
        
        n_moves_played = 0
        grid  = [empty, empty, empty, 
                empty, empty, empty, 
                empty, empty, empty]
        #render menu bg image
        screen.blit(bg_menu, bg_menu_rect)

        #render winstreak
        screen.blit(winstreak_text, (70, 200))

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
                    pygame.mixer.Sound.play(start_sound)
                    is_timer_first_time = True
                    pygame.time.set_timer(pygame.USEREVENT, 1000)
                    #generating symbol for player
                    player = random.randint(1, 2)
                    if player == o:
                        computer = x
                    if player == x:
                        computer = o
                    state = 'game'
        
                


    # THE ACTUAL GAME
    elif state == 'game':
        
        
       
        #POSITIONING SYMBOLS
        for i in range(9):
            vars()['empty' + str(i)].x,  vars()['empty' + str(i)].y = position[i]
            vars()['x' + str(i)].x,  vars()['x' + str(i)].y = position[i]
            vars()['o' + str(i)].x,  vars()['o' + str(i)].y = position[i]
        
        #render game bg image (with grid)
        screen.blit(bg_game, bg_game_rect)
        #render winstreaks
        screen.blit(winstreak_text, (70, 200))
        screen.blit(player_info_text, (70, 250))
        
        for event in pygame.event.get():
            #to quit the game when use clicks close button
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.USEREVENT:
                is_timer_first_time = False
    

        #rendering symbols:
        for i in range(9):
            if grid[i] == empty:
                screen.blit(empty_image, vars()['empty' + str(i)])
            elif grid[i] == x:
                screen.blit(x_image, vars()['x' + str(i)])
            elif grid[i] == o:
                screen.blit(o_image, vars()['o' + str(i)])
        pygame.display.update()
        
        
        if is_timer_first_time == False:
            if player == x:
                
                #clicking empty to register clicks + randomly generating move
                if did_anyone_win() == player:
                    state = 'player_won'
                    pygame.time.set_timer(pygame.USEREVENT, 3500)
                    pygame.mixer.Sound.play(player_win_sound)
                elif did_anyone_win() == computer:
                    state = 'computer_won'
                    pygame.time.set_timer(pygame.USEREVENT, 3500)
                    pygame.mixer.Sound.play(computer_win_sound)
                elif n_moves_played == 9: #TO CHECK DRAW
                    state = 'menu'
                    
                    
                    
                for i in range(9):
                    if vars()['empty' + str(i)].collidepoint(pygame.mouse.get_pos()):
                        if event.type == pygame.MOUSEBUTTONUP:
                            if grid[i] == empty:
                                # waits for 200ms and register click
                                pygame.mixer.Sound.play(click_sound)
                                grid[i] = player
                                n_moves_played += 1
                                pygame.time.wait(200)
                                if n_moves_played == 9:
                                    break
                                #rendering symbols:
                                for i in range(9):
                                    if grid[i] == empty:
                                        screen.blit(empty_image, vars()['empty' + str(i)])
                                    elif grid[i] == x:
                                        screen.blit(x_image, vars()['x' + str(i)])
                                    elif grid[i] == o:
                                        screen.blit(o_image, vars()['o' + str(i)])    
                                pygame.display.update()
                                pygame.time.wait(200)
                                
                                
                                if (n_moves_played < 9) and (did_anyone_win() == 0):

                                    #generate a random move
                                    while True:
                                        rand = random.randint(0, 8)
                                        if grid[rand] == empty:
                                            grid[rand] = computer
                                            n_moves_played += 1
                                            
                                            break
                                #rendering symbols:
                                for i in range(9):
                                    if grid[i] == empty:
                                        screen.blit(empty_image, vars()['empty' + str(i)])
                                    elif grid[i] == x:
                                        screen.blit(x_image, vars()['x' + str(i)])
                                    elif grid[i] == o:
                                        screen.blit(o_image, vars()['o' + str(i)])    
                                pygame.display.update()
                                pygame.time.wait(200)
            elif player == o:
                
                
                #generate a random move:
                waiting = True
                while waiting:
                    rand = random.randint(0, 8)

                    if grid[rand] == empty:
                        grid[rand] = computer
                        n_moves_played += 1
                        break
                #rendering symbols:
                for i in range(9):
                    if grid[i] == empty:
                        screen.blit(empty_image, vars()['empty' + str(i)])
                    elif grid[i] == x:
                        screen.blit(x_image, vars()['x' + str(i)])
                    elif grid[i] == o:
                        screen.blit(o_image, vars()['o' + str(i)])
                
                pygame.display.update()
                pygame.time.wait(200)
                
                #clicking empty to register clicks + randomly generating move
                if did_anyone_win() == player:
                    state = 'player_won'
                    pygame.time.set_timer(pygame.USEREVENT, 3500)
                    pygame.mixer.Sound.play(player_win_sound)
                elif did_anyone_win() == computer:
                    state = 'computer_won'
                    pygame.time.set_timer(pygame.USEREVENT, 3500)
                    pygame.mixer.Sound.play(computer_win_sound)
                elif n_moves_played == 9: #TO CHECK DRAW
                    state = 'menu'
                
                if (n_moves_played < 9) and (did_anyone_win() == 0):

                    waiting = True
                    while waiting:
                        for event in pygame.event.get():
                            #to quit the game when use clicks close button
                            if event.type == pygame.QUIT:
                                pygame.quit()
                        for i in range(9):
                            if vars()['empty' + str(i)].collidepoint(pygame.mouse.get_pos()):
                                if event.type == pygame.MOUSEBUTTONUP:
                                    if grid[i] == empty:
                                        # waits for 200ms and register click
                                        pygame.mixer.Sound.play(click_sound)
                                        grid[i] = player
                                        n_moves_played += 1
                                        pygame.time.wait(200)
                                        waiting = False
                                        #rendering symbols:
                                        for i in range(9):
                                            if grid[i] == empty:
                                                screen.blit(empty_image, vars()['empty' + str(i)])
                                            elif grid[i] == x:
                                                screen.blit(x_image, vars()['x' + str(i)])
                                            elif grid[i] == o:
                                                screen.blit(o_image, vars()['o' + str(i)])
                                        pygame.display.update()
                                        pygame.time.wait(200)
                        if waiting == False:
                            break
                
                #clicking empty to register clicks + randomly generating move
                if did_anyone_win() == player:
                    state = 'player_won'
                    pygame.time.set_timer(pygame.USEREVENT, 3500)
                    pygame.mixer.Sound.play(player_win_sound)
                elif did_anyone_win() == computer:
                    state = 'computer_won'
                    pygame.time.set_timer(pygame.USEREVENT, 3500)
                    pygame.mixer.Sound.play(computer_win_sound)
                elif n_moves_played == 9: #TO CHECK DRAW
                    state = 'menu'                       

            

    elif state == 'player_won':

        for event in pygame.event.get():
            #to quit the game when use clicks close button
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.USEREVENT:
                is_gameover_timer_first_time = False
        
        
        
        #pause music when computer win
        pygame.mixer.music.pause()

        #display player won screen
        screen.blit(player_won_bg, player_won_bg_rect)
        player_won_bg_rect.x, player_won_bg_rect.y = 0, 0
        #render winstreak
        screen.blit(winstreak_text, (70, 200))
        pygame.display.flip()
        
        
        
        if is_gameover_timer_first_time == False:

            #change state to menu
            state = 'menu'
            #increase winstreak by 1
            current_winstreak = current_winstreak + 1
            winstreak_text = winstreak_font.render('Winstreak = ' + str(current_winstreak), True, (241, 242, 238))

            #unpause music when going to menu
            pygame.mixer.music.unpause()

        


    elif state == 'computer_won':
        for event in pygame.event.get():
            #to quit the game when use clicks close button
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.USEREVENT:
                is_gameover_timer_first_time = False
        #reset winstreak
        current_winstreak = 0
        winstreak_text = winstreak_font.render('Winstreak = ' + str(current_winstreak), True, (241, 242, 238))


        
        #pause music when computer win
        pygame.mixer.music.pause()

        #display computer won screen
        screen.blit(computer_won_bg, computer_won_bg_rect)
        computer_won_bg_rect.x, computer_won_bg_rect.y = 0, 0
        #render winstreak
        screen.blit(winstreak_text, (70, 200))
        pygame.display.flip()
        pygame.time.wait(4000)

        if is_gameover_timer_first_time == False:

            #change state to menu
            state = 'menu'

            #unpause music when going to menu
            pygame.mixer.music.unpause()
        





    # update the game's frame
    pygame.display.flip()


    # limit framerate to 60fps
    clock.tick(60)

pygame.quit()