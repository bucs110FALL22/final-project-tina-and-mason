class Student:
  def __init__(self):
    self.health = 100
    self.xcoord = 0
    self.ycoord = 0
    self.image = pygame.image.load("assets/student.png").convert_alpha()
    self.rect = self.image.get_rect()

  def moveUp(self):
    '''
      Moves up the map to get to minigames
      Args: self
      Return: none
    '''
    self.ycoord+=10

  def moveDown(self):
    '''
      Moves down the map to get to minigames
      Args: self
      Return: none
    '''
    self.ycoord-=10


  def moveRight(self):
    '''
      Moves right to the map
      Args: self
      Return: none
    '''
    self.xcoord+=10

  def moveLeft(self):
    '''
      Moves left to the map
      Args: self
      Return: none
    '''
    self.xcoord-=10
  

    