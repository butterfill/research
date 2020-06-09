  # coding: utf-8

"""
This experiment was created using PsychoPy2 Experiment Builder (v1.78.01), Sat Nov  9 22:39:06 2013
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008

Furthermore:
This experiment is part of the research project "Perspective-taking as social cueing", by John Michael, Jakob Hohwy.
Work on this experiment started on 9th of November, 2013 by Thomas Wolf
"""

##########################################################################
### LOAD EVERYTHING THAT IS IMPORTANT (AND POTENTIALLY TIME CONSUMING) ###
## BEFORE THE ACTUAL EXPERIMENT STARTS

## importing modules
from psychopy import core, visual, data, misc, event, logging, gui, sound, prefs
prefs.general['audioLib'] = ['pyo']
import time, numpy, random, os, csv
from random import randrange

import VoiceKeyMonkeyPatch

# The import and pyo_init should always come early on:
import psychopy.voicekey as vk
vk.pyo_init(rate=44100, buffersize=32)

print 0

print prefs.general['audioLib'] 

print 1

## store info about experiment and session

expName = "2017-E1"

# 2016-E1: like 2015_Apr aka. v4.1, but with an SOA of 0 instead of 0.8 sec.
# 2016-E5: like 2016-E1, but with SOAs of 0 AND of 0.8 sec.
# 2016-E6: like 2016-E5, but with SOAs of 0 AND of 0.8 sec in two seperate sessions. Experimenter can choose when experiment is started.
# 2017-E1: DualTask Paradigm


try:                    #try to get a previous parameters file
    expInfo = misc.fromFile('expInfo' + expName + '.pickle')
except:             #if not there then use a default set
    expInfo = {'experimenter':'TW', 'participantID':00, 'participantSex':'f'}
    

## add information to the paramaters file 'expInfo'
expInfo['dateStr']= data.getDateStr()       
expInfo["expName"] = expName

## opening a dialog box to remind experimenter of certains things (such as adjusting screen brightness before experiment starts)

brightnessDialog = gui.Dlg(title="Screen Brightness")
brightnessDialog.addText("Please adjust screen brightness and volume.")
brightnessDialog.show()
if brightnessDialog.OK:
    pass
else:
    core.quit()



## opening a dialog box to input experiment info

dlg = gui.DlgFromDict(expInfo, title='Disks on Walls', fixed=['dateStr']) # shows a dialog to change expInfo.pickle file
if dlg.OK:
    misc.toFile('expInfo' + expName + '.pickle', expInfo) #save parameters to file for next time
else:
    core.quit()     #the user hit cancel so exit


## Setup files for saving data:

print 10

if expInfo['participantID'] < 10:
    fileNameEnd = "0" + str(expInfo['participantID'])
else:
    fileNameEnd = str(expInfo['participantID'])
    
fileName = str(os.getcwd()) + "/data-" + expName + "/" + expInfo['experimenter'] + expInfo['dateStr'] + "_partID_" + fileNameEnd
dataFile = open(fileName + ".csv", "w") #a simple .csv file with 'comma-separated-values'

trialsFile = open(fileName + "trialsFile" + ".csv", "w") #a simple .csv file with 'comma-separated-values' to save order of trials

print 11

## check if participant NR is < 10 and adding a 0 to the front in case it is

partID = expInfo["participantID"]
if partID < 10:                                                    
    expInfo["participantID"] = "0" + str(partID)

print 12

logFile = logging.LogFile(fileName + ".log", level = logging.DEBUG)
logging.console.setLevel(logging.WARNING)

## ExperimentHandler:
thisExp = data.ExperimentHandler(name = expName, version = "0.1", 
    extraInfo = expInfo, runtimeInfo = None, originPath = None, savePickle = True, 
    saveWideText = True, dataFileName = fileName)

## Window
win = visual.Window(fullscr = True, 
    allowGUI=False, monitor='testMonitor', units='norm')
#win.setMouseVisible(False)

## trying to store frame rate of monitor
expInfo["frameRate"] = win.getActualFrameRate()
if expInfo["frameRate"] != None:
    frameDur = 1.0/round(expInfo["frameRate"])
else:
    frameDur = 1.0/60 #we assume 60 Hz if the measurement was unsuccesful

print 13

## test gender string:
if expInfo["participantSex"] == "m":
    pass
