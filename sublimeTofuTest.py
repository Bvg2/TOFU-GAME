import pygame
import random
import time
from pygame import mixer

"""

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXX: BUG REPORT :XXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX







"""


#do lives, lost lives if hit tofu or tofu hits block
#easy peasy
pygame.init()
displayWidth = 1200 #800
displayHeight = 700 #600

game_Display = pygame.display.set_mode((displayWidth,displayHeight))
pygame.display.set_caption("Tofu Space Invader")

#set black and white
black = (0,0,0)
white = (255,255,255)
blue = (50,111,168)
red = (240,0,0)
#backround sound (taken out)
#mixer.music.load('backround.wav')
#mixer.music.play(-1)

#set the FPS, See if crashed

clock = pygame.time.Clock()
crashed = False
frogImg = pygame.image.load('Ben.png')
width, height = frogImg.get_rect().size
spaceImg = pygame.image.load('space.jpg')
spaceImg = pygame.transform.scale(spaceImg, (displayWidth, displayHeight))
gameLives = 5
gameScore = 0
tofuSpeed = 1
benSpeed = 8
notPiercing = True
waterAmount = 5 

#test of screenshake




#This is where i display text
def space(x,y):
    game_Display.blit(spaceImg, (x,y))
#this is the section where i add text
def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()
def text_objects3(text, font):
    textSurface = font.render(text, True, blue)
    return textSurface, textSurface.get_rect()
def text_objects2(text, font):
    textSurface = font.render(text, True, red)
    return textSurface, textSurface.get_rect()
def message_display(text, x, y):
    largeText = pygame.font.Font('freesansbold.ttf',25)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((75),(15))
    game_Display.blit(TextSurf, TextRect)
def message_displayScore(text, x, y):
    largeText = pygame.font.Font('freesansbold.ttf',25)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((displayWidth-100),(15))
    game_Display.blit(TextSurf, TextRect)
def message_displayWater(text, x, y):
    largeText = pygame.font.Font('freesansbold.ttf',20)
    TextSurf, TextRect = text_objects3(text, largeText)
    TextRect.center = ((100),(40))
    game_Display.blit(TextSurf, TextRect)
def message_displayGameOver(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects2(text, largeText)
    TextRect.center = ((displayWidth/2),(displayHeight/2))
    game_Display.blit(TextSurf, TextRect)
    print("displaying game over message")

    pygame.display.update()


def textLives():
    message_display("Lives left: " + str(gameLives), 0, 0)
def textScore():
    message_displayScore("Score: " + str(gameScore), 1000, 10)
def waterNum():
    message_displayWater("Water remaining: " + str(waterAmount), 0, 15)
def gameOver():
    message_displayGameOver('You Die')
    

x_change = 0
y_change = 0

class Ben(pygame.sprite.Sprite):
    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self):
       # Call the parent class (Sprite) constructor
       pygame.sprite.Sprite.__init__(self)

       # Create an image of the block, and fill it with a color.
       # This could also be an image loaded from the disk.
       self.image = pygame.image.load("Ben.png")

       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
       self.rect = self.image.get_rect()
       self.hurtCounter = 0
    def update(self,dx,dy):
        self.rect.x += dx
        self.rect.y += dy
        self.rect.x = max(0, self.rect.x)
        self.rect.x = min(1150, self.rect.x)
        self.rect.y = max(450, self.rect.y)
        self.rect.y = min(600, self.rect.y)


        if self.hurtCounter > 0:
            self.hurtCounter -= 1
        if self.hurtCounter == 0:
            self.image = pygame.image.load("Ben.png")
            
        
    def getHit(self):
        self.hurtCounter = 25
        self.image = pygame.image.load("benRed.png")
        
        

            





            
