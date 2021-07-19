import pygame
from pygame.locals import*


screen_width = 600
screen_height = 800
screen= pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Space Invaders')

#Upload image
bg =pygame.image.load("img/bg.png")

def draw_bg():
  screen.blit(bg, (0, 0))

#create spaceship class
class Spaceship(pygame.sprite.Sprite):
  def __init__(self, x, y):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load("img/spaceship.png")
    self.rect = self.image.get_rect()
    self.rect.center = [x, y]

#create a sprite groups
spaceship_group = pygame.sprite.Group()

#create player
spaceship = Spaceship(int(screen_width / 2), screen_height - 100)
spaceship_group.add(spaceship)


run = True
while run:

 # clock.tick(fps)

  #Draw background
  draw_bg()

  #event handlers
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

#Draw sprite groups
spaceship_group.draw(screen)






pygame.display.update()
pygame.quit