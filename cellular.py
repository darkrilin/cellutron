#!usr/bin/python
# Filename: cellular.py

import pygame
import math

version = '0.0.1'

def sayhi():
    print("Hello, this is cellular")

class Stage():
    class Agent():
        def __init__(self, initial_position = (0,0), initial_orientation = 'N', costume = None):
            self.position = initial_orientation
            self.orientation = initial_orientation
            self.costume = costume
            self.orientation_dict = {'N':(0,-1), 'NE':(1,-1,), 'E':(1,0), 'SE':(1,1), 'S':(1,0), 'SW':(1,-1), 'W':(0,-1), 'NW':(-1,-1)}

        def move_steps_forward(self,steps):
            self.position[0] += self.orientation_dict[self.orientation][0]*steps
            self.position[0] += self.orientation_dict[self.orientation][0]*steps

    class Cell():
        def __init__(self, colour = (255, 255, 255)):
            self.colour = colour

    def __init__(self, columns, rows):
        self.columns = columns
        self.rows = rows
        self.cells = {}

        for row in range(self.rows):
            for column in range(self.colours):
                self.cells[(row,column)] = self.Cell()




# PUT ALL THE CLASSY CODE HERE
        