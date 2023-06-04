
import pygame
import math
# настройки игры
width = 1280
height = 800
spawn_x = width // 2
spawn_y = height // 2
FPS = 60
TILE = 100
# настройки рейкастинга
FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = 128
MAX_DEPTH = 800
DELTA_ANGLE = FOV / NUM_RAYS
DIST = NUM_RAYS / (2 * math.tan(HALF_FOV))
PROJ_COEFF = 3 * DIST * TILE
SCALE = width // NUM_RAYS
# настройки наблюдателя
player_pos = (spawn_x, spawn_y)
player_angle = 0
player_speed = 2


class Player:
    def __init__(self):
        self.x, self.y = player_pos
        self.angle = player_angle

    @property
    def pos(self):
        return (self.x, self.y)

    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.x += player_speed * cos_a
            self.y += player_speed * sin_a
        if keys[pygame.K_s]:
            self.x += -player_speed * cos_a
            self.y += -player_speed * sin_a
        if keys[pygame.K_a]:
            self.angle -= 0.02
        if keys[pygame.K_d]:
            self.angle += 0.02

# цвета


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 0, 0)
GREEN = (0, 220, 0)
BLUE = (0, 0, 255)
DARKGRAY = (40, 40, 40)
PURPLE = (120, 0, 120)
