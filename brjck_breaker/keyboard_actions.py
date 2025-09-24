"""Module de lancement

auteur : JajmeLesLjcornes
"""


import pygame
from brjck_breaker.game_settings import GameSettings as GS
from brjck_breaker.game_var import GameValues as GV


__author__ = "JajmeLesLjcornes"


def player_movement(keys: tuple) -> int:
    if 225 in keys:
        GV.player_speed = 500
    else:
        GV.player_speed = 250

    if (4 in keys) ^ (7 in keys):
        GS.debug_stats["speed"] = GV.player_speed * GS.dt
        if 4 in keys:
            return -GV.player_speed * GS.dt
        else:
            return GV.player_speed * GS.dt
    else:
        GS.debug_stats["speed"], GV.player_speed = 0
        return 0
