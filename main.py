import pygame
import random
import time

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((700, 500))
pygame.display.set_caption("Snake")
ico = pygame.image.load("icone.png")
pygame.display.set_icon(ico)
bg = pygame.Color("#4d4d4d")
running = True
clock = pygame.time.Clock()
## Terrain de jeu 
abscisse = 35
ordonne = 35
largeur = 700 // abscisse
hauteur = 500 // ordonne


################################################## OBJET ##########################

# 2 Classes Snake et Food les deux elements importants du projet
class Snake() :
    def __init__(self, coordo_x = "", coordo_y = "", couleur = "", corps = "", previous = None, song_eat = r"theme\eating.mp3", count = 0) :
        # Je definis un point de depart en x soit a l'extreme gauche
        if coordo_x == "" :
            coordo_x = abscisse // 11
            self.coordo_x = coordo_x
        # Je definis un point de depart en y soit au milieu 
        if coordo_y == "" :
            coordo_y = ordonne // 2
            self.coordo_y = coordo_y
        self.couleur = couleur
        # Le corps du serpent prendra les positions données precedemment
        if corps == "" :
            corps = [
                [self.coordo_x, self.coordo_y],
                [self.coordo_x -1, self.coordo_y],
                [self.coordo_x -2, self.coordo_y]
            ]
            self.corps = corps
        self.previous = previous
        self.song_eat = song_eat
        self.count = count
        
    def Afficher(self, rect = "") :
        self.couleur = pygame.Color(self.couleur)
        if rect == "" :
            for part in self.corps :
                rect = pygame.Rect((part[0]*largeur, part[1]*hauteur),(largeur, hauteur))
                pygame.draw.rect(screen, self.couleur, rect)
                self.rect = rect
                
    def Reset(self) :
        reset_corps = [
                [self.coordo_x, self.coordo_y],
                [self.coordo_x -1, self.coordo_y],
                [self.coordo_x -2, self.coordo_y]
            ]
        self.count = 0 
        self.corps = reset_corps
        self.previous = None
        for part in self.corps :
                rect = pygame.Rect((part[0]*largeur, part[1]*hauteur),(largeur, hauteur))
                pygame.draw.rect(screen, self.couleur, rect)
                
    def Deplacer(self) :
        k = pygame.key.get_pressed()
        if k[pygame.K_RIGHT] :
            if self.previous != "left" :
                self.maj_pos("right")
                self.previous = "right"
        elif k[pygame.K_LEFT] :
            if self.previous != "right" :
                self.maj_pos("left")
                self.previous = "left"
        elif k[pygame.K_UP] :
            if self.previous != "down" :
                self.maj_pos("up")
                self.previous = "up"
        elif k[pygame.K_DOWN] :
            if self.previous != "up" :
                self.maj_pos("down")
                self.previous = "down"
        self.keeps_going()
        

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
    
    def keeps_going(self) :
        if self.previous == "right" :
            self.maj_pos(self.previous)
        elif self.previous == "left":
            self.maj_pos(self.previous)
        elif self.previous == "up":
            self.maj_pos(self.previous)
        elif self.previous == "down":
            self.maj_pos(self.previous)
    
    def MangerPomme(self) :
        if self.rect.colliderect(apple.pomme) :
            self.corps.append([self.coordo_x - (len(self.corps)+1), self.coordo_y])
            self.count += 1
            sound = pygame.mixer.Sound(self.song_eat)
            sound.play()
            return True
        return False
    
    def OverPass(self) :
        # A modifier si je veux que le joueur perd quand il touche une bordure
        if self.corps[0][0] > 34 :
            return True
        elif self.corps[0][0] < 0 :
            return True
        elif self.corps[0][1] < 0 :
            return True
        elif self.corps[0][1] > 34 :
            print(self.corps)
            return True
        return False
    
    def EatHimself(self) :
        for body in range(1, len(self.corps)) :
            if self.corps[0] == self.corps[body] :
                return True
        return False
        
        

