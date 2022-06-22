import copy

import pygame
import os

pygame.init()

# bepaald breete en hoogte scherm
schermBreete = 675
schermHoogte = 675

# maakt het scherm
scherm = pygame.display.set_mode((schermBreete, schermHoogte))
pygame.display.set_caption("Pandora's puzzels")
FPS = 60

# variabelen
tegel_groote = 75
level_nummer = 0
aantal_vakken = 9
spelen = False

# foto's laden
character = pygame.image.load(os.path.join('character', 'c1.jpg'))
grond = pygame.image.load(os.path.join('objecten', 'grond.jpg'))
steen = pygame.image.load(os.path.join('objecten', 'steen.jpg'))
muur = pygame.image.load(os.path.join('objecten', 'muur.jpg'))
portaal = pygame.image.load(os.path.join('objecten', 'portaal.png'))
doos = pygame.image.load(os.path.join('objecten', 'doos.jpg'))
gat = pygame.image.load(os.path.join('objecten', 'gat.jpg'))


class Wereld:
    def __init__(self, info):
        global player_x
        global player_y

        rij_aantal = 0
        for rij in info:
            kolom_aantal = 0
            for tegel in rij:

                if tegel == 'Char':
                    foto = pygame.transform.scale(character, (tegel_groote, tegel_groote))
                    foto_rect = foto.get_rect()
                    player_x = kolom_aantal
                    player_y = rij_aantal
                    foto_rect.x = player_x * tegel_groote
                    foto_rect.y = player_y * tegel_groote
                    scherm.blit(foto, foto_rect)

                if tegel == 0:
                    foto = pygame.transform.scale(grond, (tegel_groote, tegel_groote))
                    foto_rect = foto.get_rect()
                    foto_rect.x = kolom_aantal * tegel_groote
                    foto_rect.y = rij_aantal * tegel_groote
                    scherm.blit(foto, foto_rect)

                if tegel == 1:
                    foto = pygame.transform.scale(muur, (tegel_groote, tegel_groote))
                    foto_rect = foto.get_rect()
                    foto_rect.x = kolom_aantal * tegel_groote
                    foto_rect.y = rij_aantal * tegel_groote
                    scherm.blit(foto, foto_rect)

                if tegel == 2:
                    foto = pygame.transform.scale(steen, (tegel_groote, tegel_groote))
                    foto_rect = foto.get_rect()
                    foto_rect.x = kolom_aantal * tegel_groote
                    foto_rect.y = rij_aantal * tegel_groote
                    scherm.blit(foto, foto_rect)

                if tegel == 3:
                    foto = pygame.transform.scale(portaal, (tegel_groote, tegel_groote))
                    foto_rect = foto.get_rect()
                    foto_rect.x = kolom_aantal * tegel_groote
                    foto_rect.y = rij_aantal * tegel_groote
                    scherm.blit(foto, foto_rect)

                if tegel == 4:
                    foto = pygame.transform.scale(portaal, (tegel_groote, tegel_groote))
                    foto_rect = foto.get_rect()
                    foto_rect.x = kolom_aantal * tegel_groote
                    foto_rect.y = rij_aantal * tegel_groote
                    scherm.blit(foto, foto_rect)

                if tegel == 5:
                    foto = pygame.transform.scale(doos, (tegel_groote, tegel_groote))
                    foto_rect = foto.get_rect()
                    foto_rect.x = kolom_aantal * tegel_groote
                    foto_rect.y = rij_aantal * tegel_groote
                    scherm.blit(foto, foto_rect)

                if tegel == 6:
                    foto = pygame.transform.scale(gat, (tegel_groote, tegel_groote))
                    foto_rect = foto.get_rect()
                    foto_rect.x = kolom_aantal * tegel_groote
                    foto_rect.y = rij_aantal * tegel_groote
                    scherm.blit(foto, foto_rect)

                kolom_aantal += 1
            rij_aantal += 1


levels = {
 0: [
  [1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 0, 0, 0, 'Char', 0, 0, 0, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 1, 1, 1, 0, 2, 2, 1, 1],
  [1, 0, 0, 0, 2, 0, 0, 0, 1],
  [1, 1, 1, 1, 4, 1, 1, 1, 1],
 ],

 1: [
  [1, 1, 1, 1, 3, 1, 1, 1, 1],
  [1, 0, 0, 0, 'Char', 0, 0, 0, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 1, 2, 2, 2, 1, 0, 1],
  [1, 0, 1, 0, 0, 0, 1, 0, 1],
  [1, 1, 1, 1, 4, 1, 1, 1, 1],
 ],

 2: [
  [1, 1, 1, 1, 3, 1, 1, 1, 1],
  [1, 0, 0, 0, 'Char', 0, 0, 0, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 0, 0, 0, 6, 4],
  [1, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 0, 2, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1],
 ],

 3: [
  [1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 1],
  [3, 'Char', 0, 0, 0, 0, 5, 0, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1],
 ]
}

