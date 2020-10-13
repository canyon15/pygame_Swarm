import pygame
import point
import math
import bullet


class Player():
    # loc for location and ori for orientation
    def __init__(self, lx, ly):
        self.radius = 10
        self.length = 16
        self.locX = lx
        self.locY = ly
        self.oriX = lx
        self.oriY = ly - 16
        self.oxp = 26
        self.oyp = 0
        self.health = 10
        self.angle = [-16,-16,-16,-15,-15,-15,-14,-14,-13,-13,-12,-12,-11,-10,-9,-9,-8,-8,-7,-6,-5,-4,-3,-2,-1, #0 - 25
            0,1,2,3,4,5,6,7,8,8,9,9,10,11,12,12,13,13,14,14,15,15,15,16,16,16, #26 - 51
            16,16,15,15,15,14,14,13,13,12,12,11,10,9,9,8,8,7,6,5,4,3,2,1,0, #52 - 76
            -1,-2,-3,-4,-5,-6,-7,-8,-8,-9,-9,-10,-11,-12,-12,-13,-13,-14,-14,-15,-15,-15,-16,-16, -16] # 77 - 100

        
    def draw(self, surface):
        #print ("x ori = ", self.oriX, "y ori = ", self.oriY)
        if self.health != 0:
            pygame.draw.circle(surface, (255, 255, 255), (self.locX,self.locY), self.radius)
            pygame.draw.line(surface, (255, 255, 255), (self.locX, self.locY), (self.oriX, self.oriY), 3)
        
    def move(self, x, y):
        if self.health != 0:
            self.locX += x
            self.locY += y
            self.oriX += x
            self.oriY += y
    
    def turnLeft(self):
        if (self.oyp == 0):
            self.oyp = 100
            self.oxp = 25
        elif (self.oxp == 0):
            self.oxp = 100
            self.oyp = 74
        else:
            self.oyp -= 1
            self.oxp -= 1

        self.oriX = self.locX + self.angle[(self.oxp)]
        self.oriY = self.locY + self.angle[(self.oyp)]
       

    def turnRight(self):
        if (self.oyp == 100):
            self.oyp = 0
            self.oxp = 26
        elif (self.oxp == 100):
            self.oxp = 0
            self.oyp = 75
        else:
            self.oyp += 1
            self.oxp += 1
        
        self.oriX = self.locX + self.angle[(self.oxp)]
        self.oriY = self.locY + self.angle[(self.oyp)]

    def collision(self, enemies):
        for e in range(len(enemies)):
            if (math.sqrt((abs(self.locX - enemies[e].x)**2) + abs(self.locY - enemies[e].y)**2) < self.radius):
                return True

    def kill(self):
        del self
"""
    def shoot(self):
        bullet = type(bullet.Bullet(self.oriX, self.oriY, self.locX, self.locY))
        return bullet
"""


"""
    def getLoc(self):
        return self.loc

    def setLoc(self, point):
        self.loc.setPoint(point)

    def getOri(self):
        return self.ori

    def setOri(self, point):
        self.ori.setPoint(point)
    """
        
    #def __del__(self):
        