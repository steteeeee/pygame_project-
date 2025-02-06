import pygame
import random
import sys
from button import ImageButton
pygame.init()
WIDTH, HEIGHT = 800, 600
MAX_FPS = 60
screen = pygame.display.set_mode((WIDTH, HEIGHT), flags=pygame.NOFRAME)
main_background = pygame.image.load("sprites/go1.png")
clock = pygame.time.Clock()


def main_menu():
    start_button = ImageButton(WIDTH/2-(300/2), 150, 300, 74, "Новая игра", "sprites/green_button2.jpg")
    settings_button = ImageButton(WIDTH/2-(300/2), 250, 300, 74, "Выбор уровня", "sprites/green_button2.jpg")
    exit_button = ImageButton(WIDTH/2-(300/2), 350, 300, 74, "Выйти", "sprites/green_button2.jpg")
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(main_background, (0, 0))
        font = pygame.font.Font(None, 72)
        text_surface = font.render("МЕНЮ", True, (200, 255, 200))
        text_rect = text_surface.get_rect(center=(WIDTH/2, 50))
        screen.blit(text_surface, text_rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.USEREVENT and event.button == start_button:
                new_game()
            if event.type == pygame.USEREVENT and event.button == settings_button:
                urovni_menu()
            if event.type == pygame.USEREVENT and event.button == exit_button:
                pygame.quit()
                sys.exit()
            for btn in [start_button, settings_button, exit_button]:
                btn.handle_event(event)
        for btn in [start_button, settings_button, exit_button]:
            btn.draw(screen)
        pygame.display.flip()


def urovni_menu():
    button1 = ImageButton(WIDTH / 2 - (300 / 2), 100, 300, 74, "1", "sprites/green_button2.jpg")
    button2 = ImageButton(WIDTH / 2 - (300 / 2), 200, 300, 74, "2", "sprites/green_button2.jpg")
    button3 = ImageButton(WIDTH / 2 - (300 / 2), 300, 300, 74, "3", "sprites/green_button2.jpg")
    button4 = ImageButton(WIDTH / 2 - (300 / 2), 400, 300, 74, "4", "sprites/green_button2.jpg")
    back_button = ImageButton(WIDTH / 2 - (300 / 2), 500, 300, 74, "Назад", "sprites/green_button2.jpg")
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(main_background, (0, 0))
        font = pygame.font.Font(None, 72)
        text_surface = font.render("Выбор уровня", True, (200, 255, 200))
        text_rect = text_surface.get_rect(center=(WIDTH / 2, 50))
        screen.blit(text_surface, text_rect)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.USEREVENT and event.button == back_button:
                main_menu()
            if event.type == pygame.USEREVENT and event.button == button1:
                new_game1()
            if event.type == pygame.USEREVENT and event.button == button2:
                new_game3()
            if event.type == pygame.USEREVENT and event.button == button3:
                new_game2()
            if event.type == pygame.USEREVENT and event.button == button4:
                new_game5()
            for btn in [button1, button2, button3, button4, back_button]:
                btn.handle_event(event)
        for btn in [button1, button2, button3, button4, back_button]:
            btn.draw(screen)
        pygame.display.flip()


def proigrish():
    settings_button = ImageButton(WIDTH / 2 - (300 / 2), 250, 300, 74, "Меню", "sprites/green_button2.jpg")
    exit_button = ImageButton(WIDTH / 2 - (300 / 2), 350, 300, 74, "Выйти", "sprites/green_button2.jpg")
    running = True
    while running:
        screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 100)
        text_surface = font.render("Game Over", True, (200, 255, 200))
        text_rect = text_surface.get_rect(center=(WIDTH / 2, 150))
        screen.blit(text_surface, text_rect)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.USEREVENT and event.button == settings_button:
                main_menu()
            if event.type == pygame.USEREVENT and event.button == exit_button:
                pygame.quit()
                sys.exit()
            for btn in [settings_button, exit_button]:
                btn.handle_event(event)
        for btn in [settings_button, exit_button]:
            btn.draw(screen)
        pygame.display.flip()


