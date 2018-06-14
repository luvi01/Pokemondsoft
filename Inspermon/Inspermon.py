# -*- coding: utf-8 -*-
"""
Created on Wed May 23 16:23:03 2018

@author: guigu
"""

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
import Combate
from pygame import movie

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
            if random.randint(0,100)<0:
                return 2
            else:
                return num
        return num
#=======================================================================
pygame.init()

tela = pygame.display.set_mode((900, 706), 0, 0)
pygame.display.set_caption('Alunimon')
relogio= pygame.time.Clock()

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
comandos = pygame.image.load ('Comandos.jpg')
hospital = pygame.image.load ('Mercado.jpg')
einstein = pygame.image.load ('Alberto.jpg')
ambiente = Sound ('Ambiente.ogg')
djavu = Sound ('Bandadjavu.ogg')
darkness = Sound ('Darkness.ogg')
orgao= Sound ('Orgao.ogg')
frame20 = pygame.image.load ('Frame 20.jpg')
frame21 = pygame.image.load ('Frame 21.jpg')
frame22 = pygame.image.load ('Frame 22.jpg')
frame23 = pygame.image.load ('Frame 23.jpg')
frame24 = pygame.image.load ('Frame 24.jpg')
frame25 = pygame.image.load ('Frame 25.jpg')
frame26 = pygame.image.load ('Frame 26.jpg')
frame27 = pygame.image.load ('Frame 27.jpg')
frame28 = pygame.image.load ('Frame 28.jpg')
frame29 = pygame.image.load ('Frame 29.jpg')
frame30 = pygame.image.load ('Frame 30.jpg')
pausa = pygame.image.load ('Pausa.jpg')
portal = pygame.image.load ('Portal.jpg')
leao = pygame.image.load ('Leão.jpg')
proerd = Sound ('Proerd.ogg')
taca = pygame.image.load ('taca.jpg')
copa = Sound ('Brasil.ogg')
alien = pygame.image.load ('alien.jpg')
suspense = Sound ('Alien.ogg')

#========================================

#=======================================

