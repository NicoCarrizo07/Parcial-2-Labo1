import pygame
from config import *

class Lava(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.image = pygame.transform.scale(image, (WIDTH +50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = -10
        self.rect.y = HEIGHT - 50  # posicion
        self.mask = pygame.mask.from_surface(self.image)
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def check_collision(self, player):
        if self.rect.colliderect(player.rect):
            terminar()