def pobeda(r):
    settings_button = ImageButton(WIDTH / 2 - (300 / 2), 300, 300, 74, "Меню", "sprites/green_button2.jpg")
    save = ImageButton(WIDTH / 2 - (300 / 2), 400, 300, 74, "Сохранить результат", "sprites/green_button2.jpg")
    exit_button = ImageButton(WIDTH / 2 - (300 / 2), 500, 300, 74, "Выйти", "sprites/green_button2.jpg")
    running = True
    while running:
        screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 80)
        text_surface = font.render("Вы прошли этот уровень!", True, (200, 255, 200))
        text_rect = text_surface.get_rect(center=(WIDTH / 2, 100))
        text_surface2 = font.render(f'Ваш результат: {str(r)}', True, (200, 255, 200))
        text_rect2 = text_surface2.get_rect(center=(WIDTH / 2, 200))
        screen.blit(text_surface, text_rect)
        screen.blit(text_surface2, text_rect2)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.USEREVENT and event.button == settings_button:
                main_menu()
            if event.type == pygame.USEREVENT and event.button == save:
                saved(r)
            if event.type == pygame.USEREVENT and event.button == exit_button:
                pygame.quit()
                sys.exit()
            for btn in [settings_button, exit_button, save]:
                btn.handle_event(event)
        for btn in [settings_button, exit_button, save]:
            btn.draw(screen)
        pygame.display.flip()


def new_game():
    last_event_time = pygame.time.get_ticks()
    event_interval = 1000
    pygame.init()
    width, height = 800, 600
    player_size = 50
    player_pos = [width / 2 - 20, height / 2 + 100]
    enemy_size = 50
    enemy_pos = [random.randint(0, width - enemy_size), 0]
    enemy_speed = 10
    go_left = [pygame.image.load(f'sprites/{i}.jpg') for i in [1, 2, 3, 4]]
    go_right = [pygame.image.load(f'sprites/{i}.jpg') for i in [5, 6, 7, 8]]
    go_down = [pygame.image.load(f'sprites/{i}.jpg') for i in [13, 11, 14, 12]]
    go_up = [pygame.image.load(f'sprites/{i}.jpg') for i in [15, 9, 16, 10]]
    dcounter = 0
    count = 0
    k = 0
    kk = 0
    r = 0
    game_over = False
    while not game_over:
        if dcounter == 15:
            pobeda(r)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_over = True
            if event.type == pygame.QUIT:
                game_over = True
        current_time = pygame.time.get_ticks()
        if current_time - last_event_time >= event_interval:
            dcounter += 1
            last_event_time = current_time
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_pos[0] > 0:
            r += 1
            player_pos[0] -= 5
            k = 1
            kk = 0
        elif (not (keys[pygame.K_LEFT] and player_pos[0] > 0)) and kk == 0:
            k = 5
            kk = 0
        if keys[pygame.K_RIGHT] and player_pos[0] < width - player_size:
            player_pos[0] += 5
            r += 1
            k = 2
            kk = 1
        elif (not (keys[pygame.K_RIGHT] and player_pos[0] < width - player_size)) and kk == 1:
            k = 6
            kk = 0
        if keys[pygame.K_UP] and player_pos[1] > 0:
            player_pos[1] -= 5
            r += 1
            k = 3
            kk = 2
        elif (not (keys[pygame.K_UP] and player_pos[1] > 0)) and kk == 2:
            k = 7
            kk = 0
        if keys[pygame.K_DOWN] and player_pos[1] < height - player_size:
            r += 1
            player_pos[1] += 5
            k = 4
            kk = 3
        elif (not (keys[pygame.K_DOWN] and player_pos[1] < height - player_size)) and kk == 3:
            k = 8
            kk = 0
        enemy_pos[1] += enemy_speed
        if enemy_pos[1] >= height:
            enemy_pos[1] = 0
            enemy_pos[0] = random.randint(0, width - enemy_size)
        if (player_pos[0] < enemy_pos[0] < player_pos[0] + player_size) or (
                player_pos[0] < enemy_pos[0] + enemy_size < player_pos[0] + player_size):
            if (player_pos[1] < enemy_pos[1] < player_pos[1] + player_size) or (
                    player_pos[1] < enemy_pos[1] + enemy_size < player_pos[1] + player_size):
                game_over = True
        screen.fill((0, 0, 0))
        if k == 1:
            screen.blit(go_left[count], (player_pos[0], player_pos[1]))
        elif k == 2:
            screen.blit(go_right[count], (player_pos[0], player_pos[1]))
        elif k == 3:
            screen.blit(go_up[count], (player_pos[0], player_pos[1]))
        elif k == 4:
            screen.blit(go_down[count], (player_pos[0], player_pos[1]))
        elif k == 5:
            screen.blit(pygame.image.load('sprites/1.jpg'), (player_pos[0], player_pos[1]))
        elif k == 6:
            screen.blit(pygame.image.load('sprites/5.jpg'), (player_pos[0], player_pos[1]))
        elif k == 7:
            screen.blit(pygame.image.load('sprites/11.jpg'), (player_pos[0], player_pos[1]))
        elif k == 8:
            screen.blit(pygame.image.load('sprites/9.jpg'), (player_pos[0], player_pos[1]))
        if k in [1, 2, 3, 4]:
            count = (count + 1) % 4
            k = 0
        pygame.draw.rect(screen, (255, 0, 0), (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))
        pygame.display.flip()
        clock.tick(60)
    if game_over:
        proigrish()


