import pygame
from pygame.locals import *
from config import *

class Platform(pygame.sprite.Sprite):
    def __init__(self, groups, rectangulo, image_path = r"Clase23 Video copy/assets/images/2dplatform.png" ): 
        super().__init__(groups)
        self.image = pygame.Surface((rectangulo[2], rectangulo[3]))
        self.rect = self.image.get_rect(topleft=(rectangulo[0], rectangulo[1]))
        self.mask = pygame.mask.from_surface(self.image)
        self.image = pygame.image.load(image_path) 
        self.image = pygame.transform.scale(self.image, (rectangulo[2], rectangulo[3])) 
