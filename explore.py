import pygame
from pygame.locals import *
import player
import bullet
import enemy
import math
pygame.init()
pygame.font.init()

myfont = pygame.font.SysFont('Comic Sans MS', 30)

height = 720
width = 1080
DISPLAYSURF = pygame.display.set_mode((width,height))
black = pygame.Color(0, 0, 0)         # Black
white = pygame.Color(255, 255, 255)   # White
grey = pygame.Color(128, 128, 128)   # Grey
red = pygame.Color(255, 0, 0)       # Red
FPS = pygame.time.Clock()

player = player.Player(540, 360)

enemyO = enemy.Enemy(-50, 50)
enemyT = enemy.Enemy(1000, 740)

enemies = [enemyO, enemyT]

def nextRound(Round, enemies):
    Round += 1 
    r = 0               #calls memory error in this function
    while (r < Round):
        xO = 1 + r * 2
        yO = -50
        enemies.append(enemy.Enemy(xO, yO))
        xT = width + 50
        yT = 1 + r
        enemies.append(enemy.Enemy(xT, yT))
        xH = -50
        yH = height - r * 2 
        enemies.append(enemy.Enemy(xH, yH))
        xF = width - r * 2
        yF =  height + 50
        enemies.append(enemy.Enemy(xF, yF))


#game loop
def gameLoop():
    
    
    game = True
    press_W = False
    press_S = False
    press_A = False
    press_D = False
    press_left = False
    press_right = False
    press_up = False
    delay = False
    Round = 1
    score = 0

    bullets = []
    

    


    
    while game:
        x = 0
        y = 0
        scoreTxt = myfont.render('Score: ', False, grey)
        scoreNum = myfont.render((str(score)) , False, grey)
        roundTxt = myfont.render('Round: ', False, grey)
        roundNum = myfont.render((str(Round)) , False, grey)
        for event in pygame.event.get():
            if (event.type == pygame.QUIT): # Quit is esc or x in the corner
                game = False 
            #elif (event.type == pygame.KEYDOWN):
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
            


        if (press_W):
            y -= 3  
        elif (press_S):
            y += 3
        if (press_A):
            x -= 3   
        elif (press_D):
            x += 3   
        player.move(x, y)
        if (press_left):
            player.turnLeft() 
        elif (press_right):  
            player.turnRight() 
        if (press_up) and player.health != 0:
            bullets.append(bullet.Bullet(player.oriX, player.oriY, player.locX, player.locY)) 

        if len(bullets) > 0:
            for x in range(len(bullets)):
                bullets[x].move()
                if (bullets[x].count > 60):
                    remove = bullets[x]
                    del bullets[x]
                    remove.kill()
                    break

        if player.collision(enemies):
            player.health = 0

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
        elif (len(enemies) < 1):
            nextRound(Round, enemies)

        

        DISPLAYSURF.fill(black)
        DISPLAYSURF.blit(scoreTxt,(5,5))
        DISPLAYSURF.blit(scoreNum,(100,5))
        DISPLAYSURF.blit(roundTxt,(5,55))
        DISPLAYSURF.blit(roundNum,(100,55))
        if len(bullets) > 0:
            for x in range(len(bullets)):
                bullets[x].draw(DISPLAYSURF)
        if len(enemies) > 0:
            for x in range(len(enemies)):
                enemies[x].draw(DISPLAYSURF)
        player.draw(DISPLAYSURF)
        pygame.display.update()
        FPS.tick(45) 
       


def main():
    gameLoop()
    quit()
    exit()

if __name__=="__main__":
    main()