def new_game2():
    pygame.init()
    last_event_time1 = pygame.time.get_ticks()
    event_interval1 = 1000
    width, height = 800, 600
    player_size = 50
    player_pos = [width / 2 - 20, height / 2 + 100]
    enemy_size = 50
    go_left = [pygame.image.load(f'sprites/{i}.jpg') for i in [1, 2, 3, 4]]
    go_right = [pygame.image.load(f'sprites/{i}.jpg') for i in [5, 6, 7, 8]]
    go_down = [pygame.image.load(f'sprites/{i}.jpg') for i in [13, 11, 14, 12]]
    go_up = [pygame.image.load(f'sprites/{i}.jpg') for i in [15, 9, 16, 10]]
    enemy_speed = 8
    enemy_speed1 = 8
    enemy_speed2 = 8
    enemy_speed3 = 8
    enemy_pos = [random.randint(0, width - enemy_size), 0]
    enemy_direction = "down"
    enemy_pos1 = [random.randint(0, width - enemy_size), height]
    enemy_direction1 = "up"
    enemy_pos2 = [width, random.randint(0, height - enemy_size)]
    enemy_direction2 = "left"
    enemy_pos3 = [0, random.randint(0, height - enemy_size)]
    enemy_direction3 = "right"
    count = 0
    k = 0
    kk = 0
    ddcounter = 0
    r = 0
    game_over = False
    while not game_over:
        if ddcounter == 10:
            pobeda(r)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_over = True
            if event.type == pygame.QUIT:
                game_over = True
        current_time1 = pygame.time.get_ticks()
        if current_time1 - last_event_time1 >= event_interval1:
            ddcounter += 1
            last_event_time1 = current_time1
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_pos[0] > 0:
            player_pos[0] -= 5
            r += 1
            k = 1
            kk = 0
        elif (not (keys[pygame.K_LEFT] and player_pos[0] > 0)) and kk == 0:
            k = 5
            kk = 0
        if keys[pygame.K_RIGHT] and player_pos[0] < width - player_size:
            player_pos[0] += 5
            r += 1
            k = 2
            kk = 1
        elif (not (keys[pygame.K_RIGHT] and player_pos[0] < width - player_size)) and kk == 1:
            k = 6
            kk = 0
        if keys[pygame.K_UP] and player_pos[1] > 0:
            player_pos[1] -= 5
            r += 1
            k = 3
            kk = 2
        elif (not (keys[pygame.K_UP] and player_pos[1] > 0)) and kk == 2:
            k = 7
            kk = 0
        if keys[pygame.K_DOWN] and player_pos[1] < height - player_size:
            r += 1
            player_pos[1] += 5
            k = 4
            kk = 3
        elif (not (keys[pygame.K_DOWN] and player_pos[1] < height - player_size)) and kk == 3:
            k = 8
            kk = 0
        for enemy, speed, direction in [(enemy_pos, enemy_speed, enemy_direction),
                                        (enemy_pos1, enemy_speed1, enemy_direction1),
                                        (enemy_pos2, enemy_speed2, enemy_direction2),
                                        (enemy_pos3, enemy_speed3, enemy_direction3)]:
            if direction == "down":
                enemy[1] += speed
                if enemy[1] >= height:
                    enemy[1] = 0
                    enemy[0] = random.randint(0, width - enemy_size)
            elif direction == "up":
                enemy[1] -= speed
                if enemy[1] <= 0:
                    enemy[1] = height
                    enemy[0] = random.randint(0, width - enemy_size)
            elif direction == "left":
                enemy[0] -= speed
                if enemy[0] <= 0:
                    enemy[0] = width
                    enemy[1] = random.randint(0, height - enemy_size)
            elif direction == "right":
                enemy[0] += speed
                if enemy[0] >= width:
                    enemy[0] = 0
                    enemy[1] = random.randint(0, height - enemy_size)
        if any(player_pos[0] < e[0] + enemy_size and player_pos[0] + player_size > e[0] and
               player_pos[1] < e[1] + enemy_size and player_pos[1] + player_size > e[1]
               for e in [enemy_pos, enemy_pos1, enemy_pos2, enemy_pos3]):
            game_over = True
        screen.fill((0, 0, 0))
        if k == 1:
            screen.blit(go_left[count], (player_pos[0], player_pos[1]))
        elif k == 2:
            screen.blit(go_right[count], (player_pos[0], player_pos[1]))
        elif k == 3:
            screen.blit(go_up[count], (player_pos[0], player_pos[1]))
        elif k == 4:
            screen.blit(go_down[count], (player_pos[0], player_pos[1]))
        elif k == 5:
            screen.blit(pygame.image.load('sprites/1.jpg'), (player_pos[0], player_pos[1]))
        elif k == 6:
            screen.blit(pygame.image.load('sprites/5.jpg'), (player_pos[0], player_pos[1]))
        elif k == 7:
            screen.blit(pygame.image.load('sprites/11.jpg'), (player_pos[0], player_pos[1]))
        elif k == 8:
            screen.blit(pygame.image.load('sprites/9.jpg'), (player_pos[0], player_pos[1]))
        if k in [1, 2, 3, 4]:
            count = (count + 1) % 4
            k = 0
        for enemy in [enemy_pos, enemy_pos1, enemy_pos2, enemy_pos3]:
            pygame.draw.rect(screen, (255, 0, 0), (enemy[0], enemy[1], enemy_size, enemy_size))
        pygame.display.flip()
        clock.tick(60)
    if game_over:
        proigrish()


