
from settings import Settings
import pygame

class GameOver:
    
    def __init__(self):
        self.font = pygame.font.SysFont(Settings.GAMEOVER_FONT, Settings.GAMEOVER_FONTSIZE)


    def display(self, screen, score):
        self.message = self.font.render(str(int(score)), True, Settings.GAMEOVER_COLOUR)
        self.message_rect = self.message.get_rect(center=Settings.GAMEOVER_POS)
        screen.blit(self.message, self.message_rect)

