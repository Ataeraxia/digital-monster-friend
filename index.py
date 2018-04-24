import pygame

def main():

  pygame.init()
  logo = pygame.image.load("logo32x32.png")
  pygame.display.set_icon(logo)
  pygame.display.set_caption("minimal program")

  screen = pygame.display.set_mode((240, 180))

  running = True

  # screen.fill((200,50,50))
  screen.blit(logo, (50, 50))
  pygame.display.flip()

  while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
    

if __name__=="__main__":
  main()