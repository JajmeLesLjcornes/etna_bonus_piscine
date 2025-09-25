"""Module de lancement

auteur : JajmeLesLjcornes
"""


import pygame
from brjck_breaker import keyboard_actions
from brjck_breaker.game_settings import GameSettings as GS
from brjck_breaker.game_var import PlayerStats as Pstat
from brjck_breaker import game_var
from brjck_breaker import draw_module
from brjck_breaker.ball import BallInfo

__author__ = "JajmeLesLjcornes"


pygame.init()
running = True
screen = pygame.display.set_mode((GS.screen_size[0], GS.screen_size[1]))
clock = pygame.time.Clock()
pygame.display.set_caption("Brjck Breaker")
GS.state = "test"
key_pressed = set()

ball = BallInfo(screen)
player = Pstat(screen)
test_level = game_var.LevelInfo(
    [
        game_var.BrickInfo("classic_1hp", (0, 0)),
        game_var.BrickInfo("classic_1hp", (1, 0)),
        game_var.BrickInfo("classic_1hp", (3, 0)),
        game_var.BrickInfo("classic_1hp", (0, 1)),
        game_var.BrickInfo("classic_1hp", (10, 1)),
        game_var.BrickInfo("classic_1hp", (9, 1)),
        game_var.BrickInfo("classic_1hp", (1, 2)),
    ]
)

while running:
    # =========================================================
    # 1.                Récupérer les événements
    # =========================================================

    GS.dt = clock.tick(60) / 1000

    # limits FPS to 60
    # dt = Delta time (Temps écoulé entre deux frames) =>
    # Permet de mettre une valeur fixe par seconde pour le déplacement d'un objet par exemple playerpos = 300 * dt

    for event in pygame.event.get():  # poll for events

        if event.type == pygame.QUIT:  # pygame.QUIT event => clic sur X pour fermer la fenêtre
            running = False
        # print(event)

        if event.type == pygame.KEYDOWN:
            key_pressed.add(event.__dict__["scancode"])
        if event.type == pygame.KEYUP:
            key_pressed.discard(event.__dict__["scancode"])

    # =========================================================
    # 2.    Logique du jeu (déplacements, collisions…)
    # =========================================================

    # Pour mettre en pause le jeu si on change de fenêtre
    if not pygame.key.get_focused():
        # Mettre en pause le jeu
        # print("La fenêtre n'a plus le focus clavier !")
        pass
    if key_pressed:
        new_x_pos = player.pos.x + keyboard_actions.player_movement(
            key_pressed, player)
        if 0 <= new_x_pos <= GS.screen_size[0] - player.platform["width"]:
            player.pos.x = new_x_pos
        else:
            player.pos.x = max(
                0, min(new_x_pos, 1000 - player.platform["width"]))

    """Todo :
    Faire en sorte de tilter la plateforme pour orienter le rebond
    déplacement gauche droite
    check la direction de déplacement de la plateforme quand la
    balle tape pour le rebond
    """

    # =========================================================
    # 3.                        Dessin
    # =========================================================
    screen.fill((0, 0, 0))  # fond noir
    draw_module.draw_player_platform(screen, player)
    test_level.draw_level(screen)
    ball.draw(screen)
    # Debug tools | Texte pour afficher la vitesse
    if GS.debug_tools:
        font = pygame.font.Font(None, 48)  # 48 = taille en pixels
        text = font.render(
            str(GS.debug_stats["current_speed"]), True, (255, 255, 255))

        screen.blit(text, text.get_rect(center=(400, 300)))

    pygame.display.flip()   # met à jour l’écran


pygame.quit()
