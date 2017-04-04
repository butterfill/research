

# Terminator Study 2x2 design (investment and coordination)





import random, pygame, sys

from pygame.locals import *

import time

import csv

import cPickle

import math



FPS = 17

WINDOWWIDTH = 840

WINDOWHEIGHT = 680

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

BLUE      = (  0, 191, 255)

DARKBLUE  = (  0,   0, 139)

YELLOW    = (255, 255,   0)

PURPLE    = (128,  0,  128)

ORANGE    = (255,  165,  0)

GREENISHBLUE = (34,  208, 184)

BGCOLOR = BLACK



UP = 'up'

DOWN = 'down'

LEFT = 'left'

RIGHT = 'right'



HEAD = 0 # syntactic sugar: index of the worm's head

start = 0 # the start of duration measurement 

end = 0 # the end of duration measurement

duration = 0 

score = 0

count1 = 0

count2 = 0

investmentList = []

persistenceList = []

applesList = []

text1 = ''

robotcount1 = 0

robotcount2 = 0

participant = ' '

invisibleApple1List = []
invisibleApple2List = []
invisibleApple1 = 0
invisibleApple2 = 0
startIA1 = 0
startIA2 = 0

class Blocks:

    '''A class that organises the conditions and the measured dependent variable together.'''

    

    def __init__(self, name, investment, noncoordination, instruction1, instruction2, captchaNumber, captchaDelete = 1, durationOfpersistence = 0, scores = 0):

        self.name = name

        self.investment = investment

        self.noncoordination = noncoordination

        self.instruction1 = instruction1

        self.instruction2 = instruction2

        self.captchaNumber = captchaNumber

        self.captchaDelete = captchaDelete

        self.durationOfpersistence = durationOfpersistence

        self.scores = scores

        

    def recordduration(self):

        self.durationOfpersistence = duration

    

    def recordscores(self):# apples collected

        self.scores = score

        

#creates Blocks for Session A     

block0 = Blocks('Practice Round', 'RFh47hx3', 0, 'In this round, you will be operating the snake together with your partner.',  'You are in control of the left and right directions.', 13)  

block1 = Blocks('Round 1', 'Rg9', 1, 'In this round, you and your partner will each be operating your own snake.','You are in control of all four directions for your snake.', 3, 2)

block2 = Blocks('Round 2', 'gh7Zj9967f43', 0, 'In this round, you will be operating the snake together with your partner.',  'You are in control of the left and right directions.', 12)

block3 = Blocks('Round 3', 'iri87gHHr9f7D', 1, 'In this round, you and your partner will each be operating your own snake.','You are in control of all four directions for your snake.', 12, 3)

block4 = Blocks('Round 4', 'Z28', 0,'In this round, you will be operating the snake together with your partner.',  'You are in control of the left and right directions.', 3, 2)

block5 = Blocks('Round 5', 'ghHuJ6g4h2h', 0, 'In this round, you will be operating the snake together with your partner.',  'You are in control of the left and right directions.', 12, 4)

block6 = Blocks('Round 6', 'ifX', 1, 'In this round, you and your partner will each be operating your own snake.','You are in control of all four directions for your snake.', 3, 2)

block7 = Blocks('Round 7', '7gl', 0, 'In this round, you will be operating the snake together with your partner.',  'You are in control of the left and right directions.', 3)

block8 = Blocks('Round 8', 'f6zi90go8h7Q', 0, 'In this round, you will be operating the snake together with your partner.',  'You are in control of the left and right directions.', 12, 2)

block9 = Blocks('Round 9', 'f3Rji87D224z', 1, 'In this round, you and your partner will each be operating your own snake.','You are in control of all four directions for your snake.', 12, 4)

block10 = Blocks('Round 10', '4g2', 0, 'In this round, you will be operating the snake together with your partner.',  'You are in control of the left and right directions.', 3, 2)

block11 = Blocks('Round 11', 'di9', 1, 'In this round, you and your partner will each be operating your own snake.','You are in control of all four directions for your snake.', 3)

block12 = Blocks('Round 12', 'f9ki7z39uj993', 1, 'In this round, you and your partner will each be operating your own snake.','You are in control of all four directions for your snake.',12)

block13 = Blocks('Round 13', '47h', 0, 'In this round, you will be operating the snake together with your partner.',  'You are in control of the left and right directions.', 3)

block14 = Blocks('Round 14', 'd65g3jikbn31', 0, 'In this round, you will be operating the snake together with your partner.',  'You are in control of the left and right directions.', 12)

block15 = Blocks('Round 15', 'ghr7h3jkj20G', 1, 'In this round, you and your partner will each be operating your own snake.','You are in control of all four directions for your snake.', 12, 3)

block16 = Blocks('Round 16', 'zfr', 1, 'In this round, you and your partner will each be operating your own snake.','You are in control of all four directions for your snake.', 3)

block17 = Blocks('Round 17', '5hg7fg8h3iiZ', 0, 'In this round, you will be operating the snake together with your partner.',  'You are in control of the left and right directions.', 12)

block18 = Blocks('Round 18', 'h45', 1, 'In this round, you and your partner will each be operating your own snake.','You are in control of all four directions for your snake.', 3, 2)

block19 = Blocks('Round 19', 'k67', 0, 'In this round, you will be operating the snake together with your partner.',  'You are in control of the left and right directions.', 3)

block20 = Blocks('Round 20', 'lj0hZg59vXz5', 1,'In this round, you and your partner will each be operating your own snake.', 'You are in control of all four directions for your snake.', 12, 4)

sessionA = [block0, block1, block2, block3, block4, block5, block6, block7,

block8, block9, block10, block11, block12, block13, block14, block15, block16, block17, block18, block19, block20]





def main():

    global FPSCLOCK, DISPLAYSURF, BASICFONT



    pygame.init()

    FPSCLOCK = pygame.time.Clock()

    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), pygame.RESIZABLE)

    BASICFONT = pygame.font.Font('freesansbold.ttf', 15)

    pygame.display.set_caption('Experiment1')

    participant()

    screen_0()

    screen_1()

    screen_2()

    screen_3()

    screen_4()

    screen_5()

    captchaInstructionScreen()

    



    for item in sessionA:

        global duration

        text = item.name

        waitingscreen(text)

        investmentList.append(text)

        captchaNumber = item.captchaNumber

        captchaDelete = item.captchaDelete

        captchascreen(captchaNumber, captchaDelete)

        global text1

        text1 = item.investment

        text2 = item.instruction1

        text3 = item.instruction2

        accepctancescreen(text1,text2,text3)

        if item.noncoordination == 0:

            runGame2_coordination()

        else:

            runGame2_noncoordination()

        invisibleApple1List.append('stop')
        invisibleApple2List.append('stop')

        duration = end - start

        persistenceList.append(duration)

        item.recordduration()

        spoilScreen(score)

        applesList.append(score)

        item.recordscores()

        

    file_Name = '%s'%(participant)

    fileObject = open(file_Name, 'wb')

    cPickle.dump(sessionA,fileObject)

    fileObject.close()

        

    with open('%s.csv' %(participant), 'wb') as csvfile:

        participant_writer = csv.writer(csvfile, delimiter=' ',

                            quotechar='|', quoting=csv.QUOTE_MINIMAL)

        participant_writer.writerow(investmentList)

        participant_writer.writerow(persistenceList)

        participant_writer.writerow(applesList)

        participant_writer.writerow(invisibleApple1)
        
        participant_writer.writerow(invisibleApple2)

    thanks()

        







def runGame2_coordination():

    # Set a start point.

    startx = random.randint(5, CELLWIDTH - 6)

    starty = random.randint(5, CELLHEIGHT - 6)

    wormCoords = [{'x': startx,     'y': starty},

                  {'x': startx - 1, 'y': starty},

                  {'x': startx - 2, 'y': starty}]

    direction = RIGHT



    start2x = random.randint(5, CELLWIDTH - 6)

    start2y = random.randint(5, CELLHEIGHT - 6)

    wormCoords2 = [{'x': startx,     'y': starty},

                  {'x': startx - 1, 'y': starty},

                  {'x': startx - 2, 'y': starty}]

    direction2 = LEFT



    # Start the apple in a random place.

    apple = getRandomLocation()

    apple2 = getRandomLocation()

    # Start measuring the duration of the game

    global start

    start = time.time()

    global invisibleApple1

    invisibleApple1 = 0
    
    global invisibleApple2

    invisibleApple2 = 0

    # main game loop

    while True:

#robotsnake

        

        x = wormCoords2[HEAD]['x']

        y = wormCoords2[HEAD]['y']



        x_apple = apple2['x']

        y_apple = apple2['y']





