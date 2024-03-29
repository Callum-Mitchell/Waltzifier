"""!
Public function and command interface for turning straight- or swing-time 4/4 rhythm audio files into customizable waltz rhythms with minimal sound artifacts.
For best results, input songs must have either a) a known beatmap file (newline-separated beat timing in seconds -- see sample_music example),
or b) a known, steady tempo (in exact beats per minute).
"""

# Imports
import numpy as np
import pyrubberband as pyrb
from sklearn.model_selection import StratifiedShuffleSplit
import soundfile as sf
import sys
import WaltzParams
#Numerical constants
_ONEF                = float(1.0)
_TWOF                = float(2.0)

_ONE_HALF            = float(0.5)

_ONE_THIRD           = float(1.0/3.0)
_TWO_THIRDS          = float(2.0/3.0)
_FOUR_THIRDS         = float(4.0/3.0)

_SECONDS_PER_MINUTEF = float(60.0)
_MS_PER_SECOND       = float(1000.0)

def _appendTargetSampleMapping(timeMap, sampleOffset, waltzedSampleOffset, numSamples, globalSampleIdx, beatSampleLength, targetInSampleBeatDist, outputTimeStretch):
    """! Conveneince function used by getxxxBeatxxxTimeMap* to add a sample time mapping entry and update sample buffer position
    @param timeMap: the time mapping to append
    @param sampleOffset: the current input sample index within the local sample region
    @param waltzedSampleOffset: the current output sample index within the local sample region
    @param numSamples: the sample count within the local sample region
    @param globalSampleIndex: the initial sample index of the local sample region within the full input file
    @param beatSampleLength: the number of samples per beat in the input audio
    @param targetInSampleBeatDist: the number of beats between the current sample offset and the next target input sample position
    @param outputTimeStretch: time stretch factor in the output versus input audio between the current and next target samples 
    """

    globalSampleOffset        = globalSampleIdx + sampleOffset
    globalWaltzedSampleOffset = globalSampleIdx + waltzedSampleOffset

    nextTargetSmplDist        = min(round(beatSampleLength * targetInSampleBeatDist), numSamples - sampleOffset)
    nextTargetWaltzedSmplDist = nextTargetSmplDist * outputTimeStretch

    nextTargetGlobalSmpl        = globalSampleOffset + nextTargetSmplDist
    nextTargetWaltzedGlobalSmpl = globalWaltzedSampleOffset + nextTargetWaltzedSmplDist

    sampleOffset += nextTargetSmplDist
    waltzedSampleOffset += nextTargetWaltzedSmplDist

    return np.append(timeMap, [[nextTargetGlobalSmpl, nextTargetWaltzedGlobalSmpl]], axis=0), sampleOffset, waltzedSampleOffset

def _getStraightBeatPairTimeMap(inSamples, globalSampleIdx, beatSampleLength):
    """! Take 2 beats worth of straight-beat input samples and return straight-to-waltzified time mapping
    @param inSamples: 2-beat section of input track samples - should be of length 2*beatSampleLength, or less at the end of an input sample set
    @param globalSampleIdx: the global sample offset of the first sample in inSamples
    @param beatSampleLength: the number of audo samples per beat of the input track
    """

    timeMap = np.empty((0, 2), int)
    numSamples = len(inSamples)
    sampleOffset = 0
    waltzedSampleOffset = 0

    #Stretch the first (up to) 1/2 beat to (up to) 2/3 of a beat
    if(sampleOffset < numSamples):
        timeMap, sampleOffset, waltzedSampleOffset = _appendTargetSampleMapping(
            timeMap, sampleOffset, waltzedSampleOffset, numSamples, globalSampleIdx, beatSampleLength, _ONE_HALF, _FOUR_THIRDS
        )
    #Condense the next (up to) 1 beat to (up to) 2/3 of a beat
    if(sampleOffset < numSamples):
        timeMap, sampleOffset, waltzedSampleOffset = _appendTargetSampleMapping(
            timeMap, sampleOffset, waltzedSampleOffset, numSamples, globalSampleIdx, beatSampleLength, _ONEF,     _TWO_THIRDS
        )
    #Stretch the last (up to) 1/2 beat to (up to) 2/3 of a beat
    if(sampleOffset < numSamples):
        timeMap, sampleOffset, waltzedSampleOffset = _appendTargetSampleMapping(
            timeMap, sampleOffset, waltzedSampleOffset, numSamples, globalSampleIdx, beatSampleLength, _ONE_HALF, _FOUR_THIRDS
        )

    return timeMap

