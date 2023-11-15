import pygame

class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings"""
        # Screen settings
        self.screen_width = 1440
        self.screen_height = 900
        self.bg_color = (100, 100, 100)

        # Ship Settings
        self.ship_speed = 3.5

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet direction of 1 represents right: -1 represents left
        self.fleet_direction = 1

        # bullet settings
        self.bullet_speed = 4.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (252, 2, 159)
        self.bullets_allowed = 5

        # Music/Sounds
        pygame.mixer.init()

        # Plays background music
        music = pygame.mixer.music.load('music/battleThemeA.mp3')
        pygame.mixer.music.play(-1)

