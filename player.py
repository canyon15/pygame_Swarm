import pygame
import point
import cmath


class Player():
    # loc for location and ori for orientation
    def __init__(self, lx, ly, ox, oy):
        self.radius = 10
        self.length = 15
        self.locX = lx
        self.locY = ly
        self.oriX = ox
        self.oriY = oy
        self.health = 10
        self.shoot = False
        
    def draw(self, surface):
        pygame.draw.circle(surface, (255, 255, 255), (self.locX,self.locY), self.radius)
        pygame.draw.line(surface, (255, 255, 255), (self.locX, self.locY), (self.oriX, self.oriY), 3)
        
    def move(self, x, y):
        self.locX += x
        self.locY += y
        self.oriX += x
        self.oriY += y
"""
    def getLoc(self):
        return self.loc

    def setLoc(self, point):
        self.loc.setPoint(point)

    def getOri(self):
        return self.ori

    def setOri(self, point):
        self.ori.setPoint(point)
        

    def turnLeft(self):
        l = self.ori.getY()
        if (l >= 0):
            self.ori.addX(-1)
            self.ori.setY(cmath.sqrt(self.length**2 - (self.ori.getX())**2))

    def turnRight(self):
        r = self.ori.getY()
        if (r >= 0):
            self.ori.addX(-1)
            self.ori.setY(cmath.sqrt(self.length**2 - (self.ori.getX())**2))
"""
    

    
  

    
        