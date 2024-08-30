import pygame
import random
import math
pygame.init()

SCREEN_WIDTH = 990
SCREEN_HEIGHT = 1000
TILE_SIZE = 45
speed = 9.0
timeToComplete = 60
flags = pygame.RESIZABLE
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT),flags)
background_image = pygame.image.load('bg.png')
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()

def respawn_sprite_at_random_position(sprite_rect, walls, tile_size, screen_width, screen_height):
    possible_positions = []

    for x in range(0, screen_width, tile_size):
        for y in range(0, screen_height, tile_size):
            potential_rect = pygame.Rect(x, y, tile_size, tile_size)
            if not any(wall.colliderect(potential_rect) for wall in walls):
                possible_positions.append((x, y))

    if possible_positions:
        new_position = random.choice(possible_positions)
        sprite_rect.topleft = new_position






def gameStart(speed):
    run = True      
    ossz = 0
    font = pygame.font.Font(None, 36)

    

    start_time = pygame.time.get_ticks()


    # Szöveges térkép
    level_map = [
        "wwwwwwwwwwwwwwwwwwwwww",
        "w00000000000000000000w",
        "w0000000000000000000Pw",
        "w00000000000000000000w",
        "w000000000P0000000000w",
        "wwwwwwwwwwwwwwwwww000w",
        "w00000000000000000000w",
        "w000000000S00000B00Z0w",
        "w00000000000000000000w",
        "w00000000000000000000w",
        "wwwww000wwwwwwwwwwwwww",
        "w00000000000000000000w",
        "w00000000000000000000w",
        "w00000000000000000000w",
        "wwwwwwwwwwwwwwwww000ww",
        "w00000000000000000000w",
        "w00000000000000000000w",
        "w00000000000000000000w",
        "wwww000wwwwwwwwwwwwwww",
        "w00000000000000000000w",
        "w00000000000000000000w",
        "wwwwwwwwwwwwwwwwwwwwww",
        "wwwwwwwwwwwwwwwwwwwwww",
    ]

    # Falak és a játékos inicializálása
    walls = []
    bogi_rect = None
    puca_rect = None
    zsu_rect = None
    sac_rekt = None

    # Játékos képének betöltése és méretezése
    bogi_image = pygame.image.load('bogi.png')
    bogi_image = pygame.transform.scale(bogi_image, (TILE_SIZE, TILE_SIZE))

    puca_image = pygame.image.load('Puca.png')
    puca_image = pygame.transform.scale(puca_image, (TILE_SIZE, TILE_SIZE))

    zsu_image = pygame.image.load('Zsu.png')
    zsu_image = pygame.transform.scale(zsu_image, (TILE_SIZE, TILE_SIZE))

    sac_image = pygame.image.load('sac.png')
    sac_image = pygame.transform.scale(sac_image, (TILE_SIZE, TILE_SIZE))

    for row_index, row in enumerate(level_map):
        for col_index, cell in enumerate(row):
            x = col_index * TILE_SIZE
            y = row_index * TILE_SIZE
            if cell == "w":
                wall = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)
                walls.append(wall)
            elif cell == "B":
                bogi_rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)
            elif cell == "Z":
                zsu_rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)
            elif cell == "P":
                puca_rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)
            elif cell == "S":
                sac_rekt = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)

    for i in walls:
        print(i)
    while run:
        clock.tick(60)
        current_time = pygame.time.get_ticks()
        elapsed_time = (current_time - start_time) // 1000
        timer_surface = font.render(f'Time: {timeToComplete - elapsed_time} s', True, (255, 0, 255))
        screen.blit(background_image, (0, 0))

        # Falak kirajzolása
        for wall in walls:
            pygame.draw.rect(screen, (255, 255, 255), wall)
        screen.blit(timer_surface, (600, 10))
        # Játékos kirajzolása
        screen.blit(bogi_image, bogi_rect.topleft)
        screen.blit(puca_image, puca_rect.topleft)
        screen.blit(zsu_image, zsu_rect.topleft)
        screen.blit(sac_image, sac_rekt.topleft)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        key = pygame.key.get_pressed()
        move_x, move_y = 0.0, 0.0
        if key[pygame.K_a]:  # balra
            move_x = -speed
        if key[pygame.K_d]:  # jobbra
            move_x = speed
        if key[pygame.K_w]:  # felfele
            move_y = -speed
        if key[pygame.K_s]:  # lefele
            move_y = speed
        
        # if move_x != 0 and move_y != 0:
        #     move_x = math.floor(move_x / 1.414)  # Gyök 2-vel osztva (Pitagorasz tétele)
        #     move_y = math.floor(move_y / 1.414)
        

        for _ in range(int(speed)):

            oldBogi = bogi_rect.copy()
            bogi_rect.move_ip(move_x / abs(speed), move_y / abs(speed))

            # Collision correction
            for wall in walls:
                if bogi_rect.colliderect(wall):
                    if move_x > 0:  # Moving right; Hit the left side of the wall
                        bogi_rect.right = wall.left
                    elif move_x < 0:  # Moving left; Hit the right side of the wall
                        bogi_rect.left = wall.right
                    elif move_y > 0:  # Moving down; Hit the top side of the wall
                        bogi_rect.bottom = wall.top
                    elif move_y < 0:  # Moving up; Hit the bottom side of the wall
                        bogi_rect.top = wall.bottom


            if abs(bogi_rect.x - oldBogi.x) > speed or abs(bogi_rect.y - oldBogi.y) > speed:
                bogi_rect = oldBogi.copy()


        # Ütközésdetektálás
            
        if bogi_rect.colliderect(zsu_rect):
            osszbasz += 1
            speed += 2.0
            respawn_sprite_at_random_position(zsu_rect, walls, TILE_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT)

        if bogi_rect.colliderect(puca_rect):
            osszbasz += 1
            speed += 1.0
            respawn_sprite_at_random_position(puca_rect, walls, TILE_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT)

        if bogi_rect.colliderect(sac_rekt):
            osszbasz += 1
            speed += -1.0
            respawn_sprite_at_random_position(sac_rekt, walls, TILE_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT)

        if speed == 0: #ne alljunk mar meg azert lol 
            speed = 1

        if speed > 15: #kicsit talan tul gyorsak vagyunk
            speed = 15


        counter_surface = font.render(f'Girls {ossz}', True, (255, 0, 0))
        screen.blit(counter_surface, (800, 10))

        if elapsed_time == timeToComplete:
            game_over(ossz)
        pygame.display.update()


def game_over(ossz):
    while(True):
        screen.blit(background_image, (0, 0))
        font = pygame.font.Font(None, 150)
        counter_surface = font.render(f'Girls {ossz}', True, (255, 0, 0))
        counter_surfaceTime = font.render(f'Restarting in 5...', True, (255, 0, 0))
        screen.blit(counter_surface, (50, 400))
        screen.blit(counter_surfaceTime, (50, 600))
        pygame.display.update()
        pygame.time.delay(5000)
        gameStart(speed)
        # key = pygame.key.get_pressed()
        # print("iamhere")
        # if key[pygame.K_a]:
        #     pygame.quit()

gameStart(speed)

pygame.quit()
