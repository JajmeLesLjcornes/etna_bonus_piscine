"""Module de lancement

auteur : JajmeLesLjcornes
"""


import pygame


__author__ = "JajmeLesLjcornes"


pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
key_pressed = set()


player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    # =========================================================
    # 1.                Récupérer les événements
    # =========================================================
    for event in pygame.event.get():  # poll for events

        if event.type == pygame.QUIT:  # pygame.QUIT event => clic sur X pour fermer la fenêtre
            running = False
        print(event)
        if event.type == pygame.KEYDOWN:
            print(event.__dict__["scancode"])
            print(pygame.key.get_pressed()[event.__dict__["key"]])

        if event.type == pygame.KEYDOWN:
            key_pressed.add(event.__dict__["scancode"])
        if event.type == pygame.KEYUP:
            key_pressed.discard(event.__dict__["scancode"])

    # <Event(769-KeyUp {'unicode': 'q', 'key': 113, 'mod': 0, 'scancode': 4, 'window': None})>
    # <Event(768-KeyDown {'unicode': 'q', 'key': 113, 'mod': 0, 'scancode': 4, 'window': None})>

    # =========================================================
    # 2.    Logique du jeu (déplacements, collisions…)
    # =========================================================

    # Pour mettre en pause le jeu si on change de fenêtre
    if not pygame.key.get_focused():
        # Mettre en pause le jeu
        # print("La fenêtre n'a plus le focus clavier !")
        pass
    if key_pressed:
        if (4 in key_pressed) ^ (7 in key_pressed):
            if 4 in key_pressed:
                player_pos.x -= 300 * dt
            else:
                player_pos.x += 300 * dt

    """Todo :
    Faire en sorte de tilter la plateforme pour orienter le rebond
    déplacement gauche droite
    """

    # =========================================================
    # 3.                        Dessin
    # =========================================================
    screen.fill((0, 0, 0))  # fond noir
    pygame.draw.circle(screen, "red", player_pos, 40)

    pygame.display.flip()   # met à jour l’écran

    # limits FPS to 60
    # dt = Delta time (Temps écoulé entre deux frames) =>
    # Permet de mettre une valeur fixe par seconde pour le déplacement d'un objet par exemple playerpos = 300 * dt
    dt = clock.tick(60) / 1000

pygame.quit()
