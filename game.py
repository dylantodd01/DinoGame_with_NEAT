'''
Welcome to RUNNER

This is a very simple game...
'''

import pygame
import sys
import time
import os
import neat
import math

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
        # self.dinosaur = Dinosaur(self.screen)

        self.dinosaurs = []
        self.ge = []
        self.nets = []

        self.cacti = pygame.sprite.Group()
        self.cacti.add(Cactus(self.screen))

        self.score = Score()

        self.speed = Settings.SPEED
        self.frame_count = 0

        self.game_over = GameOver()

        self.info_text = Text(Settings.INFO_FONT, Settings.INFO_FONTSIZE, Settings.INFO_POS, "'q' to quit", Settings.INFO_COLOUR)

        self.running = True


    def play(self, genomes, config):
        
        for genome_id, genome in genomes:
            self.dinosaurs.append(Dinosaur(self.screen))
            self.ge.append(genome)
            net = neat.nn.FeedForwardNetwork.create(genome, config)
            self.nets.append(net)
            genome.fitness = 0

        # Game loop
        while self.running:
            self.check_events()
            self.update()
            
            self.frame_count += 1
            time.sleep(1/Settings.FPS)
        
        """
        while True:
            self.game_over.display(self.screen, self.score.value)
            self.check_events()
            pygame.display.update()
        """


    def check_events(self):
        #Check for user input or exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()

    def statistics(self):
        FONT = pygame.font.Font('freesansbold.ttf', 20)
        text_1 = FONT.render(f'Dinosaurs Alive:  {str(len(self.dinosaurs))}', True, (0, 0, 0))
        text_2 = FONT.render(f'Generation:  {pop.generation+1}', True, (0, 0, 0))
        text_3 = FONT.render(f'Game Speed:  {str(self.speed)}', True, (0, 0, 0))

        self.screen.blit(text_1, (50, 50))
        self.screen.blit(text_2, (50, 480))
        self.screen.blit(text_3, (50, 510))


    def update(self):
        self.screen.fill(Settings.BG_COLOUR)
        self.background.draw()

        self.cacti.update(self.speed)
        self.cacti.draw(self.screen)
        self.add_cactus()

        self.score.update(self.speed)
        self.score.draw(self.screen)

        self.info_text.draw(self.screen)


        for i, dinosaur in enumerate(self.dinosaurs):
            if self.check_collision(dinosaur, self.cacti):
                self.ge[i].fitness -= 1
                self.remove(i)

                if not self.dinosaurs:
                    self.running = False

        for i, dinosaur in enumerate(self.dinosaurs):
            output = self.nets[i].activate((dinosaur.rect.y,
                                       self.distance((dinosaur.rect.x, dinosaur.rect.y),
                                        self.get_next_cactus())))
            if output[0] > 0.5:
                dinosaur.jump()

            dinosaur.update()
            dinosaur.draw()

        if self.frame_count >= 1000:
            self.frame_count = 0
            self.speed *= Settings.SPEED_MULTIPLIER

        pygame.display.update()


    def add_cactus(self):
        if self.cacti.sprites()[-1].rect.x < Settings.CACTUS_SPAWN_X - Settings.CACTI_MIN_SPACING:
            self.cacti.add(Cactus(self.screen))

    def get_next_cactus(self):
        for cactus in self.cacti:
            if cactus.rect.x < 210:
                continue
            return cactus.rect.midtop

    def distance(self, pos_a, pos_b):
        dx = pos_a[0]-pos_b[0]
        dy = pos_a[1]-pos_b[1]
        return math.sqrt(dx**2+dy**2)

    def remove(self, index):
        self.dinosaurs.pop(index)
        self.ge.pop(index)
        self.nets.pop(index)

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollideany(sprite, group)

def eval_genomes(genomes, config):
    game = Game()
    game.play(genomes, config)


# Setup the NEAT Neural Network
def run(config_path):
    global pop
    config = neat.config.Config(
        neat.DefaultGenome,
        neat.DefaultReproduction,
        neat.DefaultSpeciesSet,
        neat.DefaultStagnation,
        config_path
    )

    pop = neat.Population(config)
    pop.run(eval_genomes, 50)


if __name__ == '__main__':
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config.txt')
    run(config_path)

"""
if __name__ == "__main__":
    game = Game()
    game.run()
"""