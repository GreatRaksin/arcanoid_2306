import pygame
from pygame.locals import *


# создадим класс мячик
class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface((15, 15))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)