elif expInfo["participantSex"] == "f":
    pass
else:
    print("participantSex was neither f nor m. Unfortunately, you have to decide")
    core.quit()
    
####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################
############################### INITALIZE COMPONENTS ###############################
print 2

fixationDuration = 0.750      # in sec. 
numberDuration = 0.75       # in sec.
SOA = 0.8

trialDuration = 2           # in sec. starting after disks appeared

interTrialBreak = 0.750         # break before next fixation appears

nrPractBlocks = 1         # should be 1
numberBlocks = 3          # should be 3

tonesAfter = 35             # should be 35

fixation = visual.TextStim(win, color=[-1, -1, -1], colorSpace='rgb', pos = [0,0], text = "+")

print 2.1


voiceKeyOn = 1

print 2.15
## initialize components for secondary task (st_)
st_tick = sound.Sound('900', secs = 0.02, sampleRate = 44100) #, bits = 8)
st_tock = sound.Sound('700', secs = 0.02, sampleRate = 44100) #, bits = 8)

print st_tick.getDuration()


print 2.2

# What signaler class to use? Here just the demo signaler:
#from psychopy.voicekey.demo_vks import DemoVoiceKeySignal as Signaler


st_sound1TimeInterval = [99, 100]          # was 50, 150
st_sound2TimeInterval = [249, 250]         # was 250, 350
st_sound1TimePoint = 0.250
st_sound2TimePoint = 0.450

recTime = 2.5           # Length of voiceKey recording, starts immediately after second tone of secondary task

print 2.3

trialText = visual.TextStim(win=win, ori=0, name='trialText',
    text='nonsense',    font='Arial',
    pos=[0, 0], height=0.2, wrapWidth=None,
    color=-1.0, colorSpace='rgb', opacity=1,
    depth=0.0)
    
imgDir = str(os.getcwd()) + "/stimuliPics/"
trialImage = visual.ImageStim(win, image = str(imgDir) + "BB01.bmp")
trialPrePic = visual.ImageStim(win, image = str(imgDir) + "BB01.bmp")
print str(imgDir)


## initalize components for routine "welcome":

welcomeA = "Welcome to the experiment.\nPress the spacebar to start."
welcomeText = visual.TextStim(win, color=[-1, -1, -1], alignHoriz = "center", 
    alignVert = "center", text=welcomeA, height = 0.1, opacity = 1, depth = 0.0)

## initalize components for routine "instructions":
#instructionsA = u"On each trial, you will first see a number from 1-4 at the center of the screen, and then an image of a room with 1-4 red discs on the walls. \nIf the number of discs on the walls matches the number you have just seen displayed on the screen, press 'b' (yes), if not press 'n' (no).\n\nPlease give your response as soon as the discs appear. Try to be as quick as possible while making as few mistakes as possible.\nFor each trial, you have a maximum of 2 seconds to respond.\n\nLet’s start with a practice block consisting of 26 trials.\n\nPress the spacebar to start."
instructions = u"On each trial, you will first see a number from 1-4 at the center of the screen, and then an image of a room. There will then be a brief delay, and then 1-4 red discs will appear on the walls. \nIf the number of discs on the walls matches the number you have just seen displayed on the screen, press 'b' (yes), if not press 'n' (no).\n\nAs soon as you see the discs, please try to respond as quickly as possible while making as few mistakes as possible.\nFor each trial, you have a maximum of 2 seconds to respond.\n\nLet’s start with a practice block consisting of 26 trials.\n\nPress the spacebar to start."
instructionsC = u"On each trial, you will first see a number from 1-4 at the center of the screen, and then an image of a room. There will then be a brief delay, and then 1-4 red discs will appear on the walls. \nIf the number of discs on the walls matches the number you have just seen displayed on the screen, press 'b' (yes), if not press 'n' (no).\n\nPlease give your response as soon as the discs appear. Try to be as quick as possible while making as few mistakes as possible.\nFor each trial, you have a maximum of 2 seconds to respond.\n\nLet’s start with a practice block consisting of 26 trials.\n\nPress the spacebar to start."
instructionsB = u"Now we will do a practice block for the Disc Task. \n\nOn each trial, you will first see a number from 1-4 at the center of the screen, and then an image of a room. There will then be a brief delay, and then 1-4 red discs will appear on the walls. \nIf the number of discs on the walls matches the number you have just seen displayed on the screen, press 'b' (yes), if not press 'n' (no).\n\nAs soon as you see the discs, please try to respond as quickly as possible while making as few mistakes as possible.\nFor each trial, you have a maximum of 2 seconds to respond.\n\nPress the space bar to start the practice block."

