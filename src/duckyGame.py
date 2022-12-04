import pygame
from src import controller
from src import duck
from src import obstacles

class DuckyMiniGame(controller):
  def __init__(self, dimensions):
    super().__init__()
  
      #RUBBER DUCKY SAILING PAST CODE ERRORS
    win = False
    
    oceanbkgd = pygame.image.load("assets/ocean.png").convert()
    self.screen.blit(oceanbkgd, (0, 0))

    ducky = duck.Duck(None, 50, 60)
    ducky.rect.x = 130
    ducky.rect.y = 340

    error404msg = obstacles.Obstacles(None, 100, 50, "assets/error404.png")
    invalidSyntaxMsg = obstacles.Obstacles(None, 100, 50, "assets/invalidsyntax.png")
    indentErrorMsg = obstacles.Obstacles(None, 100, 50, "assets/invalidsyntax.png")
    typeErrorMsg = obstacles.Obstacles(None, 100, 50, "assets/typeError.png")
    
    spritesList = pygame.sprite.Group()
    spritesList.add(ducky)
    spritesList.add(error404msg)
    spritesList.add(invalidSyntaxMsg)
    spritesList.add(indentErrorMsg)
    spritesList.add(typeErrorMsg)
    spritesList.draw(self.screen)
      

  #PUT IMAGE WITH INSTRUCTIONS
  #CLICK TO START 
  def duckyDoomLoop(self):
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        # print(event.key==pygame.K_SPACE)
        if event.key == pygame.K_SPACE:
          # JUMP SEQUENCE
          # for i in range(80):
          #   ducky.rect.y-=.5
          #   self.screen.blit(oceanbkgd, (0, 0))
          #   spritesList.draw(self.screen)
          #   pygame.display.flip()
          # pygame.time.delay(1)
          for i in range(80):
            ducky.rect.y += 1
            self.screen.blit(oceanbkgd, (0, 0))
            spritesList.draw(self.screen)
            pygame.display.flip()
      pygame.display.update()
  
    
      
    if win:
      self.points+=1
    else:
      self.points-=1
    