def _getStraightBeatQuadTimeMapHT(inSamples, globalSampleIdx, beatSampleLength):
    """! Take 4 beats worth of straight-beat input samples and return straight-to-half-time-waltzified time mapping
    @param inSamples: 4-beat section of input track samples - should be of length 4*beatSampleLength, or less at the end of an input sample set
    @param globalSampleIdx: the global sample offset of the first sample in inSamples
    @param beatSampleLength: the number of audo samples per beat of the input track
    """

    timeMap = np.empty((0, 2), int)
    numSamples = len(inSamples)
    sampleOffset = 0
    waltzedSampleOffset = 0

    #Stretch the first (up to) 1 beat to (up to) 4/3 of a beat
    if(sampleOffset < numSamples):
        timeMap, sampleOffset, waltzedSampleOffset = _appendTargetSampleMapping(
            timeMap, sampleOffset, waltzedSampleOffset, numSamples, globalSampleIdx, beatSampleLength, _ONEF, _FOUR_THIRDS
        )
    #Condense the next (up to) 2 beats to (up to) 4/3 of a beat
    if(sampleOffset < numSamples):
        timeMap, sampleOffset, waltzedSampleOffset = _appendTargetSampleMapping(
            timeMap, sampleOffset, waltzedSampleOffset, numSamples, globalSampleIdx, beatSampleLength, _TWOF, _TWO_THIRDS
        )
    #Stretch the last (up to) 1 beat to (up to) 4/3 of a beat
    if(sampleOffset < numSamples):
        timeMap, sampleOffset, waltzedSampleOffset = _appendTargetSampleMapping(
            timeMap, sampleOffset, waltzedSampleOffset, numSamples, globalSampleIdx, beatSampleLength, _ONEF, _FOUR_THIRDS
        )

    return timeMap

def _getSwingBeatPairTimeMap(inSamples, globalSampleIdx, beatSampleLength):
    """! Take 2 beats worth of swing-beat input samples and return swing-to-waltzified time mapping
    @param inSamples: 2-beat section of input track samples - should be of length 2*beatSampleLength, or less at the end of an input sample set
    @param globalSampleIdx: the global sample offset of the first sample in inSamples
    @param beatSampleLength: the number of audo samples per beat of the input track
    """

    timeMap = np.empty((0, 2), int)
    numSamples = len(inSamples)
    sampleOffset = 0
    waltzedSampleOffset = 0

    #Leave the first (up to) 1 beat unchanged
    if(sampleOffset < numSamples):
        timeMap, sampleOffset, waltzedSampleOffset = _appendTargetSampleMapping(
            timeMap, sampleOffset, waltzedSampleOffset, numSamples, globalSampleIdx, beatSampleLength, _ONEF,       _ONEF
        )
    #Condense the next (up to) 2/3 of a beat to (up to) 1/3 of a beat
    if(sampleOffset < numSamples):
         timeMap, sampleOffset, waltzedSampleOffset = _appendTargetSampleMapping(
            timeMap, sampleOffset, waltzedSampleOffset, numSamples, globalSampleIdx, beatSampleLength, _TWO_THIRDS, _ONE_HALF
        )
   #Stretch the last (up to) 1/3 beat to (up to) 2/3 of a beat
    if(sampleOffset < numSamples):
        timeMap, sampleOffset, waltzedSampleOffset = _appendTargetSampleMapping(
            timeMap, sampleOffset, waltzedSampleOffset, numSamples, globalSampleIdx, beatSampleLength, _ONE_THIRD,  _TWOF
        )

    return timeMap

