import sys
import pygame as pg
from objects import Brick, Ball, Platform
from pygame.locals import *

W = 640
H = 480

pg.init()  # инициализируем pygame
screen = pg.display.set_mode((W, H))  # создаем экран игры разрешением 1280х720px
clock = pg.time.Clock()
FPS = 60

bricks = pg.sprite.Group()
# создаем кирпичики
for row in range(5):
    for col in range(8):
        brick = Brick(75 * col + 10, 30 * row + 40, (255, 0, 0))
        bricks.add(brick)

# создание экземпляров Ball и Platform
platform = Platform((0, 0, 255), W, H)
ball = Ball(W // 2, H // 2, (0, 255, 0), W, platform, bricks)


all_sprites = pg.sprite.Group()
all_sprites.add(ball)
all_sprites.add(bricks)
all_sprites.add(platform)

while True:  # цикл игры
    for event in pg.event.get():  # обработчик событий pygame
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                platform.speed_x = -5
            elif event.key == K_RIGHT:
                platform.speed_x = 5
        elif event.type == KEYUP:
            if event.key in [K_LEFT, K_RIGHT]:
                platform.speed_x = 0

    all_sprites.update()
    screen.fill((255, 255, 255))
    all_sprites.draw(screen)
    pg.display.flip()
    clock.tick(FPS)