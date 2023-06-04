
from settings import *
from settings import Player
from map import *
pygame.init()
sc = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

player = Player()

world_map = set()
for j, row in enumerate(text_map1):
    for i, char in enumerate(row):
        if char == 'W':
            world_map.add((i * TILE, j * TILE))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    player.movement()
    sc.fill(BLACK)

    pygame.draw.rect(sc, BLUE, (0, 0, width, spawn_y))
    pygame.draw.rect(sc, DARKGRAY, (0, spawn_y, width, spawn_y))

    def ray_casting(sc, player_pos, player_angle):
        cur_angle = player_angle - HALF_FOV
        xo, yo = player_pos
        for ray in range(NUM_RAYS):
            sin_a = math.sin(cur_angle)
            cos_a = math.cos(cur_angle)
            for depth in range(MAX_DEPTH):
                x = xo + depth * cos_a
                y = yo + depth * sin_a
                if (x // TILE * TILE, y // TILE * TILE) in world_map:
                    depth *= math.cos(player_angle - cur_angle)
                    proj_height = min(PROJ_COEFF / (depth + 0.0001), height)
                    c = 255 / (1 + depth * depth * 0.0001)
                    color = (c, c // 2, c // 2)
                    pygame.draw.rect(sc, color, (ray * SCALE,
                                                 spawn_y - proj_height // 2,
                                                 SCALE, proj_height))
                    break
            cur_angle += DELTA_ANGLE

    ray_casting(sc, player.pos, player.angle)

    pygame.display.flip()
    clock.tick(FPS)
