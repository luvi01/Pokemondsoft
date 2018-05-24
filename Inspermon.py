# -*- coding: utf-8 -*-
"""
Created on Wed May 23 16:23:03 2018

@author: guigu
"""

import pygame
import sys
from pygame.locals import *
import random
from pygame.mixer import Sound
blue = (0,0,255)
red = (220,20,60)
green = (0,255,0)
yellow = (255,255,0)
class Parede(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([width, height])
        self.image.fill(blue)
        self.rect= self.image.get_rect()
        self.rect.y=y
        self.rect.x=x

class Entrada(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([width, height])
        self.image.fill(red)
        self.rect= self.image.get_rect()
        self.rect.y=y
        self.rect.x=x

class Grama (pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([width, height])
        self.image.fill(green)
        self.rect= self.image.get_rect()
        self.rect.y=y
        self.rect.x=x
        
class Entrada_lago(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([width, height])
        self.image.fill(yellow)
        self.rect= self.image.get_rect()
        self.rect.y=y
        self.rect.x=x
        
class Player(pygame.sprite.Sprite):
    def __init__(self, imagemplayer, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.velocidadex=0
        self.velocidadey=0
        self.image = pygame.image.load(imagemplayer)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
    def velocidade(self, velx, vely):
        self.velocidadex=velx
        self.velocidadey=vely
    
            
    def update (self, Parede, Entrada, Grama, num):
        self.rect.x +=self.velocidadex
        block_hit_list=pygame.sprite.spritecollide(self, Parede, False)
        for block in block_hit_list:
            if self.velocidadex>0:
                self.rect.right = block.rect.left
            else:
                self.rect.left = block.rect.right
                
        self.rect.y +=self.velocidadey        
        block_hit_list=pygame.sprite.spritecollide(self, Parede, False)
        for block in block_hit_list:
            if self.velocidadey>0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom

#================================================================                
        #
        
#=================================================================
        grama_hit_list=pygame.sprite.spritecollide(self, Grama, False)
        for block in grama_hit_list:
            if random.randint(0,100)<1e-8:
                return 2
            else:
                return num
        return num
#=======================================================================
pygame.init()

tela = pygame.display.set_mode((900, 706), 0, 0)
pygame.display.set_caption('Inspermon')
relogio= pygame.time.Clock()
 #elif pressed_keys[K_UP]:
           # Player.rect.y-Player.velocidadey
      #  elif pressed_keys[K_DOWN]:
            #Player.rect.y+Player.velocidadey
mapa= pygame.image.load("map.jpg").convert()
sala=pygame.image.load("sala.jpg").convert()
batalha=pygame.image.load("Waterloo.jpg").convert()
player= Player("character.png",415,419)
all_sprite_list = pygame.sprite.Group()
frame2 = pygame.image.load("frame 3.jpg")
frame3 = pygame.image.load ('frame 2.jpg')
musica_inicial = Sound ("Ameno.ogg")
musica_história = Sound ('O_fortuna.ogg')
menu_inicial = pygame.image.load('menu_inicial.jpeg')
historia = pygame.image.load('historia_inicial.jpg')
frame5 = pygame.image.load('Frame 5.jpg')
selecao = pygame.image.load('Slide1.jpg')
fernando = pygame.image.load('Slide2.jpg')
ayres = pygame.image.load('Slide3.jpg')
bobrow = pygame.image.load('Slide4.jpg')
victor = pygame.image.load('Slide5.jpg')
pelican = pygame.image.load('Slide6.jpg')
daniel = pygame.image.load('Slide7.jpg')
musica_selecao = Sound ('Vingadores.ogg')
frame6 = pygame.image.load ('Slide8.jpg')
#========================================

#=======================================

#=========================================
#Grama
lista_grama=pygame.sprite.Group()

grama=Grama(10,10,350,700)
lista_grama.add(grama)
all_sprite_list.add(grama)

grama=Grama(360,420,50,300)
lista_grama.add(grama)
all_sprite_list.add(grama)

grama=Grama(360,10,160,230)
lista_grama.add(grama)
all_sprite_list.add(grama)

grama=Grama(360,10,160,230)
lista_grama.add(grama)
all_sprite_list.add(grama)
#=========================================

character_group=pygame.sprite.Group()
character_group.add(player)
all_sprite_list.add(player)
#===========================================================================================================
rodando= True
frame=6
numero = 0
while rodando:
    for event in pygame.event.get():
        
        # Verifica se o evento atual é QUIT (janela fechou).
        if event.type == QUIT:
            # Neste caso, marca o flag rodando como False, 
            # para sair do loop de jogo.
            rodando = False
    if event.type == pygame.KEYDOWN:  
        pressed_keys = pygame.key.get_pressed() 
        if pressed_keys[K_UP]:
            player.velocidade(0,-3)
        elif pressed_keys[K_DOWN]:
            player.velocidade(0,3)
        elif pressed_keys[K_RIGHT]:
            player.velocidade(3,0)
        elif pressed_keys[K_LEFT]:
            player.velocidade(-3,0)
        if event.key == K_s:
            frame = numero
    if event.type == pygame.KEYUP:
        if pressed_keys[K_UP]:
         player.velocidade(0,0)
        elif pressed_keys[K_DOWN]:
         player.velocidade(0,0)
        elif pressed_keys[K_RIGHT]:
            player.velocidade(0,0)
        elif pressed_keys[K_LEFT]:
            player.velocidade(0,0)
        
               
 
   
    print(player.rect.x)
    print(player.rect.y)
    if frame == 6:
        tela.blit(menu_inicial, (0,0))
        musica_inicial.play()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key== K_UP: 
                    musica_inicial.stop()
                    frame= 7
        pygame.display.flip()

    if frame==0:
        musica_selecao.stop()
        numero = 0
        lista_paredes=pygame.sprite.Group()
        lista_casa=pygame.sprite.Group()
        

        casa=Entrada(410,410,40,10)
        lista_casa.add(casa)
        all_sprite_list.add(casa)
        

        
        parede_BAIXO=Parede(0,700,960,10)
        lista_paredes.add(parede_BAIXO)
        all_sprite_list.add(parede_BAIXO)
        
        
        parede_insper=Parede(360,240,200,180)
        lista_paredes.add(parede_insper)
        all_sprite_list.add(parede_insper)
        
        parede_mercado = Parede (720,245,200,150)
        lista_paredes.add(parede_mercado)
        all_sprite_list.add(parede_mercado)
        
        frame=player.update(lista_paredes,lista_casa,lista_grama,0)
        tela.blit(mapa, (0, 0))
        character_group.draw(tela)
        pygame.display.flip()
        if 410<=player.rect.y<=420 and 415<=player.rect.x<=425:
            frame = 10
        if player.rect.y < 0:
            player.rect.y = 680
            frame = 3
        if player.rect.x < 0:
            player.rect.x = 880
            frame = 4
        if player.rect.x>900:
            player.rect.x = 0
            frame = 8
            
        

        
        
    if frame==1:
        print('oi')
        pygame.display.flip() 
        tela.blit(sala, (0, 0))

        pygame.display.flip()
    
    if frame==2:
        print('war')
        pygame.display.flip() 
        tela.blit(batalha, (0, 0))
        pygame.display.flip()
        
    if frame == 3:
        tela.blit (frame2, (0,0))
        
        parede_TOPO=Parede(0,0,900,10)
        lista_paredes.add(parede_TOPO)
        all_sprite_list.add(parede_TOPO)
        lista_paredes.remove(parede_mercado)
        lista_paredes.remove(parede_insper)
        lista_paredes.remove(parede_BAIXO)

        numero = 3
        character_group.draw(tela)
        frame=player.update(lista_paredes,lista_casa,lista_grama,3)
        pygame.display.flip()
        if player.rect.x>874:
            player.rect.x = 0
            frame =5
        if player.rect.y>700:
            player.rect.y = 0
            frame = 0
        
        
    if frame == 4:
        tela.blit (frame3, (0,0))
        lista_paredes.remove(parede_insper)
        parede_ladoE=Parede(0,0,10, 700)
        lista_paredes.add(parede_ladoE)
        all_sprite_list.add(parede_ladoE)
        lista_paredes.remove(parede_mercado)
        numero = 4
        character_group.draw(tela)
        frame=player.update(lista_paredes,lista_casa,lista_grama,4)
        pygame.display.flip ()
        if player.rect.x>900:
            player.rect.x = 0
            frame = 0
            
    
    if frame == 5:
        tela.blit(frame5, (0,0))
        parede_ladoD=Parede(900,0,10,790)
        lista_paredes.add(parede_ladoD)
        lista_paredes.remove(parede_insper)
        all_sprite_list.add(parede_ladoD)
        lista_paredes.remove(parede_mercado)
        parede_TOPO=Parede(0,0,900,10)
        lista_paredes.add(parede_TOPO)
        all_sprite_list.add(parede_TOPO)
        numero = 5
        character_group.draw(tela)
        frame=player.update(lista_paredes,lista_casa,lista_grama,5)
        if player.rect.x<0:
            player.rect.x = 870
            frame = 3
            lista_paredes.remove(parede_ladoD)
        pygame.display.flip ()
        
    if frame == 8:
        tela.blit (frame6, (0,0))
        character_group.draw(tela)
        numero = 8
        
        frame=player.update(lista_paredes,lista_casa,lista_grama,8)
        pygame.display.flip()
        if player.rect.y < 0:
            player.rect.y = 680
            frame = 5
        if player.rect.x<0:
            player.rect.x = 880
            frame = 0
        
       
    if frame == 7:
        tela.blit(historia, (0,0))
        musica_história.play()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key== K_UP: 
                    musica_história.stop()
                    
                    frame= 10
        pygame.display.flip()
        
    if frame == 10:
        tela.blit (selecao, (0,0))
        musica_selecao.play()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key== K_a: 
                    frame = 11
                elif event.key == K_b:
                    frame = 12
                elif event.key == K_c:
                    frame = 13
                elif event.key == K_d:
                    frame = 14
                elif event.key == K_e:
                    frame = 15
                elif event.key == K_f:
                    frame = 16
                elif event.key == K_ESCAPE or event.type == QUIT:
                    rodando = False
                
        pygame.display.flip()
       
        
    if frame == 11:
        tela.blit (bobrow, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key== K_a: 
                    player.rect.x = 410
                    player.rect.y = 411
                    frame = 0
        pygame.display.flip()
    if frame == 12:
        tela.blit (fernando, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key== K_a: 
                    player.rect.x = 410
                    player.rect.y = 411
                    frame = 0
        pygame.display.flip()           
    if frame == 13:
        tela.blit (victor, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key== K_a: 
                    player.rect.x = 410
                    player.rect.y = 411
                    frame = 0    
        pygame.display.flip()
    if frame == 14:
        tela.blit (ayres, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key== K_a: 
                    player.rect.x = 410
                    player.rect.y = 411
                    frame = 0 
        pygame.display.flip()
    
    if frame == 15:
        tela.blit (pelican, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key== K_a: 
                    player.rect.x = 410
                    player.rect.y = 411
                    frame = 0
        pygame.display.flip()
                    
    if frame == 16:
        tela.blit (daniel, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key== K_a: 
                    player.rect.x = 410
                    player.rect.y = 411
                    frame = 0   
        pygame.display.flip()
        
    relogio.tick(60)

    # === FIM DA TERCEIRA PARTE ===
    # Agora volta para o início do loop e faz mais um passo do jogo.

pygame.display.quit()