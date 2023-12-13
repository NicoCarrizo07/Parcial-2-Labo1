import pygame
from pygame.locals import *
from config import *
from sprite_sheet import *
from sprite_sheet import SpriteSheet

class Player(pygame.sprite.Sprite): #heredar de Sprite
    def __init__(self,groups,sprite_sheet): #constructor de la clase hija
        super().__init__(groups) #contructor de la clase padre
        self.animatios = sprite_sheet.get_animatios_dict(scale=0.4) # tam personaje
        self.current_sprite = 0
        self.image = self.animatios["right"][self.current_sprite]
        self.rect = self.image.get_rect(topleft = (0,0))
        self.mask = pygame.mask.from_surface(self.image)
        self.speed = 5
        self.last_update = pygame.time.get_ticks()
        self.time_animation = 100
        self.gravity =1
        self.speed_vertical =0
        self.jump_power = -20
        self.player_projectiles_group = pygame.sprite.Group()
        self.visible_rect = pygame.Rect(0, 0, 32, 48)

    def draw(self):
        ...

    def update(self) -> None:
        
        self.speed_vertical += GRAVITY

        self.rect.y += self.speed_vertical

        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT
            self.speed_vertical =0
            

        keys = pygame.key.get_pressed()
        if keys[K_RIGHT]:
            if self.rect.right <= WIDTH: #no se vaya de pantalla
                self.rect.x += self.speed
                current_time = pygame.time.get_ticks()
                if current_time - self.last_update >= self.time_animation:
                    self.current_sprite +=1
                    self.image = self.animatios["right"][self.current_sprite]
                    if self.current_sprite ==3:
                        self.current_sprite =0
                    self.last_update = current_time

        if keys[K_LEFT]:
            if self.rect.x >= 0:
                self.rect.x -= self.speed
                current_time = pygame.time.get_ticks()
                if current_time - self.last_update >= self.time_animation:
                    self.current_sprite +=1
                    self.image = self.animatios["left"][self.current_sprite]
                    if self.current_sprite ==3:
                        self.current_sprite =0
                    self.last_update = current_time
        

    def jump(self):
        self.speed_vertical = self.jump_power