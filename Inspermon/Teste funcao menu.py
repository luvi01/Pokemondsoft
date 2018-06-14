# -*- coding: utf-8 -*-
"""
Created on Mon May 28 16:32:24 2018

@author: luvi01
"""
import pygame
from random import randint
black = (0,0,0)
class Pokemon(pygame.sprite.Sprite):
    def __init__(self, imagemplayer, vida, escudo, tiro, xp, nivel, nome):
        pygame.sprite.Sprite.__init__(self)
        self.nivel = nivel
        self.image = pygame.image.load(imagemplayer)
        self.rect = self.image.get_rect()
        self.vida = vida*self.nivel
        self.escudo = escudo*self.nivel
        self.tiro = tiro*self.nivel
        self.xp = xp
        self.nome = nome
    def update(self, poin):
        self.xp += poin
        if self.xp>= 100:
            self.nivel += 1
            self.xp = 0
            
        
#luvi = Pokemon("character.png", 100, 50, 50,0,1,'luvi')
#rods = Pokemon("character.png", 100, 50, 50,0,1,'rods')

alunimon1 = ('sprite_aluno1.png', 100, 15, 0, 1, 'Niubo')

alunimon2 = ('sprite_aluno2.png', 90, 20, 0, 1, 'Giovanni')

alunimon3 = ('sprite_aluno4.png', 110, 10, 0, 1, 'Pedro')

alunimon4 = ('sprite_aluno5.png', 100, 15, 0, 1, 'skank')

alunimon5 = ('sprite_aluno3.png', 90, 20, 0, 1, 'Vitória')

alunimon6 = ('sprite_aluno8.png', 110, 10, 0, 2, 'BiaM')

alunimon7 = ('sprite_aluno12.png', 100, 15, 0, 2, 'BiaA')

alunimon8 = ('sprite_aluno6.png', 90, 20, 0, 2, 'Pellizzon')

alunimon9 = ('sprite_aluno7.png', 110, 10, 0, 2, 'Weiser')

alunimon10 = ('sprite_aluno10.png', 100, 20, 0, 2, 'Ale')

alunimon11 = ('sprite_aluno2.png', 110, 15, 0, 3, 'Zanetti')

alunimon12 = ('sprite_aluno11.png', 100, 20, 0, 3, 'Abel')

alunimon13 = ('sprite_aluno13.png', 110, 15, 0, 3, 'Roger')

alunimon14 = ('sprite_aluno14.png', 100, 20, 0, 3, 'Samuel')

alunimon15 = ('sprite_aluno4.png', 110, 15, 0, 4, 'Bahia')

alunimon16 = ('sprite_aluno6.png', 100, 20, 0, 4, 'Duds')

alunimon17 = ('sprite_aluno10.png', 110, 20, 0, 4, 'Terhorst')

alunimon18 = ('sprite_aluno11.png', 110, 20, 0, 5, 'Rods')

alunimon19 = ('sprite_aluno14.png', 100, 15, 0, 5, 'Byron')

alunimon20 = ('sprite_aluno6.png', 100, 15, 0, 5, 'Camera-man')

biblio=[alunimon20, alunimon19, alunimon18, alunimon17, alunimon16, alunimon15, alunimon14, alunimon13, alunimon12, alunimon11, alunimon10, alunimon9, alunimon8, alunimon7, alunimon6, alunimon5, alunimon4, alunimon3, alunimon2, alunimon1 ]






pygame.init()
tela = pygame.display.set_mode((800, 600), 0, 32)
pygame.display.set_caption('Inspermon')
relogio= pygame.time.Clock()
Fundo = pygame.image.load("Fundo.jpg").convert()
smallfont = pygame.font.SysFont("comicsansms", 25)

def texto (i, x, y, cor):
    text = smallfont.render(i,True, cor)
    tela.blit(text, [x,y])
def menu(ammo, x, y):
    text = smallfont.render("Munição: "+str(ammo), True, black)
    tela.blit(text, [x,y])
def turn(ammo, x, y):
    text = smallfont.render("Turno: "+str(ammo), True, black)
    tela.blit(text, [x,y])



def menubatalha(biblio):
    p = randint(0, (len(biblio))-1)
    texto("A wild",300 ,300 , black)
    texto(biblio[p].nome,400,300,black)
    texto("Apears",460,300,black)
    print ("Awild" ,biblio[p].nome , "apears")
    pygame.time.wait(1000)
    
    return biblio[p]
oi = True

while oi:
    tela.blit(Fundo, (0,0))
    b=menubatalha(biblio)
    pygame.display.update()
    pygame.display.flip()
pygame.display.quit()
    