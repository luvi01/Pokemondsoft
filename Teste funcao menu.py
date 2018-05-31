# -*- coding: utf-8 -*-
"""
Created on Mon May 28 16:32:24 2018

@author: luvi01
"""
from random import randint
class Pokemon(pygame.sprite.Sprite):
    def __init__(self, imagemplayer, vida, escudo, tiro, xp, nivel):
        pygame.sprite.Sprite.__init__(self)
        self.nivel = nivel
        self.image = pygame.image.load(imagemplayer)
        self.rect = self.image.get_rect()
        self.vida = vida*self.nivel
        self.escudo = escudo*self.nivel
        self.tiro = tiro*self.nivel
        self.xp = xp
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
b=menubatalha(inventario, biblio)
print (b[10])