#calculation of distance

        



        d_x = abs(x-x_apple)

        d_y = abs(y-y_apple)

        

        d_up_y = abs((y-1)-y_apple)

        d_down_y = abs((y+1)-y_apple)

    

        d_right_x = abs((x+1)-x_apple)

        d_left_x = abs((x-1)-x_apple)

        

        randomx = random.randint(0, 100)

        

        randomy = random.randint(0, 100)





# comparing the distances and up and down control



        if x == x_apple and invisibleApple2 == 1:

            if d_up_y < d_down_y and direction2 != DOWN and randomx > 20:

                direction2 = UP

                

                

            elif d_down_y < d_up_y and direction2 != UP and randomx > 20:

                direction2 = DOWN

                

                

        else:

            if randomx > 98 and d_up_y < d_down_y and direction2 != DOWN:

                direction2 = UP

            if randomx > 98 and d_down_y < d_up_y and direction2 != UP:

                direction2 = DOWN

                

        # comparing the distances and right and left control

        

        if y == y_apple and invisibleApple2 == 1:

            if d_left_x < d_right_x and direction2 != RIGHT and randomx > 20:

                direction2 = LEFT

                

                

            elif d_right_x < d_left_x and direction2 != LEFT and randomx > 20:

                direction2 = RIGHT

                

                

        else:

            if randomx > 98 and d_left_x < d_right_x and direction2 != RIGHT:

                direction2 = LEFT

            if randomx > 98 and d_right_x < d_left_x and direction2 != LEFT:

                direction2 = RIGHT

            

        #semirobotsnake for dierection up and down

        x = wormCoords[HEAD]['x']

        y = wormCoords[HEAD]['y']



        x_apple = apple['x']

        y_apple = apple['y']



        #calculation of distance for up and down

        d_x = abs(x-x_apple)

        d_y = abs(y-y_apple)

        

        d_up_y = abs((y-1)-y_apple)

        d_down_y = abs((y+1)-y_apple)

    

        

        randomx = random.randint(0, 100)

        

# comparing the distances



        if x == x_apple and invisibleApple1 == 1:

            if d_up_y < d_down_y and direction != DOWN and randomx > 20:

                direction = UP

                

                

            elif d_down_y < d_up_y and direction != UP and randomx > 20:

                direction = DOWN

                

                

        else:

            if randomx > 98 and d_up_y < d_down_y and direction != DOWN:

                direction = UP

            if randomx > 98 and d_down_y < d_up_y and direction != UP:

                direction = DOWN

            

        for event in pygame.event.get(): # event handling loop

            if event.type == QUIT:

                terminate()

            elif event.type == KEYDOWN:

                if (event.key == K_LEFT or event.key == K_a) and direction != RIGHT:

                    direction = LEFT

                elif (event.key == K_RIGHT or event.key == K_s) and direction != LEFT:

                    direction = RIGHT

                
                elif event.key == K_b:
                    
                    if apple != {'x':-1,'y':-1}:
                    
                        now = time.time()
    
                        global startIA1
                        
                        RT1 = now - startIA1
                    
                        invisibleApple1List.append(RT1)
    
                        global invisibleApple1
    
                        invisibleApple1 = 1
                    else:
                        None
                
                    
                elif event.key == K_n:
                    
                    if apple2 != {'x':-1,'y':-1}:
                    
                        now = time.time()
    
                        global startIA2
                        RT2 = now - startIA2
    
                        invisibleApple2List.append(RT2)
    
                        global invisibleApple2
                        invisibleApple2 = 1
                    else:
                        None

                elif event.key == K_f:
                    
                    global end

                    end = time.time()

                    return end



        # check if the worm has hit itself or the edge

        if wormCoords[HEAD]['x'] == -1 or wormCoords[HEAD]['x'] == -2 or wormCoords[HEAD]['x'] == -3:

            wormCoords[HEAD]['x'] = CELLWIDTH

            

        elif wormCoords[HEAD]['x'] == CELLWIDTH or wormCoords[HEAD]['x'] == CELLWIDTH +1 or wormCoords[HEAD]['x'] == CELLWIDTH + 2:

            wormCoords[HEAD]['x'] = 0

        

        elif wormCoords[HEAD]['y'] == -1 or wormCoords[HEAD]['y'] == -2 or wormCoords[HEAD]['y'] == -3:

            wormCoords[HEAD]['y'] = CELLHEIGHT

            

        elif wormCoords[HEAD]['y'] == CELLHEIGHT or wormCoords[HEAD]['y'] == CELLHEIGHT +1 or wormCoords[HEAD]['y'] == CELLHEIGHT + 2:

            wormCoords[HEAD]['y'] = 0

          

          #second worm  

        if wormCoords2[HEAD]['x'] == -1 or wormCoords2[HEAD]['x'] == -2 or wormCoords2[HEAD]['x'] == -3:

            wormCoords2[HEAD]['x'] = CELLWIDTH

            

        elif wormCoords2[HEAD]['x'] == CELLWIDTH or wormCoords2[HEAD]['x'] == CELLWIDTH +1 or wormCoords2[HEAD]['x'] == CELLWIDTH +2:

            wormCoords2[HEAD]['x'] = 0

        

        elif wormCoords2[HEAD]['y'] == -1 or wormCoords2[HEAD]['y'] == -2 or wormCoords2[HEAD]['y'] == -3:

            wormCoords2[HEAD]['y'] = CELLHEIGHT

            

        elif wormCoords2[HEAD]['y'] == CELLHEIGHT or wormCoords2[HEAD]['y'] == CELLHEIGHT + 1 or wormCoords2[HEAD]['y'] == CELLHEIGHT +2:

            wormCoords2[HEAD]['y'] = 0

            



        # check if worm has eaten an apple

        if wormCoords[HEAD]['x'] == apple['x'] and wormCoords[HEAD]['y'] == apple['y'] and invisibleApple1 == 1:

            # don't remove worm's tail segment

            apple = {'x':-1,'y':-1} # set a new apple somewhere
            
            global invisibleApple1
            
            invisibleApple1 = 0

            global count1

            count1 = 0

            

        else:

            del wormCoords[-1] # remove worm's tail segment

            

            #second worm

        if wormCoords2[HEAD]['x'] == apple2['x'] and wormCoords2[HEAD]['y'] == apple2['y'] and invisibleApple2 == 1:

            # don't remove worm's tail segment

            apple2 = {'x':-1,'y':-1} # set a new apple somewhere
            
            global invisibleApple2
            
            invisibleApple2 = 0

            global count2

            count2 = 0

            

        else:

            del wormCoords2[-1] # remove worm's tail segment

        

        # define the delay variable for making the apple appear at an ever slower rate

        now = time.time()

        period = now - start

        if period <= 10:

            delay = 0

        elif period >= 10 and period <= 20:

            delay = 40

        elif period >= 20 and period <= 40:

            delay = 80

        elif period >= 40 and period <= 60:

            delay = 160

        elif period >= 60 and period <= 90:

            delay = 240

        elif period >= 90 and period <= 120:

            delay = 300

        elif period >= 120:

            delay = 400

        

        

        if  count1 >= delay and apple == {'x':-1,'y':-1}:

            global apple

            apple = getRandomLocation()
            
            global startIA1
            
            startIA1 = time.time()

            global count1

            count1 = 0

        

        if  count2 >= delay and apple2 == {'x':-1,'y':-1}:

            global apple2

            apple2 = getRandomLocation()
            
            global startIA2
            
            startIA2 = time.time()

            global count2

            count2 = 0



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

        

        # second worm

        if direction2 == UP:

            newHead2 = {'x': wormCoords2[HEAD]['x'], 'y': wormCoords2[HEAD]['y'] - 1}

        elif direction2 == DOWN:

            newHead2 = {'x': wormCoords2[HEAD]['x'], 'y': wormCoords2[HEAD]['y'] + 1}

        elif direction2 == LEFT:

            newHead2 = {'x': wormCoords2[HEAD]['x'] - 1, 'y': wormCoords2[HEAD]['y']}

        elif direction2 == RIGHT:

            newHead2 = {'x': wormCoords2[HEAD]['x'] + 1, 'y': wormCoords2[HEAD]['y']}

            

        wormCoords2.insert(0, newHead2)

        

        DISPLAYSURF.fill(BGCOLOR)

        drawGrid()

        drawWorm(wormCoords)

        drawWorm2(wormCoords2)
        
        if invisibleApple1 == 1:
        
            drawApple1_b(apple)
        else:
            
            drawApple1_a(apple)
            
        if invisibleApple2 == 1:
            
            drawApple2_b(apple2)
        else:
            drawApple2_a(apple2)
            
        global text1

        drawScore(text1)

        global score 

        score = len(wormCoords) - 3 + len(wormCoords2) -3

        pygame.display.update()

        FPSCLOCK.tick(FPS)

        global count1

        count1 += 1

        global count2

        count2 += 1

        

