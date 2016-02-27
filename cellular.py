#!usr/bin/python
# Filename: cellular.py

import pygame

version = '0.0.1'

def sayhi():
    print("Hello, this is cellular")

def init():
    pygame.init()

class display():
    def __init__():
        pass
    def create(swidth, sheight):
        pygame.display.set_mode((swidth, sheight), pygame.DOUBLEBUF)
    def draw():
        screen = pygame.display.get_surface()
        screen.fill((100, 100, 100))
        pygame.display.flip()

class time():
    def clock():
        