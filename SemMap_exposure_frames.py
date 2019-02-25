#SEMANTIC MAPPING - Exposure
# Participants will be presented with images behind a fixation cross
# They will be instructed to press a button when the fixation cross changes colour
# Run time = 32.5 min

# We collect functional data throughout this in order to see what 
# the patterns of activation are during each image stim 

# import libraries
from __future__ import division, print_function
import random
#from Pillow import Image
from psychopy import gui, data, core, event, logging, visual
#from psychopy.constants import visual
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os, time

# setup window
win = visual.Window([1920,1080])
win.recordFrameIntervals = True
win.refreshThreshold = 1/60 + 0.004
m = event.Mouse(win=win)
m.setVisible(False)
#win.setMouseVisible = False
logging.console.setLevel(logging.WARNING)

## Set up Experiment ##

# Experiment Name:
expName = 'SemMap'
# Used for prompt pop-up
expInfo = {'participant': '', 'age': ''}
# Display prompt that asks for part id and age
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
# Get the current data (will go into output file name) 
expInfo['date'] = data.getDateStr() # this adds a simple timestamp

# Exit if the user exits the prompt
if not dlg.OK:
    core.quit() # user pressed cancel

# Get the filename based on participant number
#participant_filename = "participant_files/participant_%s.csv" % expInfo['participant']
# Get the filename for the stimulus file
SemMap_filename = "SemMap_stim_frames.csv"
# Get the output filename based on part id and date
output_filename = "output/SemMap_participant_%s_%s" % (expInfo['participant'], expInfo['date'])
# Extra information for the output file 
info = {'date': expInfo['date'], 'participant': expInfo['participant'], 'age': expInfo['age']}

# experiment handler generates a single data file from an experiment when given trialhandler. 
# In order to have more than 1 output file, more than one experiment handler will need to be created 
# anything added to extraInfo variable will be included in output as a column

# This creates an experiment Handler for the RSA block 1
thisExp = data.ExperimentHandler(name=expName, version='',
                                 extraInfo=info, runtimeInfo=None,
                                 savePickle=True, saveWideText=True, 
                                 dataFileName=output_filename)

# class to handle trial sequencing and data storage
# anything added to the extraInfo variable will be included in output as a column
trial_handler = data.TrialHandler(nReps=1, method='sequential',
                                  extraInfo=None, trialList=data.importConditions(SemMap_filename),
                                  seed=None, name='')

# Add the trial handler to the ExperimentHandler
# Adding the trial handler will add all the columns from the read CSV into the output CSV
thisExp.addLoop(trial_handler)
#thisExp.addLoop(test_trial_handler)

# =============================== IMAGE SIZES AND LOCATIONS =============================== 
# Screen Window 
win = visual.Window(size=(1920,1080), fullscr=True, screen=0, allowGUI=False,
                   allowStencil=False, monitor='testMonitor', color=[1,1,1], colorSpace='rgb',
                   blendMode='avg', useFBO=True)

# display_time & ISI = variable and will read from file

full_screen_image = visual.ImageStim(win=win, size=2, pos=[0,0])

instruct_img = visual.ImageStim(win=win, name='instruct',
                        pos=[0,0], size=2)

wait_for_scanner_img = visual.ImageStim(win=win, name='wait_for_scanner',
                        pos=[0,0], size=2, image='SemMap_instructions/SemMap_instructions/wait.png')

stim_img = visual.ImageStim(win=win, name='stimulus', 
                        pos=[0,0], size=1)

# ===============================  FOR TESTING BUTTON PRESSES =============================== 
pressOne = visual.TextStim(win=win, ori=0, name='cross',
    text='Press 1',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)

pressTwo = visual.TextStim(win=win, ori=0, name='cross',
    text='Press 2',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)

pressThree = visual.TextStim(win=win, ori=0, name='cross',
    text='Press 3',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)

pressFour = visual.TextStim(win=win, ori=0, name='cross',
    text='Press 4',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)

# =============================== FIXATION CROSSES =============================== 
blue_cross = visual.TextStim(win=win, ori=0, name='cross',
        text='+',
        pos=[0, 0], height=0.1, wrapWidth=None,
        color='blue', colorSpace='rgb', opacity=1,
        depth=0.0)

green_cross = visual.TextStim(win=win, ori=0, name='cross',
        text='+',
        pos=[0, 0], height=0.1, wrapWidth=None,
        color='green', colorSpace='rgb', opacity=1,
        depth=0.0)

# =============================== START EXPERIMENT ===============================
# =============================== TEST BUTTON PRESSES ===============================

# Clear the key board just to be sure
event.clearEvents(eventType='keyboard')

# Asks participant to press 1 to just double check that their fingers are in the right places
pressOne.draw()
win.flip()
theseKeys = event.waitKeys(keyList=['1'])

# Asks participant to press 3 to just double check that their fingers are in the right places
pressThree.draw()
win.flip()
theseKeys = event.waitKeys(keyList=['3'])

# Asks participant to press 4 to just double check that their fingers are in the right places
pressFour.draw()
win.flip()
theseKeys = event.waitKeys(keyList=['4'])

