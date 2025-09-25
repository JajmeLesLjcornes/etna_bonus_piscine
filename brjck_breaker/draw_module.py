"""Module de lancement

auteur : JajmeLesLjcornes
"""


import pygame
from brjck_breaker.game_var import PlayerStats as Pstat

__author__ = "JajmeLesLjcornes"

brick = pygame.Rect(0, 0, 100, 25)


def draw_player_platform(screen, player: Pstat):
    pygame.draw.rect(screen, "blue",
                     (player.pos.x, player.pos.y, 150, 25)
                     )


def draw_brick(screen):
    pygame.draw.rect(screen, "red", brick)
    print(brick)
