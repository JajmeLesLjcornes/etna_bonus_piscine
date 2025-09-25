"""Module de lancement

auteur : JajmeLesLjcornes
"""


import pygame
import random
import math


__author__ = "JajmeLesLjcornes"


class BallInfo:
    def __init__(self, screen):
        self.pos = pygame.Vector2(
            screen.get_width() / 2, screen.get_height() / 2)

        self.speed = 100
        self.color = 255
        self.is_alive = False
        self.vector_angle = random.uniform(0, 2 * math.pi)

    def draw(self, screen):
        pygame.draw.circle(screen,
                           (self.color, self.color, self.color),
                           self.pos, 25
                           )

    def ball_movement(self):

        ball_speed = pygame.Vector2(
            math.cos(self.vector_angle), math.sin(self.vector_angle)) * self.speed
        pass
