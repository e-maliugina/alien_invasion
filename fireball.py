"""Name: fireball.py
   Author: Elizaveta Maliugina
   Purpose: fireball class for the Milestone project
   Source: Classroom tutorials, OpenGameArt.org
   Date: 11/22/2026"""

import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from fire_vs_water import FireVsWater

class Fireball(Sprite):
    """Creates fireball class and manages fireball properties"""
    def __init__(self, game:"FireVsWater")->None:
        super().__init__()

        self.screen = game.screen
        self.settings = game.settings

        self.image = pygame.image.load(self.settings.fireball_file)
        self.image = pygame.transform.scale(self.image, (self.settings.fireball_w, self.settings.fireball_h))
        
        self.rect = self.image.get_rect()
        self.rect.midtop = game.flame.rect.midtop
        self.y = float(self.rect.y)

    def update(self)->None:
        self.y -= self.settings.fireball_speed
        self.rect.y = self.y

    def draw_fireball(self)->None:
        self.screen.blit(self.image, self.rect)