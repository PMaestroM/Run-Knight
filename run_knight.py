import pygame
from pygame.constants import *
import time

pygame.init()
pygame.mixer.init()

carte = [[2, 0, 1, 1, 1, 0, 0, 0, 1, 1],
         [1, 0, 0, 1, 1, 0, 1, 0, 0, 1],
         [1, 1, 0, 1, 1, 0, 0, 1, 0, 1],
         [1, 0, 0, 1, 1, 1, 0, 1, 0, 1],
         [1, 0, 1, 1, 0, 0, 0, 1, 0, 1],
         [0, 0, 1, 1, 0, 1, 1, 0, 0, 1],
         [0, 1, 1, 1, 0, 1, 1, 0, 1, 1],
         [0, 1, 0, 0, 0, 0, 1, 0, 1, 1],
         [0, 0, 0, 1, 1, 0, 1, 0, 3, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

cote_fenetre = 640
fenetre = pygame.display.set_mode((cote_fenetre, cote_fenetre))
pygame.display.set_caption("Run Knight")
icone = pygame.image.load("res/sheet_hero_walk_right.png")
pygame.display.set_icon(icone)
fond = pygame.image.load("res/background.png").convert()
perso = pygame.image.load("res/sheet_hero_walk_right.png").convert_alpha()
snake = pygame.image.load("res/sheet_snake_walk.png").convert_alpha()
wall = pygame.image.load("res/wall.png").convert()
depart = pygame.image.load("res/fleche_rouge.png").convert_alpha()
pygame.mixer.music.load("res/mad_run.wav")
pygame.mixer.music.play(-1)

position_perso = perso.get_rect()


def creermap():
    fenetre.blit(fond, (0, 0))
    for x in range(0, len(carte)):
        for y in range(0, len(carte[0])):
            if carte[x][y] == 1:
                fenetre.blit(wall, (y * 64, x * 64))
            if carte[x][y] == 2:
                fenetre.blit(depart, (64, 20))
            if carte[x][y] == 3:
                fenetre.blit(snake, (y * 64, x * 64))
    fenetre.blit(perso, position_perso)

    pygame.display.flip()

def message(fenetre, text, size, x, y):
    font_name = pygame.font.match_font('arial')
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, (255, 0, 0))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    fenetre.blit(text_surface, text_rect)


def caseactuelle(x,y):
    my_x = x // 64
    my_y = y // 64
    #print(my_x, my_y, carte[my_y][my_x])
    return carte[my_y][my_x]


continuer = True
pygame.key.set_repeat(1, 1) #Vitesse
while continuer:
    for event in pygame.event.get():
        # Close windows
        if event.type == QUIT:
            continuer = False
        elif event.type == KEYDOWN:
            if event.key == K_DOWN: # "flèche bas"
                if position_perso.y <= cote_fenetre-position_perso.h - 1:
                    my_x = position_perso.x
                    my_y = position_perso.y + position_perso.h + 1
                    position1 = caseactuelle(my_x, my_y)
                    position2 = caseactuelle(my_x + position_perso.w, my_y)
                    if (position1 != 1) & (position2 != 1):
                        position_perso = position_perso.move(0, 1)
                    if (position1 == 3) & (position2 == 3):
                        message(fenetre, "GG !", 200, 100, 100)
                        time.sleep(1)
                        continuer = False
            if event.key == K_UP:  # "flèche haut"
                if position_perso.y >= 1:
                    my_x = position_perso.x
                    my_y = position_perso.y - 1
                    position1 = caseactuelle(my_x, my_y)
                    position2 = caseactuelle(my_x + position_perso.w, my_y)
                    if (position1 != 1) & (position2 != 1):
                        position_perso = position_perso.move(0, -1)
                    if (position1 == 3) & (position2 == 3):
                        message(fenetre, "GG !", 200, 100, 100)
                        time.sleep(1)
                        continuer = False
            if event.key == K_RIGHT:  # "flèche droite"
                if position_perso.x <= cote_fenetre-position_perso.w - 1:
                    my_x = position_perso.x + position_perso.w + 1
                    my_y = position_perso.y
                    position1 = caseactuelle(my_x, my_y)
                    position2 = caseactuelle(my_x, my_y + position_perso.h)
                    if (position1 != 1) & (position2 != 1):
                        position_perso = position_perso.move(1, 0)
                    if (position1 == 3) & (position2 == 3):
                        message(fenetre, "GG !", 200, 100, 100)
                        time.sleep(1)
                        continuer = False
            if event.key == K_LEFT:  # "flèche gauche"
                if position_perso.x >= 1:
                    my_x = position_perso.x - 1
                    my_y = position_perso.y
                    position1 = caseactuelle(my_x, my_y)
                    position2 = caseactuelle(my_x, my_y + position_perso.h)
                    if (position1 != 1) & (position2 != 1):
                        position_perso = position_perso.move(-1, 0)
                    if (position1 == 3) & (position2 == 3):
                        message(fenetre, "GG !", 200, 100, 100)
                        time.sleep(1)
                        continuer = False
        creermap()