#making the tofu
class Tofu(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("Tofu.png")

        self.rect = self.image.get_rect()
    def update(self,dx,dy):
        self.rect.x += dx
        self.rect.y += dy

        #baking the muffin 
class Muffin(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("muffin.png")

        self.rect = self.image.get_rect()
        self.framesAlive = 0
    def canShoot(self):
        if self.framesAlive % 130 == 0 and self.framesAlive != 0:
            return True
    
    def update(self,dx,dy):
        self.rect.x += dx
        self.rect.y += dy




class Sylv(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("Sylv.png")

        self.rect = self.image.get_rect()
    def update(self,dx,dy):
        self.rect.x += dx
        self.rect.y += dy




#muffin projectile 
class Laser(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("laserBeam.png")

        self.rect = self.image.get_rect()
    def update(self,dx,dy):
        self.rect.x += dx
        self.rect.y += dy

        
#making the worms
class Worm(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.lives = 3
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("Worm.png")
        self.rect = self.image.get_rect()
    def update(self,dx,dy):
        self.rect.x += dx
        self.rect.y += dy
class armRight(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("armRight.png")
        self.rect = self.image.get_rect()
        self.armRtimer = -1
    def update(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
        if self.armRtimer > 0:
            self.armRtimer -= 1
        if self.armRtimer == 0:
            self.kill()

    def countDownRight(self):
        self.armRtimer = 20
        rightArm_sprites_list.add(my_armRight)
        
class armLeft(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("armLeft.png")
        self.rect = self.image.get_rect()
        self.armLtimer = -1
    def update(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
        if self.armLtimer > 0:
            self.armLtimer -= 1
        if self.armLtimer == 0:
            self.kill()  
    def countDownLeft(self):
        self.armLtimer = 20
        leftArm_sprites_list.add(my_armLeft)    

#making piercing power up 
class PowerUp(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("PowerUp.png")
        self.rect = self.image.get_rect()
    def update(self,dx,dy):
        self.rect.x += dx
        self.rect.y += dy
class Bottle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("bottle.png")
        self.rect = self.image.get_rect()
    def update(self,dx,dy):
        self.rect.x += dx
        self.rect.y += dy
class Heart(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("heart.png")
        self.rect = self.image.get_rect()
    def update(self,dx,dy):
        self.rect.x += dx
        self.rect.y += dy
#water PowerUp
class Water(pygame.sprite.Sprite):
    def __init__(self,dx,dy):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("agua.png")
        self.rect = self.image.get_rect()
        self.dx = dx
        self.dy = dy
    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy
    
#make block to remove tofus
class Block(pygame.sprite.Sprite):
    def __init__(self, width, height):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([width, height])
        self.image.fill(black)
        self.rect = self.image.get_rect()
    def update(self,dx,dy):
        self.rect.x += dx
        self.rect.y += dy



# This is a list of every sprite.
# All blocks and the player block as well.
#init the objects

my_Ben = Ben()
my_Tofu = Tofu()
my_Muffin = Muffin()
my_Sylv = Sylv()
my_BlockBottom = Block(displayWidth, 1)
my_BlockTop = Block(displayWidth, 1)
my_BlockLeft = Block(1, displayHeight)
my_BlockRight = Block(1, displayHeight)
my_powerUp = PowerUp()
my_bottle = Bottle()
my_heart = Heart()
my_laser = Laser()
my_armLeft = armLeft()
my_armRight = armRight()

#init the objects to the sprite list
all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(my_Ben)

Block_sprites_list = pygame.sprite.Group()
Block_sprites_list.add(my_BlockBottom)
Block_sprites_list.add(my_BlockTop)
Block_sprites_list.add(my_BlockLeft)
Block_sprites_list.add(my_BlockRight)

Tofu_sprites_list = pygame.sprite.Group()
Tofu_sprites_list.add(my_Tofu)
TofuYHeight = my_Tofu.rect.width
TofuWidth = displayWidth
TofuHeight = displayHeight


Muffin_sprites_list = pygame.sprite.Group()

Sylv_sprites_list = pygame.sprite.Group()


Water_sprites_list = pygame.sprite.Group()
Laser_sprites_list = pygame.sprite.Group()

powerUp_sprites_list = pygame.sprite.Group()
bottle_sprites_list = pygame.sprite.Group()
heart_sprites_list = pygame.sprite.Group()

Worm_sprites_list = pygame.sprite.Group()
my_Ben.update(0,displayHeight-150)

leftArm_sprites_list = pygame.sprite.Group()
rightArm_sprites_list = pygame.sprite.Group()


randomPointx = random.randint(0, TofuWidth - my_Tofu.rect.x)
randomPointy = random.randint(0, (int (TofuHeight/12)))

#spawning tofu 
for i in range (5):
    my_Tofu = Tofu()
    Tofu_sprites_list.add(my_Tofu)
    valuex = random.randint(0, TofuWidth - my_Tofu.rect.x)
    valuey = random.randint(0, (int (TofuHeight/12)))
    my_Tofu.update(valuex,valuey)

    


def resetFun():
    #this resets all objects in the code
    global my_Tofu
    global my_powerUp
    global Tofu_sprites_list
    global TofuYHeight
    global TofuWidth
    global TofuHeight
    global powerUp_sprites_list
    global my_Muffin 
    global Muffin_sprites_list
    global valuex
    global valuey
    global gameLives
    global gameScore
    global tofuSpeed
    global benSpeed
    global notPiercing
    global randomMuffinPointY
    global my_bottle
    global bottle_sprites_list
    global my_heart
    global heart_sprites_list
    global my_laser
    global Laser_sprites_list
    global Sylv_sprites_list
    global my_Sylv
    global Worm_sprites_list
    global Water_sprites_list
    global newWater
    global waterAmount
    global gameLives

    
    gameLives = 5
    gameScore = 0
    tofuSpeed = 1
    benSpeed = 8
    notPiercing = True
    waterAmount = 5
    

    my_Tofu = Tofu()
    my_powerUp = PowerUp()
    my_Muffin = Muffin()
    my_bottle = Bottle()
    my_laser = Laser()

  
    Muffin_sprites_list = pygame.sprite.Group()
    #Muffin_sprites_list.add(my_Muffin)
    Tofu_sprites_list.add(my_Tofu)

    Tofu_sprites_list = pygame.sprite.Group()
    Tofu_sprites_list.add(my_Tofu)
    TofuYHeight = my_Tofu.rect.width
    TofuWidth = displayWidth - my_Tofu.rect.width
    TofuHeight = displayHeight



    powerUp_sprites_list = pygame.sprite.Group()
    bottle_sprites_list = pygame.sprite.Group()
    heart_sprites_list = pygame.sprite.Group()
    Laser_sprites_list = pygame.sprite.Group()
    Worm_sprites_list = pygame.sprite.Group()
    Sylv_sprites_list = pygame.sprite.Group()
    Water_sprites_list = pygame.sprite.Group()

    randomPointx = random.randint(0, TofuWidth - my_Tofu.rect.x)
    randomPointy = random.randint(0, (int (TofuHeight/12)))


    for i in range (5):
        my_Tofu = Tofu()
        Tofu_sprites_list.add(my_Tofu)
        valuex = random.randint(0, TofuWidth - my_Tofu.rect.x)
        valuey = random.randint(0, (int (TofuHeight/12)))
        my_Tofu.update(valuex,valuey)
    Worm_sprites_list.empty()
    Water_sprites_list.empty()




#Main movement loop
while not crashed:
    textLives()
    for muffin in Muffin_sprites_list:
            if muffin.canShoot():
                newLaser = Laser()
                Laser_sprites_list.add(newLaser)
                newLaser.rect.x = muffin.rect.x
                newLaser.rect.y = muffin.rect.y
            muffin.framesAlive += 1

    if gameLives < 1:
            gameOver()
            print("gameOver")
            gameOver()
            time.sleep(3)
            resetFun()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        pygame.event.pump()
            
        if gameLives < 1:
            print("gameOver")
            gameOver()
            time.sleep(3)
            resetFun()
            
        if gameScore % 2000 == 0 and gameScore != 0:
            print("new tofu")
            gameScore += 100
            my_Tofu = Tofu()
            Tofu_sprites_list.add(my_Tofu)
            valuex = random.randint(0, TofuWidth - my_Tofu.rect.x)
            valuey = random.randint(0, (int (TofuHeight/12)))
            my_Tofu.update(valuex,valuey)

        if gameScore % 2400 == 0 and gameScore != 0:
            print("new enemy Muffin")
            gameScore += 100
            my_Muffin = Muffin()
            Muffin_sprites_list.add(my_Muffin)
            randomMuffinPointY = random.randint(1, 60)
            my_Muffin.update(15, randomMuffinPointY)
        
            
        if gameScore % 3200 == 0 and gameScore != 0:
            gameScore += 100
            gameScore +=100
            tofuSpeed += 0.2
            benSpeed += 0.2
            
        if gameScore % 6300 == 0 and gameScore != 0:
            gameScore += 100
            my_powerUp = PowerUp()
            powerUp_sprites_list.add(my_powerUp)
            valuex = random.randint(0, TofuWidth - my_Tofu.rect.x)
            valuey = random.randint(0, (int (TofuHeight/12)))
            my_powerUp.update(valuex, valuey)

        if gameScore % 900 == 0 and gameScore != 0:

            gameScore += 100
            my_bottle = Bottle()
            bottle_sprites_list.add(my_bottle)
            valuex = random.randint(0, TofuWidth - my_Tofu.rect.x)
            valuey = random.randint(0, (int (TofuHeight/12)))
            my_bottle.update(valuex, valuey)
        if gameScore % 1100 == 0 and gameScore != 0:

            gameScore += 100
            my_heart = Heart()
            heart_sprites_list.add(my_heart)
            valuex = random.randint(0, TofuWidth - my_Tofu.rect.x)
            valuey = random.randint(0, (int (TofuHeight/12)))
            my_heart.update(valuex, valuey)

        if gameScore % 8500 == 0 and gameScore != 0:
            print("spawning bigGuy")
            gameScore += 200
            my_Sylv = Sylv()
            Sylv_sprites_list.add(my_Sylv)
            
            my_Sylv.update((displayWidth/2)/2,-250)
   
              
    #movement baby (for x)
        x = my_Ben.rect.x
        y = my_Ben.rect.y
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                x_change = -benSpeed

            elif event.key == pygame.K_d:
                x_change = benSpeed

            elif event.key == pygame.K_w:
                y_change = -benSpeed/2
            elif event.key == pygame.K_s:
                y_change = benSpeed/2

            
            

        if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d: 
                    x_change = 0
                elif event.key == pygame.K_s or event.key == pygame.K_w:
                    y_change = 0

                elif event.key == pygame.K_SPACE:
                    newWorm = Worm()
                    Worm_sprites_list.add(newWorm)
                    newWorm.rect.x = my_Ben.rect.x
                    newWorm.rect.y = my_Ben.rect.y
                elif event.key == pygame.K_l:
                    resetFun()
                
                elif event.key == pygame.K_LSHIFT and waterAmount > 0:
                    waterX = -2
                    for i in range(3):
                        newWater = Water(waterX,-2)
                        Water_sprites_list.add(newWater)
                        newWater.rect.x = my_Ben.rect.x
                        newWater.rect.y = my_Ben.rect.y
                        waterX += 2
                    waterAmount -= 1
                    
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            leftArm_sprites_list.add(my_armLeft)
            my_armLeft.rect.x = my_Ben.rect.x - 72
            my_armLeft.rect.y = my_Ben.rect.y
            my_armLeft.countDownLeft()
            
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 3:
            rightArm_sprites_list.add(my_armRight)
            my_armRight.rect.x = my_Ben.rect.x + 55
            my_armRight.rect.y = my_Ben.rect.y
            my_armRight.countDownRight()
            
            

                    
                        
    #hit detection and drawing sprites                    

                
    all_sprites_list.update(x_change,0)
    all_sprites_list.update(0,y_change)
#arm stuff
    rightArm_sprites_list.update(x_change, 0)
    rightArm_sprites_list.update(0, y_change)

    leftArm_sprites_list.update(x_change, 0)
    leftArm_sprites_list.update(0, y_change)


    #Tofu movement
    Tofu_sprites_list.update(0,tofuSpeed)
    #worm movement/ bullet movement 
    Worm_sprites_list.update(0,-2)
    Water_sprites_list.update()

    #muffin movement
    Muffin_sprites_list.update(2, 0)



    Laser_sprites_list.update(0,3)

    #Sylv movement
    Sylv_sprites_list.update(0,3)
    #powerUp Movement
    powerUp_sprites_list.update(0,1)
    bottle_sprites_list.update(0,1)
    heart_sprites_list.update(0,1)
        
    #Drawing them and whatnot
    game_Display.fill(black)
    space(0,0)
    #all_sprites_list.update(x_change, y_change)
    all_sprites_list.draw(game_Display)
    Tofu_sprites_list.draw(game_Display)
    Muffin_sprites_list.draw(game_Display)
    Worm_sprites_list.draw(game_Display)
    Water_sprites_list.draw(game_Display)
    Laser_sprites_list.draw(game_Display)
    powerUp_sprites_list.draw(game_Display)
    bottle_sprites_list.draw(game_Display)
    heart_sprites_list.draw(game_Display)
    rightArm_sprites_list.draw(game_Display)
    leftArm_sprites_list.draw(game_Display)
    Sylv_sprites_list.draw(game_Display)


    textLives()
    textScore()
    waterNum()
    
    Block_sprites_list.draw(game_Display)
    my_BlockBottom.rect.x = 0
    my_BlockBottom.rect.y = displayHeight+TofuYHeight
    my_BlockTop.rect.x = 0
    my_BlockTop.rect.y = 0 - TofuYHeight
    my_BlockLeft.rect.x = 0 - TofuYHeight
    my_BlockLeft.rect.y = 0
    my_BlockRight.rect.x = displayWidth + TofuYHeight
    my_BlockRight.rect.y = 0



    Tofu_hit_list = pygame.sprite.spritecollide(my_Ben, Tofu_sprites_list, True)
    Block_hit_list = pygame.sprite.spritecollide(my_BlockBottom, Tofu_sprites_list, True)
    BlockMuffin_hit_list = pygame.sprite.spritecollide(my_BlockRight, Muffin_sprites_list, True)
    BlockSylv_hit_list = pygame.sprite.spritecollide(my_BlockBottom, Sylv_sprites_list, True)
    TofuWater_hit_list = pygame.sprite.groupcollide(Tofu_sprites_list, Water_sprites_list, True, True )
    BlockWater_hit_list = pygame.sprite.groupcollide(Block_sprites_list, Water_sprites_list, False, True )
    BlockWorm_hit_list = pygame.sprite.groupcollide(Block_sprites_list, Worm_sprites_list, False, True )
    TofuWorm_hit_list = pygame.sprite.groupcollide(Tofu_sprites_list, Worm_sprites_list, True, notPiercing)
    MuffinWorm_hit_list = pygame.sprite.groupcollide(Muffin_sprites_list, Worm_sprites_list, True, True)
    MuffinWater_hit_list = pygame.sprite.groupcollide(Muffin_sprites_list, Water_sprites_list, True, True )
    powerUp_hit_list = pygame.sprite.spritecollide(my_Ben, powerUp_sprites_list, True)
    benLaser_hit_list = pygame.sprite.spritecollide(my_Ben, Laser_sprites_list, True)
    bottle_hit_list = pygame.sprite.spritecollide(my_Ben, bottle_sprites_list, True)
    heart_hit_list = pygame.sprite.spritecollide(my_Ben, heart_sprites_list, True)
    rightArm_hitlist = pygame.sprite.groupcollide(rightArm_sprites_list, Tofu_sprites_list, True, True)
    leftArm_hitlist = pygame.sprite.groupcollide(leftArm_sprites_list, Tofu_sprites_list, True, True)
    BenSylv_hit_list = pygame.sprite.spritecollide(my_Ben, Sylv_sprites_list, True)
    
#hit Detection
    for tofu in Tofu_hit_list:
    # update the tofu position
        valuex = random.randint(0, TofuWidth  - tofu.rect.width)
        tofu.rect.x = valuex
        tofu.rect.y = 0- tofu.rect.height
        Tofu_sprites_list.add(tofu)
        gameLives -= 1
        textLives()
        my_Ben.getHit()

    for tofu in rightArm_hitlist:
        valuex = random.randint(0, TofuWidth  - tofu.rect.width)
        tofu.rect.x = valuex
        tofu.rect.y = 0- tofu.rect.height
        gameScore += 100
        textScore()

        Tofu_sprites_list.add(tofu)
    for tofu in leftArm_hitlist:
        valuex = random.randint(0, TofuWidth  - tofu.rect.width)
        tofu.rect.x = valuex
        tofu.rect.y = 0- tofu.rect.height
        gameScore += 100
        textScore()
        
        Tofu_sprites_list.add(tofu)
        


    for laser in benLaser_hit_list:
        gameLives -= 1
        textLives()
        my_Ben.getHit()

    for sylvester in BenSylv_hit_list:
        gameLives -= 2
        textLives()
        my_Ben.getHit()

    for tofu in Block_hit_list:
        valuex = random.randint(0, TofuWidth  - tofu.rect.width)
        tofu.rect.x = valuex
        tofu.rect.y = 0- tofu.rect.height
        Tofu_sprites_list.add(tofu)
        gameLives -= 1
        textLives()

    for tofu in TofuWorm_hit_list:
        valuex = random.randint(0, TofuWidth  - tofu.rect.width)
        tofu.rect.x = valuex
        tofu.rect.y = 0- tofu.rect.height
        Tofu_sprites_list.add(tofu)
        gameScore += 100
        textScore()

        
    for tofu in TofuWater_hit_list:
        valuex = random.randint(0, TofuWidth  - tofu.rect.width)
        tofu.rect.x = valuex
        tofu.rect.y = 0- tofu.rect.height
        Tofu_sprites_list.add(tofu)
        gameScore += 100
        textScore()
    for muffin in BlockMuffin_hit_list:
        muffY = randomMuffinPointY = random.randint(1, 100)
        muffin.rect.x = 0
        muffin.rect.y = muffY
        Muffin_sprites_list.add(muffin)
        gameScore += 200
        textScore()
    for muffin in MuffinWorm_hit_list:
        muffY = randomMuffinPointY = random.randint(1, 100)
        muffin.rect.x = 0
        muffin.rect.y = muffY
        Muffin_sprites_list.add(muffin)
        gameScore += 200
        textScore()
    for muffin in MuffinWater_hit_list:
        muffY = randomMuffinPointY = random.randint(1, 100)
        muffin.rect.x = 0
        muffin.rect.y = muffY
        Muffin_sprites_list.add(muffin)
        gameScore += 200
        textScore()

    for tofu, wormList in TofuWorm_hit_list.items():
        for worm in wormList:
            worm.lives -= 1
            if worm.lives == 0:
                Worm_sprites_list.remove(worm)
        

    for powerUp in powerUp_hit_list:
        notPiercing = False

    for bottle in bottle_hit_list:
        waterAmount += 1 
        waterNum()

    for heart in heart_hit_list:
        gameLives += 1 
        textLives()

    
    pygame.display.update()
    clock.tick(60)

    
