import pygame

pygame.init()

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption('GK')

x = 23
y = 78
width = 70
height = 30
speed = 1
speed_x = 1
speed_y = 1


def moving(keys):
    if keys[pygame.K_w] and y > 0:
        y -= speed
    if keys[pygame.K_s] and y < 500 - width:
        y += speed
    if keys[pygame.K_a] and x > 0:
        x -= speed
    if keys[pygame.K_d] and x < 500 - height:
        x += speed


def splash(x, y, speed_x, speed_y):
    y += speed_y
    x += speed_x
    print(x, y)
    if y < 1:
        speed_y = -speed_y
    if y > 499 - height:
        speed_y = -speed_y
    if x < 1:
        speed_x = -speed_x
    if x > 499 - width:
        speed_x = -speed_x
    return x, y, speed_x, speed_y


run = True
while run:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    x, y, speed_x, speed_y = splash(x, y, speed_x, speed_y)

    win.fill((0, 0, 0))
    pygame.draw.rect(win, (0, 0, 255), (x, y, width, height))
    pygame.display.update()

pygame.quit()
