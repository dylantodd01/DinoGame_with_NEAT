

import pygame
import random
from settings import Settings

class Cactus(pygame.sprite.Sprite):

    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load(Settings.IMAGE_PATH + "cactus.png")
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(Settings.CACTUS_SPAWN_X, Settings.CACTUS_SPAWN_X + Settings.CACTI_MAX_SPACING)
        self.rect.y = Settings.CACTUS_Y

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def update(self, speed):
        self.rect.x -= speed
        if self.rect.x < -100:
                self.kill()
