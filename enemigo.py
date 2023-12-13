from disparo import *
import pygame
from config import *

class Enemigo(pygame.sprite.Sprite):
    def __init__(self, groups, platform, image_path):
        super().__init__(groups)
        original_image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(original_image, (original_image.get_width() * 1.7, original_image.get_height() * 1.7))
        self.rect = self.image.get_rect()
        self.rect.centerx = platform.rect.centerx + 10
        self.rect.bottom = platform.rect.top +5
        self.shoot_timer = 0
        self.can_shoot = True
        self.proyectiles = [] 
        self.mask = pygame.mask.from_surface(self.image)
        self.playing_music = True

    def update(self):
        self.shoot_timer += 1
        if self.shoot_timer >= 5 * FPS:
            self.shoot()
            self.shoot_timer = 0

        for proyectil in self.proyectiles:
            proyectil_rect = proyectil[1] 
            proyectil_rect.x -= 5 

    def shoot(self):
        proyectil_image = pygame.image.load(r"Clase23 Video copy 2\assets\images\flecha.png").convert_alpha()
        proyectil_rect = proyectil_image.get_rect()
        proyectil_rect.center = self.rect.center 
        self.proyectiles.append((proyectil_image, proyectil_rect))
        sound_shoot_enemy = pygame.mixer.Sound(r"Clase23 Video copy 2\assets\sounds\blaster-2-81267.mp3")
        if self.playing_music:
            sound_shoot_enemy.play()

    def move(self, amount):
        self.rect.x += amount  
