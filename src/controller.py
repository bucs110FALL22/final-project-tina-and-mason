import pygame

class Controller:

  def __init__(self, dimensions):
  ''' 
    This function sets up the screen for the player and creates objects to work with.
    Arguments: (obj) self, (list) dimensions
    Returns: N/A
  '''
    professor = ProfMoore()
    assistant = TA()
    self.screen = pygame.display.set_mode(dimensions)
    
    
  def mainloop(self):
    '''
    This function is the loop that runs throughout the game and responds to user events. 
    Arguments: (obj) self
    Returns: N/A
    '''
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
            exit()
      if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                professor.jump()
            if event.key == pygame.K_LEFT:
                professor.moveLeft()
            if event.key == pygame.K_RIGHT:
                professor.moveRight()
            if event.key == pygame.K_DOWN:
                professor.moveDown()
            if event.key == pygame.K_UP:
                professor.moveUp()
    menuloop()
    #select state loop
    
  
  ### below are some sample loop states ###

  def menuloop(self):
    '''
      This loop listens to user input after the user is in menu mode. With pressing certain keys, the user can make the professor consume food or a TA respond to Discord notifications.
    '''
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_E:
          professor.eat()
        if event.key == pygame.K_D:
          assistant.respondDiscord()
      
    
  def gameoverloop(self):
  '''  
    This function listens to events specifically when the user has lost the game(e.g. the professor died.) If the user presses the spacebar, the user can replay the game from scratch. 
  '''
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
            exit()
      if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                __init__()

