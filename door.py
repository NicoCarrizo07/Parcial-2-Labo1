import pygame
from config import *

class Door(pygame.sprite.Sprite):
    def __init__(self, image_sequence ,initial_position=(680, 107)):
        super().__init__()
        self.image_sequence = image_sequence
        self.current_frame = -4
        self.animation_speed = 15.0
        self.image = self.image_sequence[self.current_frame]
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.rect.topleft = initial_position 
        self.visible = True 
        self.active = False  #flag para activar la secuencia de imágenes

    def update(self):
        if self.active:
            self.current_frame += 1
            if self.current_frame >= len(self.image_sequence):
                self.current_frame = len(self.image_sequence) - 1
                self.image = self.image_sequence[self.current_frame]
            else:
                self.image = self.image_sequence[self.current_frame]

    def activate(self):
        if not self.active:  # si no esta activo para evitar ocultar la imagen inmediatamente
            self.active = True
            self.visible = False
        
    