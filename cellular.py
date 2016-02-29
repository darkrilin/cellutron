#!usr/bin/python
# Filename: cellular.py

#import pygame
import math

version = '0.0.1'

class Stage():
    def __init__(self, columns, rows):
        """
        :param columns: integer - number of columns that the grid will have
        :param rows: integer - number of rows that the grid will have
        """
        self.columns = columns
        self.rows = rows
        self.cells = {}
        self.agents = []

        for row in range(self.columns):
            for column in range(self.rows):
                self.cells[(row,column)] = Cell()

    def _add_new_agent(self,agent):
        """
        :description: Adds an agent to the list of agents and places it inside of the appropriate cell
        :param agent: An agent object
        """
        if type(agent) == Agent:
            self.agents.append(agent)
            location = agent.position
            cell = self.cells[(location[0],location[1])]
            cell.agents.append(self)
        else:
            return TypeError

class Cell():
    def __init__(self, colour = (255, 255, 255)):
        """
        :param colour: a tuple containing three integer values between 0 and 255
        """
        self.colour = colour
        self.agents = []

class Agent():
    def __init__(self, stage, initial_position = None, initial_orientation = 'N', costume = None):
        """
        :param stage: the stage object
        :param initial_position: a list of two integers that willl be the co-ordinates
        :param initial_orientation: A compass direction in the form of a string. e.g. "N" or "SE"
        :param costume: A string that holds the path to an image to use as the agents display picture
        """
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
        """
        :desciption: moves the agent a provided number of steps in the direction it is facing
        :param steps: an integer number of steps to move forward
        """
        self.position[0] += self.ORIENTATION_COORDINATES[self.orientation][0]*steps
        self.position[1] += self.ORIENTATION_COORDINATES[self.orientation][0]*steps

    def rotate_clockwise(self, degrees):
        """
        :description: Rotates the the agent in a clockwise direction
        :param degrees: an integer that is a multiple of 45
        """
        assert degrees % 45 == 0; 'Can only turn in 45 degree increments!'
        angle = self.ORIENTATION_DEGREES[self.orientation]
        angle += degrees
        while angle > 360:
            angle -= 360
        while angle < 0:
            angle += 360
        self.orientation = self.ORIENTATION_DEGREES_REVERSE[angle]

    def rotate_anticlockwise(self, degrees):
        """
        :description: Rotates the agent in an anti-clockwise direction
        :param degrees: an integer that is a multiple of 45
        """
        assert degrees % 45 == 0; 'Can only turn in 45 degree increments!'
        angle = self.ORIENTATION_DEGREES[self.orientation]
        angle -= degrees
        while angle > 360:
            angle -= 360
        while angle < 0:
            angle += 360
        self.orientation = self.ORIENTATION_DEGREES_REVERSE[angle]

    def set_orientation(self, orientation):
        """
        :description: Sets the agents orientation to a specified direction
        :param orientation: A compass direction in the form of a string. e.g. "N" or "SE"
        """
        assert orientation in self.ORIENTATION_COORDINATES.keys(); 'Not a valid orientation!'
        self.orientation = orientation

    def point_towards_point(self,x,y):
        """
        :description: Sets the agents direction to be facing a set of co-ordinates (45 degree increments)
        :param x: x co-ordinate of focus (integer)
        :param y: y co-ordinate of focus (integer)
        """
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
        """
        :description: Sets the agents direction to be facing another agent
        :param agent: an agent object
        """
        self.point_towards_point(agent.position[0],agent.position[1])

    def set_position(self,new_position): #not checking if new co-ordinates are within the parameters yet ---> DO THIS
        """
        :description: Sets the agents position to a set of new co-ordinates
        :param new_position: a list of co-ordinates (integers)
        """
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
