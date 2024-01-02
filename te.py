
# Inutile pour le snake.

    # Dessine le quadrillage
    for i in range(abscisse + 1):
        pygame.draw.line(screen, pygame.Color("#555555"), (i * largeur, 0), (i * largeur, 500), 2)
    for j in range(ordonne + 1):
        pygame.draw.line(screen, pygame.Color("#555555"), (0, j * hauteur), (700, j * hauteur), 2)