def runGame2_noncoordination():

    # Set a start point.

    startx = random.randint(5, CELLWIDTH - 6)

    starty = random.randint(5, CELLHEIGHT - 6)

    wormCoords = [{'x': startx,     'y': starty},

                  {'x': startx - 1, 'y': starty},

                  {'x': startx - 2, 'y': starty}]

    direction = RIGHT



    start2x = random.randint(5, CELLWIDTH - 6)

    start2y = random.randint(5, CELLHEIGHT - 6)

    wormCoords2 = [{'x': startx,     'y': starty},

                  {'x': startx - 1, 'y': starty},

                  {'x': startx - 2, 'y': starty}]

    direction2 = LEFT



    # Start the apple in a random place.

    apple = getRandomLocation()

    apple2 = getRandomLocation()

    # Start measuring the duration of the game

    global start

    start = time.time()
    
    global invisibleApple1

    invisibleApple1 = 0
    
    global invisibleApple2

    invisibleApple2 = 0

    # main game loop

    while True:

#robotsnake

        

        x = wormCoords2[HEAD]['x']

        y = wormCoords2[HEAD]['y']



        x_apple = apple2['x']

        y_apple = apple2['y']





#calculation of distance

        



        d_x = abs(x-x_apple)

        d_y = abs(y-y_apple)

        

        d_up_y = abs((y-1)-y_apple)

        d_down_y = abs((y+1)-y_apple)

    

        d_right_x = abs((x+1)-x_apple)

        d_left_x = abs((x-1)-x_apple)

        

        randomx = random.randint(0, 100)

        

        randomy = random.randint(0, 100)





# comparing the distances and up and down control



        if x == x_apple and invisibleApple2 == 1:

            if d_up_y < d_down_y and direction2 != DOWN and randomx > 20:

                direction2 = UP

                

                

            elif d_down_y < d_up_y and direction2 != UP and randomx > 20:

                direction2 = DOWN

                

                

        else:

            if randomx > 98 and d_up_y < d_down_y and direction2 != DOWN:

                direction2 = UP

            if randomx > 98 and d_down_y < d_up_y and direction2 != UP:

                direction2 = DOWN

                

        # comparing the distances and right and left control

        

        if y == y_apple and invisibleApple2 == 1:

            if d_left_x < d_right_x and direction2 != RIGHT and randomx > 20:

                direction2 = LEFT

                

                

            elif d_right_x < d_left_x and direction2 != LEFT and randomx > 20:

                direction2 = RIGHT

                

                

        else:

            if randomx > 98 and d_left_x < d_right_x and direction2 != RIGHT:

                direction2 = LEFT

            if randomx > 98 and d_right_x < d_left_x and direction2 != LEFT:

                direction2 = RIGHT

            

        for event in pygame.event.get(): # event handling loop

            if event.type == QUIT:

                terminate()

            elif event.type == KEYDOWN:

                if  event.key == K_LEFT and direction != RIGHT:

                    direction = LEFT

                if  event.key == K_a and direction2 != RIGHT:

                    direction2 = LEFT

                if  event.key == K_RIGHT and direction != LEFT:

                    direction = RIGHT

                if  event.key == K_d and direction2 != LEFT:

                    direction2 = RIGHT

                if  event.key == K_UP and direction != DOWN:

                    direction = UP

                if  event.key == K_w and direction2 != DOWN:

                    direction2 = UP

                if  event.key == K_DOWN and direction != UP:

                    direction = DOWN

                if  event.key == K_s and direction2 != UP:

                    direction2 = DOWN

                elif event.key == K_b:
                    
                    if apple != {'x':-1,'y':-1}:
                    
                        now = time.time()
    
                        global startIA1
                        
                        RT1 = now - startIA1
                    
                        invisibleApple1List.append(RT1)
    
                        global invisibleApple1
    
                        invisibleApple1 = 1
                    else:
                        None
                    
                elif event.key == K_n:
                    
                    if apple2 != {'x':-1,'y':-1}:
                    
                        now = time.time()
    
                        global startIA2
                        RT2 = now - startIA2
    
                        invisibleApple2List.append(RT2)
    
                        global invisibleApple2
                        invisibleApple2 = 1
                    else:
                        None
                    
                if event.key == K_f:

                    global end

                    end = time.time()

                    return end



        # check if the worm has hit itself or the edge

        if wormCoords[HEAD]['x'] == -1 :

            wormCoords[HEAD]['x'] = CELLWIDTH

            

        elif wormCoords[HEAD]['x'] == CELLWIDTH:

            wormCoords[HEAD]['x'] = 0

        

        elif wormCoords[HEAD]['y'] == -1:

            wormCoords[HEAD]['y'] = CELLHEIGHT

            

        elif wormCoords[HEAD]['y'] == CELLHEIGHT:

            wormCoords[HEAD]['y'] = 0

          

          #second worm  

        if wormCoords2[HEAD]['x'] == -1 :

            wormCoords2[HEAD]['x'] = CELLWIDTH

            

        elif wormCoords2[HEAD]['x'] == CELLWIDTH:

            wormCoords2[HEAD]['x'] = 0

        

        elif wormCoords2[HEAD]['y'] == -1:

            wormCoords2[HEAD]['y'] = CELLHEIGHT

            

        elif wormCoords2[HEAD]['y'] == CELLHEIGHT:

            wormCoords2[HEAD]['y'] = 0

            



        # check if worm has eaten an apple

        if wormCoords[HEAD]['x'] == apple['x'] and wormCoords[HEAD]['y'] == apple['y'] and invisibleApple1 == 1:

            # don't remove worm's tail segment

            apple = {'x':-1,'y':-1} # set a new apple somewhere
            
            global invisibleApple1
            
            invisibleApple1 = 0

            global count1

            count1 = 0

            

        else:

            del wormCoords[-1] # remove worm's tail segment

            

            #second worm

        if wormCoords2[HEAD]['x'] == apple2['x'] and wormCoords2[HEAD]['y'] == apple2['y'] and invisibleApple2 == 1:

            # don't remove worm's tail segment

            apple2 = {'x':-1,'y':-1} # set a new apple somewhere
            
            global invisibleApple2
            
            invisibleApple2 = 0
            

            global count2

            count2 = 0

            

        else:

            del wormCoords2[-1] # remove worm's tail segment

        

        # define the delay variable for making the apple appear at an ever slower rate

        now = time.time()

        period = now - start

        if period <= 10:

            delay = 0

        elif period >= 10 and period <= 20:

            delay = 40

        elif period >= 20 and period <= 40:

            delay = 80

        elif period >= 40 and period <= 60:

            delay = 160

        elif period >= 60 and period <= 90:

            delay = 240

        elif period >= 90 and period <= 120:

            delay = 300

        elif period >= 120:

            delay = 400

        

        

        if  count1 >= delay and apple == {'x':-1,'y':-1}:

            global apple

            apple = getRandomLocation()
            
            global startIA1
            
            startIA1 = time.time()

            global count1

            count1 = 0

        

        if  count2 >= delay and apple2 == {'x':-1,'y':-1}:

            global apple2

            apple2 = getRandomLocation()
            
            global startIA2
            
            startIA2 = time.time()

            global count2

            count2 = 0



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

        

        # second worm

        if direction2 == UP:

            newHead2 = {'x': wormCoords2[HEAD]['x'], 'y': wormCoords2[HEAD]['y'] - 1}

        elif direction2 == DOWN:

            newHead2 = {'x': wormCoords2[HEAD]['x'], 'y': wormCoords2[HEAD]['y'] + 1}

        elif direction2 == LEFT:

            newHead2 = {'x': wormCoords2[HEAD]['x'] - 1, 'y': wormCoords2[HEAD]['y']}

        elif direction2 == RIGHT:

            newHead2 = {'x': wormCoords2[HEAD]['x'] + 1, 'y': wormCoords2[HEAD]['y']}

            

        wormCoords2.insert(0, newHead2)

        

        DISPLAYSURF.fill(BGCOLOR)

        drawGrid()

        drawWorm(wormCoords)

       
        drawWorm2(wormCoords2)

        if invisibleApple1 == 1:
        
            drawApple1_b(apple)
        else:
            
            drawApple1_a(apple)
            
        if invisibleApple2 == 1:
            
            drawApple2_b(apple2)
        else:
            drawApple2_a(apple2)
        global text1

        drawScore(text1)

        global score 

        score = len(wormCoords) - 3 + len(wormCoords2) -3

        pygame.display.update()

        FPSCLOCK.tick(FPS)

        global count1

        count1 += 1

        global count2

        count2 += 1

        

        



def drawPressKeyMsg():

    pressKeySurf = BASICFONT.render('Wait until the experiment continues!', True, DARKGRAY)

    pressKeyRect = pressKeySurf.get_rect()

    pressKeyRect.topleft = (WINDOWWIDTH - 350, WINDOWHEIGHT - 30)

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



