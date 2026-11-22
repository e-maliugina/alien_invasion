"""Name: settings.py
   Author: Elizaveta Maliugina
   Purpose: Settings for the Milestone project
   Source: Classroom tutorials
   Date: 11/19/2026"""
from pathlib import Path

class Settings:
    """Created Settings class that is used to control things like the screen in the main game."""
    def __init__(self)->None:
        self.name: str = "Fire vs Water"
        self.screen_w = 1200
        self.screen_h = 800
        self.FPS = 60
        self.bg_file = Path.cwd() / "Assets" / "images" / "ocean_background.png"
        #self.difficulty_scale = 1.1
        #self.scores_file = Path.cwd() / "Assets" / "file" / "scores.json"

        self.ship_file = Path.cwd() / "Assets" / "images" / "flames.png"
        self.ship_w = 80
        self.ship_h = 100

        self.bullet_file = Path.cwd() / "Assets" / "images" / "fireball.png"
        self.laser_sound = Path.cwd() / "Assets" / "sound" / "foom_0.wav"
        #self.impact_sound = Path.cwd() / "Assets" / "sound" / "impactSound.mp3"
       

        # self.alien_file = Path.cwd() / "Assets" / "images" / "enemy_4.png"
        # self.alien_w = 40
        # self.alien_h = 40
        # self.fleet_direction = 1

        # self.button_w = 200
        # self.button_h = 50
        # self.button_color = (0,135,50)

        # self.text_color = (255,255,255)
        # self.button_font_size = 48
        # self.HUD_font_size = 20
        # self.font_file = Path.cwd() / "Assets" / "Fonts" / "Silkscreen" / "Silkscreen-Bold.ttf"

    def initialize_dynamic_settings(self)->None:
        self.ship_speed = 15
        #self.starting_ship_count = 3

        self.bullet_w = 28
        self.bullet_h = 80
        self.bullet_speed = 20
        self.bullet_amount = 5

        # self.fleet_speed = 4
        # self.fleet_drop_speed = 40
        # self.alien_points = 50

    # def increase_difficulty(self)->None:
    #     self.ship_speed *= self.difficulty_scale
    #     self.bullet_speed *= self.difficulty_scale
    #     self.fleet_speed *= self.difficulty_scale