import pygame
from pygame.locals import *


# создадим класс мячик
class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, color, s_width, platform, bricks):
        super().__init__()
        self.image = pygame.Surface((15, 15))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed_x = 3
        self.speed_y = -3
        self.s_width = s_width
        self.platform = platform
        self.bricks = bricks

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # отскок от стенок
        if self.rect.x <= 0 or self.rect.x >= self.s_width:
            self.speed_x *= -1
        if self.rect.top <= 0:
            self.speed_y *= -1

        # проверка столкновения с платформой
        if pygame.sprite.collide_rect(self, self.platform):
            self.speed_y *= -1

        # проверка столкновения с кирпичами
        brick_hit_list = pygame.sprite.spritecollide(self, self.bricks, True)
        if len(brick_hit_list) > 0:
            self.speed_y *= -1


class Platform(pygame.sprite.Sprite):
    def __init__(self, color, s_width, s_height):
        super().__init__()
        self.image = pygame.Surface((80, 10))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.centerx = s_width // 2
        self.rect.bottom = s_height - 20
        self.speed_x = 0
        self.s_width = s_width

    def update(self):
        self.rect.x += self.speed_x

        # ограничиваем движение
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > self.s_width:
            self.rect.right = self.s_width


class Brick(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface((60, 20))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