def waitingscreen(text):



    fontObj = pygame.font.Font('freesansbold.ttf',18)

    waitingScreen1 = fontObj.render(text, True, WHITE)

    waitingScreenRect1 = waitingScreen1.get_rect()

    waitingScreenRect1.center = (420, 330)    

    

    fontObj = pygame.font.Font('freesansbold.ttf',18)

    waitingScreen2 = fontObj.render('Please press any key to begin.', True, WHITE)

    waitingScreenRect2 = waitingScreen2.get_rect()

    waitingScreenRect2.center = (420, 390) 

    

    

    

    while True:

        DISPLAYSURF.fill(BLACK)

        DISPLAYSURF.blit(waitingScreen1,waitingScreenRect1)

        DISPLAYSURF.blit(waitingScreen2,waitingScreenRect2)

        pygame.display.update()

        



        

        if checkForKeyPress():

            pygame.event.get() # clear event queue

            return





        

        

        

def thanks():

    text = 'Thanks for your participation. Please wait for the experimenter!'

    fontObj = pygame.font.Font('freesansbold.ttf',18)

    waitingScreen1 = fontObj.render(text, True, WHITE)

    waitingScreenRect1 = waitingScreen1.get_rect()

    waitingScreenRect1.center = (420, 330)    

    

   



    while True:

        DISPLAYSURF.fill(BLACK)

        DISPLAYSURF.blit(waitingScreen1,waitingScreenRect1)



        if checkForKeyPress():

            pygame.event.get() # clear event queue

            return

        

        pygame.display.update()

        FPSCLOCK.tick(FPS)



def investmentscreen(text):

   

    fontObj = pygame.font.Font('freesansbold.ttf',18)

    investmentSurf1 = fontObj.render('The following round has an entrance fee of %s Forint. Wait until your partner decides' % (text), True, WHITE)

    investmentRect1 = investmentSurf1.get_rect()

    investmentRect1.center = (420, 330)    

    



    investmentSurf2 = fontObj.render('whether s/he is willing to pay the entry fee!', True, WHITE)

    investmentRect2 = investmentSurf2.get_rect()

    investmentRect2.center = (420, 360)    

    



    while True:

        DISPLAYSURF.fill(BLACK)

        DISPLAYSURF.blit(investmentSurf1,investmentRect1)

        DISPLAYSURF.blit(investmentSurf2,investmentRect2)



       



        if checkForKeyPress():

            pygame.event.get() # clear event queue

            return

        

        pygame.display.update()

        

def accepctancescreen(text1, text2, text3):

    

    fontObj = pygame.font.Font('freesansbold.ttf',18)

    investmentSurf1 = fontObj.render('Your partner successfully unlocked the next round. The Captcha key was', True, WHITE)

    investmentRect1 = investmentSurf1.get_rect()

    investmentRect1.center = (420, 270)    

    

    fontObj2 = pygame.font.Font('freesansbold.ttf',30)

    investmentSurf2 = fontObj2.render('%s' %(text1), True, WHITE)

    investmentRect2 = investmentSurf2.get_rect()

    investmentRect2.center = (420, 320) 

    

    fontObj2 = pygame.font.Font('freesansbold.ttf',18)

    investmentSurf3 = fontObj2.render('%s' %(text2), True, WHITE)

    investmentRect3 = investmentSurf3.get_rect()

    investmentRect3.center = (420, 390)

    

    fontObj2 = pygame.font.Font('freesansbold.ttf',18)

    investmentSurf4 = fontObj2.render('%s' %(text3), True, WHITE)

    investmentRect4 = investmentSurf4.get_rect()

    investmentRect4.center = (420, 420)

    

    

    investmentSurf5 = fontObj.render('Press any key when you are ready to start!', True, WHITE)

    investmentRect5 = investmentSurf5.get_rect()

    investmentRect5.center = (420, 460)    

    

    

    

    

    while True:

        pygame.event.clear()

        DISPLAYSURF.fill(BLACK)

        DISPLAYSURF.blit(investmentSurf1,investmentRect1)

        DISPLAYSURF.blit(investmentSurf2,investmentRect2)

        DISPLAYSURF.blit(investmentSurf3,investmentRect3)

        DISPLAYSURF.blit(investmentSurf4,investmentRect4)

        DISPLAYSURF.blit(investmentSurf5,investmentRect5)

        pygame.display.update()

        FPSCLOCK.tick(FPS)

       

        

        if checkForKeyPress():

            pygame.event.get() # clear event queue

            return

        

        



def terminate():

    pygame.quit()

    sys.exit()



def getRandomLocation():

    return {'x': random.randint(3, CELLWIDTH -3 ), 'y': random.randint(3, CELLHEIGHT - 3)}





def spoilScreen(score):

    number = score

    fontObj = pygame.font.Font('freesansbold.ttf',18)

    spoilSurf1 = fontObj.render('This round has been concluded. You collected %d apples together.' % (number), True, WHITE)

    spoilRect1 = spoilSurf1.get_rect()

    spoilRect1.center = (420, 330)    

    

    

    spoilSurf3 = fontObj.render('Press any key when you are ready for the next round.', True, WHITE)

    spoilRect3 = spoilSurf3.get_rect()

    spoilRect3.center = (420, 360) 

    

    DISPLAYSURF.blit(spoilSurf1, spoilRect1)

    DISPLAYSURF.blit(spoilSurf3, spoilRect3)

    

    pygame.display.update()

    pygame.time.wait(500)

    

    checkForKeyPress() # clear out any key presses in the event queue



    while True:

        if checkForKeyPress():

            pygame.event.get() # clear event queue

            return



def drawScore(text1):

    scoreSurf = BASICFONT.render('Captcha key: %s   -   You are Player A   -   Press the f key when you want to conclude the game.' % (text1), True, WHITE)

    scoreRect = scoreSurf.get_rect()

    scoreRect.topleft = (WINDOWWIDTH - 810, 10)

    DISPLAYSURF.blit(scoreSurf, scoreRect)





def drawWorm(wormCoords):

    for coord in wormCoords:

        x = coord['x'] * CELLSIZE

        y = coord['y'] * CELLSIZE

        wormSegmentRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)

        pygame.draw.rect(DISPLAYSURF, DARKGREEN, wormSegmentRect)

        wormInnerSegmentRect = pygame.Rect(x + 4, y + 4, CELLSIZE - 8, CELLSIZE - 8)

        pygame.draw.rect(DISPLAYSURF, GREEN, wormInnerSegmentRect)

        

def drawPurpleHead(wormCoords):

    x = wormCoords[HEAD]['x'] * CELLSIZE

    y = wormCoords[HEAD]['y'] * CELLSIZE

    BlackHeadRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)

    pygame.draw.rect(DISPLAYSURF, PURPLE, BlackHeadRect)

        

def drawWorm2(wormCoords2):

    for coord in wormCoords2:

        x = coord['x'] * CELLSIZE

        y = coord['y'] * CELLSIZE

        wormSegmentRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)

        pygame.draw.rect(DISPLAYSURF, DARKBLUE, wormSegmentRect)

        wormInnerSegmentRect = pygame.Rect(x + 4, y + 4, CELLSIZE - 8, CELLSIZE - 8)

        pygame.draw.rect(DISPLAYSURF, BLUE, wormInnerSegmentRect)





def drawApple1_a(coord):

    x = coord['x'] * CELLSIZE

    y = coord['y'] * CELLSIZE

    appleRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)

    pygame.draw.rect(DISPLAYSURF, YELLOW, appleRect)

def drawApple1_b(coord):

    x = coord['x'] * CELLSIZE

    y = coord['y'] * CELLSIZE

    appleRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)

    pygame.draw.rect(DISPLAYSURF, RED, appleRect)
    

def drawApple2_a(coord):

    x = coord['x'] * CELLSIZE

    y = coord['y'] * CELLSIZE

    appleRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)

    pygame.draw.rect(DISPLAYSURF, GREENISHBLUE, appleRect)
    
def drawApple2_b(coord):

    x = coord['x'] * CELLSIZE

    y = coord['y'] * CELLSIZE

    appleRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)

    pygame.draw.rect(DISPLAYSURF, PURPLE, appleRect)

       





def drawGrid():

    for x in range(0, WINDOWWIDTH, CELLSIZE): # draw vertical lines

        pygame.draw.line(DISPLAYSURF, DARKGRAY, (x, 0), (x, WINDOWHEIGHT))

    for y in range(0, WINDOWHEIGHT, CELLSIZE): # draw horizontal lines

        pygame.draw.line(DISPLAYSURF, DARKGRAY, (0, y), (WINDOWWIDTH, y))

        



