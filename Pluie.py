import sys
import random
import pygame as pg
from pygame.locals import *

class CréaGoutte():
    def __init__(self):
        self.x = random.randint( -10, WIDTH +10)
        self.y = random.randint( -HEIGHT , -25)
        self.w = 5
        self.h = random.randint( 25, 50)
        self.speed = random.randint( 8, 15)
        self.color = color

    def draw(self, screen, color):
        self.drop = pg.draw.rect( screen, color, ( self.x, self.y, self.w, self.h))

    def impact_sol(self):
        if self.y > HEIGHT +self.h:
            self.y = -25

class Pluie():
    def __init__(self):
        pg.init()
        pg.mixer.init()
        pg.display.set_caption('Pluie')
        self.clock = pg.time.Clock()

    def loop(self, screen):

        while True:
            delta_t = self.clock.tick( FPS )

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return

            screen.fill(Fond)

            for i in range(int(len(whitedrops))):
                whitedrops[i].draw(screen,CouleurGoutte)
                whitedrops[i].y += whitedrops[i].speed
                whitedrops[i].impact_sol()

            pg.display.flip()
            pg.display.update()
            
            
#
WIDTH = 1500
HEIGHT = 800
screen = pg.display.set_mode((WIDTH, HEIGHT))
FPS = 60
NBGOUTTES = 1000
whitedrops = []
CouleurGoutte = (200,95,223)
Fond = (0,0,0)
#


for i in range(NBGOUTTES):
            whitedrops.append(CréaGoutte())

Pluie().loop(screen)
pg.quit()
