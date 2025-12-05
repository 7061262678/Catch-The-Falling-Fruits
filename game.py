import pygame
import random

pygame.init()

width, height = 600, 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Catch The Falling Fruits")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)

basket_x = width // 2
basket_y = height - 60
basket_width = 100
basket_height = 25
basket_speed = 8

fruit_x = random.randint(20, width - 20)
fruit_y = 0
fruit_size = 30
fruit_speed = 5

score = 0
running = True

while running:
    screen.fill((245, 230, 180))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and basket_x > 0:
        basket_x -= basket_speed
    if keys[pygame.K_RIGHT] and basket_x < width - basket_width:
        basket_x += basket_speed

    fruit_y += fruit_speed
    if fruit_y > height:
        fruit_x = random.randint(20, width - 20)
        fruit_y = 0

    if (basket_x < fruit_x < basket_x + basket_width) and (fruit_y + fruit_size >= basket_y):
        score += 1
        fruit_x = random.randint(20, width - 20)
        fruit_y = 0

    pygame.draw.rect(screen, (200, 100, 50), (basket_x, basket_y, basket_width, basket_height))
    pygame.draw.circle(screen, (255, 0, 0), (fruit_x, fruit_y), fruit_size)

    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (20, 20))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