instructionText = visual.TextStim(win, color=[-1, -1, -1], alignHoriz = "center", 
alignVert = "center", text=instructionsB, height = 0.1, opacity = 1, depth = 0.0, wrapWidth = 1.8)

## initalize components for routine "afterPractBlock":
afterPractBlockA = "End of practice phase. Now there will be 3 blocks of approximately 10 minutes each.\nIf you have any questions before you start, please ask the experimentor now.\nWhen you are ready, press the spacebar to continue."
afterPractBlockText = visual.TextStim(win, color=[-1, -1, -1], alignHoriz = "center", wrapWidth = 1.8,
    alignVert = "center", text=afterPractBlockA, height = 0.1, opacity = 1, depth = 0.0)

## initalize components for routine "btwBlocks":
btwBlocksA = "Press the spacebar to start the next block!"
btwBlocksText = visual.TextStim(win, color=[-1, -1, -1], alignHoriz = "center", 
    alignVert = "center", text=btwBlocksA, height = 0.1, opacity = 1, depth = 0.0)


## initalize components for routine "btwPractBlocks":

btwPractBlocksA = u"Now we will do a practice block for the Tone Task. \n\nWhat you see will be exactly the same as on the Disc Task, but now please just ignore the numbers that appear. Just after the image of the room appears, you will hear two tones in rapid succession. Your aim is to judge whether the two tones are the same or different. If they are the same, please say 'same!' as quickly as possible into the microphone. If they are different, please do not give any response. \n\nPlease try to complete the task as quickly as possible each time. Once the discs appear on the walls of the room, it will no longer be possible to give a response for the Tone Task. \n\nOnce the discs appear, please just wait a couple of seconds until the next trial begins."
btwPractBlocksB = u"Now we will do a practice block for both tasks at the same time. \n\nJust as before, you will first see a number (1-4) displayed, and then the image of a room will appear, followed rapidly by the 2 tones. As before, please respond by saying 'same!' if the two tones are the same, and do not say anything at all if they are different. Please try to make your judgment as quickly as possible so that you are finished by the time the discs appear. \n\nOnce the discs appear, your task is to judge whether the number of discs matches the number that was displayed (1-4) at the beginning of that trial. If it does match, then please press 'b' for yes. If it does not match, please press 'n' for no. Please respond as quickly as possible on each trial."

btwPractBlocksText = visual.TextStim(win, color=[-1, -1, -1], alignHoriz = "center", wrapWidth = 1.8,
    alignVert = "center", text=btwPractBlocksA, height = 0.1, opacity = 1, depth = 0.0)





## initialize components for routine "practice block":

## Create Blocks

if expInfo["participantSex"] == "m":
    tT = "trialLists-" + expName + "/trialTypesM.csv"
    pT = "trialLists-" + expName + "/trialTypesMpract.csv"
elif expInfo["participantSex"] == "f":
    tT = "trialLists-" + expName + "/trialTypesF.csv"
    pT = "trialLists-" + expName + "/trialTypesFpract.csv"
else:
    print("participantSex was neither f nor m. Unfortunately, you have to decide")
    core.quit()

## TrialHandler for practBlock 

practBlock = data.TrialHandler(trialList = data.importConditions(pT), nReps = nrPractBlocks, method = 'random', 
    extraInfo = expInfo, originPath = None, seed = None, name = 'practBlock')

thisExp.addLoop(practBlock)


## TrialHandler for standard block
trialsBlock1 = data.TrialHandler(trialList = data.importConditions(tT), nReps = numberBlocks, method = 'random', 
    extraInfo = expInfo, originPath = None, seed = None, name = 'trialsBlock1')


thisExp.addLoop(trialsBlock1) # add the loop to the experiment

thisTrial = trialsBlock1.trialList[0] # so we can initalize stimuli with some values


# abbreviate parameter names if possible
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec(paramName + '= thisTrial.' + paramName)




## initalize components for routine "Thanks"

