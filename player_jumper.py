import pygame
from pygame.locals import *
from player import Player
from sprite_sheet import SpriteSheet
from config import *

class PlayerJumper(Player):
    def __init__(self,groups,sprite_sheet:SpriteSheet):
        super().__init__(groups,sprite_sheet)

        self.gravity =1
        self.speed_vertical =0
        self.jump_power = -20

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