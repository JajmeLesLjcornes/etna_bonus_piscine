"""Module de lancement

auteur : JajmeLesLjcornes
"""


import pygame


__author__ = "JajmeLesLjcornes"


# game_state.py
class GameSettings:
    dt = 0
    state = "playing"
    screen_size = [1000, 750]
    debug_tools = True
    debug_stats = {
        "speed": 0
    }
