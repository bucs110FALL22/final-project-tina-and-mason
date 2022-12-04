import pygame
from src import profMoore
from src import duck
from src import obstacles
 
class Controller:

  def __init__(self, dimensions):
    ''' 
    This function sets up the screen for the player and creates objects to work with.
    Arguments: (obj) self, (list) dimensions
    Returns: N/A
    '''
    professor = profMoore.ProfMoore()
    self.screen = pygame.display.set_mode(dimensions)
    
    self.homeScreen = False
    self.points = 0
    self.duckyGame = True

    #sets up background
    bingBkgd = pygame.image.load("assets/bingbkgd.jpg")
    self.screen.blit(bingBkgd, (-150, -300))
    
    #assistant = TA()
 
    
  def mainloop(self):
    '''
    This function is the loop that runs throughout the game and responds to user events. 
    Arguments: (obj) self
    Returns: N/A
    '''
    
    while self.duckyGame:
      self.duckyDoomLoop()
      
    while self.homeScreen:
      bingBkgd = pygame.image.load("assets/bingbkgd.jpg")
      self.screen.blit(bingBkgd, (-150, -300))
      professorImg = pygame.image.load("assets/profMoore.png").convert_alpha()
      professorImg = pygame.transform.scale(professorImg, (150, 200))
      self.screen.blit(professorImg, (0, 200))
      
      duckybtn = pygame.image.load("assets/btnducky.png").convert_alpha()
      duckybtn = pygame.transform.scale(duckybtn, (120, 55))
      self.screen.blit(duckybtn, (200, 250))
      pygame.display.flip()
    
       
      #FONT SAYING HELP ME
      
    
    
    pygame.display.flip()
    #select state loop
    
  
  ### below are some sample loop states ###

    
  def duckyDoomLoop(self):
      #RUBBER DUCKY SAILING PAST CODE ERRORS
      win = False
      alive = True
      
      oceanbkgd = pygame.image.load("assets/ocean.png").convert()
      self.screen.blit(oceanbkgd, (0, 0))
  
      ducky = duck.Duck(None, 50, 60)
      ducky.rect.x = 130
      ducky.rect.y = 340
  
      error404msg = obstacles.Obstacles(None, 100, 74, "assets/error404.png")
      error404msg.rect.x = 130
      error404msg.rect.y = 340
      invalidSyntaxMsg = obstacles.Obstacles(None, 100, 50, "assets/invalidsyntax.png")
      indentErrorMsg = obstacles.Obstacles(None, 100, 50, "assets/invalidsyntax.png")
      typeErrorMsg = obstacles.Obstacles(None, 100, 50, "assets/typeError.png")
      
      spritesList = pygame.sprite.Group()
      spritesList.add(ducky)
      spritesList.add(error404msg)
      print(error404msg.rect.x)
      spritesList.add(invalidSyntaxMsg)
      spritesList.add(indentErrorMsg)
      spritesList.add(typeErrorMsg)
      spritesList.draw(self.screen)
      
  
      #PUT IMAGE WITH INSTRUCTIONS
      #CLICK TO START 
      while self.duckyGame:
        error404msg.rect.x -= 10
        for event in pygame.event.get():
          if event.type == pygame.KEYDOWN:
            #print(event.key == pygame.K_a)
            if event.key == pygame.K_SPACE:
              # JUMP SEQUENCE
              for i in range(100):
                ducky.rect.y-=1
                self.screen.blit(oceanbkgd, (0, 0))
                spritesList.draw(self.screen)
                pygame.display.flip()
              pygame.time.delay(2)
              for i in range(100):
                ducky.rect.y += 1
                self.screen.blit(oceanbkgd, (0, 0))
                spritesList.draw(self.screen)
                pygame.display.flip()
        
            elif event.key == pygame.K_q:
              #escape menu pops
              self.duckyGame = False
              self.homeScreen = True
             # self.screen.fill("black")
          pygame.display.update()
        #  print(self.homeScreen)
        
      if ducky.rect.y == error404msg.rect.y:
        self.duckyGame = False
        win = False
        
      if win:
        self.points+=1
      else:
        self.points-=1
      
  #def obstacleLooping:
    
    
      
              
    
  # def whackaEmail():
  #   #whack a mole but emails during work hours
  #   emailsResponded = 0
  #   if emailsResponded == 10:
  #     self.points+=1

 
 # def menuloop(self):
    # '''
    #   This loop listens to user input after the user is in menu mode. With pressing certain keys, the user can make the professor consume food or a TA respond to Discord notifications.
    # '''
   # m = 1
    #set up sandwich shop
    #TA MODE? 
    
      
    
  # def gameoverloop(self):
  #   '''  
  #   This function listens to events specifically when the user has lost the game(e.g. the professor died.) If the user presses the spacebar, the user can replay the game from scratch. 
  #   '''
  #   #set up game over screen
  #   quit = False
  #   if quit:
  #     pygame.exit()
  #   else:
  #     __init__()
    