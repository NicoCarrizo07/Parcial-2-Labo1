import pygame
from pygame.locals import *

class Reloj(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(r"Clase23 Video copy 2\assets\images\timer.png").convert_alpha(),(35,35))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)