def screen_0():

    while True:

       

        if checkForKeyPress():

            pygame.event.get() # clear event queue

            return

    

def screen_1():



    fontObj = pygame.font.Font('freesansbold.ttf',18)

    spoilSurf1 = fontObj.render('Welcome to the experiment.', True, WHITE)

    spoilRect1 = spoilSurf1.get_rect()

    spoilRect1.center = (420, 300)    

    



    spoilSurf2 = fontObj.render('Please press any key to begin.', True, WHITE)

    spoilRect2 = spoilSurf2.get_rect()

    spoilRect2.center = (420, 360)    

    



    

    while True:

        DISPLAYSURF.fill(BLACK)

        DISPLAYSURF.blit(spoilSurf1, spoilRect1)

        DISPLAYSURF.blit(spoilSurf2, spoilRect2)

        pygame.display.update()

        

        

        if checkForKeyPress():

            pygame.event.get() # clear event queue

            return

        

def screen_2():

    fontObj = pygame.font.Font('freesansbold.ttf',18)

    screen_2Surf1 = fontObj.render('You will be playing the classic snake game using the arrow keys on the keyboard.', True, WHITE)

    screen_2Rect1 = screen_2Surf1.get_rect()

    screen_2Rect1.center = (420, 270)    

    



    screen_2Surf2 = fontObj.render('Sometimes the two players will jointly control one snake,', True, WHITE)

    screen_2Rect2 = screen_2Surf2.get_rect()

    screen_2Rect2.center = (420, 300)    

    

    screen_2Surf3 = fontObj.render('with Player A controlling the left-right axis while Player B controls the up-down axis.', True, WHITE)

    screen_2Rect3 = screen_2Surf3.get_rect()

    screen_2Rect3.center = (420, 330)

    

    screen_2Surf4 = fontObj.render(' Sometimes each player will have her/his own individual snake to operate,', True, WHITE)

    screen_2Rect4 = screen_2Surf4.get_rect()

    screen_2Rect4.center = (420, 360) 

    

    screen_2Surf5 = fontObj.render('and will have control of the left-right and the up-down directions.', True, WHITE)

    screen_2Rect5 = screen_2Surf5.get_rect()

    screen_2Rect5.center = (420, 390)  

    

    screen_2Surf6 = fontObj.render('Please press any key to continue with the instructions.', True, WHITE)

    screen_2Rect6 = screen_2Surf6.get_rect()

    screen_2Rect6.center = (420, 450)   

    

    



    while True:

        DISPLAYSURF.fill(BLACK)

        DISPLAYSURF.blit(screen_2Surf1, screen_2Rect1)

        DISPLAYSURF.blit(screen_2Surf2, screen_2Rect2)

        DISPLAYSURF.blit(screen_2Surf3, screen_2Rect3)

        DISPLAYSURF.blit(screen_2Surf4, screen_2Rect4)

        DISPLAYSURF.blit(screen_2Surf5, screen_2Rect5)

        DISPLAYSURF.blit(screen_2Surf6, screen_2Rect6)

        pygame.display.update()

        

        

        if checkForKeyPress():

            pygame.event.get() # clear event queue

            return

        

def screen_3():

    fontObj = pygame.font.Font('freesansbold.ttf',18)

    screen_3Surf1 = fontObj.render('The goal is to collect as many apples as possible. ', True, WHITE)

    screen_3Rect1 = screen_3Surf1.get_rect()

    screen_3Rect1.center = (420, 270)

    

    screen_3Surf2 = fontObj.render('In all cases, all of the apples collected by both snakes are added to your shared total.', True, WHITE)

    screen_3Rect2 = screen_3Surf2.get_rect()

    screen_3Rect2.center = (420, 300)

    

    screen_3Surf4 = fontObj.render('Within each round, the rate at which the apples appear will gradually decrease.', True, WHITE)

    screen_3Rect4 = screen_3Surf4.get_rect()

    screen_3Rect4.center = (420, 330) 



    screen_3Surf5 = fontObj.render('Player A must decide when to conclude each round and proceed to the next round.', True, WHITE)

    screen_3Rect5 = screen_3Surf5.get_rect()

    screen_3Rect5.center = (420, 360) 

    

    screen_3Surf6 = fontObj.render('To conclude a round, Player A can press the f key (finish) on the keyboard.', True, WHITE)

    screen_3Rect6 = screen_3Surf6.get_rect()

    screen_3Rect6.center = (420, 390) 

    

    screen_3Surf7 = fontObj.render('In total there are 20 rounds.', True, WHITE)

    screen_3Rect7 = screen_3Surf7.get_rect()

    screen_3Rect7.center = (420, 420) 

    

    screen_3Surf8 = fontObj.render('Please press any key to continue with the instructions.', True, WHITE)

    screen_3Rect8 = screen_3Surf8.get_rect()

    screen_3Rect8.center = (420, 470) 

    

    while True:

        DISPLAYSURF.fill(BLACK)

        DISPLAYSURF.blit(screen_3Surf1, screen_3Rect1)

        DISPLAYSURF.blit(screen_3Surf2, screen_3Rect2)

        DISPLAYSURF.blit(screen_3Surf4, screen_3Rect4)

        DISPLAYSURF.blit(screen_3Surf5, screen_3Rect5)

        DISPLAYSURF.blit(screen_3Surf6, screen_3Rect6)

        DISPLAYSURF.blit(screen_3Surf7, screen_3Rect7)

        DISPLAYSURF.blit(screen_3Surf8, screen_3Rect8)

        pygame.display.update()

    

        

        if checkForKeyPress():

            pygame.event.get() # clear event queue

            return

            

def screen_4():



    fontObj = pygame.font.Font('freesansbold.ttf',18)

    screen_4Surf1 = fontObj.render('You will play the role of Player A and you always have', True, WHITE)

    screen_4Rect1 = screen_4Surf1.get_rect()

    screen_4Rect1.center = (420, 270)    

    



    screen_4Surf2 = fontObj.render('to go for the red apples with the green snake.', True, WHITE)

    screen_4Rect2 = screen_4Surf2.get_rect()

    screen_4Rect2.center = (420, 300) 

    

    screen_4Surf3 = fontObj.render('Also, you are the only one who can decide when to conclude each round ', True, WHITE)

    screen_4Rect3 = screen_4Surf3.get_rect()

    screen_4Rect3.center = (420, 330)  

    

    screen_4Surf4 = fontObj.render('by pressing the f key on the keyboard.', True, WHITE)

    screen_4Rect4 = screen_4Surf4.get_rect()

    screen_4Rect4.center = (420, 360)  

    

    

    screen_4Surf6 = fontObj.render('Please press any key to continue with the instructions.', True, WHITE)

    screen_4Rect6 = screen_4Surf6.get_rect()

    screen_4Rect6.center = (420, 400)  

      

      

    

    while True:

        DISPLAYSURF.fill(BLACK)

        DISPLAYSURF.blit(screen_4Surf1, screen_4Rect1)

        DISPLAYSURF.blit(screen_4Surf2, screen_4Rect2)

        DISPLAYSURF.blit(screen_4Surf3, screen_4Rect3)

        DISPLAYSURF.blit(screen_4Surf4, screen_4Rect4)

        

        DISPLAYSURF.blit(screen_4Surf6, screen_4Rect6)

        pygame.display.update()

    

        

        if checkForKeyPress():

            pygame.event.get() # clear event queue

            return

def screen_5():

    fontObj = pygame.font.Font('freesansbold.ttf',18)

    screen_3Surf1 = fontObj.render('Sometimes the snake is so eager to eat apples', True, WHITE)

    screen_3Rect1 = screen_3Surf1.get_rect()

    screen_3Rect1.center = (420, 270)

    

    screen_3Surf2 = fontObj.render('that it forgets to breathe and its head turns purple.', True, WHITE)

    screen_3Rect2 = screen_3Surf2.get_rect()

    screen_3Rect2.center = (420, 300)

    

    screen_3Surf4 = fontObj.render(' When this happens, please press the SPACE key as quickly as possible', True, WHITE)

    screen_3Rect4 = screen_3Surf4.get_rect()

    screen_3Rect4.center = (420, 330) 



    screen_3Surf5 = fontObj.render('to make the snake take a deep breath.', True, WHITE)

    screen_3Rect5 = screen_3Surf5.get_rect()

    screen_3Rect5.center = (420, 360) 

    

    screen_3Surf6 = fontObj.render(' For each second that the head of the snake is purple,  ', True, WHITE)

    screen_3Rect6 = screen_3Surf6.get_rect()

    screen_3Rect6.center = (420, 390) 

    

    screen_3Surf7 = fontObj.render('1/4 of an apple will be subtracted from your joint account.', True, WHITE)

    screen_3Rect7 = screen_3Surf7.get_rect()

    screen_3Rect7.center = (420, 420) 

    

    screen_3Surf8 = fontObj.render('Please press any key to continue with the instructions.', True, WHITE)

    screen_3Rect8 = screen_3Surf8.get_rect()

    screen_3Rect8.center = (420, 490) 

    

    while True:

        DISPLAYSURF.fill(BLACK)

        DISPLAYSURF.blit(screen_3Surf1, screen_3Rect1)

        DISPLAYSURF.blit(screen_3Surf2, screen_3Rect2)

        DISPLAYSURF.blit(screen_3Surf4, screen_3Rect4)

        DISPLAYSURF.blit(screen_3Surf5, screen_3Rect5)

        DISPLAYSURF.blit(screen_3Surf6, screen_3Rect6)

        DISPLAYSURF.blit(screen_3Surf7, screen_3Rect7)

        DISPLAYSURF.blit(screen_3Surf8, screen_3Rect8)

        pygame.display.update()

    

        

        if checkForKeyPress():

            pygame.event.get() # clear event queue

            return

            

