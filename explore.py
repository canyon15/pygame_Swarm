import pygame
from pygame.locals import *
import player
pygame.init()

DISPLAYSURF = pygame.display.set_mode((1080,720))
black = pygame.Color(0, 0, 0)         # Black
white = pygame.Color(255, 255, 255)   # White
grey = pygame.Color(128, 128, 128)   # Grey
red = pygame.Color(255, 0, 0)       # Red
FPS = pygame.time.Clock()

player = Player(540, 360, 540, 375)


#game loop
def gameLoop():
    
    
    game = True
    press_W = False
    press_S = False
    press_A = False
    press_D = False
    turn_left = False
    turn_right = False

    
    while game:
        x = 0
        y = 0

        for event in pygame.event.get():
            if (event.type == pygame.QUIT): # Quit is esc or x in the corner
                game = False 
            elif (event.type == pygame.KEYDOWN):
                if (event.key == 'W' or 'w'):
                    press_W = True
                if (event.key == 'S' or 's'):
                    press_S = True
                if (event.key == 'A' or 'a'):
                    press_A = True
                if (event.key == 'D' or 'd'):
                    press_D = True
                if (event.key == pygame.K_LEFT):
                    turn_left = True
                if (event.key == pygame.K_RIGHT):
                    turn_right = True
            elif (event.type == pygame.KEYUP):
                if (event.key == 'W' or 'w'):
                    press_W = False
                if event.key == 'S' or 's':
                    press_S = False
                if event.key == 'A' or 'a':
                    press_A = False
                if event.key == 'D' or 'd':
                    press_D = False
                if event.key == pygame.K_LEFT:
                    turn_left = False
                if event.key == pygame.K_RIGHT:
                    turn_right = False

        if (press_W):
            y -= 5   
        if (press_S):
            y += 5 
        if (press_A):
            x -= 5   
        if (press_D):
            x += 5    
        player.move(x, y)
        
        #player.turnLeft()   
        #player.turnRight()  
               
        
        player.draw(DISPLAYSURF)
        pygame.display.update()
        FPS.tick(30) 
       


def main():
    gameLoop()
    quit()
    exit()

if __name__=="__main__":
    main()