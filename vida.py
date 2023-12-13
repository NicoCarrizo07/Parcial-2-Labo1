from config import *
import pygame

class Vida(pygame.sprite.Sprite):
    def __init__(self, x, y, image_sequence,animation_speed=7):
        super().__init__()
        self.image_sequence = image_sequence  
        self.current_frame = 0  
        self.image = self.image_sequence[self.current_frame]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = x
        self.rect.y = y
        self.animation_speed = animation_speed  
        self.timer = 0  

    def update(self):
        self.timer += 1
        if self.timer >= self.animation_speed:
            self.timer = 0
            self.current_frame = (self.current_frame + 1) % len(self.image_sequence)
            self.image = self.image_sequence[self.current_frame]