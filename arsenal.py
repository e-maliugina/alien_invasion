"""Name: arsenal.py
   Author: Elizaveta Maliugina
   Purpose: Arsenal class for the Milestone project
   Source: Classroom tutorials, OpenGameArt.org
   Date: 11/22/2026"""

import pygame
from fireball import Fireball
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from fire_vs_water import FireVsWater

class Arsenal:
    """Creates the arsenal class; manages fireballs"""
    def __init__(self, game: "FireVsWater"):
        self.game = game
        self.settings = game.settings
        self.arsenal = pygame.sprite.Group()

    def update_arsenal(self)->None:
        self.arsenal.update()
        self._remove_fireballs_offscreen()

    def _remove_fireballs_offscreen(self)->None:
        for fireball in self.arsenal.copy():
            if fireball.rect.bottom <= 0:
                self.arsenal.remove(fireball)

    def draw(self)->None:
        for fireball in self.arsenal:
            fireball.draw_fireball()

    def fire_fireball(self)->None:
        if len(self.arsenal) < self.settings.fireball_amount:
            new_fireball = Fireball(self.game)
            self.arsenal.add(new_fireball)
            return True
        return False