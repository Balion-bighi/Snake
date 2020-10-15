import pygame
import sys
from Class import Snake
from mancare import Mancare

window = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Snake")
fps = pygame.time.Clock()

scor = 0

snake = Snake()
mancare = Mancare()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake.changeDirectio("R")
            if event.key == pygame.K_LEFT:
                snake.changeDirectio("L")
            if event.key == pygame.K_UP:
                snake.changeDirectio("U")
            if event.key == pygame.K_DOWN:
                snake.changeDirectio("D")

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    foodPosition = mancare.generateFood()

    if snake.move(foodPosition):
        scor += 100
        mancare.setMancare(True)

    window.fill(pygame.Color(241, 90, 33))

    for position in snake.body:
        pygame.draw.rect(window, pygame.Color(255, 255, 255), pygame.Rect(position[0], position[1], 10, 10))

    pygame.draw.rect(window, pygame.Color(0, 123, 255), pygame.Rect(foodPosition[0], foodPosition[1], 10, 10))

    if snake.checkDead():
        pygame.quit()
        sys.exit()

    pygame.display.set_caption("Snake / Scor:" + str(scor))
    pygame.display.flip()
    fps.tick(12)
