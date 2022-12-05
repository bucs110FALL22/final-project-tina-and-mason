import pygame
 

class Obstacles(pygame.sprite.Sprite):
  def __init__(self, color, width, height, imageAddress):
    super().__init__()
    self.image = pygame.image.load(imageAddress).convert_alpha()
    self.image = pygame.transform.scale(self.image, (width, height))
        # Fetch the rectangle object that has the dimensions of the image.
    self.rect = self.image.get_rect()
    self.rect.x = 250
    self.rect.y = 600
    self.coords = (self.rect.x, self.rect.y)

  def draw(self, screen):
    screen.blit(self.image, (self.rect.x, self.rect.y))