thanksText = visual.TextStim(win=win, ori=0, name='word',
    text="Thank you for your participation. Please contact the experimenter.",    font='Arial',
    pos=[0, 0], height=0.2, wrapWidth=None,
    color= -1.0, colorSpace='rgb', opacity=1,
    depth=0.0)
    

## clocks and timers:
instructionClock = core.Clock()
globalClock = core.Clock()                     # to track the time since experiment started
trialClock = core.Clock()
routineTimer = core.CountdownTimer() # to track time remaining of each (non-slip) routine







##########################################################
##########################################################
## -------------  EXPERIMENT STARTS HERE -------------- ##
print 3




##########################################
## ------------- WELCOME -------------- ##


#Prepare to start routine "welcome"
welcomeStatus = "notStarted"
continueWelcome = True

## ------- Start Routine "Welcome" ------- ##

while continueWelcome == True:
    
    if welcomeStatus == "notStarted":
        welcomeText.setAutoDraw(True)
        welcomeStatus = "started"
        
    if welcomeStatus == "started":
        if event.getKeys(["escape"]):
            core.quit()
        if event.getKeys(["space"]):
            # a response ende the routine
            welcomeText.setAutoDraw(False)
            win.flip()
            continueWelcome = False  
        
    # refresh screen
    if continueWelcome == True: # don't flip if this routine is over or we'll get a blank screen
        win.flip()  



#######################################
## --------- INSTRUCTIONS -----------##


#Prepare to start routine "instructions"
t = 0
instructionClock.reset()
frameN = -1
instructionStatus = "notStarted"



## ------- Start Routine "instruction" --------

continueRoutine = True
while continueRoutine == True:
    t = instructionClock.getTime()
    frameN = frameN + 1
    
    if t >= 0 and instructionStatus == "notStarted":
        # keep track of start time/frame for later
        instructionText.tStart = t
        instructionText.frameNStart = frameN
        instructionText.setAutoDraw(True)
        instructionStatus = "started"
        
    if instructionStatus == "started":
        if event.getKeys(["escape"]):
            core.quit()
        if event.getKeys(["space"]):
            # a response ende the routine
            instructionText.setAutoDraw(False)
            win.flip()
            continueRoutine = False  
        
    # refresh screen
    if continueRoutine == True: # don't flip if this routine is over or we'll get a blank screen
        win.flip()  



####################################################
####################################################
## ------------ START PRACTICE BLOCK ------------ ##
## ------------ START PRACTICE BLOCK ------------ ##
## ------------ START PRACTICE BLOCK ------------ ##
print "Start Pract Block"

## prepare to start routine "practBlock"
#practTrialCounter = 0