def captchaInstructionScreen():

    

    fontObj = pygame.font.Font('freesansbold.ttf',18)

    screen_4Surf1 = fontObj.render('Your partner is Player B. S/he will play the role of the captcha reader.', True, WHITE)

    screen_4Rect1 = screen_4Surf1.get_rect()

    screen_4Rect1.center = (420, 250)    

    



    screen_4Surf2 = fontObj.render(' The captcha reader must decipher a captcha key to unlock each round and begin the game.', True, WHITE)

    screen_4Rect2 = screen_4Surf2.get_rect()

    screen_4Rect2.center = (420, 280) 

    

    screen_4Surf3 = fontObj.render('Some of the captcha keys are easy and some are difficult: ', True, WHITE)

    screen_4Rect3 = screen_4Surf3.get_rect()

    screen_4Rect3.center = (420, 310)  

    

    screen_4Surf4 = fontObj.render('For example:', True, WHITE)

    screen_4Rect4 = screen_4Surf4.get_rect()

    screen_4Rect4.center = (420, 340)  

    

    screen_4Surf5 = pygame.image.load('smallc.png')

    screen_4Rect5 = screen_4Surf5.get_rect()

    screen_4Rect5.center = (250, 400) 

    

    screen_4Surf6 = pygame.image.load('bigc.png')

    screen_4Rect6 = screen_4Surf6.get_rect()

    screen_4Rect6.center = (600, 400)  

      

    

    screen_4Surf7 = fontObj.render('Let us begin with one practice round. Please press any key to begin.', True, WHITE)

    screen_4Rect7 = screen_4Surf7.get_rect()

    screen_4Rect7.center = (420, 500)  

      

      

    

    while True:

        DISPLAYSURF.fill(BLACK)

        DISPLAYSURF.blit(screen_4Surf1, screen_4Rect1)

        DISPLAYSURF.blit(screen_4Surf2, screen_4Rect2)

        DISPLAYSURF.blit(screen_4Surf3, screen_4Rect3)

        DISPLAYSURF.blit(screen_4Surf4, screen_4Rect4)

        DISPLAYSURF.blit(screen_4Surf5, screen_4Rect5)

        DISPLAYSURF.blit(screen_4Surf6, screen_4Rect6)

        DISPLAYSURF.blit(screen_4Surf7, screen_4Rect7)

        pygame.display.update()

    

        

        if checkForKeyPress():

            pygame.event.get() # clear event queue

            return

            

            

