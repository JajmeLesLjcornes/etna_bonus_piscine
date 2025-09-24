"""Module de lancement

auteur : JajmeLesLjcornes
"""


import pygame
from brjck_breaker.game_state import GameValue as GV


__author__ = "JajmeLesLjcornes"


def player_movement(keys: tuple) -> int:

    if (4 in keys) ^ (7 in keys):
        print(GV.dt)
        if 4 in keys:
            return -300 * GV.dt
        else:
            return 300 * GV.dt
    else:
        return 0
