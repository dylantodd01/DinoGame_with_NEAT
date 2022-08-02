"""
Class for the backdrop of the game, as well as 
the floor
"""

import pygame
from settings import Settings

class Background:

    def __init__(self, screen):
        self.screen = screen

    def draw_floor(self):
        pygame.draw.rect(self.screen, Settings.FLOOR_COLOUR, pygame.Rect(0, 350, 1200, 50))