def captchascreen(captchaNumber, captchaDelete):

                    

    

    captchaList = []



    fontObj = pygame.font.Font('freesansbold.ttf',18)

    investmentSurf1 = fontObj.render('Wait until your partner unlocks the next round by solving a captcha!', True, WHITE)

    investmentRect1 = investmentSurf1.get_rect()

    investmentRect1.center = (420, 270)    



    fontObj2 = pygame.font.Font('freesansbold.ttf',40)

    investmentSurf2 = fontObj2.render(''.join(captchaList), True, WHITE)

    investmentRect2 = investmentSurf2.get_rect()

    investmentRect2.center = (420, 330) 

    

    DISPLAYSURF.fill(BLACK)

    DISPLAYSURF.blit(investmentSurf1,investmentRect1)

    DISPLAYSURF.blit(investmentSurf2,investmentRect2)

    pygame.display.update()

    FPSCLOCK.tick(FPS)



    if captchaNumber == 3 or captchaNumber >= 12:

        

        pygame.time.delay(2000)          

        captchaList.append('*')

    

        fontObj = pygame.font.Font('freesansbold.ttf',18)

        investmentSurf1 = fontObj.render('Wait until your partner unlocks the next round by solving a captcha!', True, WHITE)

        investmentRect1 = investmentSurf1.get_rect()

        investmentRect1.center = (420, 270)    

    

        fontObj2 = pygame.font.Font('freesansbold.ttf',40)

        investmentSurf2 = fontObj2.render(''.join(captchaList), True, WHITE)

        investmentRect2 = investmentSurf2.get_rect()

        investmentRect2.center = (420, 330) 

        

        DISPLAYSURF.fill(BLACK)

        DISPLAYSURF.blit(investmentSurf1,investmentRect1)

        DISPLAYSURF.blit(investmentSurf2,investmentRect2)

        pygame.display.update()

        FPSCLOCK.tick(FPS)

    

    if captchaNumber == 3 or captchaNumber >= 12:

        

        pygame.time.delay(1000)            

        captchaList.append('*')

    

        fontObj = pygame.font.Font('freesansbold.ttf',18)

        investmentSurf1 = fontObj.render('Wait until your partner unlocks the next round by solving a captcha!', True, WHITE)

        investmentRect1 = investmentSurf1.get_rect()

        investmentRect1.center = (420, 270)    

    

        fontObj2 = pygame.font.Font('freesansbold.ttf',40)

        investmentSurf2 = fontObj2.render(''.join(captchaList), True, WHITE)

        investmentRect2 = investmentSurf2.get_rect()

        investmentRect2.center = (420, 330) 

        

        DISPLAYSURF.fill(BLACK)

        DISPLAYSURF.blit(investmentSurf1,investmentRect1)

        DISPLAYSURF.blit(investmentSurf2,investmentRect2)

        pygame.display.update()

        FPSCLOCK.tick(FPS)

        

    if captchaDelete == 2:

        pygame.time.delay(1000)

        captchaList.pop()

        

        fontObj = pygame.font.Font('freesansbold.ttf',18)

        investmentSurf1 = fontObj.render('Wait until your partner unlocks the next round by solving a captcha!', True, WHITE)

        investmentRect1 = investmentSurf1.get_rect()

        investmentRect1.center = (420, 270)    

    

        fontObj2 = pygame.font.Font('freesansbold.ttf',40)

        investmentSurf2 = fontObj2.render(''.join(captchaList), True, WHITE)

        investmentRect2 = investmentSurf2.get_rect()

        investmentRect2.center = (420, 330) 

        

        DISPLAYSURF.fill(BLACK)

        DISPLAYSURF.blit(investmentSurf1,investmentRect1)

        DISPLAYSURF.blit(investmentSurf2,investmentRect2)

        pygame.display.update()

        FPSCLOCK.tick(FPS)

        

    if captchaDelete == 2:

        pygame.time.delay(3000)            

        captchaList.append('*')

        

        fontObj = pygame.font.Font('freesansbold.ttf',18)

        investmentSurf1 = fontObj.render('Wait until your partner unlocks the next round by solving a captcha!', True, WHITE)

        investmentRect1 = investmentSurf1.get_rect()

        investmentRect1.center = (420, 270)    

    

        fontObj2 = pygame.font.Font('freesansbold.ttf',40)

        investmentSurf2 = fontObj2.render(''.join(captchaList), True, WHITE)

        investmentRect2 = investmentSurf2.get_rect()

        investmentRect2.center = (420, 330) 

        

        DISPLAYSURF.fill(BLACK)

        DISPLAYSURF.blit(investmentSurf1,investmentRect1)

        DISPLAYSURF.blit(investmentSurf2,investmentRect2)

        pygame.display.update()

        FPSCLOCK.tick(FPS)

    

    if captchaNumber == 3 or captchaNumber >= 12:

        

        pygame.time.delay(1000)            

        captchaList.append('*')

    

        fontObj = pygame.font.Font('freesansbold.ttf',18)

        investmentSurf1 = fontObj.render('Wait until your partner unlocks the next round by solving a captcha!', True, WHITE)

        investmentRect1 = investmentSurf1.get_rect()

        investmentRect1.center = (420, 270)    

    

        fontObj2 = pygame.font.Font('freesansbold.ttf',40)

        investmentSurf2 = fontObj2.render(''.join(captchaList), True, WHITE)

        investmentRect2 = investmentSurf2.get_rect()

        investmentRect2.center = (420, 330) 

        

        DISPLAYSURF.fill(BLACK)

        DISPLAYSURF.blit(investmentSurf1,investmentRect1)

        DISPLAYSURF.blit(investmentSurf2,investmentRect2)

        pygame.display.update()

        FPSCLOCK.tick(FPS)

    

   

    if captchaNumber == 3:

            return

    

    if  captchaNumber >= 12:

        

        pygame.time.delay(3000)            

        captchaList.append('*')

    

        fontObj = pygame.font.Font('freesansbold.ttf',18)

        investmentSurf1 = fontObj.render('Wait until your partner unlocks the next round by solving a captcha!', True, WHITE)

        investmentRect1 = investmentSurf1.get_rect()

        investmentRect1.center = (420, 270)    

    

        fontObj2 = pygame.font.Font('freesansbold.ttf',40)

        investmentSurf2 = fontObj2.render(''.join(captchaList), True, WHITE)

        investmentRect2 = investmentSurf2.get_rect()

        investmentRect2.center = (420, 330) 

        

        DISPLAYSURF.fill(BLACK)

        DISPLAYSURF.blit(investmentSurf1,investmentRect1)

        DISPLAYSURF.blit(investmentSurf2,investmentRect2)

        pygame.display.update()

        FPSCLOCK.tick(FPS)

    

    if captchaNumber >= 12:

        

        pygame.time.delay(1000)            

        captchaList.append('*')

    

        fontObj = pygame.font.Font('freesansbold.ttf',18)

        investmentSurf1 = fontObj.render('Wait until your partner unlocks the next round by solving a captcha!', True, WHITE)

        investmentRect1 = investmentSurf1.get_rect()

        investmentRect1.center = (420, 270)    

    

        fontObj2 = pygame.font.Font('freesansbold.ttf',40)

        investmentSurf2 = fontObj2.render(''.join(captchaList), True, WHITE)

        investmentRect2 = investmentSurf2.get_rect()

        investmentRect2.center = (420, 330) 

        

        DISPLAYSURF.fill(BLACK)

        DISPLAYSURF.blit(investmentSurf1,investmentRect1)

        DISPLAYSURF.blit(investmentSurf2,investmentRect2)

        pygame.display.update()

        FPSCLOCK.tick(FPS)

    

    if captchaNumber >= 12:

        

        pygame.time.delay(500)            

        captchaList.append('*')

    

        fontObj = pygame.font.Font('freesansbold.ttf',18)

        investmentSurf1 = fontObj.render('Wait until your partner unlocks the next round by solving a captcha!', True, WHITE)

        investmentRect1 = investmentSurf1.get_rect()

        investmentRect1.center = (420, 270)    

    

        fontObj2 = pygame.font.Font('freesansbold.ttf',40)

        investmentSurf2 = fontObj2.render(''.join(captchaList), True, WHITE)

        investmentRect2 = investmentSurf2.get_rect()

        investmentRect2.center = (420, 330) 

        

        DISPLAYSURF.fill(BLACK)

        DISPLAYSURF.blit(investmentSurf1,investmentRect1)

        DISPLAYSURF.blit(investmentSurf2,investmentRect2)

        pygame.display.update()

        FPSCLOCK.tick(FPS)

    

    if captchaNumber >= 12:

        

        pygame.time.delay(1000)            

        captchaList.append('*')

    

        fontObj = pygame.font.Font('freesansbold.ttf',18)

        investmentSurf1 = fontObj.render('Wait until your partner unlocks the next round by solving a captcha!', True, WHITE)

        investmentRect1 = investmentSurf1.get_rect()

        investmentRect1.center = (420, 270)    

    

        fontObj2 = pygame.font.Font('freesansbold.ttf',40)

        investmentSurf2 = fontObj2.render(''.join(captchaList), True, WHITE)

        investmentRect2 = investmentSurf2.get_rect()

        investmentRect2.center = (420, 330) 

        

        DISPLAYSURF.fill(BLACK)

        DISPLAYSURF.blit(investmentSurf1,investmentRect1)

        DISPLAYSURF.blit(investmentSurf2,investmentRect2)

        pygame.display.update()

        FPSCLOCK.tick(FPS)

    

    if captchaDelete == 3:

        pygame.time.delay(1000)

        captchaList.pop()

        

        fontObj = pygame.font.Font('freesansbold.ttf',18)

        investmentSurf1 = fontObj.render('Wait until your partner unlocks the next round by solving a captcha!', True, WHITE)

        investmentRect1 = investmentSurf1.get_rect()

        investmentRect1.center = (420, 270)    

    

        fontObj2 = pygame.font.Font('freesansbold.ttf',40)

        investmentSurf2 = fontObj2.render(''.join(captchaList), True, WHITE)

        investmentRect2 = investmentSurf2.get_rect()

        investmentRect2.center = (420, 330) 

        

        DISPLAYSURF.fill(BLACK)

        DISPLAYSURF.blit(investmentSurf1,investmentRect1)

        DISPLAYSURF.blit(investmentSurf2,investmentRect2)

        pygame.display.update()

        FPSCLOCK.tick(FPS)

        

        

        pygame.time.delay(500)

        captchaList.pop()

        

        fontObj = pygame.font.Font('freesansbold.ttf',18)

        investmentSurf1 = fontObj.render('Wait until your partner unlocks the next round by solving a captcha!', True, WHITE)

        investmentRect1 = investmentSurf1.get_rect()

        investmentRect1.center = (420, 270)    

    

        fontObj2 = pygame.font.Font('freesansbold.ttf',40)

        investmentSurf2 = fontObj2.render(''.join(captchaList), True, WHITE)

        investmentRect2 = investmentSurf2.get_rect()

        investmentRect2.center = (420, 330) 

        

        DISPLAYSURF.fill(BLACK)

        DISPLAYSURF.blit(investmentSurf1,investmentRect1)

        DISPLAYSURF.blit(investmentSurf2,investmentRect2)

        pygame.display.update()

        FPSCLOCK.tick(FPS)

        

    if captchaDelete == 3:

        pygame.time.delay(3000)            

        captchaList.append('*')

        

        fontObj = pygame.font.Font('freesansbold.ttf',18)

        investmentSurf1 = fontObj.render('Wait until your partner unlocks the next round by solving a captcha!', True, WHITE)

        investmentRect1 = investmentSurf1.get_rect()

        investmentRect1.center = (420, 270)    

    

        fontObj2 = pygame.font.Font('freesansbold.ttf',40)

        investmentSurf2 = fontObj2.render(''.join(captchaList), True, WHITE)

        investmentRect2 = investmentSurf2.get_rect()

        investmentRect2.center = (420, 330) 

        

        DISPLAYSURF.fill(BLACK)

        DISPLAYSURF.blit(investmentSurf1,investmentRect1)

        DISPLAYSURF.blit(investmentSurf2,investmentRect2)

        pygame.display.update()

        FPSCLOCK.tick(FPS)

        

        pygame.time.delay(500)

        captchaList.append('*')

        

        fontObj = pygame.font.Font('freesansbold.ttf',18)

        investmentSurf1 = fontObj.render('Wait until your partner unlocks the next round by solving a captcha!', True, WHITE)

        investmentRect1 = investmentSurf1.get_rect()

        investmentRect1.center = (420, 270)    

    

        fontObj2 = pygame.font.Font('freesansbold.ttf',40)

        investmentSurf2 = fontObj2.render(''.join(captchaList), True, WHITE)

        investmentRect2 = investmentSurf2.get_rect()

        investmentRect2.center = (420, 330) 

        

        DISPLAYSURF.fill(BLACK)

        DISPLAYSURF.blit(investmentSurf1,investmentRect1)

        DISPLAYSURF.blit(investmentSurf2,investmentRect2)

        pygame.display.update()

        FPSCLOCK.tick(FPS)

    

    if captchaNumber >= 12:

        

        pygame.time.delay(2000)            

        captchaList.append('*')

    

        fontObj = pygame.font.Font('freesansbold.ttf',18)

        investmentSurf1 = fontObj.render('Wait until your partner unlocks the next round by solving a captcha!', True, WHITE)

        investmentRect1 = investmentSurf1.get_rect()

        investmentRect1.center = (420, 270)    

    

        fontObj2 = pygame.font.Font('freesansbold.ttf',40)

        investmentSurf2 = fontObj2.render(''.join(captchaList), True, WHITE)

        investmentRect2 = investmentSurf2.get_rect()

        investmentRect2.center = (420, 330) 

        

        DISPLAYSURF.fill(BLACK)

        DISPLAYSURF.blit(investmentSurf1,investmentRect1)

        DISPLAYSURF.blit(investmentSurf2,investmentRect2)

        pygame.display.update()

        FPSCLOCK.tick(FPS)

    

    if captchaNumber >= 12:

        

        pygame.time.delay(500)            

        captchaList.append('*')

    

        fontObj = pygame.font.Font('freesansbold.ttf',18)

        investmentSurf1 = fontObj.render('Wait until your partner unlocks the next round by solving a captcha!', True, WHITE)

        investmentRect1 = investmentSurf1.get_rect()

        investmentRect1.center = (420, 270)    

    

        fontObj2 = pygame.font.Font('freesansbold.ttf',40)

        investmentSurf2 = fontObj2.render(''.join(captchaList), True, WHITE)

        investmentRect2 = investmentSurf2.get_rect()

        investmentRect2.center = (420, 330) 

        

        DISPLAYSURF.fill(BLACK)

        DISPLAYSURF.blit(investmentSurf1,investmentRect1)

        DISPLAYSURF.blit(investmentSurf2,investmentRect2)

        pygame.display.update()

        FPSCLOCK.tick(FPS)

    

    if captchaNumber == 12:

        

        pygame.time.delay(500)            

        captchaList.append('*')

    

        fontObj = pygame.font.Font('freesansbold.ttf',18)

        investmentSurf1 = fontObj.render('Wait until your partner unlocks the next round by solving a captcha!', True, WHITE)

        investmentRect1 = investmentSurf1.get_rect()

        investmentRect1.center = (420, 270)    

    

        fontObj2 = pygame.font.Font('freesansbold.ttf',40)

        investmentSurf2 = fontObj2.render(''.join(captchaList), True, WHITE)

        investmentRect2 = investmentSurf2.get_rect()

        investmentRect2.center = (420, 330) 

        

        DISPLAYSURF.fill(BLACK)

        DISPLAYSURF.blit(investmentSurf1,investmentRect1)

        DISPLAYSURF.blit(investmentSurf2,investmentRect2)

        pygame.display.update()

        FPSCLOCK.tick(FPS)

    

   

    if captchaNumber == 12:

        

        pygame.time.delay(800)            

        captchaList.append('*')

    

        fontObj = pygame.font.Font('freesansbold.ttf',18)

        investmentSurf1 = fontObj.render('Wait until your partner unlocks the next round by solving a captcha!', True, WHITE)

        investmentRect1 = investmentSurf1.get_rect()

        investmentRect1.center = (420, 270)    

    

        fontObj2 = pygame.font.Font('freesansbold.ttf',40)

        investmentSurf2 = fontObj2.render(''.join(captchaList), True, WHITE)

        investmentRect2 = investmentSurf2.get_rect()

        investmentRect2.center = (420, 330) 

        

        DISPLAYSURF.fill(BLACK)

        DISPLAYSURF.blit(investmentSurf1,investmentRect1)

        DISPLAYSURF.blit(investmentSurf2,investmentRect2)

        pygame.display.update()

        FPSCLOCK.tick(FPS)

    

    if captchaNumber == 12:

        

        pygame.time.delay(1000)            

        captchaList.append('*')

    

        fontObj = pygame.font.Font('freesansbold.ttf',18)

        investmentSurf1 = fontObj.render('Wait until your partner unlocks the next round by solving a captcha!', True, WHITE)

        investmentRect1 = investmentSurf1.get_rect()

        investmentRect1.center = (420, 270)    

    

        fontObj2 = pygame.font.Font('freesansbold.ttf',40)

        investmentSurf2 = fontObj2.render(''.join(captchaList), True, WHITE)

        investmentRect2 = investmentSurf2.get_rect()

        investmentRect2.center = (420, 330) 

        

        DISPLAYSURF.fill(BLACK)

        DISPLAYSURF.blit(investmentSurf1,investmentRect1)

        DISPLAYSURF.blit(investmentSurf2,investmentRect2)

        pygame.display.update()

        FPSCLOCK.tick(FPS)

        

    if captchaDelete == 4:

        pygame.time.delay(1000)

        captchaList.pop()

       

        fontObj = pygame.font.Font('freesansbold.ttf',18)

        investmentSurf1 = fontObj.render('Wait until your partner unlocks the next round by solving a captcha!', True, WHITE)

        investmentRect1 = investmentSurf1.get_rect()

        investmentRect1.center = (420, 270)    

    

        fontObj2 = pygame.font.Font('freesansbold.ttf',40)

        investmentSurf2 = fontObj2.render(''.join(captchaList), True, WHITE)

        investmentRect2 = investmentSurf2.get_rect()

        investmentRect2.center = (420, 330) 

        

        DISPLAYSURF.fill(BLACK)

        DISPLAYSURF.blit(investmentSurf1,investmentRect1)

        DISPLAYSURF.blit(investmentSurf2,investmentRect2)

        pygame.display.update()

        FPSCLOCK.tick(FPS)

        

    if captchaDelete == 4:

        pygame.time.delay(2000)            

        captchaList.append('*')

        

        fontObj = pygame.font.Font('freesansbold.ttf',18)

        investmentSurf1 = fontObj.render('Wait until your partner unlocks the next round by solving a captcha!', True, WHITE)

        investmentRect1 = investmentSurf1.get_rect()

        investmentRect1.center = (420, 270)    

    

        fontObj2 = pygame.font.Font('freesansbold.ttf',40)

        investmentSurf2 = fontObj2.render(''.join(captchaList), True, WHITE)

        investmentRect2 = investmentSurf2.get_rect()

        investmentRect2.center = (420, 330) 

        

        DISPLAYSURF.fill(BLACK)

        DISPLAYSURF.blit(investmentSurf1,investmentRect1)

        DISPLAYSURF.blit(investmentSurf2,investmentRect2)

        pygame.display.update()

        FPSCLOCK.tick(FPS)

    

    if captchaNumber == 12:

        

        pygame.time.delay(800)            

        captchaList.append('*')

    

        fontObj = pygame.font.Font('freesansbold.ttf',18)

        investmentSurf1 = fontObj.render('Wait until your partner unlocks the next round by solving a captcha!', True, WHITE)

        investmentRect1 = investmentSurf1.get_rect()

        investmentRect1.center = (420, 270)    

    

        fontObj2 = pygame.font.Font('freesansbold.ttf',40)

        investmentSurf2 = fontObj2.render(''.join(captchaList), True, WHITE)

        investmentRect2 = investmentSurf2.get_rect()

        investmentRect2.center = (420, 330) 

        

        DISPLAYSURF.fill(BLACK)

        DISPLAYSURF.blit(investmentSurf1,investmentRect1)

        DISPLAYSURF.blit(investmentSurf2,investmentRect2)

        pygame.display.update()

        FPSCLOCK.tick(FPS)

    

    return

    

