from plataforma import Platform
from config import *
import pygame

class PlataformaMovil(Platform):
    def __init__(self, grupos, rect, imagen):
        super().__init__(grupos, rect)
        self.image = imagen  
        self.rect = self.image.get_rect(topleft=rect[:2]) 
        self.speed = 2  
        self.direction = 1  #dirección inicial (1 para mover hacia abajo -1 para mover hacia arriba)

    def update(self):
        self.rect.y += self.speed * self.direction 
        #cambia la dirección si alcanza el límite superior o inferior
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.direction *= -1

    def draw(self, screen):
        screen.blit(self.image, self.rect)