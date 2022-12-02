class ProfMoore:
  def __init__(self):
    self.health = 100
    self.hungerLevel = 0
    self.xcoord = 0
    self.ycoord = 0
    self.image = pygame.image.load("assets/profMoore.png").convert_alpha()
    self.rect = self.image.get_rect()

  def eat(self):
    '''
      After every mini game, he gets to eat a ham and cheese sandwich.
    '''
    self.hungerLevel-=1

  def moveUp(self):
    '''
      Moves up the map to get to minigames
    '''
    self.ycoord+=10

  def moveDown(self):
    '''
      Moves down the map to get to minigames
    '''
    self.ycoord-=10


  def moveRight(self):
    '''
      Moves right to the map
    '''
    self.xcoord+=10

  def moveLeft(self):
    '''
      Moves left to the map
    '''
    self.xcoord-=10
  

    