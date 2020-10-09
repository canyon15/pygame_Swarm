import pygame
import point
import cmath


class Player():
    # loc for location and ori for orientation
    def __init__(self):
        self.radius = 10
        self.length = 15
        self.locX = 540
        self.locY = 360 
        self.oriX = 
        self.health = 10
        self.shoot = False
        
    def draw(self, surface):
        pygame.draw.circle(surface, (255, 255, 255), (self.loc.getX(),self.loc.getY()), self.radius)
        pygame.draw.line(surface, (255, 255, 255), (self.loc.getX(),self.loc.getY()), (self.ori.getX(),self.ori.getY()), 3)

    def getLoc(self):
        return self.loc

    def setLoc(self, point):
        self.loc.setPoint(point)

    def getOri(self):
        return self.ori

    def setOri(self, point):
        self.ori.setPoint(point)
        """

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
    def move(self, x, y):
        self.loc.addX(x)
        self.loc.addY(y)
        self.ori.addX(x)
        self.ori.addY(y)

    