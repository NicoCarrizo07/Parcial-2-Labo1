import pygame
from config import *

class Boss(pygame.sprite.Sprite):
    def __init__(self, groups, x, y, image_sequence,animation_speed):
        super().__init__(groups)
        self.image_sequence = image_sequence 
        self.image_index = 0  #indice de la imagen actual en la secuencia
        self.image = self.image_sequence[self.image_index]  # imagen inicial
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.shoot_timer = 0
        self.can_shoot = True
        self.proyectiles = []
        self.playing_music = True
        self.animation_speed = animation_speed
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.shoot_timer += 1
        if self.shoot_timer >= 2 * FPS:
            self.shoot()
            self.shoot_timer = 0

        #actualizar y mover los proyectiles
        for proyectil in self.proyectiles:
            proyectil_rect = proyectil[1]
            proyectil_rect.x += 15  

        self.animation_speed -= 1
        if self.animation_speed <= 0:
            #actualizar la animacion cambiando la imagen en la secuencia
            self.image_index = (self.image_index + 1) % len(self.image_sequence)
            self.image = self.image_sequence[self.image_index]
            self.animation_speed = FPS  # reinicia el contador de velocidad

    def shoot(self):
        #creo y lanzo el proyecyil del boss
        proyectil_image = pygame.image.load(r"Clase23 Video copy 2\assets\images\boss\10.png").convert_alpha()  
        proyectil_rect = proyectil_image.get_rect()
        proyectil_rect.center = self.rect.center  # (centro del enemigo) desde donde sale el proyectil
        self.proyectiles.append((proyectil_image, proyectil_rect))
        sound_shoot_enemy = pygame.mixer.Sound(r"Clase23 Video copy 2\assets\sounds\dragon_sound.mp3")
        if self.playing_music:
            sound_shoot_enemy.play()

    def move(self, amount_x, amount_y):
        self.rect.x += amount_x 
        self.rect.y += amount_y  

    def draw(self, screen):
        screen.blit(self.image, self.rect)