for thisTrial in practBlock:
    currentLoop = practBlock
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
            
    
    if practBlock.thisTrialN in [36, 72]:
        trialDuration = 1.0
        continueBtwPractBlocks = True
        btwPractBlocksStatus = "notStarted"
        if practBlock.thisTrialN == 72:
            trialDuration = 2.0
            btwPractBlocksText = visual.TextStim(win, color=[-1, -1, -1], alignHoriz = "center", wrapWidth = 1.8,
            alignVert = "center", text=btwPractBlocksB, height = 0.1, opacity = 1, depth = 0.0)
        
    else:
        continueBtwPractBlocks = False

        
    while continueBtwPractBlocks == True:
        if btwPractBlocksStatus == "notStarted":
            btwPractBlocksText.setAutoDraw(True)
            btwPractBlocksStatus = "started"
            
        if btwPractBlocksStatus == "started":
            if event.getKeys(["escape"]):
                core.quit()
            if event.getKeys(["space"]):
                # a response ends the routine
                btwPractBlocksText.setAutoDraw(False)
                win.flip()
                continueBtwPractBlocks = False  
            
        # refresh screen
        if continueBtwPractBlocks == True: # don't flip if this routine is over or we'll get a blank screen
            win.flip()  

    t = 0
    trialClock.reset()
    frameN = -1
    trialStatus = 'notStarted'
    respStatus = 'notStarted'

    # update secondary task (st_) parameters for each repeat
    
    st_interval1 = randrange(st_sound1TimeInterval[0], st_sound1TimeInterval[1]) / 1000.    # st_sound1TimeInterval[0]
    st_interval2 = randrange(st_sound2TimeInterval[0], st_sound2TimeInterval[1]) / 1000.    # st_sound2TimeInterval[0]
    
    st_time1 = 0.8 - st_interval1
    st_time2 = 0.8 - st_interval2
    #st_time1 = st_sound1TimePoint
    #st_time2 = st_sound2TimePoint
    
    
    if randrange(0, 2) == 0:
        st_sound1 = st_tick
        st_audio1 = 1
    else:
        st_sound1 = st_tock
        st_audio1 = 2
        
    if randrange(0, 2) == 0:
        st_sound2 = st_tick
        st_audio2 = 1
    else:
        st_sound2 = st_tock
        st_audio2 = 2
        
    
    # If we are beyond the first part of the practice phase, prepare everything for secondary task
    
    if practBlock.thisTrialN > tonesAfter:
        st_start1 = 1
        vpvk = vk.OnsetVoiceKey(
        sec = recTime, 
        file_out = 'audio-files/' + str(expInfo['participantID']) + "-prct" + str(practBlock.thisN) + '.wav')   # trialsBlock1.thisN
    else:
        st_start1 = 0
    st_start2 = 0
    
    
    
    if text > 10:
        correctTemp = text - 10
        if correctTemp == 3:
            if randrange(0,2,1) == 0:
                text = correctTemp - 1
            else:
                text = correctTemp + 1
        elif correctTemp == 4:
            text = 4 - randrange(1, 3, 1)
        elif correctTemp == 2:
            if randrange(0,2,1) == 0:
                text = correctTemp - 1
            else:
                text = correctTemp + 1
        elif correctTemp == 1:
            text = 1 + randrange(1, 3, 1)
        else:
            pass
        trialText.setText(text)
    else:
        trialText.setText(text)
        
    trialImage.setImage(stimulus)
    trialPrePic.setImage(prePic)
    actualText = text

    ## inter-trial-break loop:
    if practBlock.thisTrialN > 72:
        
        interTrialTimer = core.CountdownTimer(interTrialBreak) 
        win.flip()
        while interTrialTimer.getTime() > 0: 
            if event.getKeys(["escape"]):
                core.quit()
            core.wait(0.001)


    
    ## fixation loop:
    fixationTimer = core.CountdownTimer(fixationDuration) 
    fixation.setAutoDraw(True)
    win.flip()
    while fixationTimer.getTime() > 0: 
        if event.getKeys(["escape"]):
            core.quit()
        core.wait(0.001)
    fixation.setAutoDraw(False)
    
    
    ## number loop:
    textTimer = core.CountdownTimer(numberDuration) 
    trialText.setAutoDraw(True)
    win.flip()
    while textTimer.getTime() > 0: 
        if event.getKeys(["escape"]):
            core.quit()
        core.wait(0.001)
    trialText.setAutoDraw(False)
    #win.flip()
    
    event.clearEvents()
    
    ## prePic loop:
    # prePic is the same pic as in the following trial, but without discs, for 800 ms
    prePicTimer = core.CountdownTimer(SOA)
    
    trialPrePic.draw()
    win.flip()
    
    
    
    while prePicTimer.getTime() > 0:
        #print "loop"
        #print prePicTimer.getTime() * 1000
       
        if prePicTimer.getTime() > st_time1:
            st_go1 = 0
            st_go2 = 0
        else:
            st_go1 = 1
        
        if prePicTimer.getTime() > st_time2:
            st_go2 = 0
        else:
            st_go2 = 1
            
        if st_start1 == 1:
            if st_go1 == 1:
                #print "InnerLoop1"
                st_sound1.play()
                st_actual1 = SOA - prePicTimer.getTime()
                st_start1 = 0
                st_start2 = 1
        
        if st_start2 == 1:
            if st_go2 == 1:
                #print "InnerLoop2"
                #print 1000 * prePicTimer.getTime()
                st_sound2.play()
                st_actual2 = SOA - prePicTimer.getTime()
                st_start2 = 0
                if voiceKeyOn == 1:
                    vpvk.start()
                
                
            
        #trialPrePic.setAutoDraw(False)
        #win.flip()
        core.wait(0.001)
        
        if event.getKeys(["escape"]):
            core.quit()
        # draw initialImage
        
    #trialPrePic.setAutoDraw(False)
    
    event.clearEvents()


    ### ----------Start Routine "PractBlock" ---------------- ###

    stimTimer = core.CountdownTimer(trialDuration)
    rt = 9999
    continueStim = True
    
    trialImage.setAutoDraw(True)
    win.flip()
    trialClock.reset()

    while stimTimer.getTime() > 0 and continueStim == True:
        noResponse = True
        #win.flip()   # refresh screen
        theseKeys = event.getKeys() #get all pressed keys
        #t = trialClock.getTime()   # get current time:
        frameN = frameN + 1 # number of completed frames (so 0 is the first frame)
                
        #if t > 0 and trialStatus == 'notStarted':
            # keep track of start time/frame for later
            #trialImage.tStart = t  # underestimates by a little under one frame
            #trialImage.frameNStart = frameN  # exact frame index
            
            #trialClock.reset()
         #   trialStatus = "started"
         
        #if trialStatus == "started":
        if len(theseKeys) > 0:
            noResponse = False
            thisKey = []
            thisKey = theseKeys[-1] # just the last keypress

            if thisKey == "escape":
                core.quit()
            rt = trialClock.getTime()
            if thisKey == "b":     # "b" is defined as YES
                thisKey = 1
            elif thisKey == "n":  # "n" is defined as NO
                thisKey = 0
            else:
                thisKey = 9999
                
            key = thisKey
            # was this correct?
            if key == corrAns:
                respCorr = 1
            else:
                respCorr = 0
            continueStim = False
        core.wait(0.001)
            
                        
    ## --- Ending Routine PractBlock --------
    routineTimer.reset()
    trialImage.setAutoDraw(False)
    win.flip()
    event.clearEvents()
    
    if noResponse == True:
        respCorr = 9999
        thisKey = 9999
    
    if practBlock.thisTrialN > tonesAfter:
        if voiceKeyOn == 1:
            
            vpvk.stop()
    
            # Add the detected time into the PsychoPy data file:
            #print('vocal_RT', round(vpvk.event_onset, 3))
            #print('bad_baseline', vpvk.bad_baseline)
            #print('filename', vpvk.filename)
  
    
    practBlock.addData("corrResponse", respCorr)
    practBlock.addData("RT", rt)
    practBlock.addData("KeyPressed", thisKey)
    practBlock.addData("actualText", actualText)
    practBlock.addData("sessionSOA", SOA * 1000)
    #practBlock.addData("st_time1", st_interval1 * 1000)
    #practBlock.addData("st_time2", st_interval2 * 1000)
    
    if practBlock.thisTrialN > tonesAfter:
        practBlock.addData("st_time1_actual", st_actual1 * 1000)
        practBlock.addData("st_time2_actual", st_actual2 * 1000)
        practBlock.addData("st_audio1", st_audio1)
        practBlock.addData("st_audio2", st_audio2)
        practBlock.addData("vocal_RT", vpvk.event_onset)
        practBlock.addData('filename', vpvk.filename)
        practBlock.addData('bad_baseline', vpvk.bad_baseline)
    
    thisExp.nextEntry()


