import pygame

# Initialisation de Pygame
pygame.init()

# Configuration de la fenêtre du jeu
screen = pygame.display.set_mode((700, 500))
pygame.display.set_caption("Snake")
ico = pygame.image.load("icone.png")
pygame.display.set_icon(ico)
bg = pygame.Color("#4d4d4d")
running = True

# Configuration du terrain de jeu
abscisse = 35
ordonne = 35
largeur = 700 // abscisse
hauteur = 500 // ordonne

# Classe Snake
class Snake:
    def __init__(self, coordo_x="", coordo_y="", couleur="", corps=""):
        if coordo_x == "":
            coordo_x = abscisse // 11
            self.coordo_x = coordo_x
        if coordo_y == "":
            coordo_y = ordonne // 2
            self.coordo_y = coordo_y
        self.couleur = couleur
        if corps == "":
            corps = [
                [self.coordo_x, self.coordo_y],
                [self.coordo_x - 1, self.coordo_y],
                [self.coordo_x - 2, self.coordo_y]
            ]
            self.corps = corps

    def Afficher(self, rect=""):
        self.couleur = pygame.Color(self.couleur)
        if rect == "":
            for part in self.corps:
                rect = pygame.Rect((part[0] * largeur, part[1] * hauteur), (largeur, hauteur))
                pygame.draw.rect(screen, self.couleur, rect)
    
    def Deplacer(self) :
        clock = pygame.time.Clock()
        k = pygame.key.get_pressed()
        if k[pygame.K_RIGHT] :
            self.maj_pos("right")
        elif k[pygame.K_LEFT] :
            self.maj_pos("left")
        elif k[pygame.K_UP] :
            self.maj_pos("up")
        elif k[pygame.K_DOWN] :
            self.maj_pos("down")
        clock.tick(15)
        print(self.corps)

    def maj_pos(self, direction) :
        for i in range(len(self.corps) -1,0,-1) :
                self.corps[i][0] = self.corps[i-1][0]
                self.corps[i][1] = self.corps[i-1][1]
        if direction == "right" :
            self.corps[0][0] += 1
        elif direction == "left" :
            self.corps[0][0] -= 1
        elif direction == "up" :
            self.corps[0][1] -= 1
        elif direction == "down" :
            self.corps[0][1] += 1

# Création d'une instance de Snake
snake = Snake(couleur="#00FF00")

# Boucle principale
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Mise à jour de la position ou de l'état du serpent
    # (à faire en fonction des interactions du joueur ou de la logique du jeu)

    # Remplit l'écran avec la couleur de fond
    screen.fill(bg)

    # Dessine le quadrillage
    for i in range(abscisse + 1):
        pygame.draw.line(screen, pygame.Color("#555555"), (i * largeur, 0), (i * largeur, 500), 2)
    for j in range(ordonne + 1):
        pygame.draw.line(screen, pygame.Color("#555555"), (0, j * hauteur), (700, j * hauteur), 2)

    # Affiche le serpent à l'écran (dessiner après le remplissage de l'écran)
    snake.Afficher()
    snake.Deplacer()

    # Met à jour l'affichage
    pygame.display.flip()

# Fermeture de Pygame
pygame.quit()
