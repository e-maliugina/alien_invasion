"""Name: settings.py
   Author: Elizaveta Maliugina
   Purpose: Settings for the Alien Invasion project
   Source: Classroom tutorials
   Date: 10/19/2026"""
from pathlib import Path

class Settings:
    """Created Seetings class that is used to control things like the screen in the main game."""
    def __init__(self)->None:
        self.name: str = "Alien Invasion"
        self.screen_w = 1200
        self.screen_h = 800
        self.FPS = 60
        self.bg_file = Path.cwd() / "Assets" / "images" / "Starbasesnow.png"