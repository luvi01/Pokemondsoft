# -*- coding: utf-8 -*-
"""
Created on Mon May 28 15:22:24 2018

@author: luvi01
"""

import pygame
import sys
from pygame.locals import *
import random

class Pokemon(pygame.sprite.Sprite):
    def __init__(self, imagemplayer, vida, escudo, tiro, xp, nivel):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(imagemplayer)
        self.rect = self.image.get_rect()
        self.vida = vida*self.nivel
        self.escudo = escudo*self.nivel
        self.tiro = tiro*self.nivel
        self.xp = xp
        self.nivel = nivel
    def update(self, poin):
        self.xp += poin
        if self.xp>= 100:
            self.nivel += 1
            self.xp = 0
            
        
luvi = Pokemon("character.png", 100, 50, 50,0,1)
rods = Pokemon("character.png", 100, 50, 50,0,1)

biblio=[{"luvi":luvi},{"rods":rods}]
inventario = [{'rods':rods}, {"luvi":luvi}]
def menubatalha(inventario, biblio):
    p = randint(0, (len(biblio))-1)
    for k in biblio[p]:
        print ("A wild" ,k , "apears")
    i=0
    while i < len(inventario):
        for k in inventario[i]:
            print(i,":",k)
            i+=1
    a = int(input('Escolha o seu pokemon:'))
    return inventario[a].values(), biblio[p].values()

while rodando:
    b=menubatalha(inventario, biblio)
    b[0]=player
    b[1]=computador
    for event in pygame.event.get():
        
        # Verifica se o evento atual é QUIT (janela fechou).
        if event.type == QUIT:
            # Neste caso, marca o flag rodando como False, 
            # para sair do loop de jogo.
            rodando = False
    while player.vida and computador.vida > 0:
        if event.type == pygame.KEYDOWN:  
            pressed_keys = pygame.key.get_pressed() 
            if pressed_keys[K_UP]:
                
            elif pressed_keys[K_DOWN]:
    
            elif pressed_keys[K_RIGHT]:
    
            elif pressed_keys[K_LEFT]:
    
        if event.type == pygame.KEYUP:
            if pressed_keys[K_UP]:
    
            elif pressed_keys[K_DOWN]:
    
            elif pressed_keys[K_RIGHT]:
    
            elif pressed_keys[K_LEFT]:

        
       
       
        
    
    
    
    relogio.tick(60)

    # === FIM DA TERCEIRA PARTE ===
    # Agora volta para o início do loop e faz mais um passo do jogo.

pygame.display.quit()