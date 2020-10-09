import pygame

class Point():
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def addX(self, x):
        self.x += x

    def addY(self, y):
        self.y += y

    def getPoint(self):
        return self

    def setPoint(self, point):
        self.x = point.getX()
        self.y = point.getY()
