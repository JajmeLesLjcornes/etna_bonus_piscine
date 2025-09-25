"""Module de lancement

auteur : JajmeLesLjcornes
"""


import pygame


__author__ = "JajmeLesLjcornes"


# game_state.py
class PlayerStats:
    def __init__(self, screen):
        self.pos = pygame.Vector2(
            screen.get_width() / 2, screen.get_height() - 50)
        self.platform = {
            "width": 150,
            "height": 25,
        }

        self.speed = 0


brick_type = {
    "unbreakable": -1,
    "true unbreakable": -100,
    "classic_1hp": 1,
    "classic_3hp": 3,
    "classic_5hp": 5,
    "regen_3hp": 3,
    "regen_5hp": 5
}


class BrickInfo:
    def __init__(self, type: str, pos: tuple):
        self.type = type
        self.pos = pos
        self.hp = brick_type[type]
        pass


class LevelStats:
    def __init__(self, brick_list: list):
        self.brick_list = brick_list
        pass


class Bidule:
    truc = 0
