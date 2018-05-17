# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pygame
import sys
from pygame.locals import *
import random

class Pokemon(pygame.sprite.Sprite):
    def __init__(self, imagempokemon, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.velocidadex=0
        self.velocidadey=0
        self.image = pygame.image.load(imagempokemon)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
    def velocidade(self, velx, vely):
        self.velocidadex=velx
        self.velocidadey=vely
        
    
            
    def update (self, Tiro):
        self.rect.x +=self.velocidadex
        block_hit_list=pygame.sprite.spritecollide(self, Tiro, False)
        for block in block_hit_list:
            if self.velocidadex>0:
                self.rect.right = block.rect.left
            else:
                self.rect.left = block.rect.right
                
        self.rect.y +=self.velocidadey        
        block_hit_list=pygame.sprite.spritecollide(self, Tiro, False)
        for block in block_hit_list:
            if self.velocidadey>0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom
    
    
#==========================================================
pygame.init()

tela = pygame.display.set_mode((800, 600), 0, 32)
pygame.display.set_caption('Inspermon')
relogio= pygame.time.Clock()
 #elif pressed_keys[K_UP]:
           # Player.rect.y-Player.velocidadey
      #  elif pressed_keys[K_DOWN]:
            #Player.rect.y+Player.velocidadey
arena= pygame.image.load("Arena.jpg").convert()
player= Player("character.png",100,300,)
all_sprite_list = pygame.sprite.Group()
pokemon_group=pygame.sprite.Group()
pokemon_group.add(player)
all_sprite_list.add(player)

runmode = True
while runmode:
    for event in pygame.event.get():
        
        # Verifica se o evento atual é QUIT (janela fechou).
        if event.type == QUIT:
            # Neste caso, marca o flag rodando como False, 
            # para sair do loop de jogo.
            rodando = False
            
            if event.type == pygame.KEYDOWN:  
        pressed_keys = pygame.key.get_pressed() 
        if pressed_keys[K_UP]:
            if jc>=-10:
                neg=1
            elif jc<0:
                neg=-1
            player.recty-=jc**2*0.5*neg
            
        elif pressed_keys[K_DOWN]:
            player.velocidade(0,3)
        elif pressed_keys[K_RIGHT]:
            player.velocidade(3,0)
        elif pressed_keys[K_LEFT]:
            player.velocidade(-3,0)
    if event.type == pygame.KEYUP:
        if pressed_keys[K_UP]:
         player.velocidade(0,0)
        elif pressed_keys[K_DOWN]:
         player.velocidade(0,0)
        elif pressed_keys[K_RIGHT]:
            player.velocidade(0,0)
        elif pressed_keys[K_LEFT]:
            player.velocidade(0,0)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    