def _getSwingBeatQuadTimeMapHT(inSamples, globalSampleIdx, beatSampleLength):
    """! Take 4 beats worth of swing-beat input samples and return swing-to-waltzified time mapping
    @param inSamples: 4-beat section of input track samples - should be of length 4*beatSampleLength, or less at the end of an input sample set
    @param globalSampleIdx: the global sample offset of the first sample in inSamples
    @param beatSampleLength: the number of audo samples per beat of the input track
    """

    timeMap = np.empty((0, 2), int)
    numSamples = len(inSamples)
    sampleOffset = 0
    waltzedSampleOffset = 0

    #Leave the first (up to) 2/3 of a beat unchanged
    if(sampleOffset < numSamples):
        timeMap, sampleOffset, waltzedSampleOffset = _appendTargetSampleMapping(
            timeMap, sampleOffset, waltzedSampleOffset, numSamples, globalSampleIdx, beatSampleLength, _TWO_THIRDS, _ONEF
        )
    #Stretch the next (up to) 1/3 of a beat to (up to) 2/3 of a beat
    if(sampleOffset < numSamples):
        timeMap, sampleOffset, waltzedSampleOffset = _appendTargetSampleMapping(
            timeMap, sampleOffset, waltzedSampleOffset, numSamples, globalSampleIdx, beatSampleLength, _ONE_THIRD,  _TWOF
        )
    #Condense the next (up to) 2/3 beat to (up to) 1/3 of a beat
    if(sampleOffset < numSamples):
        timeMap, sampleOffset, waltzedSampleOffset = _appendTargetSampleMapping(
            timeMap, sampleOffset, waltzedSampleOffset, numSamples, globalSampleIdx, beatSampleLength, _TWO_THIRDS, _ONE_HALF
        )
    #Leave the next (up to) 1/3 beat unchanged
    if(sampleOffset < numSamples):
        timeMap, sampleOffset, waltzedSampleOffset = _appendTargetSampleMapping(
            timeMap, sampleOffset, waltzedSampleOffset, numSamples, globalSampleIdx, beatSampleLength, _ONE_THIRD,  _ONEF
        )
    #Condense the next (up to) 2/3 beat to (up to) 1/3 of a beat
    if(sampleOffset < numSamples):
        timeMap, sampleOffset, waltzedSampleOffset = _appendTargetSampleMapping(
            timeMap, sampleOffset, waltzedSampleOffset, numSamples, globalSampleIdx, beatSampleLength, _TWO_THIRDS, _ONE_HALF
        )
    #Leave the next (up to) 1 beat unchanged
    if(sampleOffset < numSamples):
        timeMap, sampleOffset, waltzedSampleOffset = _appendTargetSampleMapping(
            timeMap, sampleOffset, waltzedSampleOffset, numSamples, globalSampleIdx, beatSampleLength, _ONEF,       _ONEF
        )
    #Stretch the last (up to) 1/3 of a beat to (up to) 2/3 of a beat
    if(sampleOffset < numSamples):
        timeMap, sampleOffset, waltzedSampleOffset = _appendTargetSampleMapping(
            timeMap, sampleOffset, waltzedSampleOffset, numSamples, globalSampleIdx, beatSampleLength, _ONE_THIRD,  _TWOF
        )

    return timeMap