######################################
## ------- AFTER PRACTBLOCK ------- ##


##Prepare to start routine "afterPractBlock"
afterPractBlockStatus = "notStarted"
continueafterPractBlock = True



## ------- Start Routine "afterpractBlock" --------

while continueafterPractBlock == True:
    
    if afterPractBlockStatus == "notStarted":
        afterPractBlockText.setAutoDraw(True)
        afterPractBlockStatus = "started"
        
    if afterPractBlockStatus == "started":
        if event.getKeys(["escape"]):
            core.quit()
        if event.getKeys(["space"]):
            # a response ende the routine
            afterPractBlockText.setAutoDraw(False)
            win.flip()
            continueafterPractBlock = False  
        
    # refresh screen
    if continueafterPractBlock == True: # don't flip if this routine is over or we'll get a blank screen
        win.flip()  




#############################################
#############################################
#############################################
### ----------- START TRIALS ------------ ###
### ----------- START TRIALS ------------ ###
### ----------- START TRIALS ------------ ###
### ----------- START TRIALS ------------ ###

    
blockNr = 0

## prepare to start routine "Trials"

for thisTrial in trialsBlock1:
    
    currentLoop = trialsBlock1
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
    
    #Prepare to start routine "btwBlocks" if necessary:
    
    prevBlockNr = blockNr
    blockNr = trialsBlock1.thisRepN
    if prevBlockNr == blockNr:
        continueBtwBlocks = False
    else:
        print "Block Nr has changed from", prevBlockNr, "to", blockNr
        continueBtwBlocks = True
        btwBlocksStatus = "notStarted"