wereld_info = levels[level_nummer]
wereld = Wereld(wereld_info)


def beweeg_links():
    global level_nummer

    if wereld_info[player_y][player_x - 1] == 0:
        wereld_info[player_y][player_x] = 0
        wereld_info[player_y][player_x - 1] = 'Char'
    if wereld_info[player_y][player_x - 1] == 2:
        if wereld_info[player_y][player_x - 2] == 0:
            wereld_info[player_y][player_x] = 0
            wereld_info[player_y][player_x - 1] = 'Char'
            wereld_info[player_y][player_x - 2] = 2
        if wereld_info[player_y][player_x - 2] == 6:
            wereld_info[player_y][player_x] = 0
            wereld_info[player_y][player_x - 1] = 'Char'
            wereld_info[player_y][player_x - 2] = 0
    if wereld_info[player_y][player_x - 1] == 3:
        level_nummer -= 1
    if wereld_info[player_y][player_x - 1] == 5:
        return False


def beweeg_rechts():
    global level_nummer

    if wereld_info[player_y][player_x + 1] == 0:
        wereld_info[player_y][player_x] = 0
        wereld_info[player_y][player_x + 1] = 'Char'
    if wereld_info[player_y][player_x + 1] == 2:
        if wereld_info[player_y][player_x + 2] == 0:
            wereld_info[player_y][player_x] = 0
            wereld_info[player_y][player_x + 1] = 'Char'
            wereld_info[player_y][player_x + 2] = 2
        if wereld_info[player_y][player_x + 2] == 6:
            wereld_info[player_y][player_x] = 0
            wereld_info[player_y][player_x + 1] = 'Char'
            wereld_info[player_y][player_x + 2] = 0
    if wereld_info[player_y][player_x + 1] == 4:
        level_nummer += 1
    if wereld_info[player_y][player_x + 1] == 5:
        return False


def beweeg_omhoog():
    global level_nummer

    if wereld_info[player_y - 1][player_x] == 0:
        wereld_info[player_y][player_x] = 0
        wereld_info[player_y - 1][player_x] = 'Char'
    if wereld_info[player_y - 1][player_x] == 2:
        if wereld_info[player_y - 2][player_x] == 0:
            wereld_info[player_y][player_x] = 0
            wereld_info[player_y - 1][player_x] = 'Char'
            wereld_info[player_y - 2][player_x] = 2
        if wereld_info[player_y - 2][player_x] == 6:
            wereld_info[player_y][player_x] = 0
            wereld_info[player_y - 1][player_x] = 'Char'
            wereld_info[player_y - 2][player_x] = 0
    if wereld_info[player_y - 1][player_x] == 3:
        level_nummer -= 1
    if wereld_info[player_y - 1][player_x] == 5:
        return False


def beweeg_omlaag():
    global level_nummer

    if wereld_info[player_y + 1][player_x] == 0:
        wereld_info[player_y][player_x] = 0
        wereld_info[player_y + 1][player_x] = 'Char'
    if wereld_info[player_y + 1][player_x] == 2:
        if wereld_info[player_y + 2][player_x] == 0:
            wereld_info[player_y][player_x] = 0
            wereld_info[player_y + 1][player_x] = 'Char'
            wereld_info[player_y + 2][player_x] = 2
        if wereld_info[player_y + 2][player_x] == 6:
            wereld_info[player_y][player_x] = 0
            wereld_info[player_y + 1][player_x] = 'Char'
            wereld_info[player_y + 2][player_x] = 0
    if wereld_info[player_y + 1][player_x] == 4:
        level_nummer += 1
    if wereld_info[player_y + 1][player_x] == 5:
        return False


def scherm_updaten():
    Wereld(wereld_info)
    pygame.display.update()


def main():
    global wereld_info
    global level_nummer

    wereld_copie = copy.deepcopy(wereld_info)
    level_copie = level_nummer
    clock = pygame.time.Clock()
    aan = True
    while aan:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                aan = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if beweeg_links() is False:
                        aan = False

                if event.key == pygame.K_RIGHT:
                    if beweeg_rechts() is False:
                        aan = False

                if event.key == pygame.K_UP:
                    if beweeg_omhoog() is False:
                        aan = False

                if event.key == pygame.K_DOWN:
                    if beweeg_omlaag() is False:
                        aan = False

                if event.key == pygame.K_SPACE:
                    level_nummer += 1

                if event.key == pygame.K_r:
                    levels[level_nummer] = copy.deepcopy(wereld_copie)

        wereld_info = levels[level_nummer]

        if level_copie != level_nummer:
            level_copie = level_nummer
            wereld_copie = copy.deepcopy(wereld_info)

        scherm_updaten()


main()
