"""
Bullet Class
Author: Bryson Rogers
Functions: initialize, move , draw, kill
"""

import pygame
import point
import cmath
import player

class Bullet():
    def __init__(self, x, y, dirX, dirY):
        self.x = x
        self.y = y
        self.dirX = x - dirX
        self.dirY = y - dirY
        self.count = 0
    # Change position
    def move(self):
        self.x += self.dirX
        self.y += self.dirY
        self.count += 1
    # draw function
    def draw(self, surface):
        pygame.draw.circle(surface, (255, 255, 255), (self.x,self.y), 2)
    # delete self
    def kill(self):
        del self
