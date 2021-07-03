#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 15:42:07 2020

@author: ivicino
"""

import random, pygame, os
from pygame.locals import *

# code to ignore depreciation warnings
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

FPS = 7
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
CELLSIZE = 20
assert WINDOWWIDTH % CELLSIZE == 0, "Window width must be a multiple of cell size."
assert WINDOWHEIGHT % CELLSIZE == 0, "Window height must be a multiple of cell size."
CELLWIDTH = int(WINDOWWIDTH / CELLSIZE)
CELLHEIGHT = int(WINDOWHEIGHT / CELLSIZE)

#             R    G    B
WHITE     = (255, 255, 255)
BLACK     = (  0,   0,   0)
RED       = (255,   0,   0)
GREEN     = (  0, 255,   0)
DARKGREEN = (  0, 155,   0)
DARKGRAY  = ( 40,  40,  40)
DARKBLUE =  (  0,   0, 139)
LIGHTBLUE = (  0, 191, 255)

BGCOLOR = BLACK


UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

HEAD = 0    # syntactic sugar: index of the worm's head




def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
    pygame.display.set_caption('Wormy')

    showStartScreen()
    while True:
        runGame()
        showGameOverScreen()


def runGame():
    # Set a random start point.
    startx = random.randint(5, CELLWIDTH - 6)
    starty = random.randint(5, CELLHEIGHT - 6)
    wormCoords = [{'x': startx,     'y': starty},
                  {'x': startx - 1, 'y': starty},
                  {'x': startx - 2, 'y': starty}]
    PortalX = CELLWIDTH/2
    PortalY = 0

    direction = RIGHT

    NextLevel = 10

    # Start the apple in a random place.
    apple = getRandomLocation()
    apple1 = getRandomLocation()
    apple2 = getRandomLocation()
    apple3 = getRandomLocation()
    apple4 = getRandomLocation()
    apple5 = getRandomLocation()

    while True:     # main game loop
        for event in pygame.event.get():    # event handling loop
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if (event.key == K_LEFT or event.key == K_a) and direction != RIGHT:
                    direction = LEFT
                elif (event.key == K_RIGHT or event.key == K_d) and direction != LEFT:
                    direction = RIGHT
                elif (event.key == K_UP or event.key == K_w) and direction != DOWN:
                    direction = UP
                elif (event.key == K_DOWN or event.key == K_s) and direction != UP:
                    direction = DOWN
                elif event.key == K_ESCAPE:
                    terminate()

        # collision with portal leading to level2
        if len(wormCoords) - 3 >= NextLevel:
            if wormCoords[HEAD]['x'] == PortalX and wormCoords[HEAD]['y'] == PortalY:
                # print('hit!')
                runGame2()
         
        # check if the worm has hit itself or the edge
        if wormCoords[HEAD]['x'] == -1 or wormCoords[HEAD]['x'] == CELLWIDTH or wormCoords[HEAD]['y'] == -1 or wormCoords[HEAD]['y'] == CELLHEIGHT:
            return  # game over
        for wormBody in wormCoords[1:]:
            if wormBody['x'] == wormCoords[HEAD]['x'] and wormBody['y'] == wormCoords[HEAD]['y']:
                return  # game over

        # check if worm has eaten an apply
        if wormCoords[HEAD]['x'] == apple['x'] and wormCoords[HEAD]['y'] == apple['y']:
            apple = getRandomLocation()     # set a new apple somewhere
        elif wormCoords[HEAD]['x'] == apple1['x'] and wormCoords[HEAD]['y'] == apple1['y']:
            apple1 = getRandomLocation()
        elif wormCoords[HEAD]['x'] == apple2['x'] and wormCoords[HEAD]['y'] == apple2['y']:
            apple2 = getRandomLocation()
        elif wormCoords[HEAD]['x'] == apple3['x'] and wormCoords[HEAD]['y'] == apple3['y']:
            apple3 = getRandomLocation()
        elif wormCoords[HEAD]['x'] == apple4['x'] and wormCoords[HEAD]['y'] == apple4['y']:
            apple4 = getRandomLocation()
        elif wormCoords[HEAD]['x'] == apple5['x'] and wormCoords[HEAD]['y'] == apple5['y']:
            apple5 = getRandomLocation()
            # don't remove worm's tail segment
        else:
            del wormCoords[-1]  # remove worm's tail segment

        # move the worm by adding a segment in the direction it is moving
        if direction == UP:
            newHead = {'x': wormCoords[HEAD]['x'], 'y': wormCoords[HEAD]['y'] - 1}
        elif direction == DOWN:
            newHead = {'x': wormCoords[HEAD]['x'], 'y': wormCoords[HEAD]['y'] + 1}
        elif direction == LEFT:
            newHead = {'x': wormCoords[HEAD]['x'] - 1, 'y': wormCoords[HEAD]['y']}
        elif direction == RIGHT:
            newHead = {'x': wormCoords[HEAD]['x'] + 1, 'y': wormCoords[HEAD]['y']}
        wormCoords.insert(0, newHead)
        DISPLAYSURF.fill(BGCOLOR)
        drawGrid()
        drawWorm(wormCoords)
        drawApple(apple)
        drawApple(apple1)
        drawApple(apple2)
        drawApple(apple3)
        drawApple(apple4)
        drawApple(apple5)
        drawScore(len(wormCoords) - 3)
        # When the portal will spawn
        if len(wormCoords) - 3 >= NextLevel:
            drawPortal()
        pygame.display.update()
        FPSCLOCK.tick(FPS)


def runGame2():
    # set to move at a faster speed
    FPS = 7
    # Set a random start point.
    startx = 20
    starty = 22
    wormCoords = [{'x': startx,     'y': starty},
                  {'x': startx - 1, 'y': starty},
                  {'x': startx - 2, 'y': starty}]
    PortalX = CELLWIDTH/2
    PortalY = 0

    Wallx1 = CELLWIDTH/2

    Wally7 = 12
    Wally8 = 13
    Wally9 = 14
    Wally10 = 15
    Wally11 = 16
    Wally12 = 17
  

    direction = RIGHT

    NextLevel = 10

    # Start the apple in a random place.
    apple = getRandomLocation()
    apple1 = getRandomLocation()
    apple2 = getRandomLocation()
    apple3 = getRandomLocation()
    apple4 = getRandomLocation()
    apple5 = getRandomLocation()

    
    while True:     # main game loop
        for event in pygame.event.get():    # event handling loop
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if (event.key == K_LEFT or event.key == K_a) and direction != RIGHT:
                    direction = LEFT
                elif (event.key == K_RIGHT or event.key == K_d) and direction != LEFT:
                    direction = RIGHT
                elif (event.key == K_UP or event.key == K_w) and direction != DOWN:
                    direction = UP
                elif (event.key == K_DOWN or event.key == K_s) and direction != UP:
                    direction = DOWN
                elif event.key == K_ESCAPE:
                    terminate()


        # collisions with the walls____________________________________________________
        if wormCoords[HEAD]['x'] == Wallx1 and wormCoords[HEAD]['y'] == Wally7 or wormCoords[HEAD]['x'] == Wallx1 and wormCoords[HEAD]['y'] == Wally8 or wormCoords[HEAD]['x'] == Wallx1 and wormCoords[HEAD]['y'] == Wally9 or wormCoords[HEAD]['x'] == Wallx1 and wormCoords[HEAD]['y'] == Wally10 or wormCoords[HEAD]['x'] == Wallx1 and wormCoords[HEAD]['y'] == Wally11 or wormCoords[HEAD]['x'] == Wallx1 and wormCoords[HEAD]['y'] == Wally12:
            return

        # collision with portal leading to level2
        if len(wormCoords) - 3 >= NextLevel:
            if wormCoords[HEAD]['x'] == PortalX and wormCoords[HEAD]['y'] == PortalY:
                print('FiNal LevEL!')
                runGame3()

        # check if the worm has hit itself or the edge
        if wormCoords[HEAD]['x'] == -1 or wormCoords[HEAD]['x'] == CELLWIDTH or wormCoords[HEAD]['y'] == -1 or wormCoords[HEAD]['y'] == CELLHEIGHT:
            return  # game over
        for wormBody in wormCoords[1:]:
            if wormBody['x'] == wormCoords[HEAD]['x'] and wormBody['y'] == wormCoords[HEAD]['y']:
                return  # game over

        # check if worm has eaten an apply
        if wormCoords[HEAD]['x'] == apple['x'] and wormCoords[HEAD]['y'] == apple['y']:
            apple = getRandomLocation()     # set a new apple somewhere
        elif wormCoords[HEAD]['x'] == apple1['x'] and wormCoords[HEAD]['y'] == apple1['y']:
            apple1 = getRandomLocation()
        elif wormCoords[HEAD]['x'] == apple2['x'] and wormCoords[HEAD]['y'] == apple2['y']:
            apple2 = getRandomLocation()
        elif wormCoords[HEAD]['x'] == apple3['x'] and wormCoords[HEAD]['y'] == apple3['y']:
            apple3 = getRandomLocation()
        elif wormCoords[HEAD]['x'] == apple4['x'] and wormCoords[HEAD]['y'] == apple4['y']:
            apple4 = getRandomLocation()
        elif wormCoords[HEAD]['x'] == apple5['x'] and wormCoords[HEAD]['y'] == apple5['y']:
            apple5 = getRandomLocation()
            # don't remove worm's tail segment
        else:
            del wormCoords[-1]  # remove worm's tail segment

        # move the worm by adding a segment in the direction it is moving
        if direction == UP:
            newHead = {'x': wormCoords[HEAD]['x'], 'y': wormCoords[HEAD]['y'] - 1}
        elif direction == DOWN:
            newHead = {'x': wormCoords[HEAD]['x'], 'y': wormCoords[HEAD]['y'] + 1}
        elif direction == LEFT:
            newHead = {'x': wormCoords[HEAD]['x'] - 1, 'y': wormCoords[HEAD]['y']}
        elif direction == RIGHT:
            newHead = {'x': wormCoords[HEAD]['x'] + 1, 'y': wormCoords[HEAD]['y']}
        wormCoords.insert(0, newHead)
        DISPLAYSURF.fill(BGCOLOR)
        drawGrid()
        drawWorm(wormCoords)
        drawApple(apple)
        drawApple(apple1)
        drawApple(apple2)
        drawApple(apple3)
        drawApple(apple4)
        drawApple(apple5)
        drawScore(len(wormCoords) - 3)
        drawWalls()
        # When the portal will spawn
        if len(wormCoords) - 3 >= NextLevel:
            drawPortal()
        pygame.display.update()
        FPSCLOCK.tick(FPS)


def runGame3():
    # set to move at a faster speed
    FPS = 10
    # Set a random start point.
    startx = 15
    starty = 18
    wormCoords = [{'x': startx,     'y': starty},
                  {'x': startx - 1, 'y': starty},
                  {'x': startx - 2, 'y': starty}]
    PortalX = CELLWIDTH/2
    PortalY = 0
    
    Wallx2 = CELLWIDTH/4
    Wallx = CELLWIDTH/4*3

    Wally1 = 6
    Wally2 = 7
    Wally3 = 8
    Wally4 = 9
    Wally5 = 10
    Wally6 = 11
    Wally7 = 12
    Wally8 = 13
    Wally9 = 14
    Wally10 = 15
    Wally11 = 16
    Wally12 = 17
    Wally13 = 18
    Wally14 = 19
    Wally15 = 20

    direction = RIGHT

    NextLevel = 20

    # Start the apple in a random place.
    apple = getRandomLocation()
    apple = getRandomLocation()
    apple1 = getRandomLocation()
    apple2 = getRandomLocation()
    apple3 = getRandomLocation()
    apple4 = getRandomLocation()
    apple5 = getRandomLocation()

    while True:     # main game loop
        for event in pygame.event.get():    # event handling loop
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if (event.key == K_LEFT or event.key == K_a) and direction != RIGHT:
                    direction = LEFT
                elif (event.key == K_RIGHT or event.key == K_d) and direction != LEFT:
                    direction = RIGHT
                elif (event.key == K_UP or event.key == K_w) and direction != DOWN:
                    direction = UP
                elif (event.key == K_DOWN or event.key == K_s) and direction != UP:
                    direction = DOWN
                elif event.key == K_ESCAPE:
                    terminate()
        
        # collisions with the walls____________________________________________________
        if wormCoords[HEAD]['x'] == Wallx2 and wormCoords[HEAD]['y'] == Wally1 or wormCoords[HEAD]['x'] == Wallx2 and wormCoords[HEAD]['y'] == Wally2 or wormCoords[HEAD]['x'] == Wallx2 and wormCoords[HEAD]['y'] == Wally3 or wormCoords[HEAD]['x'] == Wallx2 and wormCoords[HEAD]['y'] == Wally4 or wormCoords[HEAD]['x'] == Wallx2 and wormCoords[HEAD]['y'] == Wally5 or wormCoords[HEAD]['x'] == Wallx2 and wormCoords[HEAD]['y'] == Wally6 or wormCoords[HEAD]['x'] == Wallx2 and wormCoords[HEAD]['y'] == Wally7 or wormCoords[HEAD]['x'] == Wallx2 and wormCoords[HEAD]['y'] == Wally8 or wormCoords[HEAD]['x'] == Wallx2 and wormCoords[HEAD]['y'] == Wally9 or wormCoords[HEAD]['x'] == Wallx2 and wormCoords[HEAD]['y'] == Wally10 or wormCoords[HEAD]['x'] == Wallx2 and wormCoords[HEAD]['y'] == Wally11 or wormCoords[HEAD]['x'] == Wallx2 and wormCoords[HEAD]['y'] == Wally12 or wormCoords[HEAD]['x'] == Wallx2 and wormCoords[HEAD]['y'] == Wally13 or wormCoords[HEAD]['x'] == Wallx2 and wormCoords[HEAD]['y'] == Wally14 or wormCoords[HEAD]['x'] == Wallx2 and wormCoords[HEAD]['y'] == Wally15:
            return
        if wormCoords[HEAD]['x'] == Wallx and wormCoords[HEAD]['y'] == Wally1 or wormCoords[HEAD]['x'] == Wallx and wormCoords[HEAD]['y'] == Wally2 or wormCoords[HEAD]['x'] == Wallx and wormCoords[HEAD]['y'] == Wally3 or wormCoords[HEAD]['x'] == Wallx and wormCoords[HEAD]['y'] == Wally4 or wormCoords[HEAD]['x'] == Wallx and wormCoords[HEAD]['y'] == Wally5 or wormCoords[HEAD]['x'] == Wallx and wormCoords[HEAD]['y'] == Wally6 or wormCoords[HEAD]['x'] == Wallx and wormCoords[HEAD]['y'] == Wally7 or wormCoords[HEAD]['x'] == Wallx and wormCoords[HEAD]['y'] == Wally8 or wormCoords[HEAD]['x'] == Wallx and wormCoords[HEAD]['y'] == Wally9 or wormCoords[HEAD]['x'] == Wallx and wormCoords[HEAD]['y'] == Wally10 or wormCoords[HEAD]['x'] == Wallx and wormCoords[HEAD]['y'] == Wally11 or wormCoords[HEAD]['x'] == Wallx and wormCoords[HEAD]['y'] == Wally12 or wormCoords[HEAD]['x'] == Wallx and wormCoords[HEAD]['y'] == Wally13 or wormCoords[HEAD]['x'] == Wallx and wormCoords[HEAD]['y'] == Wally14 or wormCoords[HEAD]['x'] == Wallx and wormCoords[HEAD]['y'] == Wally15:
            return

        # collision with portal leading to win screen
        if len(wormCoords) - 3 >= NextLevel:
            if wormCoords[HEAD]['x'] == PortalX and wormCoords[HEAD]['y'] == PortalY:
                showWinGameScreen()
            
        # check if the worm has hit itself or the edge
        if wormCoords[HEAD]['x'] == -1 or wormCoords[HEAD]['x'] == CELLWIDTH or wormCoords[HEAD]['y'] == -1 or wormCoords[HEAD]['y'] == CELLHEIGHT:
            return  # game over
        for wormBody in wormCoords[1:]:
            if wormBody['x'] == wormCoords[HEAD]['x'] and wormBody['y'] == wormCoords[HEAD]['y']:
                return  # game over

        # check if worm has eaten an apply
        if wormCoords[HEAD]['x'] == apple['x'] and wormCoords[HEAD]['y'] == apple['y']:
            apple = getRandomLocation()     # set a new apple somewhere
        elif wormCoords[HEAD]['x'] == apple1['x'] and wormCoords[HEAD]['y'] == apple1['y']:
            apple1 = getRandomLocation()
        elif wormCoords[HEAD]['x'] == apple2['x'] and wormCoords[HEAD]['y'] == apple2['y']:
            apple2 = getRandomLocation()
        elif wormCoords[HEAD]['x'] == apple3['x'] and wormCoords[HEAD]['y'] == apple3['y']:
            apple3 = getRandomLocation()
        elif wormCoords[HEAD]['x'] == apple4['x'] and wormCoords[HEAD]['y'] == apple4['y']:
            apple4 = getRandomLocation()
        elif wormCoords[HEAD]['x'] == apple5['x'] and wormCoords[HEAD]['y'] == apple5['y']:
            apple5 = getRandomLocation()
        # don't remove worm's tail segment
        else:
            del wormCoords[-1]  # remove worm's tail segment

        # move the worm by adding a segment in the direction it is moving
        if direction == UP:
            newHead = {'x': wormCoords[HEAD]['x'], 'y': wormCoords[HEAD]['y'] - 1}
        elif direction == DOWN:
            newHead = {'x': wormCoords[HEAD]['x'], 'y': wormCoords[HEAD]['y'] + 1}
        elif direction == LEFT:
            newHead = {'x': wormCoords[HEAD]['x'] - 1, 'y': wormCoords[HEAD]['y']}
        elif direction == RIGHT:
            newHead = {'x': wormCoords[HEAD]['x'] + 1, 'y': wormCoords[HEAD]['y']}
        wormCoords.insert(0, newHead)
        DISPLAYSURF.fill(BGCOLOR)
        drawGrid()
        drawWorm(wormCoords)
        drawApple(apple)
        drawApple(apple1)
        drawApple(apple2)
        drawApple(apple3)
        drawApple(apple4)
        drawApple(apple5)
        drawScore(len(wormCoords) - 3)
        drawWalls2()
        drawWalls3()
        # When the portal will spawn
        if len(wormCoords) - 3 >= NextLevel:
            drawPortal()
        pygame.display.update()
        FPSCLOCK.tick(FPS)



def drawPressKeyMsg():
    pressKeySurf = BASICFONT.render('Press a key to play.', True, WHITE)
    pressKeyRect = pressKeySurf.get_rect()
    pressKeyRect.topleft = (WINDOWWIDTH - 200, WINDOWHEIGHT - 30)
    DISPLAYSURF.blit(pressKeySurf, pressKeyRect)

def drawPressKeyMsg2():  # for use with the win screen
    pressKeySurf = BASICFONT.render('Press a key to play.', True, BLACK)
    pressKeyRect = pressKeySurf.get_rect()
    pressKeyRect.topleft = (WINDOWWIDTH - 200, WINDOWHEIGHT - 30)
    DISPLAYSURF.blit(pressKeySurf, pressKeyRect)


def checkForKeyPress():
    if len(pygame.event.get(QUIT)) > 0:
        terminate()

    keyUpEvents = pygame.event.get(KEYUP)
    if len(keyUpEvents) == 0:
        return None
    if keyUpEvents[0].key == K_ESCAPE:
        terminate()
    return keyUpEvents[0].key


def showStartScreen():
    titleFont = pygame.font.Font('freesansbold.ttf', 100)
    titleSurf1 = titleFont.render('Wormy!', True, WHITE, DARKGREEN)
    titleSurf2 = titleFont.render('Wormy!', True, GREEN)

    degrees1 = 0
    degrees2 = 0
    while True:
        DISPLAYSURF.fill(BGCOLOR)
        rotatedSurf1 = pygame.transform.rotate(titleSurf1, degrees1)
        rotatedRect1 = rotatedSurf1.get_rect()
        rotatedRect1.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2)
        DISPLAYSURF.blit(rotatedSurf1, rotatedRect1)

        rotatedSurf2 = pygame.transform.rotate(titleSurf2, degrees2)
        rotatedRect2 = rotatedSurf2.get_rect()
        rotatedRect2.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2)
        DISPLAYSURF.blit(rotatedSurf2, rotatedRect2)

        drawPressKeyMsg()

        if checkForKeyPress():
            pygame.event.get() # clear event queue
            return
        pygame.display.update()
        FPSCLOCK.tick(FPS)
        degrees1 += 3 # rotate by 3 degrees each frame
        degrees2 += 7 # rotate by 7 degrees each frame


def terminate():
    pygame.quit()
    os._exit(0)


def getRandomLocation():
    return {'x': random.randint(0, CELLWIDTH - 1), 'y': random.randint(0, CELLHEIGHT - 1)}
    


def showGameOverScreen():
    DISPLAYSURF.fill(BGCOLOR)
    gameOverFont = pygame.font.Font('freesansbold.ttf', 150)
    gameSurf = gameOverFont.render('Game', True, WHITE)
    overSurf = gameOverFont.render('Over', True, WHITE)
    gameRect = gameSurf.get_rect()
    overRect = overSurf.get_rect()
    gameRect.midtop = (WINDOWWIDTH / 2, 10)
    overRect.midtop = (WINDOWWIDTH / 2, gameRect.height + 10 + 25)

    DISPLAYSURF.blit(gameSurf, gameRect)
    DISPLAYSURF.blit(overSurf, overRect)
    drawPressKeyMsg()
    pygame.display.update()
    pygame.time.wait(500)
    checkForKeyPress()  # clear out any key presses in the event queue

    while True:
        if checkForKeyPress():
            pygame.event.get()  # clear event queue
            return
def showWinGameScreen():
    DISPLAYSURF.fill(GREEN)
    gameOverFont = pygame.font.Font('freesansbold.ttf', 75)
    gameSurf = gameOverFont.render('You', True, BLACK)
    overSurf = gameOverFont.render('Won', True, BLACK)
    gameRect = gameSurf.get_rect()
    overRect = overSurf.get_rect()
    gameRect.midtop = (WINDOWWIDTH / 2, 10)
    overRect.midtop = (WINDOWWIDTH / 2, gameRect.height + 10 + 25)

    DISPLAYSURF.blit(gameSurf, gameRect)
    DISPLAYSURF.blit(overSurf, overRect)
    drawPressKeyMsg2()
    pygame.display.update()
    pygame.time.wait(500)
    checkForKeyPress()  # clear out any key presses in the event queue

    while True:
        if checkForKeyPress():
            pygame.event.get()  # clear event queue
            return



def drawScore(score):
    scoreSurf = BASICFONT.render('Score: %s' % (score), True, WHITE)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (WINDOWWIDTH - 120, 10)
    DISPLAYSURF.blit(scoreSurf, scoreRect)


def drawWorm(wormCoords):
    for coord in wormCoords:
        x = coord['x'] * CELLSIZE
        y = coord['y'] * CELLSIZE
        wormSegmentRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
        pygame.draw.rect(DISPLAYSURF, DARKBLUE, wormSegmentRect)  #DARKGREEN
        wormInnerSegmentRect = pygame.Rect(x + 4, y + 4, CELLSIZE - 8, CELLSIZE - 8)
        pygame.draw.rect(DISPLAYSURF, GREEN, wormInnerSegmentRect)


def drawApple(coord):
    x = coord['x'] * CELLSIZE
    y = coord['y'] * CELLSIZE
    appleRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
    pygame.draw.rect(DISPLAYSURF, RED, appleRect)


def drawGrid():
    for x in range(0, WINDOWWIDTH, CELLSIZE):   # draw vertical lines
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (x, 0), (x, WINDOWHEIGHT))
    for y in range(0, WINDOWHEIGHT, CELLSIZE):  # draw horizontal lines
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (0, y), (WINDOWWIDTH, y))


def drawPortal():
    x = WINDOWWIDTH/2
    y = 0
    PORTAL = pygame.Rect(x, y, CELLSIZE, 10)
    pygame.draw.rect(DISPLAYSURF, WHITE, PORTAL)
    # pygame.Rect(left, top, width, height)


def drawWalls():
    wall = pygame.Rect(WINDOWWIDTH/2, WINDOWHEIGHT*.5, CELLSIZE, WINDOWWIDTH/4)
    pygame.draw.rect(DISPLAYSURF, LIGHTBLUE, wall)


def drawWalls2():
    wall = pygame.Rect(WINDOWWIDTH/4, WINDOWHEIGHT*.25, CELLSIZE, WINDOWWIDTH/2)
    pygame.draw.rect(DISPLAYSURF, LIGHTBLUE, wall)


def drawWalls3():
    wall = pygame.Rect(WINDOWWIDTH/4*3, WINDOWHEIGHT*.25, CELLSIZE, WINDOWWIDTH/2)
    pygame.draw.rect(DISPLAYSURF, LIGHTBLUE, wall)
    

if __name__ == '__main__':
    main()