def new_game1():
    pygame.init()
    last_event_time2 = pygame.time.get_ticks()
    event_interval2 = 1000
    dddcounter = 0
    width, height = 800, 600
    player_size = 50
    player_pos = [width / 2 - 20, height / 2 + 100]
    enemy_size = 50
    go_left = [pygame.image.load(f'sprites/{i}.jpg') for i in [1, 2, 3, 4]]
    go_right = [pygame.image.load(f'sprites/{i}.jpg') for i in [5, 6, 7, 8]]
    go_down = [pygame.image.load(f'sprites/{i}.jpg') for i in [13, 11, 14, 12]]
    go_up = [pygame.image.load(f'sprites/{i}.jpg') for i in [15, 9, 16, 10]]
    enemy_speed = 10
    enemy_speed1 = 10
    enemy_pos = [random.randint(0, width - enemy_size), 0]
    enemy_direction = "down"
    enemy_pos1 = [random.randint(0, width - enemy_size), height]
    enemy_direction1 = "up"
    count = 0
    k = 0
    kk = 0
    r = 0
    game_over = False
    while not game_over:
        if dddcounter == 15:
            pobeda(r)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_over = True
            if event.type == pygame.QUIT:
                game_over = True
        current_time2 = pygame.time.get_ticks()
        if current_time2 - last_event_time2 >= event_interval2:
            dddcounter += 1
            last_event_time2 = current_time2
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_pos[0] > 0:
            r += 1
            player_pos[0] -= 5
            k = 1
            kk = 0
        elif (not (keys[pygame.K_LEFT] and player_pos[0] > 0)) and kk == 0:
            k = 5
            kk = 0
        if keys[pygame.K_RIGHT] and player_pos[0] < width - player_size:
            r += 1
            player_pos[0] += 5
            k = 2
            kk = 1
        elif (not (keys[pygame.K_RIGHT] and player_pos[0] < width - player_size)) and kk == 1:
            k = 6
            kk = 0
        if keys[pygame.K_UP] and player_pos[1] > 0:
            r += 1
            player_pos[1] -= 5
            k = 3
            kk = 2
        elif (not (keys[pygame.K_UP] and player_pos[1] > 0)) and kk == 2:
            k = 7
            kk = 0
        if keys[pygame.K_DOWN] and player_pos[1] < height - player_size:
            r += 1
            player_pos[1] += 5
            k = 4
            kk = 3
        elif (not (keys[pygame.K_DOWN] and player_pos[1] < height - player_size)) and kk == 3:
            k = 8
            kk = 0
        if enemy_direction == "down":
            enemy_pos[1] += enemy_speed
        elif enemy_direction == "up":
            enemy_pos[1] -= enemy_speed
        elif enemy_direction == "left":
            enemy_pos[0] -= enemy_speed
        elif enemy_direction == "right":
            enemy_pos[0] += enemy_speed
        if enemy_pos[1] >= height:
            enemy_pos[1] = 0
            enemy_pos[0] = random.randint(0, width - enemy_size)
        if enemy_direction1 == "down":
            enemy_pos1[1] += enemy_speed1
        elif enemy_direction1 == "up":
            enemy_pos1[1] -= enemy_speed1
        elif enemy_direction1 == "left":
            enemy_pos1[0] -= enemy_speed1
        elif enemy_direction1 == "right":
            enemy_pos1[0] += enemy_speed1
        if enemy_pos1[1] <= 0:
            enemy_pos1[1] = height
            enemy_pos1[0] = random.randint(0, width - enemy_size)
        if (player_pos[0] < enemy_pos[0] + enemy_size and
                player_pos[0] + player_size > enemy_pos[0] and
                player_pos[1] < enemy_pos[1] + enemy_size and
                player_pos[1] + player_size > enemy_pos[1]):
            game_over = True
        if (player_pos[0] < enemy_pos1[0] + enemy_size and
                player_pos[0] + player_size > enemy_pos1[0] and
                player_pos[1] < enemy_pos1[1] + enemy_size and
                player_pos[1] + player_size > enemy_pos1[1]):
            game_over = True
        screen.fill((0, 0, 0))
        if k == 1:
            screen.blit(go_left[count], (player_pos[0], player_pos[1]))
        elif k == 2:
            screen.blit(go_right[count], (player_pos[0], player_pos[1]))
        elif k == 3:
            screen.blit(go_up[count], (player_pos[0], player_pos[1]))
        elif k == 4:
            screen.blit(go_down[count], (player_pos[0], player_pos[1]))
        elif k == 5:
            screen.blit(pygame.image.load('sprites/1.jpg'), (player_pos[0], player_pos[1]))
        elif k == 6:
            screen.blit(pygame.image.load('sprites/5.jpg'), (player_pos[0], player_pos[1]))
        elif k == 7:
            screen.blit(pygame.image.load('sprites/11.jpg'), (player_pos[0], player_pos[1]))
        elif k == 8:
            screen.blit(pygame.image.load('sprites/9.jpg'), (player_pos[0], player_pos[1]))
        if k in [1, 2, 3, 4]:
            count = (count + 1) % 4
            k = 0
        pygame.draw.rect(screen, (255, 0, 0), (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))
        pygame.draw.rect(screen, (255, 0, 0), (enemy_pos1[0], enemy_pos1[1], enemy_size, enemy_size))
        pygame.display.flip()
        clock.tick(60)
    if game_over:
        proigrish()