#=========================================
#Grama
lista_grama=pygame.sprite.Group()
lista_paredes=pygame.sprite.Group()
lista_casa=pygame.sprite.Group()

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
forro = False
easteregg = 0
while rodando:
    for event in pygame.event.get():
        
        # Verifica se o evento atual é QUIT (janela fechou).
        if event.type == QUIT:
            ambiente.stop()
            musica_inicial.stop()
            musica_selecao.stop()
            musica_história.stop()
            djavu.stop()
            darkness.stop()
            orgao.stop()
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
        
        if event.key == K_p:
            frame = 31
        if event.key == K_q:
            frame = numero
            ambiente.stop()
            musica_inicial.stop()
            musica_selecao.stop()
            musica_história.stop()
            djavu.stop()
            orgao.stop()
        if event.key == K_k:
            if event.key == K_k:
                if event.key == K_k:
                    if event.key == K_j:
                        frame == 38



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
        darkness.stop()
        orgao.stop()
        numero = 0
        lista_paredes=pygame.sprite.Group()
        lista_casa=pygame.sprite.Group()
        ambiente.play()
        
        parede_insper=Parede(360,240,200,180)
        lista_paredes.add(parede_insper)
        all_sprite_list.add(parede_insper)       
        parede_mercado = Parede (720,245,200,150)
        lista_paredes.add(parede_mercado)
        all_sprite_list.add(parede_mercado)
        parede_hospital = Parede (686,576,200,100)
        lista_paredes.add(parede_hospital)
        all_sprite_list.add(parede_hospital)

        frame=player.update(lista_paredes,lista_casa,lista_grama,0)
        tela.blit(mapa, (0, 0))
        character_group.draw(tela)
        pygame.display.flip()
        if player.rect.y >= 665 and 655< player.rect.x < 680:
            frame = 19
        if 410<=player.rect.y<=420 and 415<=player.rect.x<=425:
            frame = 10
            ambiente.stop()
            musica_selecao.play()
            
        if player.rect.y < 11:
            player.rect.y = 674
            frame = 3
            all_sprite_list.remove(parede_hospital)
            all_sprite_list.remove(parede_mercado)
            all_sprite_list.remove(parede_insper)
            lista_paredes.remove(parede_hospital)
            lista_paredes.remove(parede_mercado)
            lista_paredes.remove(parede_insper)

        if player.rect.x < 11:
            player.rect.x = 870
            frame = 4
            all_sprite_list.remove(parede_hospital)
            all_sprite_list.remove(parede_mercado)
            all_sprite_list.remove(parede_insper)
            lista_paredes.remove(parede_hospital)
            lista_paredes.remove(parede_mercado)
            lista_paredes.remove(parede_insper)
            
        if player.rect.x>874:
            player.rect.x = 11
            frame = 8
            all_sprite_list.remove(parede_hospital)
            all_sprite_list.remove(parede_mercado)
            all_sprite_list.remove(parede_insper)
            lista_paredes.remove(parede_hospital)
            lista_paredes.remove(parede_mercado)
            lista_paredes.remove(parede_insper)
            
        if player.rect.y > 674:
            player.rect.y = 11
            frame = 21
            all_sprite_list.remove(parede_hospital)
            all_sprite_list.remove(parede_mercado)
            all_sprite_list.remove(parede_insper)
            lista_paredes.remove(parede_hospital)
            lista_paredes.remove(parede_mercado)
            lista_paredes.remove(parede_insper)
            
        if 800<player.rect.x<=810 and 390<player.rect.y<400:
            frame = 1
            

    if frame==1:
        ambiente.stop()
        pygame.display.flip() 
        tela.blit(sala, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == K_b:
                    frame = numero
                    player.rect.x = 790
                    player.rect.y = 410
        
        pygame.display.flip()
    
    if frame==2:
        print ('oi')
        ambiente.stop()
        frame=Combate.jogo(numero,ide)
        pygame.display.flip() 
        
        
    if frame == 3:
        tela.blit (frame2, (0,0))
        if not forro:
            ambiente.play()
        numero = 3
        character_group.draw(tela)
        
        parede_ladoE=Parede(0,0,10, 700)
        lista_paredes.add(parede_ladoE)
        all_sprite_list.add(parede_ladoE)

        frame=player.update(lista_paredes,lista_casa,lista_grama,3)
        pygame.display.flip()
        if 760<player.rect.x<805 and 290<player.rect.y<340:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == K_j:
                        print ('Easteregg')
                        
        if player.rect.x>874:
            player.rect.x = 11
            all_sprite_list.remove(parede_ladoE)
            lista_paredes.remove(parede_ladoE)
            frame =5
            
        if player.rect.y>674:
            player.rect.y = 11
            all_sprite_list.remove(parede_ladoE)
            lista_paredes.remove(parede_ladoE)
            frame = 0
            
        if player.rect.y<11:
            player.rect.y = 674
            all_sprite_list.remove(parede_ladoE)
            lista_paredes.remove(parede_ladoE)
            frame = 23
        
        
    if frame == 4:
        tela.blit (frame3, (0,0))
        numero = 4
        if not forro:
            ambiente.play()

        character_group.draw(tela)
        frame=player.update(lista_paredes,lista_casa,lista_grama,4)
        pygame.display.flip ()
        if player.rect.x>874:
            player.rect.x = 11
            frame = 0
        if player.rect.y>674:
            player.rect.y = 11
            frame = 20
        if player.rect.x <11:
            player.rect.x = 870
            frame = 25
        if player.rect.y<11:
            player.rect.y = 674
            frame = 30
            
    
    if frame == 5:
        tela.blit(frame5, (0,0))
        numero = 5
        
        parede_BAIXO=Parede(0,700,960,10)
        lista_paredes.add(parede_BAIXO)
        all_sprite_list.add(parede_BAIXO)
        parede_ladoD=Parede(900,0,10,790)
        lista_paredes.add(parede_ladoD)
        all_sprite_list.add(parede_ladoD)

        if 90<player.rect.x <110 and 11<=player.rect.y<17:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == K_j:
                        ambiente.stop()
                        djavu.play()
                        easteregg +=1
                        print (easteregg)
        character_group.draw(tela)
        frame=player.update(lista_paredes,lista_casa,lista_grama,5)
        pygame.display.flip ()
        
        if player.rect.x<11:
            player.rect.x = 870
            all_sprite_list.remove(parede_ladoD)
            lista_paredes.remove(parede_ladoD)
            all_sprite_list.remove(parede_BAIXO)
            lista_paredes.remove(parede_BAIXO)
            frame = 3
            
        if player.rect.y<11:
            player.rect.y = 674
            all_sprite_list.remove(parede_ladoD)
            lista_paredes.remove(parede_ladoD)
            all_sprite_list.remove(parede_BAIXO)
            lista_paredes.remove(parede_BAIXO)
            frame = 28
            
        
    if frame == 8:
        tela.blit (frame6, (0,0))
        character_group.draw(tela)
        numero = 8
        ambiente.stop()
        orgao.play()
        
        parede_TOPO=Parede(0,0,900,10)
        lista_paredes.add(parede_TOPO)
        all_sprite_list.add(parede_TOPO)
        parede_ladoD=Parede(900,0,10,790)
        lista_paredes.add(parede_ladoD)
        all_sprite_list.add(parede_ladoD)
        parede_BAIXO=Parede(0,700,960,10)
        lista_paredes.add(parede_BAIXO)
        all_sprite_list.add(parede_BAIXO)

        frame=player.update(lista_paredes,lista_casa,lista_grama,8)
        pygame.display.flip()
        if player.rect.x<11:
            player.rect.x = 870
            all_sprite_list.remove(parede_TOPO)
            all_sprite_list.remove(parede_BAIXO)
            all_sprite_list.remove(parede_ladoD)
            lista_paredes.remove(parede_TOPO)
            lista_paredes.remove(parede_BAIXO)
            lista_paredes.remove(parede_ladoD)
            frame = 0
        
       
    if frame == 7:
        tela.blit(historia, (0,0))
        musica_história.play()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key== K_UP: 
                    musica_história.stop()
                    
                    frame= 17
        pygame.display.flip()
        
    if frame == 9:
        tela.blit(Mercado,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == K_v:
                    Combate.recu(ide)
                    frame == 18
        pygame.display.flip()
      
    if frame == 10:
        tela.blit (selecao, (0,0))
        
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
        
    if frame == 17:
        tela.blit (comandos, (0,0))
        musica_selecao.play()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key== K_UP: 
                    frame = 10
        pygame.display.flip()   
    
    if frame == 18:
        tela.blit (einstein, (0,0))
        darkness.play()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == K_a:
                    player.rect.x = 655
                    player.rect.y = 667
                    frame = numero
        pygame.display.flip()
        
    if frame == 19:
        tela.blit (hospital, (0,0))
        ambiente.stop()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == K_v:
                    frame = 18
        pygame.display.flip()
    relogio.tick(60)
    
    if frame == 20:
        tela.blit (frame20, (0,0))
        character_group.draw(tela)
        numero = 20
        ambiente.play()
        
        parede_BAIXO=Parede(0,700,960,10)
        lista_paredes.add(parede_BAIXO)
        all_sprite_list.add(parede_BAIXO)
        parede_ladoE=Parede(0,0,10, 700)
        lista_paredes.add(parede_ladoE)
        all_sprite_list.add(parede_ladoE)

        frame=player.update(lista_paredes,lista_casa,lista_grama,20)
        pygame.display.flip()
        if player.rect.y <11:
            player.rect.y = 674 
            lista_paredes.remove(parede_BAIXO)
            all_sprite_list.remove(parede_BAIXO)
            all_sprite_list.remove(parede_ladoE)
            lista_paredes.remove(parede_ladoE)
            frame = 4
        if player.rect.x > 874:
            lista_paredes.remove(parede_BAIXO)
            all_sprite_list.remove(parede_BAIXO)
            lista_paredes.remove(parede_ladoE)
            all_sprite_list.remove(parede_ladoE)
            player.rect.x = 11
            frame = 21
    
    if frame == 21:
        tela.blit (frame21, (0,0))
        character_group.draw(tela)
        numero = 21
        ambiente.play()
        
        parede_BAIXO=Parede(0,700,960,10)
        lista_paredes.add(parede_BAIXO)
        all_sprite_list.add(parede_BAIXO)
        
        frame=player.update(lista_paredes,lista_casa,lista_grama,21)
        pygame.display.flip()
        
        if player.rect.y <11:
            player.rect.y = 674 
            all_sprite_list.remove(parede_BAIXO)
            lista_paredes.remove(parede_BAIXO)
            frame = 0
        if player.rect.x< 11:
            player.rect.x = 873
            all_sprite_list.remove(parede_BAIXO)
            lista_paredes.remove(parede_BAIXO)
            frame = 20
        if player.rect.x > 874:
            player.rect.x = 15
            all_sprite_list.remove(parede_BAIXO)
            lista_paredes.remove(parede_BAIXO)
            frame = 22
            
    if frame == 22:
        tela.blit (frame22, (0,0))
        character_group.draw(tela)
        numero = 22
        ambiente.play()
        
        parede_BAIXO=Parede(0,700,960,10)
        lista_paredes.add(parede_BAIXO)
        all_sprite_list.add(parede_BAIXO)
        parede_TOPO=Parede(0,0,900,10)
        lista_paredes.add(parede_TOPO)
        all_sprite_list.add(parede_TOPO)
        parede_ladoD=Parede(900,0,10,790)
        lista_paredes.add(parede_ladoD)
        all_sprite_list.add(parede_ladoD)
        
        frame=player.update(lista_paredes,lista_casa,lista_grama,22)
        pygame.display.flip()
        if player.rect.x < 11:
            player.rect.x = 870
            all_sprite_list.remove(parede_BAIXO)
            lista_paredes.remove(parede_BAIXO)
            all_sprite_list.remove(parede_TOPO)
            lista_paredes.remove(parede_TOPO)
            all_sprite_list.remove(parede_ladoD)
            lista_paredes.remove(parede_ladoD)
            frame = 21
        if 155<player.rect.x <180:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == K_j:
                        frame = 32
                        easteregg += 1
            
    
    if frame == 23:
        tela.blit (frame23, (0,0))
        character_group.draw(tela)
        numero = 23
        ambiente.play()
        
        parede_TOPO=Parede(0,0,900,10)
        lista_paredes.add(parede_TOPO)
        all_sprite_list.add(parede_TOPO)
        parede_ladoE=Parede(0,0,10, 700)
        lista_paredes.add(parede_ladoE)
        all_sprite_list.add(parede_ladoE)

        frame=player.update(lista_paredes,lista_casa,lista_grama,23)
        pygame.display.flip()
        if player.rect.x > 874:
            player.rect.x = 11
            all_sprite_list.remove(parede_ladoE)
            lista_paredes.remove(parede_ladoE)
            all_sprite_list.remove(parede_TOPO)
            lista_paredes.remove(parede_TOPO)
            frame = 24
        if player.rect.y > 674:
            player.rect.y = 11
            all_sprite_list.remove(parede_ladoE)
            lista_paredes.remove(parede_ladoE)
            all_sprite_list.remove(parede_TOPO)
            lista_paredes.remove(parede_TOPO)
            frame = 3
            
    if frame == 24:
        tela.blit (frame24, (0,0))
        character_group.draw(tela)
        numero = 24
        ambiente.play()
        
        parede_BAIXO=Parede(0,700,960,10)
        lista_paredes.add(parede_BAIXO)
        all_sprite_list.add(parede_BAIXO)
        parede_TOPO=Parede(0,0,900,10)
        lista_paredes.add(parede_TOPO)
        all_sprite_list.add(parede_TOPO)
        parede_ladoD=Parede(900,0,10,790)
        lista_paredes.add(parede_ladoD)
        all_sprite_list.add(parede_ladoD)
 
        frame=player.update(lista_paredes,lista_casa,lista_grama,24)
        pygame.display.flip()
        if player.rect.x < 11:
            player.rect.x = 870
            all_sprite_list.remove(parede_TOPO)
            lista_paredes.remove(parede_TOPO)
            all_sprite_list.remove(parede_BAIXO)
            lista_paredes.remove(parede_BAIXO)
            all_sprite_list.remove(parede_ladoD)
            lista_paredes.remove(parede_ladoD)
            frame = 23
        if 620<player.rect.x<640 and 150<player.rect.y <180:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == K_j:
                        frame = 33
                        easteregg += 30
    
    if frame == 25:
        tela.blit (frame25, (0,0))
        character_group.draw(tela)
        numero = 25
        ambiente.play()
        
        parede_BAIXO=Parede(0,700,960,10)
        lista_paredes.add(parede_BAIXO)
        all_sprite_list.add(parede_BAIXO)
        parede_ladoE=Parede(0,0,10, 700)
        lista_paredes.add(parede_ladoE)
        all_sprite_list.add(parede_ladoE)
        
        frame=player.update(lista_paredes,lista_casa,lista_grama,25)
        pygame.display.flip()
        if player.rect.y < 11:
            player.rect.y = 674
            all_sprite_list.remove(parede_BAIXO)
            lista_paredes.remove(parede_BAIXO)
            all_sprite_list.remove(parede_ladoE)
            lista_paredes.remove(parede_ladoE)
            frame = 26
        if player.rect.x > 874:
            player.rect.x = 11
            all_sprite_list.remove(parede_BAIXO)
            lista_paredes.remove(parede_BAIXO)
            all_sprite_list.remove(parede_ladoE)
            lista_paredes.remove(parede_ladoE)
            frame = 4

    if frame == 26:
        tela.blit (frame26, (0,0))
        character_group.draw(tela)
        numero = 26
        ambiente.play()
        
        parede_ladoD=Parede(900,0,10,790)
        lista_paredes.add(parede_ladoD)
        all_sprite_list.add(parede_ladoD)
        parede_ladoE=Parede(0,0,10, 700)
        lista_paredes.add(parede_ladoE)
        all_sprite_list.add(parede_ladoE)
                
        frame=player.update(lista_paredes,lista_casa,lista_grama,26)
        pygame.display.flip()
        if player.rect.y < 11:
            player.rect.y = 674
            all_sprite_list.remove(parede_ladoD)
            lista_paredes.remove(parede_ladoD)
            all_sprite_list.remove(parede_ladoE)
            lista_paredes.remove(parede_ladoE)
            frame = 27        
        if player.rect.y > 674:
            player.rect.y = 11
            all_sprite_list.remove(parede_ladoD)
            lista_paredes.remove(parede_ladoD)
            all_sprite_list.remove(parede_ladoE)
            lista_paredes.remove(parede_ladoE)
            frame = 25
        
    if frame == 27:
        tela.blit (frame27, (0,0))
        character_group.draw(tela)
        numero = 27
        ambiente.play()
        
        parede_ladoE=Parede(0,0,10, 700)
        lista_paredes.add(parede_ladoE)
        all_sprite_list.add(parede_ladoE)       
        parede_TOPO=Parede(0,0,900,10)
        lista_paredes.add(parede_TOPO)
        all_sprite_list.add(parede_TOPO)        
        parede_ladoD=Parede(900,0,10,790)
        lista_paredes.add(parede_ladoD)
        all_sprite_list.add(parede_ladoD)
        

        
        frame=player.update(lista_paredes,lista_casa,lista_grama,27)
        pygame.display.flip()
        if player.rect.y > 674:
            player.rect.y = 11
            all_sprite_list.remove(parede_ladoD)
            lista_paredes.remove(parede_ladoD)
            all_sprite_list.remove(parede_ladoE)
            lista_paredes.remove(parede_ladoE)
            all_sprite_list.remove(parede_TOPO)
            lista_paredes.remove(parede_TOPO)
            frame = 26
    
    if frame == 28:
        tela.blit (frame28, (0,0))
        character_group.draw(tela)
        numero = 28
        ambiente.play()
        
        parede_TOPO=Parede(0,0,900,10)
        lista_paredes.add(parede_TOPO)
        all_sprite_list.add(parede_TOPO)
        parede_ladoE=Parede(0,0,10, 700)
        lista_paredes.add(parede_ladoE)
        all_sprite_list.add(parede_ladoE)        

            
        frame=player.update(lista_paredes,lista_casa,lista_grama,28)
        pygame.display.flip()
        if player.rect.y > 674:
            player.rect.y = 11
            all_sprite_list.remove(parede_ladoE)
            lista_paredes.remove(parede_ladoE)
            all_sprite_list.remove(parede_TOPO)
            lista_paredes.remove(parede_TOPO)
            frame = 5
        if player.rect.y<11 :
            player.rect.y = 674
            all_sprite_list.remove(parede_ladoE)
            lista_paredes.remove(parede_ladoE)
            all_sprite_list.remove(parede_TOPO)
            lista_paredes.remove(parede_TOPO)
            frame = 29
            
    if frame == 29:
        tela.blit (frame29, (0,0))
        character_group.draw(tela)
        numero = 29
        ambiente.play()
        
        parede_TOPO=Parede(0,0,900,10)
        lista_paredes.add(parede_TOPO)
        all_sprite_list.add(parede_TOPO)        
        parede_ladoD=Parede(900,0,10,790)
        lista_paredes.add(parede_ladoD)
        all_sprite_list.add(parede_ladoD)
        parede_BAIXO=Parede(0,700,960,10)
        lista_paredes.add(parede_BAIXO)
        all_sprite_list.add(parede_BAIXO)
       
        frame=player.update(lista_paredes,lista_casa,lista_grama,29)
        pygame.display.flip()
        if player.rect.y > 674:
            player.rect.y = 11
            all_sprite_list.remove(parede_TOPO)
            lista_paredes.remove(parede_TOPO)
            all_sprite_list.remove(parede_BAIXO)
            lista_paredes.remove(parede_BAIXO)
            all_sprite_list.remove(parede_ladoD)
            lista_paredes.remove(parede_ladoD)
            frame = 28
            
    if frame == 30:
        tela.blit (frame30, (0,0))
        character_group.draw(tela)
        numero = 30
        ambiente.play()
        
        parede_ladoE=Parede(0,0,10, 700)
        lista_paredes.add(parede_ladoE)
        all_sprite_list.add(parede_ladoE)        
        parede_TOPO=Parede(0,0,900,10)
        lista_paredes.add(parede_TOPO)
        all_sprite_list.add(parede_TOPO)        
        parede_ladoD=Parede(900,0,10,790)
        lista_paredes.add(parede_ladoD)
        all_sprite_list.add(parede_ladoD)
                
        frame=player.update(lista_paredes,lista_casa,lista_grama,30)
        pygame.display.flip()
        if player.rect.y > 674:
            player.rect.y = 11
            all_sprite_list.remove(parede_ladoD)
            lista_paredes.remove(parede_ladoD)
            all_sprite_list.remove(parede_ladoE)
            lista_paredes.remove(parede_ladoE)
            all_sprite_list.remove(parede_TOPO)
            lista_paredes.remove(parede_TOPO)
            frame = 4
    
    if frame == 31:
        tela.blit (pausa, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == K_c:
                    frame = numero
                elif event.key == K_r:
                    frame = 6
                    easteregg = 0
                    ambiente.stop()
                    djavu.stop()
                    musica_selecao.stop()
                    musica_história.stop()
        pygame.display.flip()
    
    if frame == 32:
        tela.blit (portal, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == K_a:
                    frame = 0
                elif event.key == K_b:
                    frame = 29
                elif event.key == K_c:
                    frame = 8
        pygame.display.flip()
    
    if frame == 33:
        ambiente.stop()
        tela.blit(leao, (0,0))
        proerd.play()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == K_s:
                    frame = numero
                    proerd.stop()
        pygame.display.flip()
        
    if frame == 34:
        tela.blit(alien, (0,0))
        suspense.play()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == K_s:
                    frame = numero
        pygame.display.flip()
        
    if frame == 35:
        tela.blit(taca, (0,0))
        copa.play()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == K_s:
                    frame = numero
        pygame.display.flip()
        
        
    if easteregg == 678:
        frame = 38

    
        



    # === FIM DA TERCEIRA PARTE ===
    # Agora volta para o início do loop e faz mais um passo do jogo.

pygame.display.quit()
ambiente.stop()