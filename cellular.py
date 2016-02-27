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
                raise TypeError
        self.orientation = initial_orientation
        self.costume = costume
        stage._add_new_agent(self)
        self.ORIENTATION_COORDINATES = {'N':[0,-1], 'NE':[1,-1,], 'E':[1,0], 'SE':[1,1], 'S':[1,0], 'SW':[1,-1], 'W':[0,-1], 'NW':[-1,-1]}
        self.ORIENTATION_DEGREES = {'N':90, 'NE':45, 'E':0, 'SE':315, 'S':270, 'SW':225, 'W':180, 'NW':135}
        self.ORIENTATION_DEGREES_REVERSE = {90:'N', 45:'NE', 0:'E', 315:'SE', 270:'S', 225:'SW', 180:'W', 135:'NW', 360:'E'}

    def move_steps_forward(self,steps):
        self.position[0] += self.ORIENTATION_COORDINATES[self.orientation][0]*steps
        self.position[1] += self.ORIENTATION_COORDINATES[self.orientation][0]*steps

    def rotate_clockwise(self, degrees):
        assert degrees % 45 == 0; 'Can only turn in 45 degree increments!'
        angle = self.ORIENTATION_DEGREES[self.orientation]
        angle += degrees
        while angle > 360:
            angle -= 360
        while angle < 0:
            angle += 360
        self.orientation = self.ORIENTATION_DEGREES_REVERSE[angle]

    def rotate_anticlockwise(self, degrees):
        assert degrees % 45 == 0; 'Can only turn in 45 degree increments!'
        angle = self.ORIENTATION_DEGREES[self.orientation]
        angle -= degrees
        while angle > 360:
            angle -= 360
        while angle < 0:
            angle += 360
        self.orientation = self.ORIENTATION_DEGREES_REVERSE[angle]

    def set_orientation(self, orientation):
        assert orientation in self.ORIENTATION_COORDINATES.keys(); 'Not a valid orientation!'
        self.orientation = orientation

    def point_towards_point(self,x,y):
        if y == self.position[1]:
            if x > self.position[x]:
                self.orientation = 'S'
                return self.orientation
            else:
                self.orientation = 'N'
                return self.orientation
        angle = math.degrees(math.tan(float(self.position[1] - y)/float(x - self.position[0])))
        angle = int(angle/45)*45
        while angle > 360:
            angle -= 360
        while angle < 0:
            angle += 360
        self.orientation = self.ORIENTATION_DEGREES_REVERSE[angle]
        return self.orientation

    def point_towards_agent(self, agent):
        self.point_towards_point(agent.position[0],agent.position[1])

    def set_position(self,new_position): #not checking if new co-ordinates are within the parameters yet ---> DO THIS
        if type(new_position) == list and len(new_position) == 2:
            old_cell = self.stage.cells[(self.position[0],self.position[1])]
            new_cell = self.stage.cells[(new_position[0],new_position[1])]
            for i in old_cell.agents:
                if i == self:
                    index = old_cell.index(i)
                    old_cell.pop(index)
            new_cell.agents.append(self)
            return True
        else:
            raise TypeError
        
# PUT ALL THE CLASSY CODE HERE
if __name__ =="__main__":
    my_stage = Stage(4,6)
    my_agent_1 = Agent(my_stage,[2,4])
