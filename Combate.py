# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pygame
import random
import sys

from pygame.locals import *
from pygame.math import Vector2

tiros = pygame.sprite.Group()

blue = (0,0,255)
red = (220,20,60)
green = (0,255,0)

class Parede(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill(blue)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

class Pokemon(pygame.sprite.Sprite):
    def __init__(self, imagempokemon, pos_x, pos_y, Parede):
        pygame.sprite.Sprite.__init__(self)
        self.velocidadex = 0
        self.velocidadey = 0
        self.image = pygame.image.load(imagempokemon)
        self.rect = self.image.get_rect()
        self.pulo = 100
        self.a = 1
        self.pos = Vector2(pos_x, pos_y)
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y
        self.Parede = Parede
            
    def update (self):
        self.pos.x += self.velocidadex
        block_hit_list = pygame.sprite.spritecollide(self, self.Parede, False)
        for block in block_hit_list:
            self.velocidadex = 0
        self.velocidadey += self.a
        self.pos.y += (self.velocidadey)
        if self.pos.y > y:
            self.velocidadey = 0
            self.pos.y = y
            
                    
        if self.pos.x>600:
            self.rect.right = self.rect.left
        if self.pos.x<0:
            self.rect.left=self.rect.right
        self.rect.x=self.pos.x
        self.rect.y=self.pos.y
                
class Tiro(pygame.sprite.Sprite):
    def __init__(self, Imagemtiro, dano, pos, velocidade):
        pygame.sprite.Sprite.__init__(self)
        self.pos = Vector2(pos)
        self.velocidade=velocidade
        self.dano = dano
        self.image = pygame.image.load(Imagemtiro)
        self.rect = self.image.get_rect()
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y
        all_sprite_list.add(self)
        tiros.add(self)
            
    def update (self):
        self.pos += self.velocidade
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y
        
        #print(self.velocidade)
        #print(self.pos)
       
    def eventos(self):
        pass
    

class Inimigo(pygame.sprite.Sprite):
    def __init__(self, imagempokemon, pos_x, pos_y,Parede,vida):
        pygame.sprite.Sprite.__init__(self)
        self.velocidadex=0
        self.velocidadey=0
        self.image = pygame.image.load(imagempokemon)
        self.rect = self.image.get_rect()
        self.pulo=100
        self.a=1
        self.pos=Vector2(pos_x,pos_y)
        self.rect.x=self.pos.x
        self.rect.y=self.pos.y
        self.Parede=Parede
        self.vida=vida

    def update (self):
        self.pos.x +=self.velocidadex
        block_hit_list=pygame.sprite.spritecollide(self, self.Parede, False)
        for block in block_hit_list:
            if self.velocidadex>0:
                self.rect.right = block.rect.left
            else:
                self.rect.left = block.rect.right
        self.velocidadey+=self.a
        self.pos.y +=(self.velocidadey)
        if self.pos.y>y:
            self.velocidadey=0
            self.pos.y=y
            
            
        
        block_hit_list=pygame.sprite.spritecollide(self, self.Parede, False)
        for block in block_hit_list:
            if self.velocidadey>0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom
        self.rect.x=self.pos.x
        self.rect.y=self.pos.y        
    
all_sprite_list = pygame.sprite.Group()

lista_paredes = pygame.sprite.Group()
parede = Parede(0,0,10,600)
lista_paredes.add(parede)
all_sprite_list.add(parede)

parede_LADO = Parede(790,0,10,600)
lista_paredes.add(parede_LADO)
all_sprite_list.add(parede_LADO)

parede_TOPO = Parede(0,0,790,10)
lista_paredes.add(parede_TOPO)
all_sprite_list.add(parede_TOPO)

parede_BAIXO = Parede(0,330,790,10)
lista_paredes.add(parede_BAIXO)
all_sprite_list.add(parede_BAIXO)

#==========================================================
pygame.init()

tela = pygame.display.set_mode((800, 600), 0, 32)
pygame.display.set_caption('Inspermon')
relogio = pygame.time.Clock()
batalha = pygame.image.load("Arena.jpg").convert()
 #elif pressed_keys[K_UP]:
           # Player.rect.y-Player.velocidadey
      #  elif pressed_keys[K_DOWN]:
            #Player.rect.y+Player.velocidadey
#arena= pygame.image.load("Arena.jpg").convert()
x = 100
y = 300

player = Pokemon("character.png",x,y,lista_paredes)
Inimigo = Inimigo("character.png",300,y,lista_paredes,100)

pokemon_group=pygame.sprite.Group()
pokemon_group.add(player)
all_sprite_list.add(player)

inimigos_group=pygame.sprite.Group()
inimigos_group.add(Inimigo)
all_sprite_list.add(Inimigo)


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
    
        if event.type == pygame.KEYDOWN:
            if event.key == K_UP:
                player.velocidadey=-10
            elif event.key == K_RIGHT:
                player.velocidadex=3
            elif event.key == K_LEFT:
                player.velocidadex=-3
            if event.key == K_SPACE:
                if player.velocidadex>0:
                    b=Tiro('character.png',1,player.pos,Vector2(4,0))
                else:
                    b=Tiro('character.png',1,player.pos,Vector2(-4,0))
                
                
        if event.type == pygame.KEYUP:
            if event.key == K_RIGHT:
                player.velocidadex=0
            elif event.key == K_LEFT:
                player.velocidadex=0
#=====================================================
    coli=pygame.sprite.groupcollide(inimigos_group, tiros, False, True)
    for inimigo, tiros_nele in coli.items():
        if tiros_nele:
            print('Inimigo {0} levou {1} tiros'.format(inimigo, len(tiros_nele)))
    
    tela.blit(batalha, (0, 0))

        # Pinta os elementos do grupo de bolinhas na tela auxiliar.
    all_sprite_list.draw(tela)
    all_sprite_list.update()
        # Troca de tela na janela principal.
    pygame.display.flip()
    #print(player.rect.x)
    #print(player.rect.y)
    
    
    relogio.tick(60)

    # === FIM DA TERCEIRA PARTE ===
    # Agora volta para o início do loop e faz mais um passo do jogo.

pygame.display.quit()    
    
    
    
    
    
    
    
    
    
    
    
    
    
    