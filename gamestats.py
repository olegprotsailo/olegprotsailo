import pygame
class Stats():
    def __init__(self,game_settings):
        self.game_settings = game_settings
        self.reset_stats()
    def reset_stats (self):
        self.ship_left = self.game_settings.ship_limit