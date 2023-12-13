import pygame
from config import *

class SpriteSheet:
    def __init__(self,sheet,rows,cols,width,height,keys=None):
        self.sheet = sheet
        self.width = self.sheet.get_width()
        self.height = self.sheet.get_height()
        self.rows = rows
        self.cols = cols
        self.width_sprite = width
        self.height_sprite = height
        self.keys = keys

    def get_animatios(self,scale =1):

        self.width = scale  * self.width
        self.height = scale  * self.height
        self.width_sprite = scale *self.width_sprite
        self.height_sprite = scale * self.height_sprite



        self.sheet = pygame.transform.scale(self.sheet,(self.width, self.height))
        contador_cols = 0
        animation_list = []

        for row in range(self.rows):
            animation_row = []
            for _ in range(self.cols):
                animation_row.append(self.sheet.subsurface((contador_cols *self.width_sprite,row * self.height_sprite ,
                self.width_sprite,self.height_sprite)))
                contador_cols +=1

            contador_cols = 0
            animation_list.append(animation_row)
        
        return animation_list
    
    def get_animatios_dict(self,scale =1):

        self.width = scale  * self.width
        self.height = scale  * self.height
        self.width_sprite = scale *self.width_sprite
        self.height_sprite = scale * self.height_sprite

        self.sheet = pygame.transform.scale(self.sheet,(self.width, self.height))
        contador_cols = 0
        animation_dict = {}

        for row in range(self.rows):
            animation_row = []
            for _ in range(self.cols):
                animation_row.append(self.sheet.subsurface((contador_cols *self.width_sprite,row * self.height_sprite ,
                self.width_sprite,self.height_sprite)))
                contador_cols +=1

            animation_dict[self.keys[row]]=animation_row
            contador_cols = 0

        return animation_dict