"""Name: fire.py
   Author: Elizaveta Maliugina
   Purpose: Fire class for the Milestone project
   Source: Classroom tutorials, OpenGameArt.org
   Date: 11/22/2026"""

import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from fire_vs_water import FireVsWater
    from arsenal import Arsenal

class Flame:
    """Creates and manages flame entities"""
    def __init__(self, game: "FireVsWater", arsenal: "Arsenal")->None:
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundaries = self.screen.get_rect()

        self.image = pygame.image.load(self.settings.flame_file)
        self.image = pygame.transform.scale(self.image, (self.settings.flame_w, self.settings.flame_h))

        self.rect = self.image.get_rect()
        self._center_flame()
        self.moving_right = False
        self.moving_left = False
        self.arsenal = arsenal

    def _center_flame(self):
        self.rect.midbottom = self.boundaries.midbottom
        self.x = float(self.rect.x)

    def update(self):
        self._update_flame_movement()
        self.arsenal.update_arsenal()

    def _update_flame_movement(self):
        #Updating position of the flame
        temp_speed = self.settings.flame_speed
        if self.moving_right and self.rect.right < self.boundaries.right:
            self.x += temp_speed
        if self.moving_left and self.rect.left > self.boundaries.left:
            self.x -= temp_speed

        self.rect.x = self.x

    def draw(self)->None:
        self.arsenal.draw()
        self.screen.blit(self.image, self.rect)

    def fire(self)->bool:
        return self.arsenal.fire_fireball()

    # def check_collisions(self, other_group):
    #     if pygame.sprite.spritecollideany(self, other_group):
    #         self._center_flame()
    #         return True
    #     return False
    