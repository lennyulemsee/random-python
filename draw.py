#!/usr/bin/python3

import matplotlib.pyplot as plt
matplotlib inline

class Circle(object):
    """ A Circle class. """
    def __init__(self, radius, color):
        self.radius = radius;
        self.color = color;

    def add_radius(self, r):
        self.radius = self.radius + r
        return (self.radius)
    
    def drawCircle(self):
        plt.gca().add_patch(plt.Circle((0,0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show()

redCircle = Circle(5, 'yellow')
redCircle.drawCircle()
