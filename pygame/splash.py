import pygame
import config
import color as cl


def splash():
    run = True
    rect_cl = cl.blue
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
        if config.splash_y < 1:
            config.splash_speed_y = -config.splash_speed_y
            rect_cl = cl.random()
        if config.splash_y > config.win_height - 1 - config.splash_height:
            config.splash_speed_y = -config.splash_speed_y
            rect_cl = cl.random()
        if config.splash_x < 1:
            config.splash_speed_x = -config.splash_speed_x
            rect_cl = cl.random()
        if config.splash_x > config.win_width - 1 - config.splash_width:
            config.splash_speed_x = -config.splash_speed_x
            rect_cl = cl.random()

        config.win.fill(cl.black)
        pygame.draw.ellipse(config.win, rect_cl, (config.splash_x,
                                                  config.splash_y,
                                                  config.splash_width,
                                               config.splash_height))
        pygame.display.update()
