import pygame
import point
import cmath
import player

speed = 5

class Bullet():
    def __init__(self, x, y, dirX, dirY):
        self.x = x
        self.y = y
        self.dirX = x - dirX
        self.dirY = y - dirY
        self.count = 0

    def move(self):
        self.x += self.dirX
        self.y += self.dirY
        self.count += 1
        #if (self.count >= 120):
         #   self.kill()

        
    
    def draw(self, surface):
        pygame.draw.circle(surface, (255, 255, 255), (self.x,self.y), 2)


    
    def kill(self):
        del self
