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
        """Initializes game reference, settings, and the arsenal"""
        self.game = game
        self.settings = game.settings
        self.arsenal = pygame.sprite.Group()

    def update_arsenal(self)->None:
        """Updates the arsenal"""
        self.arsenal.update()
        self._remove_fireballs_offscreen()

    def _remove_fireballs_offscreen(self)->None:
        """Removes the fireballs off the screen"""
        for fireball in self.arsenal.copy():
            if fireball.rect.bottom <= 0:
                self.arsenal.remove(fireball)

    def draw(self)->None:
        """Draws the fireballs if they are available"""
        for fireball in self.arsenal:
            fireball.draw_fireball()

    def fire_fireball(self)->None:
        """Checks if fireballs are available, add an instance if yes and returns True, false if not"""
        if len(self.arsenal) < self.settings.fireball_amount:
            new_fireball = Fireball(self.game)
            self.arsenal.add(new_fireball)
            return True
        return False