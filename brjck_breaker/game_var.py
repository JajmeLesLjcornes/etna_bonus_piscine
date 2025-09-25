"""Module de lancement

auteur : JajmeLesLjcornes
"""


import pygame
from random import randint


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
    brick = pygame.Rect(0, 0, 100, 25)

    def __init__(self, type: str, pos: tuple):
        self.type = type
        self.pos = pos  # (x, y)
        self.hp = brick_type[type]
        pass

    def draw(self, screen):
        if self.pos[1] % 2 == 0:
            pixel_pos = (self.pos[0] * 100, self.pos[1] * 25)
        else:
            pixel_pos = (self.pos[0] * 100 - 50, self.pos[1] * 25)
        pygame.draw.rect(screen, (200, randint(0, 255), 100),
                         self.brick.move(pixel_pos))


class LevelInfo:

    def __init__(self, brick_list: list[BrickInfo]):
        self.brick_list = brick_list
        pass

    def draw_level(self, screen):
        for brick in self.brick_list:
            brick.draw(screen)
