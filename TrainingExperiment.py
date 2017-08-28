#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.70.01),
    on August 23, 2017, at 16:28
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding
import pandas as pd

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
expName = u'Test'  # from the Builder filename that created this script
expInfo = {'participant':'', 'session':03}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data' + os.sep + '%s_%s' % (expInfo['participant'], expInfo['date'])



# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'C:\\Users\\James\\Desktop\\ErrorRelatedPotentialProject\\TrainingExperimentPsychoPy',
    savePickle=False, saveWideText=True,
    dataFileName=filename)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1536, 864), fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0, 0, 0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess


# Initialize components for Routine "trial"
trialClock = core.Clock()



presentSet = visual.TextStim(win=win, name='presentSet',
    text='default text',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
presentTarget = visual.TextStim(win=win, name='presentTarget',
    text='default text',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);
presentTarget2 = visual.TextStim(win=win, name='presentTarget',
    text='default text',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);
presentTarget3 = visual.TextStim(win=win, name='presentTarget',
    text='default text',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);
presentTarget4 = visual.TextStim(win=win, name='presentTarget',
    text='default text',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
#msg variable just needs some value at start
msg=''
feedback_2 = visual.TextStim(win=win, name='feedback_2',
    text='default text',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color=[1,1,1], colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "mainInstruct"
mainInstructClock = core.Clock()
instr2 = visual.TextStim(win=win, name='instr2',
    text='OK, ready to start the main experiment?\n\nRemember:\n - LEFT CURSOR for NOT in the sequence\n - RIGHT CURSOR for IN the sequence\nTry to respond as quickly and as accurately as possible.\n\nWhen you are ready to proceed press any key.',
    font='Arial',
    pos=[0, 0], height=0.05, wrapWidth=None, ori=0, 
    color=[1, 1, 1], colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()

presentSet = visual.TextStim(win=win, name='presentSet',
    text='default text',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
presentTarget = visual.TextStim(win=win, name='presentTarget',
    text='default text',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);
presentTarget2 = visual.TextStim(win=win, name='presentTarget2',
    text='default text',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);
presentTarget3 = visual.TextStim(win=win, name='presentTarget3',
    text='default text',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);
presentTarget4 = visual.TextStim(win=win, name='presentTarget4',
    text='default text',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);
presentTarget5 = visual.TextStim(win=win, name='presentTarget5',
    text='default text',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);


# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "mainInstruct"-------
t = 0
mainInstructClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
OK2 = event.BuilderKeyResponse()
# keep track of which components have finished
mainInstructComponents = [instr2, OK2]
for thisComponent in mainInstructComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "mainInstruct"-------
while continueRoutine:
    # get current time
    t = mainInstructClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *instr2* updates
    if t >= 0.0 and instr2.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr2.tStart = t
        instr2.frameNStart = frameN  # exact frame index
        instr2.setAutoDraw(True)

    # *OK2* updates
    if t >= 0.0 and OK2.status == NOT_STARTED:
        # keep track of start time/frame for later
        OK2.tStart = t
        OK2.frameNStart = frameN  # exact frame index
        OK2.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(OK2.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if OK2.status == STARTED:
        theseKeys = event.getKeys()

        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            OK2.keys = theseKeys[-1]  # just the last key pressed
            OK2.rt = OK2.clock.getTime()
            # a response ends the routine
            continueRoutine = False

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in mainInstructComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "mainInstruct"-------
for thisComponent in mainInstructComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if OK2.keys in ['', [], None]:  # No response was made
    OK2.keys = None
thisExp.addData('OK2.keys', OK2.keys)
if OK2.keys != None:  # we had a response
    thisExp.addData('OK2.rt', OK2.rt)
thisExp.nextEntry()
# the Routine "mainInstruct" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='random',
                           extraInfo=expInfo, originPath=-1,
                           trialList=data.importConditions('mainTrialsAlice.xlsx'),
                           seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)

if thisTrial != None:
    for paramName in thisTrial.keys():
        exec (paramName + '= thisTrial.' + paramName)

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec (paramName + '= thisTrial.' + paramName)

    # ------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat


    presentSet.setText(numberSet)
    presentTarget.setText(target[0])
    presentTarget2.setText(target[1])
    presentTarget3.setText(target[2])
    presentTarget4.setText(target[3])
    presentTarget5.setText(target[4])

    resp = event.BuilderKeyResponse()
    # keep track of which components have finished
    trialComponents = [presentSet, presentTarget, presentTarget2, presentTarget3, presentTarget4, presentTarget5, resp]
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    # -------Start Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame


        # *presentSet* updates
        if t >= 1.2 and presentSet.status == NOT_STARTED:
            # keep track of start time/frame for later
            presentSet.tStart = t
            presentSet.frameNStart = frameN  # exact frame index
            presentSet.setAutoDraw(True)
        frameRemains = 1.2 + 1.5 - win.monitorFramePeriod * 0.75  # most of one frame period left
        if presentSet.status == STARTED and t >= frameRemains:
            presentSet.setAutoDraw(False)

        # *presentTarget* updates
        #Target1
        if t >= 4.7 and presentTarget.status == NOT_STARTED:
            presentTarget.tStart = t
            presentTarget.frameNStart = frameN
            presentTarget.setAutoDraw(True)
        frameRemains = 4.7 + 2 - win.monitorFramePeriod * 0.75  # most of one frame period left
        if presentTarget.status == STARTED and t >= frameRemains:
            presentTarget.setAutoDraw(False)
            #Target2
        if t >= 6.7 and presentTarget2.status == NOT_STARTED:
            presentTarget2.tStart = t
            presentTarget2.frameNStart = frameN
            presentTarget2.setAutoDraw(True)
        frameRemains = 6.7 + 2 - win.monitorFramePeriod * 0.75  # most of one frame period left
        if presentTarget2.status == STARTED and t >= frameRemains:
            presentTarget2.setAutoDraw(False)
            #Target3
        if t >= 8.7 and presentTarget3.status == NOT_STARTED:
            presentTarget3.tStart = t
            presentTarget3.frameNStart = frameN
            presentTarget3.setAutoDraw(True)
        frameRemains = 8.7 + 2 - win.monitorFramePeriod * 0.75  # most of one frame period left
        if presentTarget3.status == STARTED and t >= frameRemains:
            presentTarget3.setAutoDraw(False)
            #Target4
        if t >= 10.7 and presentTarget4.status == NOT_STARTED:
            presentTarget4.tStart = t
            presentTarget4.frameNStart = frameN
            presentTarget4.setAutoDraw(True)
        frameRemains = 10.7 + 2 - win.monitorFramePeriod * 0.75  # most of one frame period left
        if presentTarget4.status == STARTED and t >= frameRemains:
            presentTarget4.setAutoDraw(False)
            #Target5
        if t >= 12.7 and presentTarget5.status == NOT_STARTED:
            presentTarget5.tStart = t
            presentTarget5.frameNStart = frameN
            presentTarget5.setAutoDraw(True)
        frameRemains = 12.7 + 2 - win.monitorFramePeriod * 0.75  # most of one frame period left
        if presentTarget5.status == STARTED and t >= frameRemains:
            presentTarget5.setAutoDraw(False)

        # *resp* updates
        if t >= 15.0 and resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            resp.tStart = t
            resp.frameNStart = frameN  # exact frame index
            resp.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(resp.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if resp.status == STARTED:
            theseKeys = event.getKeys(keyList=['left', 'right'])

            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                resp.keys = theseKeys[-1]  # just the last key pressed
                resp.rt = resp.clock.getTime()
                # was this 'correct'?
                if (resp.keys == str(corrAns)) or (resp.keys == corrAns):
                    resp.corr = 1
                else:
                    resp.corr = 0
                # a response ends the routine
                continueRoutine = False

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)

    # check responses
    if resp.keys in ['', [], None]:  # No response was made
        resp.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
            resp.corr = 1  # correct non-response
        else:
            resp.corr = 0  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('resp.keys', resp.keys)
    trials.addData('resp.corr', resp.corr)
    if resp.keys != None:  # we had a response
        trials.addData('resp.rt', resp.rt)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    # ------Prepare to start Routine "feedback"-------
    t = 0
    feedbackClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    if resp.corr:  # stored on last run routine
        msg = "Correct! RT=%.3f" % (resp.rt)
    else:
        msg = "Oops! That was wrong"
    feedback_2.setText(msg)
    # keep track of which components have finished
    feedbackComponents = [feedback_2]
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    # -------Start Routine "feedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedbackClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame


        # *feedback_2* updates
        if t >= 0.0 and feedback_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            feedback_2.tStart = t
            feedback_2.frameNStart = frameN  # exact frame index
            feedback_2.setAutoDraw(True)
        frameRemains = 0.0 + 1.0 - win.monitorFramePeriod * 0.75  # most of one frame period left
        if feedback_2.status == STARTED and t >= frameRemains:
            feedback_2.setAutoDraw(False)

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "feedback"-------
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)

    thisExp.nextEntry()

# completed 1.0 repeats of 'trials'

# get names of stimulus parameters
if trials.trialList in ([], [None], None):
    params = []
else:
    params = trials.trialList[0].keys()
# save data for this loop
trials.saveAsExcel(filename + '.xlsx', sheetName='trials',
                   stimOut=params,
                   dataOut=['n', 'all_mean', 'all_std', 'all_raw'])

    








# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
