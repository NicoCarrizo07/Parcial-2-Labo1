import pygame
import random
from config import *

class Meteorito(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(r"Clase23 Video copy 2\assets\images\meteorito.png").convert_alpha(),(30,30))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.rect.width)  
        self.rect.y = random.randint(-100, -50)  
        self.speed = 8  # velocidad de caída

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > HEIGHT:  #si el meteorito sale de la pantalla resetea su posición
            self.rect.x = random.randint(0, WIDTH - self.rect.width)
            self.rect.y = random.randint(-100, -50)