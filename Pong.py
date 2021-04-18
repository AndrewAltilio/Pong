"""Pong, by Andrew Altilio
    This is a classic recreation of the retro game "Pong" for the Atari."""
#Import the modules to run the program.
import pygame, random, sys, time
from pygame.locals import *

def main():
    #Clock timer setup.
    pygame.init()
    mainClock = pygame.time.Clock()
    powerUp = pygame.time.Clock()

    #Set up the field.
    Field = pygame.image.load('soccer.jpg')
    BackRect = Field.get_rect()

    #Set up images for power ups.
    anchor = pygame.transform.scale(pygame.image.load('anchor.jpg'), (50,50))
    SlowDown = anchor.get_rect()

    #random variables to determine where the power ups will go.
    randomX = random.randint(71, 1120)
    randomY = random.randint(0,901)

    #Set up the window.
    WINDOWWIDTH = 1200
    WINDOWHEIGHT = 900
    windowSurface = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT),0,32)
    pygame.display.set_caption('Pong')

    #Set up the colors.
    WHITE = (255,255,255)
    BLACK = (0,0,0)
    RED = (255,0,0)
    GREEN = (0,255,0)
    BLUE = (0,0,255)
    ORANGE = (255,128,0)
    PURPLE = (145,34,255)
    PINK = (250,25,250)

    #Direction variables.
    moveDown = False
    moveUp = False
    moveDown2 = False
    moveUp2 = False
    UPLEFT = 7
    UPRIGHT= 9
    DOWNLEFT = 1
    DOWNRIGHT = 3
    RIGHT = 6
    LEFT = 4

    #Set up the move speed.
    MOVESPEED = 10

    #Set up the random color of player one.
    p1color = random.randint(1,7)
    if p1color == 1:
        p1color =  WHITE
    elif p1color == 2:
        p1color = RED
    elif p1color == 3:
        p1color = GREEN
    elif p1color == 4:
        p1color = BLUE
    elif p1color == 5:
        p1color = ORANGE
    elif p1color == 6:
        p1color = PURPLE
    elif p1color == 7:
        p1color = PINK

    #Set up the random color of player two.
    p2color = random.randint(1,7)
    if p2color == 1:
        p2color =  WHITE
    elif p2color == 2:
        p2color = RED
    elif p2color == 3:
        p1color = GREEN
    elif p2color == 4:
        p2color = BLUE
    elif p2color == 5:
        p2color = ORANGE
    elif p2color == 6:
        p2color = PURPLE
    elif p2color == 7:
        p2color = PINK

    #Set up the random color of the ball.
    ballColor = random.randint(1,7)
    if ballColor == 1:
        ballColor =  WHITE
    elif ballColor == 2:
        ballColor = RED
    elif ballColor == 3:
        ballColor = GREEN
    elif ballColor == 4:
        ballColor = BLUE
    elif ballColor == 5:
        ballColor = ORANGE
    elif ballColor == 6:
        ballColor = PURPLE
    elif ballColor == 7:
        ballColor = PINK

    #Sets up score trackers.
    p1Score = 0
    p2Score = 0
                          
    #Random direction of the ball.
    ballDir = random.randint(1,2)
    if ballDir == 1:
        ballDir = LEFT
    else:
        ballDir = RIGHT

    #Set up paddles and ball.
    #Information for the ball.
    b1 = {'rect':pygame.Rect(590,420,20,20),'color':ballColor,'dir': ballDir, 'speed':MOVESPEED*0.5}
    P1X = 70
    P1Y = 410
    P2X = 1120
    P2Y = 410
    
    #The paddles
    P1 = pygame.draw.rect(windowSurface,p1color,(P1X,P1Y,10,600))
    P2 = pygame.draw.rect(windowSurface,p2color,(P2X,P2Y,10,600))
    pong = [b1]

    #Set up the sounds.
    hitSound = pygame.mixer.Sound('hit sound.wav')
    goal1 = pygame.mixer.Sound('goal.wav')
    hitSound2 = pygame.mixer.Sound('hit sound2.wav')
    hitSound3 = pygame.mixer.Sound('hit sound3.wav')

    #theme = pygame.mixer.music.load('theme.wav')

    powerUp = pygame.time.get_ticks()




    #pygame.mixer.music.play(100,0.0)


    #Run the game loop.
    while True:
        
        #Draws the backround field.
        windowSurface.blit(Field,BackRect)

        #Adds counters to track the scores of each player.
        basicFont = pygame.font.SysFont(None,125)
        text = basicFont.render(str(p1Score),True, p1color)
        windowSurface.blit(text,(65,80))

        text2 = basicFont.render(str(p2Score),True, p2color)
        windowSurface.blit(text2,(1090,80))

        #Sets up a timer to spawn power ups.
        """seconds = (pygame.time.get_ticks() - powerUp)/1000
        if seconds > 5:
            slowList = [windowSurface.blit(anchor,(randomX,randomY))]"""
            
        #Redraws the paddles.
        P1 = pygame.draw.rect(windowSurface,p1color,(P1X,P1Y,10,125))
        P2 = pygame.draw.rect(windowSurface,p2color,(P2X,P2Y,10,125))
        
        #Check for QUIT.
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            MoveUp2 = True
            moveDown2 = False
            P1Y -= 25
        if keys[pygame.K_s]:
            moveUp2 = False
            moveDown2 = True
            P1Y += 25
        if keys[pygame.K_UP]:
            MoveUp = True
            moveDown = False
            P2Y -= 25
        if keys[pygame.K_DOWN]:
            moveUp = False
            moveDown = True
            P2Y += 25   
            """#Set up the controls for each player.
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    moveUp = True
                    moveDown = False
                    P2Y -= 25
                if event.key == K_DOWN:
                    moveUp = False
                    moveDown = True
                    P2Y += 25
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    MoveUp2 = True
                    moveDown2 = False
                    P1Y -= 25
                if event.key == pygame.K_s:
                    moveUp2 = False
                    moveDown2 = True
                    P1Y += 25
            if event.type == KEYUP:
                if event.key == K_UP:
                    moveUp = False
                if event.key == K_DOWN:
                    moveDown = False
            if event.type == KEYUP:
                if event.key == pygame.K_w:
                    moveUp2 = False
                if event.key == pygame.K_s:
                    MoveDown2 = False"""
                
        #move block data structure.
        if b1['dir'] == LEFT:
            b1['rect'].left -= MOVESPEED
        if b1['dir'] == RIGHT:
            b1['rect'].right += MOVESPEED
        if b1['dir'] == UPRIGHT:
            b1['rect'].right += MOVESPEED
            b1['rect'].top -= MOVESPEED
        if b1['dir'] == DOWNLEFT:
            b1['rect'].left -= MOVESPEED
            b1['rect'].top += MOVESPEED
        if b1['dir'] == DOWNRIGHT:
            b1['rect'].left += MOVESPEED
            b1['rect'].top += MOVESPEED
        if b1['dir'] == UPLEFT:
            b1['rect'].left -= MOVESPEED
            b1['rect'].top -= MOVESPEED

            #Check if block has moved out of the window.
        if b1['rect'].top < 0:
            hitSound2.play()
            if b1['dir'] == UPLEFT:
                #Plays sound when hit.
                hitSound2.play()
                b1['dir'] = DOWNLEFT
            if b1['dir'] == UPRIGHT:
                b1['dir'] = DOWNRIGHT
        if b1['rect'].bottom > WINDOWHEIGHT:
            #Plays sound when hit.
            hitSound3.play()
            if b1['dir'] == DOWNLEFT:
                b1['dir'] = UPLEFT
            if b1['dir'] == DOWNRIGHT:
                b1['dir'] = UPRIGHT

        #If player 2 scores, the block resets.
        if b1['rect'].left < 0:
            b1 = {'rect':pygame.Rect(590,420,20,20),'color':ballColor,'dir': LEFT, 'speed':MOVESPEED}
            goal1.play()
            p2Score += 1
            
        #If player 1 scores, the block resets.
        if b1['rect'].right > WINDOWWIDTH:
            b1 = {'rect':pygame.Rect(590,420,20,20),'color':ballColor,'dir': RIGHT, 'speed':MOVESPEED}
            goal1.play()
            p1Score += 1

        #If the ball hits one of the players, it will bounce off.
        if P1.colliderect(b1['rect']):
            b1['dir']=DOWNRIGHT
            hitSound.play()
        if P2.colliderect(b1['rect']):
            b1['dir']=UPLEFT
            hitSound.play()

        #Detect ball collision with a power up.
        if SlowDown.colliderect(b1['rect']):
            print("test")
            slowList.remove(anchor)
            
        #Redraws the ball and updates the screen.
        pygame.draw.rect(windowSurface, b1['color'], b1['rect'])
        mainClock.tick(60)
        pygame.display.update()

def title():
    gameMenu = True
    titleFont = pygame.font.SysFont(None,125)
    text = titleFont.render("press space to play",True , (255, 255, 255))
    windowSurface.fill(BLACK)
    windowSurface.blit(text, [320,240])
    #Startup menu.
    while gameMenu:
        windowSurface.fill(BLACK)
        windowSurface.blit(text, [320,240])
        pygame.display.update()
        mainClock.tick(15)

        for events in pygame.event.get():
                if events.type == K_SPACE:
                    return
                    #gameMenu = False

#title()
main()
