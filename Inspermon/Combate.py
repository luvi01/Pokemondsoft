#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 12:09:48 2018

@author: luvi
"""

import pygame
import sys
from pygame.locals import *
import random
import time
green = (0,255,0)
yellow = (255,255,0)
red = (255,0,0)
black = (0,0,0)
class Pokemon(pygame.sprite.Sprite):
    def __init__(self, imagemplayer, vida, tiro, xp, nivel,nome):
        pygame.sprite.Sprite.__init__(self)
        self.shield = False
        self.tiro = False
        self.carregar = False
        self.ammo = 0
        self.nome = nome
        self.image = pygame.image.load(imagemplayer)
        self.rect = self.image.get_rect()
        self.nivel = nivel
        self.vida = vida
        self.vida += (1*(self.nivel))*0.5
        self.tiro_dano = tiro
        self.tiro_dano += (1*(self.nivel))*0.5
        self.xp = xp
#==================================================
        if self.xp >= 100:
            self.nivel +=1
            self.xp = 0

class Props(pygame.sprite.Sprite):
      def __init__(self, imagemprop):
        self.image = pygame.image.load(imagemprop)
        self.rect = self.image.get_rect()
        
        
        
#luvi = Pokemon("luvi.png", 100, 20,0,1,"luvi")
#rods = Pokemon("character.png", 100, 20,0,1,"rods")

ayres = Pokemon("ayres.png", 100, 20,0,1,"ayres")
vitor = Pokemon("vitor.png", 100, 20,0,1,"vitor")
pelicano = Pokemon("pelicano.png", 100, 20,0,1,"pelicano")
fernando = Pokemon("fernando.png", 100, 20,0,1,"fernando")
daniel = Pokemon("daniel.png", 100, 20,0,1,"daniel")
bobrow = Pokemon("bobrow.png", 100, 20,0,1,"bobrow")

mosquete = Props("Mosquetein.png")

pygame.init()
tela = pygame.display.set_mode((800, 600), 0, 32)
pygame.display.set_caption('Inspermon')
relogio= pygame.time.Clock()

Fundo = pygame.image.load("Fundo.jpg").convert()
vitoria = pygame.image.load("vitoria.jpeg").convert()
derrota = pygame.image.load("derrota.jpeg").convert()
Branco = pygame.image.load("Branco.jpg").convert()

smallfont = pygame.font.SysFont("comicsansms", 25)

def health_bars(player_health, enemy_health):
    
    if player_health > 75:
        player_health_color = green
    elif player_health > 50:
        player_health_color = yellow
    else:
        player_health_color = red
    
    if enemy_health > 75:
        enemy_health_color = green
    elif enemy_health > 50:
        enemy_health_color = yellow
    else:
        enemy_health_color = red
    
    pygame.draw.rect(tela, player_health_color, (680,25,player_health,25))
    pygame.draw.rect(tela, enemy_health_color, (20,25,enemy_health,25))
    
def texto (oi, x, y, cor):
    text = smallfont.render(oi,True, cor)
    tela.blit(text, [x,y])
def menu(ammo, x, y):
    text = smallfont.render("Munição: "+str(ammo), True, black)
    tela.blit(text, [x,y])
def turn(ammo, x, y):
    text = smallfont.render("Turno: "+str(ammo), True, black)
    tela.blit(text, [x,y])
def xp(xp, x, y):
    text = smallfont.render("XP ganho: "+str(xp), True, black)
    tela.blit(text, [x,y])    
    
    
    
def menubatalha(biblio):
    p = random.randint(0, (len(biblio))-1)
    texto("A wild",300 ,300 , black)
    texto(biblio[p].nome,400,300,black)
    texto("Apears",530,300,black)
    #print ("Awild" ,biblio[p].nome , "apears")
    
    return biblio[p]
    
alunimon1 = Pokemon('sprite_aluno1.png', 100, 15, 0, 1, 'Niubo')

alunimon2 = Pokemon('sprite_aluno2.png', 90, 20, 0, 1, 'Giovanni')

alunimon3 = Pokemon('sprite_aluno4.png', 110, 10, 0, 1, 'Pedro')

alunimon4 = Pokemon('sprite_aluno5.png', 100, 15, 0, 1, 'skank')

alunimon5 = Pokemon('sprite_aluno3.png', 90, 20, 0, 1, 'Vitória')

alunimon6 = Pokemon('sprite_aluno8.png', 110, 10, 0, 2, 'BiaM')

alunimon7 = Pokemon('sprite_aluno12.png', 100, 15, 0, 2, 'BiaA')

alunimon8 = Pokemon('sprite_aluno6.png', 90, 20, 0, 2, 'Pellizzon')

alunimon9 = Pokemon('sprite_aluno7.png', 110, 10, 0, 2, 'Weiser')

alunimon10 = Pokemon('sprite_aluno10.png', 100, 20, 0, 2, 'Ale')

alunimon11 = Pokemon('sprite_aluno2.png', 110, 15, 0, 3, 'Zanetti')

alunimon12 = Pokemon('sprite_aluno11.png', 100, 20, 0, 3, 'Abel')

alunimon13 = Pokemon('sprite_aluno13.png', 110, 15, 0, 3, 'Roger')

alunimon14 = Pokemon('sprite_aluno14.png', 100, 20, 0, 3, 'Samuel')

alunimon15 = Pokemon('sprite_aluno4.png', 110, 15, 0, 4, 'Bahia')

alunimon16 = Pokemon('sprite_aluno6.png', 100, 20, 0, 4, 'Duds')

alunimon17 = Pokemon('sprite_aluno10.png', 110, 20, 0, 4, 'Terhorst')

alunimon18 = Pokemon('sprite_aluno11.png', 110, 20, 0, 5, 'Rods')

alunimon19 = Pokemon('sprite_aluno14.png', 100, 15, 0, 5, 'Byron')

alunimon20 = Pokemon('sprite_aluno6.png', 100, 15, 0, 5, 'Camera-man')

biblio=[alunimon20, alunimon19, alunimon18, alunimon17, alunimon16, alunimon15, alunimon14, alunimon13, alunimon12, alunimon11, alunimon10, alunimon9, alunimon8, alunimon7, alunimon6, alunimon5, alunimon4, alunimon3, alunimon2, alunimon1 ]

def confronto(comp,ide):
    inventario = [vitor, pelicano, fernando, daniel, bobrow, ayres]
    player=inventario[ide]
    
    computador = comp
    player.amo = 0
    action = True
    rodando = True
    turno = 0
    computador.vida = 100
    computador.ammo = 0
    sprite_pokemon = pygame.sprite.Group()
    sprite_pokemon.add(player)
    sprite_pokemon.add(computador)    
    while rodando:
        player.rect.x = 100
        player.rect.y = 400
        computador.rect.x = 500
        computador.rect.y = 400
        
        health_bars(player.vida, computador.vida)
    #=========================================================================================
       
        #print('shield:',player.shield)
        #print('carregar:',player.carregar)
        #print('turno:',turno)
        #print('action:',action)
        #print('vidacomp:',computador.vida)
        #print('vidaplayer:',player.vida)
        #print('ammoplayer:',player.ammo)
        #print('ammocomp:',computador.ammo)
        if player.vida <= 0 or computador.vida <= 0:
            sprite_pokemon.remove(player)
            sprite_pokemon.remove(computador)
            if player.vida > 0:
                xp = random.randint(10,15)
                player.xp += xp
                rodando = False
                return (4,xp)
                
            if player.vida <= 0:
                rodando = False
                return (5,1)
                
        for event in pygame.event.get():
            player.tiro = False
            player.shield = False
            player.carregar = False
            
            if event.type == QUIT:
                rodando = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == K_DOWN:
                    player.shield = True
                    turno += 1
                    action = True
                elif event.key == K_UP:
                    player.carregar = True
                    turno += 1
                    action = True
                elif event.key == K_RIGHT:
                    player.tiro = True
                    turno += 1
                    action = True
    #==========================AI===============================================================
            if turno == 0:
                 computador.shield = True
                 computador.tiro = False
                 computador.carregar = False
            else:
                if random.randint(0,100)<10:
                    computador.shield = True
                else:
                    computador.shield = False
                if random.randint(0,100)<50:
                    computador.tiro = True
                else:
                    computador.tiro = False
                if random.randint(0,100)<30:
                    computador.carregar = True
                else:
                    computador.carregar = False
                    
                if computador.carregar == False and computador.tiro == False and computador.carregar == False:
                    computador.shield = True
    #========================CHECK=================================================================
        else:
            if action:
                if player.tiro:
                    if player.ammo > 0:       
                        if computador.shield:
                            player.ammo -= 1
                        else:
                            computador.vida-=(player.tiro_dano)
                            player.ammo -= 1
                    else:
                        print('No Amooo')
                            
                if player.carregar == True:
                    player.ammo+=1
                
                if computador.tiro == True:
                        if computador.ammo > 0:
                            if player.shield == True:
                                computador.ammo-=1
                            else:
                                player.vida-=(computador.tiro_dano)
                                computador.ammo-=1
                        else:
                            print()
                if computador.carregar == True:
                    computador.ammo += 1
                action = False
    
        relogio.tick(60)
    #=========================ANIMAÇÃO=======================================================================================
        tela.blit(Fundo, (0,0))
        sprite_pokemon.draw(tela)
        health_bars(computador.vida, player.vida)
        menu(player.ammo, 20, 50)
        menu(computador.ammo,670,50)
        turn(turno, 350, 10)
        pygame.display.update()
        pygame.display.flip()
    pygame.display.quit()
    
    
def recu(ide):
    inventario = [vitor, pelicano, fernando, daniel, bobrow, ayres]
    player = inventario[ide]
    player.vida += 100
    
    
    
    
    
    
    
def jogo(num, ide):
    estado = True
    print (estado)
    telo = -1
    tela.blit(Branco, (0,0))
    k=menubatalha(biblio)
    pygame.display.update
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == QUIT:
            rodando = False
                    
            
    while estado:
        for event in pygame.event.get():
            if event.type == QUIT:
                rodando = False
                    
            if event.type == pygame.KEYDOWN:
                if event.key == K_SPACE:
                    telo = 0
        
        if telo == 0:
            u = confronto(k,ide)
            print (u)
            telo = u[0]
        if telo == 4:
            tela.blit(vitoria, (0,0))
            xp(u[1],300,300)
            pygame.display.update
            pygame.display.flip()
            for event in pygame.event.get():
                    
                    
                    if event.type == pygame.KEYDOWN:
                        if event.key == K_SPACE:
                            telo = 6
            
        if telo == 5:
            tela.blit(derrota, (0,0))
            pygame.display.update
            pygame.display.flip()
            for event in pygame.event.get():
                    
                    
                    if event.type == pygame.KEYDOWN:
                        if event.key == K_SPACE:
                            telo = 7
        if telo == 6:
            return num
            estado = False
        
        if telo == 7:
            return num 
            estado = False
        
          