class Apple() :
    def __init__(self, couleur = "", taillex = "", tailley = "", pomme = "") :
        self.couleur = couleur
        if taillex == "" :
            taillex, tailley = (abscisse // 2), (ordonne // 2) 
            self.taillex = taillex
            self.tailley = tailley
        if pomme == "" :
            pomme = pygame.Rect((self.taillex*largeur, self.tailley*hauteur),(largeur, hauteur))
            self.pomme = pomme
            
    def Afficher(self) :
        self.couleur = pygame.Color(self.couleur)
        pygame.draw.rect(screen, self.couleur, self.pomme)
        
    def Reset(self):
        taillex, tailley = (abscisse // 2), (ordonne // 2) 
        self.taillex = taillex
        self.tailley = tailley
        self.pomme = pygame.Rect((self.taillex*largeur, self.tailley*hauteur),(largeur, hauteur))
        pygame.draw.rect(screen, self.couleur, self.pomme)
    
    def DeleteAndPopup(self) :
            self.random_taillex, self.random_tailley = (random.randint(0,35)), (random.randint(0,35)) 
            self.pomme = (((self.random_taillex*largeur)-3, (self.random_tailley*hauteur)-3),(largeur, hauteur))
            pygame.draw.rect(screen, self.couleur, self.pomme)


class User() :
    def __init__(self, song = "") :
        if song == "" :
            song = r"theme\theme.mp3"
            self.song = song
            self.img_volume = pygame.image.load("volume.png").convert_alpha()
            self.binaire = 0
            
            
    def Music(self) :
        pygame.mixer.music.load(self.song)
        pygame.mixer.music.play(loops=-1)
        
    def StopMusic(self) :
        pygame.mixer.music.stop()
        
    def MenuOver(self, snake_count) :
        overlay = pygame.Surface((700, 500), pygame.SRCALPHA)
        overlay.fill((1,1,1,128))
        self.bouton = pygame.Rect((200, 400),(300, 60))
        color = pygame.Color("#f1f1f1")
        police = pygame.font.Font(None, 50)
        txt = police.render("Start a new game", 3, (1,1,1))
        score_txt = police.render(str(snake_count), 3, (1,1,1))
        newscore = self.RegisterBetterScore(snake_count)
        record_txt = police.render(str(newscore), 3, (1,1,1))
        score = pygame.Rect((200,50),(300, 300))
        color_screen = (164, 24, 27)
        pygame.draw.rect(overlay, color_screen, score)
        pygame.draw.rect(overlay, color, self.bouton)
        img_pomme = pygame.image.load("apple.png").convert_alpha()
        img_trophy = pygame.image.load("trophy.png").convert_alpha()
        screen.blit(overlay, (0,0))
        screen.blit(txt, (210, 412))
        screen.blit(img_pomme, (210, 150))
        screen.blit(score_txt, (400,165))
        screen.blit(img_trophy, (210, 270))
        screen.blit(record_txt, (400,285))
        screen.blit(self.img_volume, (630, 10))
    
    def RegisterBetterScore(self, snake_count) :
        compare = int(snake_count)
        with open("record.txt", "r") as file:
            content = file.read().strip()
            if not content:
                record = snake_count
                file.close()
                with open("record.txt", "w") as file :
                    file.write(str(record))
                    file.close()
                return record
            else :
                with open("record.txt", "r") as file:
                    for line in file :
                        other = line
                    file.close()
                other = int(other)
                if compare >= other :
                    with open("record.txt", "w") as file :
                        file.write(str(compare))
                        file.close()
                        return compare
                else :
                    return other
    
        
    def ClickOnButton(self) :
        if event.type == pygame.MOUSEBUTTONDOWN :
            if self.bouton.collidepoint(event.pos):
                snake.Reset()
                apple.Reset()
                user.Music()
            
                    
        
################################################## OBJET ##########################

snake = Snake(couleur="#00FF00")
apple = Apple(couleur="#FF0000")
user = User()
user.Music()
open_ = False
count = 0  

while running :
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            running = False

    screen.fill(bg)
    ## Affichage des elements
    apple.Afficher()
    snake.Afficher()
    over = snake.OverPass() or snake.EatHimself()
    
    if event.type == pygame.KEYDOWN :
        if event.key == pygame.K_ESCAPE :
            if count == 0 :
                open_ = not open_ 
            count += 1
    if event.type == pygame.KEYUP :
        count = 0
    if open_ :
        user.MenuOver(snake.count) 
        user.RegisterBetterScore(snake.count)
        user.ClickOnButton()
        
    if not over and not open_ :
        snake.Deplacer()
    if over :
        user.StopMusic()
        user.MenuOver(snake.count)
        user.RegisterBetterScore(snake.count)
        user.ClickOnButton()
        
    if snake.MangerPomme() :
        apple.DeleteAndPopup()
    
    clock.tick(15)        
    pygame.display.flip()
    

pygame.display.quit()