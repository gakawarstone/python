import pygame
import config
import random


def splash():
    run = True
    R = 0
    G = 0
    B = 255
    while run:
        pygame.time.delay(10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_z]:
            run = False

        config.splash_y += config.splash_speed_y
        config.splash_x += config.splash_speed_x
        print(config.splash_x, config.splash_y)
        if config.splash_y < 1:
            config.splash_speed_y = -config.splash_speed_y
            R = random.randint(0, 255)
            G = random.randint(0, 255)
            B = random.randint(0, 255)
        if config.splash_y > 499 - config.splash_height:
            config.splash_speed_y = -config.splash_speed_y
            R = random.randint(0, 255)
            G = random.randint(0, 255)
            B = random.randint(0, 255)
        if config.splash_x < 1:
            config.splash_speed_x = -config.splash_speed_x
            R = random.randint(0, 255)
            G = random.randint(0, 255)
            B = random.randint(0, 255)
        if config.splash_x > 499 - config.splash_width:
            config.splash_speed_x = -config.splash_speed_x
            R = random.randint(0, 255)
            G = random.randint(0, 255)
            B = random.randint(0, 255)

        config.win.fill((0, 0, 0))
        pygame.draw.rect(config.win, (R, G, B), (config.splash_x,
                                                   config.splash_y,
                                                   config.splash_width,
                                                   config.splash_height))
        pygame.display.update()