def participant():

    

    captchaList = []

    

    while True:

        

        for event in pygame.event.get(): # event handling loop

            if event.type == QUIT:

                terminate()

            elif event.type == KEYDOWN:

                if event.key == K_1:

                    x = '1'

                    captchaList.append(x)

                elif event.key == K_2:

                    x = '2'

                    captchaList.append(x)

                elif event.key == K_3:

                    x = '3'

                    captchaList.append(x)

                elif event.key == K_4:

                    x = '4'

                    captchaList.append(x)

                elif event.key == K_5:

                    x = '5'

                    captchaList.append(x)

                elif event.key == K_6:

                    x = '6'

                    captchaList.append(x)

                elif event.key == K_7:

                    x = '7'

                    captchaList.append(x)

                elif event.key == K_8:

                    x = '8'

                    captchaList.append(x)

                elif event.key == K_9:

                    x = '9'

                    captchaList.append(x)

                elif event.key == K_0:

                    x = '0'

                    captchaList.append(x)

                elif event.key == K_BACKSPACE:

                    captchaList.pop()

                elif event.key == K_RETURN:

                    pygame.event.get() # clear event queue

                    global participant 

                    participant = ''.join(captchaList)

                    return  participant

                   

                    

        

    

        fontObj = pygame.font.Font('freesansbold.ttf',18)

        investmentSurf1 = fontObj.render('Enter participant number:', True, WHITE)

        investmentRect1 = investmentSurf1.get_rect()

        investmentRect1.center = (420, 270)    

        

    

        investmentSurf2 = fontObj.render(''.join(captchaList), True, WHITE)

        investmentRect2 = investmentSurf2.get_rect()

        investmentRect2.center = (420, 330)  

        

        

        

        DISPLAYSURF.fill(BLACK)

        DISPLAYSURF.blit(investmentSurf1,investmentRect1)

        DISPLAYSURF.blit(investmentSurf2,investmentRect2)

        pygame.display.update()

        FPSCLOCK.tick(FPS)

        

    while True:

       

        if checkForKeyPress():

            pygame.event.get() # clear event queue

            return



if __name__ == '__main__':

    main()

