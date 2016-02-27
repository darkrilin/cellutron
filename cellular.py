#!usr/bin/python
# Filename: cellular.py

#import pygame
import math

version = '0.0.1'

class Stage():
    def __init__(self, columns, rows):
        self.columns = columns
        self.rows = rows
        self.cells = {}
        self.agents = []

        for row in range(self.columns):
            for column in range(self.rows):
                self.cells[(row,column)] = Cell()

    def _add_new_agent(self,agent):
        if type(agent) == Agent:
            self.agents.append(agent)
            location = agent.position
            cell = self.cells[(location[0],location[1])]
            cell.agents.append(self)
        else:
            return TypeError

class Cell():
    def __init__(self, colour = (255, 255, 255)):
        self.colour = colour
        self.agents = []

class Agent():
    def __init__(self, stage, initial_position = None, initial_orientation = 'N', costume = None):
        if initial_position is None:
            self.position = [0,0]
        else:
            if type(initial_position) == list:
                self.position = initial_position
            else:
                return TypeError
        self.orientation = initial_orientation
        self.costume = costume
        self.orientation_dict = {'N':[0,-1], 'NE':[1,-1,], 'E':[1,0], 'SE':[1,1], 'S':[1,0], 'SW':[1,-1], 'W':[0,-1], 'NW':[-1,-1]}
        stage._add_new_agent(self)

    def move_steps_forward(self,steps):
        self.position[0] += self.orientation_dict[self.orientation][0]*steps
        self.position[1] += self.orientation_dict[self.orientation][0]*steps


# PUT ALL THE CLASSY CODE HERE
if __name__ =="__main__":
    my_stage = Stage(4,6)
    my_agent_1 = Agent(my_stage,[2,4])