def new_game5():
    pygame.init()
    last_event_time5 = pygame.time.get_ticks()
    event_interval5 = 1000
    width, height = 800, 600
    player_size = 50
    player_pos = [width / 2 - 20, height / 2 + 100]
    enemy_size = 50
    go_left = [pygame.image.load(f'sprites/{i}.jpg') for i in [1, 2, 3, 4]]
    go_right = [pygame.image.load(f'sprites/{i}.jpg') for i in [5, 6, 7, 8]]
    go_down = [pygame.image.load(f'sprites/{i}.jpg') for i in [13, 11, 14, 12]]
    go_up = [pygame.image.load(f'sprites/{i}.jpg') for i in [15, 9, 16, 10]]
    enemy_speed = 7
    enemy_speed1 = 10
    enemy_speed2 = 7
    enemy_speed3 = 10
    enemy_speed5 = 7
    enemy_pos = [random.randint(0, width - enemy_size), 0]
    enemy_direction = "down"
    enemy_pos1 = [random.randint(0, width - enemy_size), height]
    enemy_direction1 = "up"
    enemy_pos2 = [width, random.randint(0, height - enemy_size)]
    enemy_direction2 = "left"
    enemy_pos3 = [0, random.randint(0, height - enemy_size)]
    enemy_direction3 = "right"
    enemy_pos5 = [random.randint(0, width - enemy_size), 0]
    enemy_direction5 = "down"
    count = 0
    k = 0
    kk = 0
    r = 0
    dddddcounter = 0
    game_over = False
    while not game_over:
        if dddddcounter == 10:
            pobeda(r)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_over = True
            if event.type == pygame.QUIT:
                game_over = True
        current_time5 = pygame.time.get_ticks()
        if current_time5 - last_event_time5 >= event_interval5:
            dddddcounter += 1
            last_event_time5 = current_time5
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_pos[0] > 0:
            r += 1
            player_pos[0] -= 5
            k = 1
            kk = 0
        elif (not (keys[pygame.K_LEFT] and player_pos[0] > 0)) and kk == 0:
            k = 5
            kk = 0
        if keys[pygame.K_RIGHT] and player_pos[0] < width - player_size:
            player_pos[0] += 5
            r += 1
            k = 2
            kk = 1
        elif (not (keys[pygame.K_RIGHT] and player_pos[0] < width - player_size)) and kk == 1:
            k = 6
            kk = 0
        if keys[pygame.K_UP] and player_pos[1] > 0:
            r += 1
            player_pos[1] -= 5
            k = 3
            kk = 2
        elif (not (keys[pygame.K_UP] and player_pos[1] > 0)) and kk == 2:
            k = 7
            kk = 0
        if keys[pygame.K_DOWN] and player_pos[1] < height - player_size:
            r += 1
            player_pos[1] += 5
            k = 4
            kk = 3
        elif (not (keys[pygame.K_DOWN] and player_pos[1] < height - player_size)) and kk == 3:
            k = 8
            kk = 0
        for enemy, speed, direction in [(enemy_pos, enemy_speed, enemy_direction),
                                        (enemy_pos1, enemy_speed1, enemy_direction1),
                                        (enemy_pos2, enemy_speed2, enemy_direction2),
                                        (enemy_pos3, enemy_speed3, enemy_direction3),
                                        (enemy_pos5, enemy_speed5, enemy_direction5)]:
            if direction == "down":
                enemy[1] += speed
                if enemy[1] >= height:
                    enemy[1] = 0
                    enemy[0] = random.randint(0, width - enemy_size)
            elif direction == "up":
                enemy[1] -= speed
                if enemy[1] <= 0:
                    enemy[1] = height
                    enemy[0] = random.randint(0, width - enemy_size)
            elif direction == "left":
                enemy[0] -= speed
                if enemy[0] <= 0:
                    enemy[0] = width
                    enemy[1] = random.randint(0, height - enemy_size)
            elif direction == "right":
                enemy[0] += speed
                if enemy[0] >= width:
                    enemy[0] = 0
                    enemy[1] = random.randint(0, height - enemy_size)
        if any(player_pos[0] < e[0] + enemy_size and player_pos[0] + player_size > e[0] and
               player_pos[1] < e[1] + enemy_size and player_pos[1] + player_size > e[1]
               for e in [enemy_pos, enemy_pos1, enemy_pos2, enemy_pos3, enemy_pos5]):
            game_over = True
        screen.fill((0, 0, 0))
        if k == 1:
            screen.blit(go_left[count], (player_pos[0], player_pos[1]))
        elif k == 2:
            screen.blit(go_right[count], (player_pos[0], player_pos[1]))
        elif k == 3:
            screen.blit(go_up[count], (player_pos[0], player_pos[1]))
        elif k == 4:
            screen.blit(go_down[count], (player_pos[0], player_pos[1]))
        elif k == 5:
            screen.blit(pygame.image.load('sprites/1.jpg'), (player_pos[0], player_pos[1]))
        elif k == 6:
            screen.blit(pygame.image.load('sprites/5.jpg'), (player_pos[0], player_pos[1]))
        elif k == 7:
            screen.blit(pygame.image.load('sprites/11.jpg'), (player_pos[0], player_pos[1]))
        elif k == 8:
            screen.blit(pygame.image.load('sprites/9.jpg'), (player_pos[0], player_pos[1]))
        if k in [1, 2, 3, 4]:
            count = (count + 1) % 4
            k = 0
        for enemy in [enemy_pos, enemy_pos1, enemy_pos2, enemy_pos3, enemy_pos5]:
            pygame.draw.rect(screen, (255, 0, 0), (enemy[0], enemy[1], enemy_size, enemy_size))
        pygame.display.flip()
        clock.tick(60)
    if game_over:
        proigrish()