# Asks participant to press 2 to just double check that their fingers are in the right places
pressTwo.draw()
win.flip()
theseKeys = event.waitKeys(keyList=['2'])

# =============================== INSTRUCTIONS ===============================

instructions_list1 = ['Slide1.png', 'Slide2.png', 'Slide3.png', 'Slide4.png']
#instructions_list1 = ['instr_1.png', 'instr_2.png', 'instr_3.png', 'instr_4.png']

for instruction in instructions_list1:
    instruct_img.setImage('SemMap_instructions/SemMap_instructions/%s' % instruction)
    instruct_img.draw()
    win.flip()
    while True: 
        time.sleep(1) # reduces amount of resources used
        if event.getKeys(keyList=['escape','esc']):
            core.quit()
        elif event.getKeys(keyList=['1']):
            break

# =============================== STARTING SCAN ===============================

#Display wait message
wait_for_scanner_img.draw()
win.flip()

# Wait for MRI signal '5'
while(not event.getKeys(keyList=['5'])):
    time.sleep(0.01)

#enc_resp=event.BuilderKeyResponse()  # create an object of type KeyResponse

# start the full experiment clock as soon as the scanner pulse is sent to us
expClock = core.Clock()
rtClock = core.Clock()
trialClock = core.Clock()
RT_resp=event.BuilderKeyResponse()  # create an object of type KeyResponse
frameN = -1
continueRoutine = True

# =============================== LOOP THROUGH ALL TRIALS ===============================

# check for quit
if event.getKeys(keyList=["escape"]):
   print("NO MORE")
   core.quit()

# initial ISI
trialClock.reset()
frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
#print(trialClock.getTime())
#print('isi start time: %i' % (frameN + 1))
for frameN in range(600):
    blue_cross.draw()
    win.flip()

# start trial 
for trial in trial_handler:
    
    # check for quit
    if event.getKeys(keyList=["escape"]):
       print("NO MORE")
       core.quit()
           
    # set the image to the right one
    stim_img.setImage('final_stimuli/stim/%s' % trial['item'])
    
    # draw the image on the screen
    # draw the fixation
    # begin trial
    trialClock.reset()
    #print(trialClock.getTime())
    #print('trial start time: %i' % (frameN + 1))
    trial_start_time = expClock.getTime()
    for frameN in range(trial['trial_start_time_frames'],trial['trial_start_time_frames']+trial['flip_time_frames']):
        stim_img.draw()
        blue_cross.draw()
        win.flip()    
    
    # switch the fixation cross to green
    #print('flip start time: %i' % (frameN + 1))
    # get ready to collect responses during green cross time
    RT_resp.clock.reset()
    found=False
    event.clearEvents(eventType='keyboard')
    flipped_time = trialClock.getTime()
    for frameN in range(trial['trial_start_time_frames']+trial['flip_time_frames'],trial['trial_start_time_frames']+trial['display_time_frames']):
        stim_img.draw()
        green_cross.draw()
        win.flip()
        rtClock.reset()
        
    # collect response
        theseKeys = event.getKeys(keyList=['1', '2','3','4'])
        if(len(theseKeys)>0 and not found):
            RT_resp.keys=theseKeys[0]
            RT_resp.RT=RT_resp.clock.getTime()
            RT_on_time = 'yes'
            found=True
        if not found:
            RT_resp.keys='NA'
            RT_resp.RT='NA'
            RT_on_time='NA'    
    # switch the fixation cross back to blue for the ISI
    #print('isi2 start time: %i' % (frameN + 1))
    trial_time = trialClock.getTime()
    for frameN in range(trial['trial_start_time_frames']+trial['display_time_frames'],trial['trial_start_time_frames']+trial['total_trial_time_frames']):
        blue_cross.draw()
        win.flip()
   
    #for frameN in range(trial['trial_start_time_frames'],trial['trial_start_time_frames']+trial['total_trial_time_frames']):
        theseKeys = event.getKeys(keyList=['1', '2','3','4'])
        #if found:
        if(len(theseKeys)>0 and not found):
            RT_resp.keys=theseKeys[0]
            RT_resp.RT=RT_resp.clock.getTime()
            RT_on_time = 'late'
            found=True
        if not found:
            RT_resp.keys='NA'
            RT_resp.RT='NA'
            RT_on_time='NA' 
            
    # print dropped frames
    print('%i frames were dropped.' % win.nDroppedFrames)
        
    # --- add data to output file after each trial ---
    thisExp.addData('sub_num',expInfo['participant'])
    thisExp.addData('flipped_time', flipped_time)
    thisExp.addData('stimulus_num',trial['item'])
    thisExp.addData('cross_resp',RT_resp.keys)
    thisExp.addData('cross_RT',RT_resp.RT)
    thisExp.addData('RT_press_on_time?', RT_on_time)
    thisExp.addData('trial_start_time', trial_start_time)
    thisExp.addData('trial_time',trial_time)
    thisExp.nextEntry()

core.quit()