## ------- Start Routine "btwBlocks" if necessary --------
    
    while continueBtwBlocks == True:
        if btwBlocksStatus == "notStarted":
            btwBlocksText.setAutoDraw(True)
            btwBlocksStatus = "started"
            
        if btwBlocksStatus == "started":
            if event.getKeys(["escape"]):
                core.quit()
            if event.getKeys(["space"]):
                # a response ende the routine
                btwBlocksText.setAutoDraw(False)
                win.flip()
                continueBtwBlocks = False  
            
        # refresh screen
        if continueBtwBlocks == True: # don't flip if this routine is over or we'll get a blank screen
            win.flip()  

## ------ continue preparing routine "Trial" -------

    t = 0
    trialClock.reset()
    frameN = -1
    trialStatus = 'notStarted'
    respStatus = 'notStarted'

    # update component parameters for each repeat
    # this includes numbers displayed, pre-picture and trial image
    # SOA = trialSOA   - only needs to be updated for 2016-E5
    
    # update secondary task (st_) parameters for each repeat
    
    st_interval1 = randrange(st_sound1TimeInterval[0], st_sound1TimeInterval[1]) / 1000.
    st_interval2 = randrange(st_sound2TimeInterval[0], st_sound2TimeInterval[1]) / 1000.
    
    st_time1 = 0.8 - st_interval1
    st_time2 = 0.8 - st_interval2
    
    #st_time1 = st_sound1TimePoint
    #st_time2 = st_sound2TimePoint
    
    
    if randrange(0, 2) == 0:
        st_sound1 = st_tick
        st_audio1 = 1
    else:
        st_sound1 = st_tock
        st_audio1 = 2
        
    if randrange(0, 2) == 0:
        st_sound2 = st_tick
        st_audio2 = 1
    else:
        st_sound2 = st_tock
        st_audio2 = 2
        
    st_start1 = 1
    st_start2 = 0
    
    vpvk = vk.OnsetVoiceKey(
        sec = recTime, 
        file_out = 'audio-files/' + str(expInfo['participantID']) + "-xprmnt" + str(trialsBlock1.thisN) + '.wav')   # trialsBlock1.thisN
    
    
    
    if text > 10:
        correctTemp = text - 10
        if correctTemp == 3:
            if randrange(0,2,1) == 0:
                text = correctTemp - 1
            else:
                text = correctTemp + 1
        elif correctTemp == 4:
            text = 4 - randrange(1, 3, 1)
        elif correctTemp == 2:
            if randrange(0,2,1) == 0:
                text = correctTemp - 1
            else:
                text = correctTemp + 1
        elif correctTemp == 1:
            text = 1 + randrange(1, 3, 1)
        else:
            pass
        trialText.setText(text)
    else:
        trialText.setText(text)
        
    trialImage.setImage(stimulus)
    trialPrePic.setImage(prePic)
    actualText = text

    # inter-trial-break loop:
    interTrialTimer = core.CountdownTimer(interTrialBreak) 
    win.flip()
    while interTrialTimer.getTime() > 0: 
        if event.getKeys(["escape"]):
            core.quit()
        core.wait(0.001)
    
    # fixation loop:
    fixationTimer = core.CountdownTimer(fixationDuration)
    fixation.setAutoDraw(True)
    win.flip()
    while fixationTimer.getTime() > 0: 
        if event.getKeys(["escape"]):
            core.quit()
        core.wait(0.001)
    fixation.setAutoDraw(False)
    
    # number loop:
    textTimer = core.CountdownTimer(numberDuration)
    trialText.setAutoDraw(True)
    win.flip()
    while textTimer.getTime() > 0: 
        if event.getKeys(["escape"]):
            core.quit()
        core.wait(0.001)
    trialText.setAutoDraw(False)
    
    event.clearEvents()
    
    # prePic loop:
    # prePic is the same pic as in the following trial, but without discs, for 800 ms (depending on SOA, set in the beginning)
    prePicTimer = core.CountdownTimer(SOA)
    trialPrePic.setAutoDraw(True)
    win.flip()
    
    while prePicTimer.getTime() > 0:
        
        if prePicTimer.getTime() > st_time1:
            st_go1 = 0
            st_go2 = 0
        else:
            st_go1 = 1
            if prePicTimer.getTime() > st_time2:
                st_go2 = 0
            else:
                st_go2 = 1
        if st_start1 == 1:
            if st_go1 == 1:
                st_sound1.play()
                st_actual1 = SOA - prePicTimer.getTime()
                st_start1 = 0
                st_start2 = 1
        else:
            if st_start2 == 1:
                if st_go2 == 1:
                    st_sound2.play()
                    st_actual2 = SOA - prePicTimer.getTime()
                    st_start2 = 0
                    if voiceKeyOn == 1:
                        vpvk.start()
        
        if event.getKeys(["escape"]):
            core.quit()
        core.wait(0.001)
        
    trialPrePic.setAutoDraw(False)
    event.clearEvents()

    ##----------Start Routine "Trial" ----------------

    stimTimer = core.CountdownTimer(trialDuration)
    rt = 9999
    continueStim = True
    
    trialImage.setAutoDraw(True)
    win.flip()
    trialClock.reset()

            
    while stimTimer.getTime() > 0 and continueStim == True:
        noResponse = True
        #win.flip()   # refresh screen
        theseKeys = event.getKeys() #get all pressed keys
        #t = trialClock.getTime()   # get current time:
        frameN = frameN + 1 # number of completed frames (so 0 is the first frame)
                
        
        if len(theseKeys) > 0:
            noResponse = False
            thisKey = []
            thisKey = theseKeys[-1] # just the last keypress

            if thisKey == "escape":
                core.quit()
            rt = trialClock.getTime()
            if thisKey == "b":     # "b" is defined as YES
                thisKey = 1
            elif thisKey == "n":  # "n" is defined as NO
                thisKey = 0
            else:
                thisKey = 9999
                
            key = thisKey
            # was this correct?
            if key == corrAns:
                respCorr = 1
            else:
                respCorr = 0
            continueStim = False
            
        core.wait(0.001)
           
            
                     
    ## --- Ending Routine Trial --------
    routineTimer.reset()
    trialImage.setAutoDraw(False)
    win.flip()
    event.clearEvents()
    
    
    if voiceKeyOn == 1:
        vpvk.stop()
    
    if noResponse == True:
        respCorr = 9999
        thisKey = 9999
    
    trialsBlock1.addData("corrResponse", respCorr)
    trialsBlock1.addData("RT", rt)
    trialsBlock1.addData("KeyPressed", thisKey)
    trialsBlock1.addData("actualText", actualText)
    trialsBlock1.addData("sessionSOA", SOA * 1000)
    trialsBlock1.addData("st_time1", st_interval1 * 1000)
    trialsBlock1.addData("st_time1_actual", st_actual1 * 1000)
    trialsBlock1.addData("st_time2", st_interval2 * 1000)
    trialsBlock1.addData("st_time2_actual", st_actual2 * 1000)
    trialsBlock1.addData("st_audio1", st_audio1)
    trialsBlock1.addData("st_audio2", st_audio2)
    trialsBlock1.addData("vocal_RT", vpvk.event_onset)
    trialsBlock1.addData('filename', vpvk.filename)
    trialsBlock1.addData('bad_baseline', vpvk.bad_baseline)
    
    thisExp.nextEntry()


##########################################
##########################################
## ---------- START THANKS -------------##

## preparing routine "Thanks"
thanksStatus = "notStarted"
event.clearEvents()

## start routine "Thanks"
continueThanks = True
while continueThanks == True:
     
    if thanksStatus == "notStarted":
        thanksText.setAutoDraw(True)
        thanksStatus = "started"
        
    if thanksStatus == "started":
        if event.getKeys(["escape"]):
            thanksText.setAutoDraw(False)
            win.flip()
            continueThanks = False
            dataFile.close()
            core.quit()
        
        
    # refresh screen
    if continueThanks == True: # don't flip if this routine is over or we'll get a blank screen
        win.flip()  


dataFile.close()
win.close()
core.quit()

