"""Module de lancement

auteur : JajmeLesLjcornes
"""


import pygame
import random
import math
# mes packets
from brjck_breaker.game_settings import GameSettings as GS
from brjck_breaker import game_var as gv

__author__ = "JajmeLesLjcornes"


class BallInfo:
    def __init__(self, screen, name: str, vector_angle):
        self.pos = pygame.Vector2(
            screen.get_width() / 2, screen.get_height() / 2)

        self.name = name
        self.speed = 300
        self.color = 255
        self.radius = 25
        self.is_alive = False
        self.vector_angle = vector_angle

    def draw(self, screen):
        pygame.draw.circle(screen,
                           (self.color, self.color, self.color),
                           self.pos, self.radius
                           )

    def ball_movement(self):
        # Vitesse courante en fonction de l’angle
        ball_speed = pygame.Vector2(
            math.cos(self.vector_angle),
            math.sin(self.vector_angle)
        ) * self.speed

        new_ball_pos = self.pos + ball_speed * GS.dt

        hit_x = new_ball_pos.x - self.radius < 0 or new_ball_pos.x + \
            self.radius > GS.screen_size[0]
        hit_y = new_ball_pos.y - self.radius < 0 or new_ball_pos.y + \
            self.radius > GS.screen_size[1]

        if hit_x and hit_y:
            self.vector_angle += math.pi  # inverse les deux axes
        elif hit_x:
            self.vector_angle = math.pi - self.vector_angle
        elif hit_y:
            self.vector_angle = -self.vector_angle

        # Normaliser l’angle
        self.vector_angle %= 2 * math.pi

        # ⚠️ Correction de position pour éviter de sortir de l’écran
        if new_ball_pos.x - self.radius < 0:
            new_ball_pos.x = self.radius
        elif new_ball_pos.x + self.radius > GS.screen_size[0]:
            new_ball_pos.x = GS.screen_size[0] - self.radius

        if new_ball_pos.y - self.radius < 0:
            new_ball_pos.y = self.radius
        elif new_ball_pos.y + self.radius > GS.screen_size[1]:
            new_ball_pos.y = GS.screen_size[1] - self.radius

        # Mise à jour de la position corrigée
        self.pos = new_ball_pos
