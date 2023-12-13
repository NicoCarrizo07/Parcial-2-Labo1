import pygame
from config import *

class Proyectil(pygame.sprite.Sprite):
    def __init__(self, groups, pos, direction, image_path=r"Clase23 Video copy 2\assets\images\00 (1).png"):
        super().__init__(groups)
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(center=pos)
        self.speed = 8  #velocidad del proyectil
        self.direction = direction  

        if direction == "right":  #voltear la imagen si se dispara hacia la derecha
            self.image = pygame.transform.flip(self.image, True, False)

        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        if self.direction == "left":
            self.rect.x -= self.speed
        elif self.direction == "right":
            self.rect.x += self.speed

        #elimina el proyectil si sale de la pantalla
        if self.rect.right < 0 or self.rect.left > WIDTH:
            self.kill()