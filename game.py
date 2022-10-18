'''
Welcome to RUNNER

This is a very simple game...
'''

import pygame
import sys
import time

from settings import Settings
from background import Background
from dinosaur import Dinosaur
from cactus import Cactus
from score import Score
from gameOver import GameOver
from text import Text

class Game:
    
    def __init__(self):

        pygame.init()

        self.screen = pygame.display.set_mode((Settings.SCREEN_WIDTH, Settings.SCREEN_HEIGHT))
        pygame.display.set_caption(Settings.CAPTION)

        self.background = Background(self.screen)
        self.dinosaur = Dinosaur(self.screen)

        self.cacti = pygame.sprite.Group()
        self.cacti.add(Cactus(self.screen))

        self.score = Score()

        self.speed = Settings.SPEED
        self.frame_count = 0

        self.game_over = GameOver()

        self.info_text = Text(Settings.INFO_FONT, Settings.INFO_FONTSIZE, Settings.INFO_POS, "'q' to quit", Settings.INFO_COLOUR)

        self.running = True


    def run(self):
        # Game loop
        while self.running:
            self.check_events()
            self.update()
            
            self.frame_count += 1
            time.sleep(1/Settings.FPS)
        
        while True:
            self.game_over.display(self.screen, self.score.value)
            self.check_events()
            pygame.display.update()


    def check_events(self):
        #Check for user input or exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
                if event.key == pygame.K_SPACE:
                    self.dinosaur.jump()


    def update(self):
        self.screen.fill(Settings.BG_COLOUR)
        self.background.draw()

        self.cacti.update(self.speed)
        self.cacti.draw(self.screen)
        self.add_cactus()

        self.dinosaur.update()
        self.dinosaur.draw()

        self.score.update(self.speed)
        self.score.draw(self.screen)

        self.info_text.draw(self.screen)
        
        pygame.display.update()

        if self.check_collision(self.dinosaur, self.cacti):
            time.sleep(0.2)
            self.running = False

        if self.frame_count >= 1000:
            self.frame_count = 0
            self.speed *= Settings.SPEED_MULTIPLIER


    def add_cactus(self):
        if self.cacti.sprites()[-1].rect.x < Settings.CACTUS_SPAWN_X - Settings.CACTI_MIN_SPACING:
            self.cacti.add(Cactus(self.screen))

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollideany(sprite, group)

if __name__ == "__main__":
    game = Game()
    game.run()