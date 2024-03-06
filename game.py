import sys, pygame
import random




pygame.init()
windowsize = (1280, 720)
screen = pygame.display.set_mode(windowsize)
clock = pygame.time.Clock()
running = True

screencolor = 108, 105, 141

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    screen.fill(screencolor)

    
    pygame.display.flip()

    clock.tick(60)  

pygame.quit()