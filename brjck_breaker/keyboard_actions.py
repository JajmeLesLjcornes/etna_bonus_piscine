"""Module de lancement

auteur : JajmeLesLjcornes
"""


import pygame
from brjck_breaker.game_settings import GameSettings as GS
from brjck_breaker.game_var import PlayerStats as Pstat


__author__ = "JajmeLesLjcornes"


def player_movement(keys: tuple, player: Pstat) -> int:
    if 225 in keys:
        player.speed = 500
    else:
        player.speed = 250

    if (4 in keys) ^ (7 in keys):
        GS.debug_stats["current_speed"] = player.speed * GS.dt
        if 4 in keys:
            return -player.speed * GS.dt
        else:
            return player.speed * GS.dt
    else:
        GS.debug_stats["current_speed"] = 0
        player.speed = 0
        return player.speed
