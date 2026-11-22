"""Name: arsenal.py
   Author: Elizaveta Maliugina
   Purpose: Arsenal class for the Milestone project
   Source: Classroom tutorials
   Date: 11/22/2026"""

import pygame
from bullet import Bullet
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from fire_vs_water import FireVsWater

class Arsenal:
    """Creates the arsenal class; manages bullets"""
    def __init__(self, game: "FireVsWater"):
        self.game = game
        self.settings = game.settings
        self.arsenal = pygame.sprite.Group()

    def update_arsenal(self)->None:
        self.arsenal.update()
        self._remove_bullets_offscreen()

    def _remove_bullets_offscreen(self)->None:
        for bullet in self.arsenal.copy():
            if bullet.rect.bottom <= 0:
                self.arsenal.remove(bullet)

    def draw(self)->None:
        for bullet in self.arsenal:
            bullet.draw_bullet()

    def fire_bullet(self)->None:
        if len(self.arsenal) < self.settings.bullet_amount:
            new_bullet = Bullet(self.game)
            self.arsenal.add(new_bullet)
            return True
        return False