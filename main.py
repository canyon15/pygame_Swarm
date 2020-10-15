"""
Author: Bryson Rogers
Functions: main, game loop, and next round
"""

import pygame
from pygame.locals import *
import player
import bullet
import enemy
import math
pygame.init()
pygame.font.init()
# for score board
myfont = pygame.font.SysFont('Comic Sans MS', 30)
# screen dimensions
height = 720
width = 1080
# set display surface
DISPLAYSURF = pygame.display.set_mode((width,height))
#preset colors
black = pygame.Color(0, 0, 0)         # Black
white = pygame.Color(255, 255, 255)   # White
grey = pygame.Color(128, 128, 128)   # Grey
red = pygame.Color(255, 0, 0)       # Red
# for screen refresh rate
FPS = pygame.time.Clock()
# initialize player
player = player.Player(540, 360)
# initialize first two enemies
enemyO = enemy.Enemy(-50, 50)
enemyT = enemy.Enemy(1000, 740)

enemies = [enemyO, enemyT]
# a Round function so increasing 
# numbers of enemies come in waves.
def nextRound(Round, enemies): 
    r = 0               
    while (r < Round):
        xO = 1 + r * 5
        yO = -50 - r
        enemies.append(enemy.Enemy(xO, yO))
        xT = width + 50 + r
        yT = 1 + r * 5
        enemies.append(enemy.Enemy(xT, yT))
        xH = -50 - r
        yH = height - r * 5 
        enemies.append(enemy.Enemy(xH, yH))
        xF = width - r * 5
        yF =  height + 50 + r
        enemies.append(enemy.Enemy(xF, yF))
        r += 1


#game loop function
def gameLoop():
    
    # initialize exit condition
    game = True
    # user inputs
    press_W = False
    press_S = False
    press_A = False
    press_D = False
    press_left = False
    press_right = False
    press_up = False
    # Variables for display
    Round = 1
    score = 0
    # List of bullet instances
    bullets = []
    

    


    # game loop
    while game:
        # resets movement inputs so player stops when there is no input.
        x = 0
        y = 0
        # variables to be drawn on display
        scoreTxt = myfont.render('Score: ', False, grey)
        scoreNum = myfont.render((str(score)) , False, grey)
        roundTxt = myfont.render('Round: ', False, grey)
        roundNum = myfont.render((str(Round)) , False, grey)
        # Collects user inputs and exit condition.
        for event in pygame.event.get():
            if (event.type == pygame.QUIT): # exit condition / X button in corner 
                game = False 
            # Checks for key presses from 'W' 'A' 'S' 'D' and arrow keys.
            elif ((event.type == pygame.KEYDOWN) and (event.key == pygame.K_w)):
                press_W = True
            elif ((event.type == pygame.KEYUP) and (event.key == pygame.K_w)):
                press_W = False
            elif ((event.type == pygame.KEYDOWN) and (event.key == pygame.K_s)):
                press_S = True
            elif ((event.type == pygame.KEYUP) and (event.key == pygame.K_s)):
                press_S = False
            elif ((event.type == pygame.KEYDOWN) and (event.key == pygame.K_a)):
                press_A = True
            elif ((event.type == pygame.KEYUP) and (event.key == pygame.K_a)):
                press_A = False
            elif ((event.type == pygame.KEYDOWN) and (event.key == pygame.K_d)):
                press_D = True
            elif ((event.type == pygame.KEYUP) and (event.key == pygame.K_d)):
                press_D = False
            elif ((event.type == pygame.KEYDOWN) and (event.key == pygame.K_LEFT)):
                press_left = True
            elif ((event.type == pygame.KEYUP) and (event.key == pygame.K_LEFT)):
                press_left = False
            elif ((event.type == pygame.KEYDOWN) and (event.key == pygame.K_RIGHT)):
                press_right = True
            elif ((event.type == pygame.KEYUP) and (event.key == pygame.K_RIGHT)):
                press_right = False
            elif ((event.type == pygame.KEYDOWN) and (event.key == pygame.K_UP)):
                press_up = True
            elif ((event.type == pygame.KEYUP) and (event.key == pygame.K_UP)):
                press_up = False
            

        # These inputs change player location
        if (press_W):
            y -= 3  
        elif (press_S):
            y += 3
        if (press_A):
            x -= 3   
        elif (press_D):
            x += 3   
        player.move(x, y)
        
        # These inputs rotate the player.
        if (press_left):
            player.turnLeft() 
        elif (press_right):  
            player.turnRight() 
        # Up arrow fires bullets. (because the spacebar felt to awkward)
        if (press_up) and player.health != 0:
            bullets.append(bullet.Bullet(player.oriX, player.oriY, player.locX, player.locY)) 
        # Delete bullets after they have moved 60 times 
        if len(bullets) > 0:
            for x in range(len(bullets)):
                bullets[x].move()
                if (bullets[x].count > 60):
                    remove = bullets[x]
                    del bullets[x]
                    remove.kill()
                    break
        # Stop inputs if player dies.
        if player.collision(enemies):
            player.health = 0
        # If bullets hit enemies, enemies die.
        if (len(enemies) > 0):
            for x in range(len(enemies)):
                enemies[x].move(player.locX, player.locY)
            for x in range(len(enemies)):
                for b in range(len(bullets)):
                    if (math.sqrt((abs(bullets[b].x - enemies[x].x)**2) + abs(bullets[b].y - enemies[x].y)**2) < 10):
                        score += 1
                        remove = enemies[x]
                        del enemies[x]
                        remove.kill()
                        break
                break
        # If all the enemies are dead increase 
        # round by 1 and add more enemies.
        elif (len(enemies) < 1):
            nextRound(Round, enemies)
            Round += 1

        
        # Draw everything.
        DISPLAYSURF.fill(black) # Draw new background
        DISPLAYSURF.blit(scoreTxt,(5,5)) # Draw score
        DISPLAYSURF.blit(scoreNum,(100,5))
        DISPLAYSURF.blit(roundTxt,(5,55)) # Draw round
        DISPLAYSURF.blit(roundNum,(100,55))
        if len(bullets) > 0:        # Draw all the bullets.
            for x in range(len(bullets)):
                bullets[x].draw(DISPLAYSURF)
        if len(enemies) > 0:        # Draw all the enemies.
            for x in range(len(enemies)):
                enemies[x].draw(DISPLAYSURF)
        player.draw(DISPLAYSURF)    # Draw the player.
        pygame.display.update()
        FPS.tick(45)                # Refresh rate.
       

# main
def main():
    gameLoop() # gameloop
    quit()      # pygame close
    exit()      #system close

if __name__=="__main__":
    main()