# cSpell:ignore pygame, rect
import pygame

pygame.init()

white = (240, 240, 240)
black = (40,20,20)
red = (200, 40, 40)

screen = pygame.display.set_mode((400, 350))
pygame.display.set_caption("Little Guy")

gameExit = False

while not gameExit:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      gameExit = True

  screen.fill(black, rect=[175,150,50,50])
  # pygame.draw.rect(screen, red, [175,150,50,50])  # x,y,w,h
  pygame.display.update()

pygame.quit()
quit()