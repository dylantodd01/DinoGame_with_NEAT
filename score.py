"""
Scoring Class
"""

from settings import Settings
import pygame

class Score:

    def __init__(self):
        self.value = 0
        self.font = pygame.font.SysFont(Settings.SCORE_FONT, Settings.SCORE_FONTSIZE)

    def update(self, speed):
        self.value += (speed**3) * 0.001
        self.message = self.font.render(str(int(self.value)), True, Settings.SCORE_COLOUR)
        self.message_rect = self.message.get_rect(midright=Settings.SCORE_POS)

    def draw(self, screen):
        screen.blit(self.message, self.message_rect)