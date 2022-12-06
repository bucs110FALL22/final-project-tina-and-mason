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
    pygame.init()
     
    self.screen = pygame.display.set_mode(dimensions)
    
    self.homeScreen = True
    self.points = 0
    self.lives = 2
    self.duckyGame = False
    self.win = False

    #sets up background
    bingBkgd = pygame.image.load("assets/bingbkgd.jpg")
    self.screen.blit(bingBkgd, (-150, -300))
    pygame.mixer.init()

    pygame.mixer.music.load("assets/sillyMusic.mp3")

    pygame.mixer.music.play()
    
     
 
    
  def mainloop(self):
    '''
    This function is the loop that runs throughout the game and responds to user events. 
    Arguments: (obj) self
    Returns: N/A
    '''
     

     
    while self.duckyGame:
      self.duckyDoomLoop()
      
    while self.homeScreen:
      if self.lives == -1:
        self.screen.fill("black")
        finalLoss = pygame.image.load("assets/finalLoss.png")
        finalLoss = pygame.transform.scale(finalLoss, (357, 110))
        self.screen.blit(finalLoss, (50, 150))
        click2playMsg = pygame.image.load("assets/click2playMsg.png")
        click2playMsg = pygame.transform.scale(click2playMsg, (270, 80))
        self.screen.blit(click2playMsg, (100, 300))
        pygame.display.flip()
        loseScreen = True
        while loseScreen:
          for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
              self.homeScreen = True
              self.lives = 2
              self.points = 0
              loseScreen = False
        pygame.display.flip()
        
     
       
        
      bingBkgd = pygame.image.load("assets/bingbkgd.jpg")
      self.screen.blit(bingBkgd, (-150, -300))
      professorImg = pygame.image.load("assets/profMoore.png").convert_alpha()
      professorImg = pygame.transform.scale(professorImg, (150, 200))
      self.screen.blit(professorImg, (0, 300))
      
      duckybtn = pygame.image.load("assets/btnducky.png").convert_alpha()
      duckybtn = pygame.transform.scale(duckybtn, (140, 60))
      self.screen.blit(duckybtn, (300, 350))
      mooreBubble1 = pygame.image.load("assets/mooreBubble1.png")
      mooreBubble1 = pygame.transform.scale(mooreBubble1, (290, 120))
      self.screen.blit(mooreBubble1, (50, 225))

      kitchenBtn = pygame.image.load("assets/kitchenBtn.png")
      kitchenBtn = pygame.transform.scale(kitchenBtn, (250, 50))
      self.screen.blit(kitchenBtn, (110, 140))
      
      pointsBtn = pygame.image.load("assets/pointsBtn.png").convert_alpha()
      pointsBtn = pygame.transform.scale(pointsBtn, (150, 60))
      self.screen.blit(pointsBtn, (350, 0))
      text = str(self.points)
      font = pygame.font.SysFont(None, 48)
      points = font.render(text, True, "black")

      pointsRect = points.get_rect()
      pointsRect.topleft = (20, 20)
      self.screen.blit(points, (450, 15))

      livesBtn = pygame.image.load("assets/livesBtn.png").convert_alpha()
      livesBtn = pygame.transform.scale(livesBtn, (150, 60))
      self.screen.blit(livesBtn, (0, 0))
      text = str(self.lives)
      font = pygame.font.SysFont(None, 48)
      lives = font.render(text, True, "black")

      pointsRect = points.get_rect()
      pointsRect.topleft = (20, 20)
      self.screen.blit(lives, (80, 15))
      pygame.display.flip()
    
      for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and self.homeScreen and not self.win and self.lives!=-1:
          if pygame.mouse.get_pos() <= (440, 410) and pygame.mouse.get_pos() >= (300, 350) and pygame.mouse.get_pos()[1] > 350 and pygame.mouse.get_pos()[1] < 410:
            self.duckyGame = True
            self.duckyDoomLoop()
          elif pygame.mouse.get_pos() <= (360, 190) and pygame.mouse.get_pos() >= (110, 140) and pygame.mouse.get_pos()[1] > 140 and pygame.mouse.get_pos()[1] < 190:
            self.shopLoop() 
    
    pygame.display.flip()

 
    
  def duckyDoomLoop(self):
      '''
        This is the loop for the ducky doom game, checking when the user jumps and such.
      '''
      oceanbkgd = pygame.image.load("assets/ocean.png").convert()
      self.screen.blit(oceanbkgd, (0, 0))
      
      ducky = duck.Duck(None, 50, 60)
      ducky.rect.x = 130
      ducky.rect.y = 360

      
      error404msg = obstacles.Obstacles(None, 80, 69, "assets/error404.png")
      error404msg.rect.x = 700
      error404msg.rect.y = 370
      invalidSyntaxMsg = obstacles.Obstacles(None, 80, 30, "assets/invalidsyntax.png")
      invalidSyntaxMsg.rect.x = 700
      invalidSyntaxMsg.rect.y = 400
      indentErrorMsg = obstacles.Obstacles(None, 80, 30, "assets/invalidsyntax.png")
      indentErrorMsg.rect.x = 700
      indentErrorMsg.rect.y = 400
      typeErrorMsg = obstacles.Obstacles(None, 80, 40, "assets/typeError.png")
      typeErrorMsg.rect.x = 700
      typeErrorMsg.rect.y = 400
      spritesList = pygame.sprite.Group()
      spritesList.add(ducky)
      spritesList.add(error404msg)
      spritesList.add(invalidSyntaxMsg)
      spritesList.add(indentErrorMsg)
      spritesList.add(typeErrorMsg)
      spritesList.draw(self.screen)
      
      pygame.display.flip()
      running = False
      obstacleNum = -1
      duckyIntro = pygame.image.load("assets/duckyDoomIntro.png").convert_alpha()
      finalMsg = pygame.image.load("assets/goodLuckDucky.png").convert_alpha()
      finalMsg = pygame.transform.scale(finalMsg, (357, 110))
      duckyIntro = pygame.transform.scale(duckyIntro, (357, 110))
      self.screen.blit(duckyIntro, (90, 100))
      pygame.display.flip()
      pygame.time.delay(3000)
      self.screen.blit(oceanbkgd, (0, 0))
      ducky.draw(self.screen)
      self.screen.blit(finalMsg, (90, 100))
      pygame.display.flip()
      
      while running != True:
        for event in pygame.event.get():  
          if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            running = True
      self.screen.blit(oceanbkgd, (0, 0))
      ducky.draw(self.screen)
      pygame.display.flip()
    
      while running:
        if obstacleNum==-1:
          pygame.time.delay(1000)
          obstacleNum+=1
        if obstacleNum==0:
          error = error404msg
        elif obstacleNum==1:
          error = invalidSyntaxMsg
        elif obstacleNum==2:
          error = indentErrorMsg
        elif obstacleNum==3:
          error = typeErrorMsg
        else:
          obstacleNum=0
          
        error.rect.x -= 0.1
        if error.rect.x <= 0:
            error.rect.x -=1
        if error.rect.x <= -30:
            error.rect.x = 700
            self.points +=1
            obstacleNum+=1
        
        self.screen.blit(oceanbkgd, (0, 0))
        spritesList.draw(self.screen)
        pygame.display.flip()

        # ERROR CHECK
        if pygame.sprite.collide_rect(ducky, error):
            self.minigameLoss()
            self.duckyGame = False
            self.lives-=1
            running = False
            
          
        for event in pygame.event.get():
           if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
              #ESCAPE
             self.duckyGame = False
             self.homeScreen = True
             running = False
              
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and running:
          for i in range(110):
            ducky.rect.y -= 1
            self.screen.blit(oceanbkgd, (0, 0))
            ducky.draw(self.screen)
            error.draw(self.screen)
            ducky.draw(self.screen)
            error.rect.x-=0.1
            spritesList.draw(self.screen)
            pygame.display.flip()
          error.rect.x-=2
          for i in range(110):
            ducky.rect.y += 1
            #error.rect.x-=1
            self.screen.blit(oceanbkgd, (0, 0))
            error.draw(self.screen)
            ducky.draw(self.screen)
            error.rect.x-=1
            spritesList.draw(self.screen)
            pygame.display.flip()
       
        pygame.display.update()

      
      
  def minigameLoss(self):
    '''
      This loop plays when the user loses the ducky doom minigame and then exits to the homescreen.
    '''
    self.screen.fill("black")
    loseMsg = pygame.image.load("assets/gameLoseMsg.png").convert_alpha()
    pressKey = pygame.image.load("assets/pressAnyKeyMsg.png").convert_alpha()
    loseMsg = pygame.transform.scale(loseMsg, (450, 150))
    pressKey = pygame.transform.scale(pressKey, (400, 125))
    self.screen.blit(loseMsg, (40, 100))
    self.screen.blit(pressKey, (70, 300))
    pygame.display.flip()
    pygame.time.delay(2000)
    running = True
    while running:
      for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:  
          self.homeScreen = True
          running = False 
   
    
 
  def shopLoop(self):
    '''
      This loop listens to user input after the user is in menu mode. With pressing certain keys, the user can exchange 3 points for a ham and cheese sandwich and win the game. 
    '''
    pygame.mixer.music.stop()
    pygame.mixer.music.load("assets/sickoSandwich.mp3")

    pygame.mixer.music.play() 
    self.screen.fill("black")
    if self.points>=3:
      sandwich = pygame.image.load("assets/sandwich.jpg").convert_alpha()
      sandwich = pygame.transform.scale(sandwich, (500,500))
      self.screen.blit(sandwich, (0, 0))
      winMsg = pygame.image.load("assets/winSandwich.png")
      winMsg = pygame.transform.scale(winMsg, (450, 90))
      self.screen.blit(winMsg, (10, 200))
       
      pygame.display.flip()
      self.win = True
      while self.win:
        pygame.time.delay(10000)
    else:
       
      running = True
      while running:
        text ="You don't have enough points to get anything.."
        font = pygame.font.SysFont(None, 30)
        sandwich = font.render(text, True, "White")
  
        sandwichRect = sandwich.get_rect()
        sandwichRect.topleft = (20, 20)
        self.screen.blit(sandwich, (25, 150))
        text2 = "Click anywhere to go back to hard labor."
        font2 = pygame.font.SysFont(None, 30)
        clickAgain = font2.render(text2, True, "White")
        self.screen.blit(clickAgain, (60, 310))

        blurSandwich = pygame.image.load("assets/blurSandwich.png")
        blurSandwich = pygame.transform.scale(blurSandwich, (140, 90))
        self.screen.blit(blurSandwich, (200, 200))
        pygame.display.flip()
        for event in pygame.event.get():
          if event.type == pygame.MOUSEBUTTONDOWN:  
            self.homeScreen = True
            running = False 
      
    
    
  
    
    