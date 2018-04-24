import pygame

pygame.init()

screen = pygame.display.set_mode((400, 350))
pygame.display.set_caption("Little Guy")

pygame.display.update()

gameExit = False

while not gameExit:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      gameExit = True

pygame.quit()
quit()