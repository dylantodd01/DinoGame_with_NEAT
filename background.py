"""
Class for the backdrop of the game, as well as 
the floor
"""

import pygame
import random
from settings import Settings
from dinosaur import Dinosaur

class Background:

    def __init__(self, screen):
        self.screen = screen
        self.dinosaur = Dinosaur(self.screen)

    def draw(self):
        self.draw_floor()

    def draw_floor(self):
        pygame.draw.rect(self.screen, Settings.FLOOR_COLOUR, pygame.Rect(0, 350, 1200, 50))

