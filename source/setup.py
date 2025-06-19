__author__ = 'half Vatsal Varshney'

import os
import pygame as pg
from . import constants as c
from .states import tools

pg.init()
pg.event.set_allowed([pg.KEYDOWN, pg.KEYUP, pg.QUIT])

# Set window caption
pg.display.set_caption(c.ORIGINAL_CAPTION)

# Set logo as window icon
logo = pg.image.load(os.path.join("resources", "graphics", "your_logo.png"))
pg.display.set_icon(logo)

# Set up display
SCREEN = pg.display.set_mode(c.SCREEN_SIZE)
SCREEN_RECT = SCREEN.get_rect()

# Load all game graphics
GFX = tools.load_all_gfx(os.path.join("resources", "graphics"))

# Show logo on screen briefly
logo_image = pg.image.load(os.path.join("resources", "graphics", "your_logo.png")).convert_alpha()
logo_rect = logo_image.get_rect(center=SCREEN_RECT.center)
SCREEN.blit(logo_image, logo_rect)
pg.display.update()
pg.time.wait(6000)