def new_game3():
    pygame.init()
    last_event_time5 = pygame.time.get_ticks()
    event_interval5 = 1000
    width, height = 800, 600
    player_size = 50
    player_pos = [width / 2 - 20, height / 2 + 100]
    enemy_size = 50
    go_left = [pygame.image.load(f'sprites/{i}.jpg') for i in [1, 2, 3, 4]]
    go_right = [pygame.image.load(f'sprites/{i}.jpg') for i in [5, 6, 7, 8]]
    go_down = [pygame.image.load(f'sprites/{i}.jpg') for i in [13, 11, 14, 12]]
    go_up = [pygame.image.load(f'sprites/{i}.jpg') for i in [15, 9, 16, 10]]
    enemy_speed = 10
    enemy_speed1 = 7
    enemy_speed2 = 10
    enemy_pos = [random.randint(0, width - enemy_size), 0]
    enemy_direction = "down"
    enemy_pos1 = [random.randint(0, width - enemy_size), height]
    enemy_direction1 = "up"
    enemy_pos2 = [width, random.randint(0, height - enemy_size)]
    enemy_direction2 = "left"
    count = 0
    k = 0
    kk = 0
    r = 0
    dddcounter = 0
    game_over = False
    while not game_over:
        if dddcounter == 15:
            pobeda(r)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_over = True
            if event.type == pygame.QUIT:
                game_over = True
        current_time5 = pygame.time.get_ticks()
        if current_time5 - last_event_time5 >= event_interval5:
            dddcounter += 1
            last_event_time5 = current_time5
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_pos[0] > 0:
            r += 1
            player_pos[0] -= 5
            k = 1
            kk = 0
        elif (not (keys[pygame.K_LEFT] and player_pos[0] > 0)) and kk == 0:
            k = 5
            kk = 0
        if keys[pygame.K_RIGHT] and player_pos[0] < width - player_size:
            r += 1
            player_pos[0] += 5
            k = 2
            kk = 1
        elif (not (keys[pygame.K_RIGHT] and player_pos[0] < width - player_size)) and kk == 1:
            k = 6
            kk = 0
        if keys[pygame.K_UP] and player_pos[1] > 0:
            r += 1
            player_pos[1] -= 5
            k = 3
            kk = 2
        elif (not (keys[pygame.K_UP] and player_pos[1] > 0)) and kk == 2:
            k = 7
            kk = 0
        if keys[pygame.K_DOWN] and player_pos[1] < height - player_size:
            r += 1
            player_pos[1] += 5
            k = 4
            kk = 3
        elif (not (keys[pygame.K_DOWN] and player_pos[1] < height - player_size)) and kk == 3:
            k = 8
            kk = 0
        for enemy, speed, direction in [(enemy_pos, enemy_speed, enemy_direction),
                                        (enemy_pos1, enemy_speed1, enemy_direction1),
                                        (enemy_pos2, enemy_speed2, enemy_direction2)]:
            if direction == "down":
                enemy[1] += speed
                if enemy[1] >= height:
                    enemy[1] = 0
                    enemy[0] = random.randint(0, width - enemy_size)
            elif direction == "up":
                enemy[1] -= speed
                if enemy[1] <= 0:
                    enemy[1] = height
                    enemy[0] = random.randint(0, width - enemy_size)
            elif direction == "left":
                enemy[0] -= speed
                if enemy[0] <= 0:
                    enemy[0] = width
                    enemy[1] = random.randint(0, height - enemy_size)
            elif direction == "right":
                enemy[0] += speed
                if enemy[0] >= width:
                    enemy[0] = 0
                    enemy[1] = random.randint(0, height - enemy_size)
        if any(player_pos[0] < e[0] + enemy_size and player_pos[0] + player_size > e[0] and
               player_pos[1] < e[1] + enemy_size and player_pos[1] + player_size > e[1]
               for e in [enemy_pos, enemy_pos1, enemy_pos2]):
            game_over = True
        screen.fill((0, 0, 0))
        if k == 1:
            screen.blit(go_left[count], (player_pos[0], player_pos[1]))
        elif k == 2:
            screen.blit(go_right[count], (player_pos[0], player_pos[1]))
        elif k == 3:
            screen.blit(go_up[count], (player_pos[0], player_pos[1]))
        elif k == 4:
            screen.blit(go_down[count], (player_pos[0], player_pos[1]))
        elif k == 5:
            screen.blit(pygame.image.load('sprites/1.jpg'), (player_pos[0], player_pos[1]))
        elif k == 6:
            screen.blit(pygame.image.load('sprites/5.jpg'), (player_pos[0], player_pos[1]))
        elif k == 7:
            screen.blit(pygame.image.load('sprites/11.jpg'), (player_pos[0], player_pos[1]))
        elif k == 8:
            screen.blit(pygame.image.load('sprites/9.jpg'), (player_pos[0], player_pos[1]))
        if k in [1, 2, 3, 4]:
            count = (count + 1) % 4
            k = 0
        for enemy in [enemy_pos, enemy_pos1, enemy_pos2]:
            pygame.draw.rect(screen, (255, 0, 0), (enemy[0], enemy[1], enemy_size, enemy_size))
        pygame.display.flip()
        clock.tick(60)
    if game_over:
        proigrish()


def saved(r):
    my_file = open("File.txt", "a+")
    my_file.write(f'Ваш резултат: {str(r)}\n')
    my_file.close()


if __name__ == '__main__':
    main_menu()
