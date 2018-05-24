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
tiros_inimigo = pygame.sprite.Group()

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
    def __init__(self, imagempokemon, pos_x, pos_y,vida):
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
        self.vida = vida
            
    def update (self):
        self.pos.x += self.velocidadex
        if self.rect.x>765:
            self.pos.x = 765
            self.velocidadex = 0
        self.velocidadey += self.a
        self.pos.y += (self.velocidadey)
        if self.pos.y > y:
            self.velocidadey = 0
            self.pos.y = y
        if self.rect.y<2:
            self.pos.y = 2
            self.velocidadey = 0
        if self.rect.x<10:
            self.pos.x = 10
            self.velocidadex = 0
        self.rect.x=self.pos.x
        self.rect.y=self.pos.y
                
class Tiro(pygame.sprite.Sprite):
    def __init__(self, Imagemtiro, dano, delay, pos, velocidade):
        pygame.sprite.Sprite.__init__(self)
        self.pos = Vector2(pos)
        self.velocidade=velocidade
        self.dano = dano
        self.image = pygame.image.load(Imagemtiro)
        self.rect = self.image.get_rect()
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y
        self.time = pygame.time.get_ticks()
        self.last_shot = 0
        self.shot_delay = delay
            
    def update (self):
        if self.time - self.last_shot> self.shot_delay:
            self.pos += self.velocidade
            self.rect.x = self.pos.x
            self.rect.y = self.pos.y
            self.last_shot = self.time
        
        #print(self.velocidade)
        #print(self.pos)
       
    def eventos(self):
        pass
    

class Inimigo(pygame.sprite.Sprite):
    def __init__(self, imagempokemon, pos_x, pos_y,adver,vida):
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
        self.vida=vida
        self.adversario=adver

    def update (self):
        if self.vida>=0:
            self.velocidadex = random.randint(-10,10)
            self.velocidadey = random.randint(-5,3)
            self.pos.x += self.velocidadex
            if self.adversario.rect.x>self.rect.x:
                a=Tiro('character.png',1,2,self.pos,Vector2(4,1))
            else:
                a=Tiro('character.png',1,2,self.pos,Vector2(-4,0))
            all_sprite_list.add(a)
            tiros_inimigo.add(a)
            
            if self.rect.x>765:
                self.pos.x = 765
                self.velocidadex = 0
            self.velocidadey += self.a
            self.pos.y += (self.velocidadey)
            if self.pos.y > y:
                self.velocidadey = 0
                self.pos.y = y
            if self.rect.y<2:
                self.pos.y = 2
                self.velocidadey = 0
            if self.rect.x<10:
                self.pos.x = 10
                self.velocidadex = 0
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

player = Pokemon("character.png",x,y,100)
pokemomwild = Inimigo("character.png",300,y,player,100)

pokemon_group=pygame.sprite.Group()
pokemon_group.add(player)
all_sprite_list.add(player)

inimigos_group=pygame.sprite.Group()
inimigos_group.add(pokemomwild)
all_sprite_list.add(pokemomwild)


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
                    b=Tiro('character.png',1,2,player.pos,Vector2(4,0))
                    all_sprite_list.add(b)
                    tiros.add(b)
                else:
                    b=Tiro('character.png',1,2,player.pos,Vector2(-4,0))
                    all_sprite_list.add(b)
                    tiros.add(b)
           
                
                
        if event.type == pygame.KEYUP:
            if event.key == K_RIGHT:
                player.velocidadex=0
            elif event.key == K_LEFT:
                player.velocidadex=0
#=====================================================
   
#=====================================================
    coli=pygame.sprite.groupcollide(inimigos_group, tiros, False, True)
    for inimigo, tiros_nele in coli.items():
        if tiros_nele:
            print('Inimigo {0} levou {1} tiros'.format(inimigo, len(tiros_nele)))
            pokemomwild.vida-=b.dano
        
    #print(pokemomwild.vida)
    print(pygame.time.get_ticks())
#=====================================================
    
    tela.blit(batalha, (0, 0))

        # Pinta os elementos do grupo de bolinhas na tela auxiliar.
    all_sprite_list.draw(tela)
    all_sprite_list.update()
    if pokemomwild.vida<0:
        inimigos_group.remove(pokemomwild)
        all_sprite_list.remove(pokemomwild)
    pygame.display.flip()
    #print(player.rect.x)
    #print(player.rect.y)
    
    
    relogio.tick(60)

    # === FIM DA TERCEIRA PARTE ===
    # Agora volta para o início do loop e faz mais um passo do jogo.

pygame.display.quit()    
    
    
    
    
    
    
    
    
    
    
    
    
    
    