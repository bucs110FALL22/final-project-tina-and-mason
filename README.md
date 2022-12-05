:warning: Everything between << >> needs to be replaced (remove << >> after replacing)
# CS110 Project Proposal
# << Project Title >>
## CS 110 Final Project
### << Semester, Year >>
### [Assignment Description](https://docs.google.com/document/d/1H4R6yLL7som1lglyXWZ04RvTp_RvRFCCBn6sqv-82ps/edit?usp=sharing)

[REPL Link](https://replit.com/join/cdrzcjiegn-tinalenguyen)

<< [link to demo presentation slides](#) >>

### Team: Nashville Nugget
#### Tina Nguyen, Mason Nash

***

## Project Description

This project is a Professor Moore Life Simulator. There is just one mini game implemented where the user plays as a rubber duck to avoid coding errors. The game is styled after the Google Dinosaur game. Once the user reaches 5 points, they are able to exchange it for a ham and cheese sandwich and win the game. They only have two lives to achieve 5 points. For every obstacle avoided, they get a point.

***    

## User Interface Design

- **Initial Concept**
  - 
  - << A wireframe or drawing of the user interface concept along with a short description of the interface. You should have one for each screen in your program. For example, if your program has a start screen, game screen, and game over screen, you should include a wireframe / screenshot / drawing of each one and a short description of the components. >>
    
    
- **Final GUI**
  - << You should also have a screenshot of each screen for your final GUI >>

***        

## Program Design

* profMoore:
  *  health 
     hungerLevel 
     xcoord 
     ycoord
     eat()
     moveUp()
     moveDown()
     moveRight()
     moveLeft()
     
* obstacle:
  * draw()

  duck:
    getCoords()
    draw()
  


* Non-Standard libraries
    * << You should have a list of any additional libraries or modules used (pygame, request) beyond non-standard python. 
         For each additional module you should include
         - url for the module documentation
         - a short description of the module >>
* Class Interface Design
    * << A simple drawing that shows the class relationships in your code (see below for an example). This does not need to be overly detailed, but should show how your code fits into the Model/View/Controller paradigm. >>
        * ![class diagram](assets/class_diagram.jpg) 
* Classes
    class profMoore:
      a class containing coordinates
    class duck:
      a class containing coordinates of the duck and a function to draw it
    class obstacles:
      a sprite class for all the ducky game obstacles with variables for coordinates 

## Project Structure and File List

The Project is broken down into the following file structure:

* main.py
* src
    controller.py
    duck.py
    obstacles.py
    profMoore.py
  
* assets
    bingbkgd.jpg
    btn.ducky.png
    class_diagram.jpg
    duck.png
    duckyDoomIntro.png
    error404.png
    finalLoss.png
    gameLoseMsg.png
    goodLuckyDucky.png
    indenterror.png
    invalidsyntax.png
    livesBtn.png
    mooreBubble1.png
    ocean.png
    pointsBtn.ong
    pressAnyKeyMsg.png
    profMoore.png
    sandwich.jpg
    typeError.png
  

***

## Tasks and Responsibilities 

    Tina: Coding the technicalities of the ducky doom game and creating the loops 
    Mason: Aesthetics and gathering images, creating buttons and text message boxes, positioning images 

## Testing

    - Play the game to win to see if the win screen correctly pops up and if the points keep up
    - Play the game to lose and see if points don't coordinate and if the lose screen shows up

## ATP

| Step                 |Procedure             |Expected Results                   |
|----------------------|:--------------------:|----------------------------------:|
|  1                   | Run Controller()     | Main menu appears with options to play certain minigames. One point will be loaded automatically|
|  2                   | Click on Ducky Doom  | Loads ducky mini game screen      |
|  3                   | Press spacebar       | Obstacles will come at the duck and the user must press space to make the duck jump to avoid them |
| 4                    | Attempt to win       | 1. Gain 5 points by jumping over the appropriate amount of obstacles 2. User will be able to cash in those points to win the game and get a sandwich|
| 5                    | Gain 10 points and win | 1. Winning screen will be shown with an option to play again
| 6                    | Points are at a negative value from losing | 1. A losing screen will be shown with an option to play again

etc...
