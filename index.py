# cSpell:ignore pygame, rect KEYUP
import pygame
import random
import math

pygame.init()

white = (240, 240, 240)
black = (40, 20, 20)
red = (200, 40, 40)

screen = pygame.display.set_mode((400, 350))
pygame.display.set_caption("Little Guy")

gameExit = False

lead_x = 175
lead_y = 175
lead_x_change = 10
lead_y_change = 0
squash = -50

isDead = False

millsInSec = 1000
millsInMinute = millsInSec * 60
minLifeMinutes = millsInMinute*60
maxLifeMinutes = minLifeMinutes*5

deathTime = random.randrange(minLifeMinutes, maxLifeMinutes)
print(deathTime)

clock = pygame.time.Clock()

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_LEFT:
        #         lead_x_change = -10
        #         lead_y_change = 0
        #     elif event.key == pygame.K_RIGHT:
        #         lead_x_change = 10
        #         lead_y_change = 0
        #     elif event.key == pygame.K_UP:
        #         lead_y_change = -10
        #         lead_x_change = 0
        #     elif event.key == pygame.K_DOWN:
        #         lead_y_change = 10
        #         lead_x_change = 0

    # IS IT DEAD?
    if pygame.time.get_ticks() >= deathTime:
        isDead = True

    if isDead:
        screen.fill(red)
        pygame.draw.circle(screen, white, [140, 140], 10)
        pygame.draw.circle(screen, white, [240, 140], 10)
        pygame.draw.arc(
            screen, white, [125, 200, 150, 100], 0, math.pi, 4)
        pygame.display.update()

    else:
        if lead_x > 350:
            lead_x_change = -10
        elif lead_x < 0:
            lead_x_change = 10
        if lead_y > 300:
            lead_y_change = -10
        elif lead_y < 0:
            lead_y_change = 10

        choiceList = [-10, 10]

        if lead_x > 300:
            choiceList = [-10, -10, 10]
        elif lead_x < 100:
            choiceList = [-10, 10, 10]

        lead_x_change = random.choice(choiceList)

        if squash == -50:
            squash = -40
        elif squash == -40:
            squash = -50

        lead_x += lead_x_change
        lead_y += lead_y_change

        screen.fill(black)
        pygame.draw.rect(screen, red, [lead_x, lead_y, 50, squash])  # x,y,w,h
        pygame.display.update()

        clock.tick(2)

pygame.quit()
quit()