def waltzifyFile(waltzParams: WaltzParams):
    """! Procedurally time-stretches an audio file from a straight/swing rhythm to a waltz rhythm
    @param waltzParams: configuration for waltz settings
    """
    #Input samples
    inSamples, sr = sf.read(waltzParams.inFilePath)
    if len(inSamples) == 0:
        print("Unable to read audio file: " + waltzParams.inFilePath)
        exit()

    
    beatDelaySamples = round(sr * (waltzParams.beatDelayMs / _MS_PER_SECOND))
    currentSampleIdx = beatDelaySamples

    #Output file properties
    if not waltzParams.outFilePath:
        #Split input directory and file name
        inDirectory, splitter, inFileName = waltzParams.inFilePath.replace("\\", "/").rpartition("/")
        waltzParams.outFilePath = inDirectory + splitter + 'waltz'
        if waltzParams.ht:
            waltzParams.outFilePath += 'ht'
    
        waltzParams.outFilePath += '_' + inFileName
        pathNoExt, period, _ = waltzParams.outFilePath.rpartition(".")
        waltzParams.outFilePath = pathNoExt + period + 'wav'
    
    #Sorted ordering needed for waltz timeswitching/rhythmswitching to work
    waltzParams.timeSwitchBeats.sort(reverse=True)
    waltzParams.rhythmSwitchBeats.sort(reverse=True)

    #Parse custom beat samples if available
    customBeatSamples = []
    if len(waltzParams.beatmapFile) > 0:
        fBeatmap = open(waltzParams.beatmapFile)
        if fBeatmap:
            for line in fBeatmap.read().split('\n'):
                beatTimestamp = float(line)
                customBeatSamples.append(round(beatTimestamp * sr))
        else:
            print("Warning: could not open custom beatmap file " + waltzParams.beatmapFile + ". Falling back on BPM.")

    #Create map from input to output sample timestamps
    waltzSampleTimeMap = np.empty((0, 2), int)
    waltzSampleTimeMap = np.append(waltzSampleTimeMap, [[0, 0]], axis=0)

    #Handle beat sync offset
    if currentSampleIdx > 0:
        waltzSampleTimeMap = np.append(waltzSampleTimeMap, [[currentSampleIdx, currentSampleIdx]], axis=0)

    lastBPM = float(0.0)
    currentBeatIdx = 0
    #NEW: work through the file 2 (or 4 for half time) beats at a time and call waltzifying functions
    while(currentSampleIdx < len(inSamples)):
        beatsPerWaltzSegment = 4 if waltzParams.ht else 2

        #Estimate beat sample length from either BPM or custom beat mapping
        beatSampleLength = 0
        if len(customBeatSamples) - 1 > currentBeatIdx:
            remainingCustomBeatPoints = min(beatsPerWaltzSegment, len(customBeatSamples) - 1 - currentBeatIdx) #Not including current beat point
            beatSampleLength = (customBeatSamples[currentBeatIdx + remainingCustomBeatPoints] \
                             - customBeatSamples[currentBeatIdx]) \
                             / remainingCustomBeatPoints
        elif lastBPM > 0.0:
            beatSampleLength = float(sr * _SECONDS_PER_MINUTEF / lastBPM)
        elif waltzParams.bpm > 0.0:
            beatSampleLength = float(sr * _SECONDS_PER_MINUTEF / waltzParams.bpm)
        else:
            print("Error: no valid BPM nor beatmaps available to waltzify file")
            exit()

        nextBeatSetSampleIdx = round(currentSampleIdx + (beatsPerWaltzSegment * beatSampleLength))
        currentBeatPairInSamples = inSamples[max(0, currentSampleIdx):nextBeatSetSampleIdx]
        if waltzParams.sw:
            if waltzParams.ht:
                waltzSampleTimeMap = np.append(waltzSampleTimeMap, _getSwingBeatQuadTimeMapHT(   currentBeatPairInSamples, currentSampleIdx, beatSampleLength), axis=0)
            else:
                waltzSampleTimeMap = np.append(waltzSampleTimeMap, _getSwingBeatPairTimeMap(     currentBeatPairInSamples, currentSampleIdx, beatSampleLength), axis=0)
        else:
            if waltzParams.ht:
                waltzSampleTimeMap = np.append(waltzSampleTimeMap, _getStraightBeatQuadTimeMapHT(currentBeatPairInSamples, currentSampleIdx, beatSampleLength), axis=0)
            else:        
                waltzSampleTimeMap = np.append(waltzSampleTimeMap, _getStraightBeatPairTimeMap(  currentBeatPairInSamples, currentSampleIdx, beatSampleLength), axis=0)
        #Go to next beat index
        currentBeatIdx += beatsPerWaltzSegment
        currentSampleIdx = nextBeatSetSampleIdx

        #Store the last BPM estimate to use as a backup value in case custom beatmap runs out
        lastBPM = sr * _SECONDS_PER_MINUTEF / beatSampleLength 
        #Switch between full/half time if applicable
        if len(waltzParams.timeSwitchBeats) != 0 and waltzParams.timeSwitchBeats[-1] <= currentBeatIdx:
            waltzParams.ht = not waltzParams.ht
            waltzParams.timeSwitchBeats.pop(-1)

        #Switch between straight/swing input handling if applicable
        if len(waltzParams.rhythmSwitchBeats) != 0 and waltzParams.rhythmSwitchBeats[-1] <= currentBeatIdx:
            waltzParams.sw = not waltzParams.sw
            waltzParams.rhythmSwitchBeats.pop(-1)

    #Using the final time map, stretch the whole song at once
    outSamples = pyrb.pyrb.timemap_stretch(inSamples, sr, waltzSampleTimeMap)
    
    #Write the final .wav file
    sf.write(waltzParams.outFilePath, outSamples, sr, format='wav')
    print('Successfully wrote to ' + waltzParams.outFilePath)

