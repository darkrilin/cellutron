#!usr/bin/python
# Filename: cellular.py

import pygame

version = '0.0.1'

class Stage():
    class Agent():
        def __init__(self, initial_position = (0,0), initial_orientation = 0, costume = None):
            self.position = initial_orientation
            self.orientation = initial_orientation
            self.costume = costume

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