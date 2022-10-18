"""
Class for the running character
"""

import pygame
from settings import Settings

class Dinosaur(pygame.sprite.Sprite):

    def __init__(self, screen):
        super().__init__()
        self.dinoA = pygame.image.load(Settings.IMAGE_PATH + "dinosaurA.png")
        self.dinoB = pygame.image.load(Settings.IMAGE_PATH + "dinosaurB.png")
        self.dino_jumping = pygame.image.load(Settings.IMAGE_PATH + "dinosaurJumping.png")
        self.animation_counter = 0
        self.image = self.dinoA
        self.rect = self.image.get_rect().inflate(-25, -4)
        self.screen = screen
        self.rect.x, self.rect.y = Settings.DINO_X, Settings.DINO_Y
        self.y_vel = 0
        self.jumping = False


    def draw(self):
        self.screen.blit(self.image, self.rect)

    def switch_image(self):
        if self.image == self.dinoA:
            self.image = self.dinoB
        else:
            self.image = self.dinoA

    def update(self):
        self.update_animation()
        self.update_y()

    def update_animation(self):
        # Update dinosaur animation
        self.animation_counter += 1

        if self.jumping:
            self.image = self.dino_jumping
            return

        if self.animation_counter >= (Settings.FPS / Settings.ANIMATION_FPS):
            self.switch_image()
            self.animation_counter = 0

    def update_y(self):
        # Update dinosaur position when jumping
        if self.rect.y >= Settings.DINO_Y:
            return
        self.y_vel += Settings.GRAV_CONST
        self.rect.y += self.y_vel
        if self.rect.y > Settings.DINO_Y:
            self.rect.y = Settings.DINO_Y
            self.y_vel = 0
            self.jumping = False
    
    def jump(self):
        # Dinosaur is not allowed to jump if in the air
        if self.rect.y != Settings.DINO_Y:
            return
        self.y_vel = Settings.JUMP_VEL
        self.jumping = True
        self.rect.y -= 1

        
        


