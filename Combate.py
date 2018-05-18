# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pygame
import sys
from pygame.locals import *
import random
blue = (0,0,255)
red = (220,20,60)
green = (0,255,0)
class Parede(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([width, height])
        self.image.fill(blue)
        self.rect= self.image.get_rect()
        self.rect.y=y
        self.rect.x=x
class Pokemon(pygame.sprite.Sprite):
    def __init__(self, imagempokemon, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.velocidadex=0
        self.velocidadey=0
        self.image = pygame.image.load(imagempokemon)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.pulo=100
        self.a=1
        
    
            
    def update (self, Parede):
        self.rect.x +=self.velocidadex
        block_hit_list=pygame.sprite.spritecollide(self, Parede, False)
        for block in block_hit_list:
            if self.velocidadex>0:
                self.rect.right = block.rect.left
            else:
                self.rect.left = block.rect.right
        print(self.rect.y)
        print(self.velocidadex)
        print(y) 
        self.velocidadey+=self.a
        self.rect.y +=(self.velocidadey)
        if self.rect.y>y:
            self.velocidadey=0
            self.rect.y=y
            
            
        
        block_hit_list=pygame.sprite.spritecollide(self, Parede, False)
        for block in block_hit_list:
            if self.velocidadey>0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom


all_sprite_list = pygame.sprite.Group()

lista_paredes=pygame.sprite.Group()
parede=Parede(0,0,10,600)
lista_paredes.add(parede)
all_sprite_list.add(parede)

parede_LADO=Parede(790,0,10,600)
lista_paredes.add(parede_LADO)
all_sprite_list.add(parede_LADO)

parede_TOPO=Parede(0,0,790,10)
lista_paredes.add(parede_TOPO)
all_sprite_list.add(parede_TOPO)

parede_BAIXO=Parede(0,330,790,10)
lista_paredes.add(parede_BAIXO)
all_sprite_list.add(parede_BAIXO)









    
    
#==========================================================
pygame.init()

tela = pygame.display.set_mode((800, 600), 0, 32)
pygame.display.set_caption('Inspermon')
relogio= pygame.time.Clock()
batalha=pygame.image.load("Arena.jpg").convert()
 #elif pressed_keys[K_UP]:
           # Player.rect.y-Player.velocidadey
      #  elif pressed_keys[K_DOWN]:
            #Player.rect.y+Player.velocidadey
#arena= pygame.image.load("Arena.jpg").convert()
x=100
y=300
player = Pokemon("character.png",x,y,)

pokemon_group=pygame.sprite.Group()
pokemon_group.add(player)
all_sprite_list.add(player)
contapulo=10
pula=False
runmode = True
while runmode:
    for event in pygame.event.get():
        
        # Verifica se o evento atual é QUIT (janela fechou).
        if event.type == QUIT:
            # Neste caso, marca o flag rodando como False, 
            # para sair do loop de jogo.
            runmode = False
        pressed_keys = pygame.key.get_pressed()
    
        if event.type == pygame.KEYDOWN:
            if pressed_keys[K_UP]:
                player.velocidadey=-10
            if pressed_keys[K_RIGHT]:
                player.velocidadex=3
            elif pressed_keys[K_LEFT]:
                player.velocidadex=-3
        if event.type == pygame.KEYUP:
            if pressed_keys[K_RIGHT]:
                player.velocidadex=0
            elif pressed_keys[K_LEFT]:
                player.velocidadex=0
    
    tela.blit(batalha, (0, 0))

        # Pinta os elementos do grupo de bolinhas na tela auxiliar.
    all_sprite_list.draw(tela)
    player.update(lista_paredes)
        # Troca de tela na janela principal.
    pygame.display.flip()
    #print(player.rect.x)
    #print(player.rect.y)
    
    
    relogio.tick(60)

    # === FIM DA TERCEIRA PARTE ===
    # Agora volta para o início do loop e faz mais um passo do jogo.

pygame.display.quit()    
    
    
    
    
    
    
    
    
    
    
    
    
    
    