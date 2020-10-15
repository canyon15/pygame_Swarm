"""
Enemy Class
Author: Bryson Rogers
Functions: initialize, move , draw, kill
"""
import pygame
import point
import cmath
import bullet


class Enemy():
    # loc for location and ori for orientation
    def __init__(self, x, y):
        self.radius = 10
        self.x = x
        self.y = y
        self.health = 10

    # draw function
    def draw(self, surface):
        #print ("x ori = ", self.oriX, "y ori = ", self.oriY)
        pygame.draw.circle(surface, (255, 0, 0), (self.x,self.y), self.radius)
    # change location
    def move(self, playerX, playerY):
        if (abs(self.x - playerX) >=  abs(self.y - playerY)):
            if self.x > playerX:
                self.x -= 1
            elif self.x < playerX:
                self.x += 1
        else:
            if self.y > playerY:
                self.y -= 1
            elif self.y < playerY:
                self.y += 1
            
    # delete self
    def kill(self):
        del self
    
    
       

    