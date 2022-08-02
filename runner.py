'''
Welcome to RUNNER

This is a very simple game...
'''

import pygame
import sys
import time

from settings import Settings
from background import Background

class Runner:
    
    def __init__(self):

        pygame.init()

        self.screen = pygame.display.set_mode((Settings.SCREEN_WIDTH, Settings.SCREEN_HEIGHT))
        pygame.display.set_caption(Settings.CAPTION)

        self.background = Background(self.screen)


    def run(self):
        # Game loop
        while True:
            self.check_events()
            self.update()
            
            time.sleep(1/Settings.FPS)


    def check_events(self):
        #Check for user input or exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


    def update(self):
        self.screen.fill(Settings.BG_COLOUR)
        self.background.draw_floor()

        pygame.display.update()


runner = Runner()
runner.run()