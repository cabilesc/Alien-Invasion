class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings"""
        # Screen settings
        self.screen_width = 1440
        self.screen_height = 900
        self.bg_color = (100, 100, 100)

        # Ship Settings
        self.ship_speed = 6.5

        # bullet settings
        self.bullet_speed = 9.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet.color = (252, 2, 159)

