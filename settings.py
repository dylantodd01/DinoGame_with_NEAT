"""
Settings Class
"""

import os

class Settings:

    # General settings
    SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 400
    CAPTION = "RUNNER"
    BG_COLOUR = (255, 255, 255)
    FPS = 50
    FLOOR_COLOUR = (0, 0, 0)
    SPEED = 10
    SPEED_MULTIPLIER = 1.1
    IMAGE_PATH = os.path.dirname(__file__) + '/images/'

    # Dinosaur settings
    DINO_Y = 257
    DINO_X = 200
    JUMP_VEL = -28  # Negative due to inverted coordinate system
    GRAV_CONST = 2
    ANIMATION_FPS = 8

    # Cactus settings
    CACTUS_Y = 280
    CACTUS_SPAWN_X = SCREEN_WIDTH + 100
    NUM_CACTI = 3
    CACTI_MIN_SPACING = 300
    CACTI_MAX_SPACING = 800

    # Score settings
    SCORE_FONT = "bahnschrift"
    SCORE_FONTSIZE = 50
    SCORE_POS = (1190, 20)
    SCORE_COLOUR = (0, 0, 0)

    # Game over settings
    GAMEOVER_FONT = "bahnschrift"
    GAMEOVER_FONTSIZE = 150
    GAMEOVER_POS = (600, 150)
    GAMEOVER_COLOUR = (0, 0, 0)

    # Info text settings
    INFO_FONT = "bahnschrift"
    INFO_FONTSIZE = 30
    INFO_POS = (5, 20)
    INFO_COLOUR = (0, 0, 0)