def main():
    """! Main program entry; provides command interface for song waltzification"""
    args = sys.argv[1:]
    if len(args) < 2:
        print("Usage: walzifier.py infile [-bpm bpm] [-beatmap filepath] [sw] [ht] [-delay beatdelayms] [-out outfile] [-tsb timeswitchbeat] [-rsb rhythmswitchbeat]\n")
        print("infile: input audio file path")
        print("-bpm: specify song tempo in beats per minute. Required unless using a custom beatmap")
        print("-beatmap: path to custom beatmap text file (should list newline-separated beat points in seconds). *This will override bpm*")
        print("sw: use to indicate the input has a swing rhythm")
        print("ht: use to produce a half-time waltz rhythm (4 beats/measure instead of 2)")
        print("-delay: specify delay in milliseconds before the first beat; use if the timing/rhythm sounds off\n")
        print("-out: specify a custom output file path (.wav recommended). Default is \"waltz\" [+ \"ht\"] + \"_\" + <input file name (.wav converted)> in the current directory")
        print("-tsb: specify a beat on which to switch between half- and full-time waltz (can specify multiple)")
        print("-rsb: specify a beat on which to switch between straight- and swing-rhythm input handling (can specify multiple)")
        print("\nExamples:")
        print("python Waltzifier.py \"./sample_music/HoliznaCC0 - Rising Hero.ogg\" -bpm 120 -delay 10 -out \"./sample_music/HoliznaCC0 - Rising Hero - Waltzified.wav\"")
        print("python Waltzifier.py \"./sample_music/HoliznaCC0 - Coins.ogg\" -bpm 80 -delay 10")
        print("python Waltzifier.py \"./sample_music/HoliznaCC0 - Night Driving.ogg\" -bpm 95 -delay 20 ht")
        exit()

    inFilePath = args[0]
    outFilePath = ""
    bpm = float(-1.0)
    sw = False
    ht = False
    beatDelayMs = 0
    i = 1
    timeSwitchBeats = []
    rhythmSwitchBeats = []
    customBeatmapFile = ""

    while i < len(args):
        arg = args[i]
        if arg == "sw":
            sw = True
            print("Swing mode activated!")
            i += 1

        elif arg == "ht":
            ht = True
            print("Half-time waltz")
            i += 1

        elif arg == "-out":
            if i == len(args) - 1:
                print("Error: -out option must be followed by an output file path")
                exit()
            outFilePath = args[i+1]
            i += 2

        elif arg == "-bpm":
            if i == len(args) - 1:
                print("Error: -bpm option must be followed by a number (tempo in beats per minute)")
                exit()
            bpm = float(args[i+1])
            if(bpm <= float(0.0)):
                print("Error: bpm must be a positive number")
                exit()
            i += 2

        elif arg == "-delay":
            if i == len(args) - 1:
                print("Error: -delay option must be followed by a number (beat delay in milliseconds)")    
            beatDelayMs = int(args[i+1])
            print("Beat delay of " + str(beatDelayMs) + "ms applied")
            i += 2

        elif arg == "-tsb":
            if i == len(args) - 1 or not int(args[i+1]):
                print("Error: -tsb option must be followed by a number (beat on which to switch half/full time)")
                exit()
            timeSwitchBeats.append(int(args[i+1]))
            i += 2

        elif arg == "-rsb":
            if i == len(args) - 1:
                print("Error: -rsb option must be followed by a number (beat on which input rhythm changes)")
                exit()
            rhythmSwitchBeats.append(int(args[i+1]))
            i += 2

        elif arg == "-beatmap":
            if i == len(args) - 1:
                print("Error: -beatmap option must be followed by a beatmap file path")
                exit()
            customBeatmapFile = args[i+1]
            i += 2

        else:
            print("Warning: unrecognized argument \"" + arg + "\"")
            i += 1
    
    if not bpm and not customBeatmapFile:
        print("Error: either BPM or beatmap file is required")
        exit()
    waltzParams = WaltzParams.WaltzParams(inFilePath, bpm, sw, ht, beatDelayMs, outFilePath, timeSwitchBeats, rhythmSwitchBeats, customBeatmapFile)
    print("Performing walzification")
    waltzifyFile(waltzParams)
    exit()

if __name__=="__main__":
    main()
