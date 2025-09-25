"""Module de lancement

auteur : JajmeLesLjcornes
"""


import pygame
from brjck_breaker.game_var import PlayerStats as Pstat

__author__ = "JajmeLesLjcornes"


def draw_player_platform(screen, player: Pstat):
    pygame.draw.rect(screen, "blue",
                     (player.pos.x, player.pos.y, 150, 25)
                     )
