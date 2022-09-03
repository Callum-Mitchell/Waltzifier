from colorsys import TWO_THIRD
import numpy as np
import pyrubberband as pyrb
import pyogg
import soundfile as sf #For creating output files
import sys
import wave

#Numerical constants
ONEF   = float(1.0)
TWOF   = float(2.0)

ONE_HALF       = float(0.5)
THREE_HALVES   = float(1.5)

ONE_THIRD      = float(1.0/3.0)
TWO_THIRDS     = float(2.0/3.0)
FOUR_THIRDS    = float(4.0/3.0)

SECONDS_PER_MINUTEF = float(60.0)
MS_PER_SECOND       = float(1000.0)

#TODOS:
#Allow user to specify custom output file name

#Conveneince function used by getxxxBeatxxxTimeMap to add a sample time mapping entry and update sample buffer position
# @timeMap: the time mapping to append
# @sampleOffset: the current input sample index within the local sample region
# @waltzedSampleOffset: the current output sample index within the local sample region
# @numSamples: the sample count within the local sample region
# @globalSampleIndex: the initial sample index of the local sample region within the full input file
# @beatSampleLength: the number of samples per beat in the input audio
# @targetInSampleBeatDist: the number of beats between the current sample offset and the next target input sample position
# @outputTimeStretch: time stretch factor in the output versus input audio between the current and next target samples 
def appendTargetSampleMapping(timeMap, sampleOffset, waltzedSampleOffset, numSamples, globalSampleIdx, beatSampleLength, targetInSampleBeatDist, outputTimeStretch):
    globalSampleOffset = globalSampleIdx + sampleOffset
    globalWaltzedSampleOffset = globalSampleIdx + waltzedSampleOffset

    nextTargetSmplDist        = min(round(beatSampleLength * targetInSampleBeatDist), numSamples - sampleOffset)
    nextTargetWaltzedSmplDist = nextTargetSmplDist * outputTimeStretch

    nextTargetGlobalSmpl        = globalSampleOffset + nextTargetSmplDist
    nextTargetWaltzedGlobalSmpl = globalWaltzedSampleOffset + nextTargetWaltzedSmplDist

    sampleOffset += nextTargetSmplDist
    waltzedSampleOffset += nextTargetWaltzedSmplDist

    return np.append(timeMap, [[nextTargetGlobalSmpl, nextTargetWaltzedGlobalSmpl]], axis=0), sampleOffset, waltzedSampleOffset


#Take 2 beats worth of straight-beat input samples and return straight-to-waltzified time mapping
# @inSamples: 2-beat section of input track samples - should be of length 2*beatSampleLength, or less at the end of an input sample set
# @globalSampleIdx: the index of the first sample in the global buffer
# @beatSampleLength: the number of audo samples per beat of the input track
def getStraightBeatPairTimeMap(inSamples, globalSampleIdx, beatSampleLength):

    timeMap = np.empty((0, 2), int)
    numSamples = len(inSamples)
    sampleOffset = 0
    waltzedSampleOffset = 0

    #Stretch the first (up to) 1/2 beat to (up to) 2/3 of a beat
    if(sampleOffset < numSamples):
        timeMap, sampleOffset, waltzedSampleOffset = appendTargetSampleMapping(
            timeMap, sampleOffset, waltzedSampleOffset, numSamples, globalSampleIdx, beatSampleLength, ONE_HALF, FOUR_THIRDS
        )
    #Condense the next (up to) 1 beat to (up to) 2/3 of a beat
    if(sampleOffset < numSamples):
        timeMap, sampleOffset, waltzedSampleOffset = appendTargetSampleMapping(
            timeMap, sampleOffset, waltzedSampleOffset, numSamples, globalSampleIdx, beatSampleLength, ONEF, TWO_THIRDS
        )
    #Stretch the last (up to) 1/2 beat to (up to) 2/3 of a beat
    if(sampleOffset < numSamples):
        timeMap, sampleOffset, waltzedSampleOffset = appendTargetSampleMapping(
            timeMap, sampleOffset, waltzedSampleOffset, numSamples, globalSampleIdx, beatSampleLength, ONE_HALF, FOUR_THIRDS
        )

    return timeMap

#Take 4 beats worth of straight-beat input samples and return straight-to-half-time-waltzified time mapping
# @inSamples: 4-beat section of input track samples - should be of length 4*beatSampleLength, or less at the end of an input sample set
# @globalSampleIdx: the index of the first sample in the global buffer
# @beatSampleLength: the number of audo samples per beat of the input track
def getStraightBeatQuadTimeMapHT(inSamples, globalSampleIdx, beatSampleLength):

    timeMap = np.empty((0, 2), int)
    numSamples = len(inSamples)
    sampleOffset = 0
    waltzedSampleOffset = 0

    #Stretch the first (up to) 1 beat to (up to) 4/3 of a beat
    if(sampleOffset < numSamples):
        timeMap, sampleOffset, waltzedSampleOffset = appendTargetSampleMapping(
            timeMap, sampleOffset, waltzedSampleOffset, numSamples, globalSampleIdx, beatSampleLength, ONEF, FOUR_THIRDS
        )
    #Condense the next (up to) 2 beats to (up to) 4/3 of a beat
    if(sampleOffset < numSamples):
        timeMap, sampleOffset, waltzedSampleOffset = appendTargetSampleMapping(
            timeMap, sampleOffset, waltzedSampleOffset, numSamples, globalSampleIdx, beatSampleLength, TWOF, TWO_THIRDS
        )
    #Stretch the last (up to) 1 beat to (up to) 4/3 of a beat
    if(sampleOffset < numSamples):
        timeMap, sampleOffset, waltzedSampleOffset = appendTargetSampleMapping(
            timeMap, sampleOffset, waltzedSampleOffset, numSamples, globalSampleIdx, beatSampleLength, ONEF, FOUR_THIRDS
        )

    return timeMap

#Take 2 beats worth of swing-beat input samples and return swing-to-waltzified time mapping
# @inSamples: 2-beat section of input track samples - should be of length 2*beatSampleLength, or less at the end of an input sample set
# @globalSampleIdx: the index of the first sample in the global buffer
# @beatSampleLength: the number of audo samples per beat of the input track
def getSwingBeatPairTimeMap(inSamples, globalSampleIdx, beatSampleLength):

    timeMap = np.empty((0, 2), int)
    numSamples = len(inSamples)
    sampleOffset = 0
    waltzedSampleOffset = 0

    #Leave the first (up to) 1 beat unchanged
    if(sampleOffset < numSamples):
        timeMap, sampleOffset, waltzedSampleOffset = appendTargetSampleMapping(
            timeMap, sampleOffset, waltzedSampleOffset, numSamples, globalSampleIdx, beatSampleLength, ONEF, ONEF
        )
    #Condense the next (up to) 2/3 of a beat to (up to) 1/3 of a beat
    if(sampleOffset < numSamples):
         timeMap, sampleOffset, waltzedSampleOffset = appendTargetSampleMapping(
            timeMap, sampleOffset, waltzedSampleOffset, numSamples, globalSampleIdx, beatSampleLength, TWO_THIRDS, ONE_HALF
        )
   #Stretch the last (up to) 1/3 beat to (up to) 2/3 of a beat
    if(sampleOffset < numSamples):
        timeMap, sampleOffset, waltzedSampleOffset = appendTargetSampleMapping(
            timeMap, sampleOffset, waltzedSampleOffset, numSamples, globalSampleIdx, beatSampleLength, ONE_THIRD, TWOF
        )

    return timeMap

#Take 4 beats worth of swing-beat input samples and return swing-to-waltzified time mapping
# @inSamples: 4-beat section of input track samples - should be of length 4*beatSampleLength, or less at the end of an input sample set
# @globalSampleIdx: the index of the first sample in the global buffer
# @beatSampleLength: the number of audo samples per beat of the input track
def getSwingBeatQuadTimeMapHT(inSamples, globalSampleIdx, beatSampleLength):

    timeMap = np.empty((0, 2), int)
    numSamples = len(inSamples)
    sampleOffset = 0
    waltzedSampleOffset = 0

    #Leave the first (up to) 2/3 of a beat unchanged
    if(sampleOffset < numSamples):
        timeMap, sampleOffset, waltzedSampleOffset = appendTargetSampleMapping(
            timeMap, sampleOffset, waltzedSampleOffset, numSamples, globalSampleIdx, beatSampleLength, TWO_THIRDS, ONEF
        )
    #Stretch the next (up to) 1/3 of a beat to (up to) 2/3 of a beat
    if(sampleOffset < numSamples):
        timeMap, sampleOffset, waltzedSampleOffset = appendTargetSampleMapping(
            timeMap, sampleOffset, waltzedSampleOffset, numSamples, globalSampleIdx, beatSampleLength, ONE_THIRD, TWOF
        )
    #Condense the next (up to) 2/3 beat to (up to) 1/3 of a beat
    if(sampleOffset < numSamples):
        timeMap, sampleOffset, waltzedSampleOffset = appendTargetSampleMapping(
            timeMap, sampleOffset, waltzedSampleOffset, numSamples, globalSampleIdx, beatSampleLength, TWO_THIRDS, ONE_HALF
        )
    #Leave the next (up to) 1/3 beat unchanged
    if(sampleOffset < numSamples):
        timeMap, sampleOffset, waltzedSampleOffset = appendTargetSampleMapping(
            timeMap, sampleOffset, waltzedSampleOffset, numSamples, globalSampleIdx, beatSampleLength, ONE_THIRD, ONEF
        )
    #Condense the next (up to) 2/3 beat to (up to) 1/3 of a beat
    if(sampleOffset < numSamples):
        timeMap, sampleOffset, waltzedSampleOffset = appendTargetSampleMapping(
            timeMap, sampleOffset, waltzedSampleOffset, numSamples, globalSampleIdx, beatSampleLength, TWO_THIRDS, ONE_HALF
        )
    #Leave the next (up to) 1 beat unchanged
    if(sampleOffset < numSamples):
        timeMap, sampleOffset, waltzedSampleOffset = appendTargetSampleMapping(
            timeMap, sampleOffset, waltzedSampleOffset, numSamples, globalSampleIdx, beatSampleLength, ONEF, ONEF
        )
    #Stretch the last (up to) 1/3 of a beat to (up to) 2/3 of a beat
    if(sampleOffset < numSamples):
        timeMap, sampleOffset, waltzedSampleOffset = appendTargetSampleMapping(
            timeMap, sampleOffset, waltzedSampleOffset, numSamples, globalSampleIdx, beatSampleLength, ONE_THIRD, TWOF
        )

    return timeMap

def fileWaltzifier(inputFileName, bpm, sw, ht, beatDelayMS):

    #Input samples
    inSamples, sr = sf.read(inputFileName)
    if(len(inSamples) == 0):
        print("Unable to read audio file: " + inputFileName)
        exit()

    
    currentBeatPairIdx = 0
    beatDelaySamples = round(sr * (beatDelayMS / MS_PER_SECOND))
    currentSampleIdx = beatDelaySamples

    #Output file properties
    outFileName = 'waltz'
    if ht:
        outFileName += 'ht'
    
    outFileName += '_' + inputFileName

    #Create map from input to output sample timestamps
    waltzSampleTimeMap = np.empty((0, 2), int)
    waltzSampleTimeMap = np.append(waltzSampleTimeMap, [[0, 0]], axis=0)

    #Handle beat sync offset
    if(currentSampleIdx > 0):
        waltzSampleTimeMap = np.append(waltzSampleTimeMap, [[currentSampleIdx, currentSampleIdx]], axis=0)

    beatSampleLength = float(sr * SECONDS_PER_MINUTEF / bpm)
    beatsPerWaltzSegment = 4 if ht else 2

    #NEW: work through the file 2 (or 4 for half time) beats at a time and call waltzifying functions
    while(currentSampleIdx < len(inSamples)):
        nextBeatSetSampleIdx = round((currentBeatPairIdx + 1) * beatsPerWaltzSegment * beatSampleLength) + beatDelaySamples
        currentBeatPairInSamples = inSamples[max(0, currentSampleIdx):nextBeatSetSampleIdx]
        if(sw):
            if(ht):
                waltzSampleTimeMap = np.append(waltzSampleTimeMap, getSwingBeatQuadTimeMapHT(   currentBeatPairInSamples, currentSampleIdx, beatSampleLength), axis=0)
            else:
                waltzSampleTimeMap = np.append(waltzSampleTimeMap, getSwingBeatPairTimeMap(     currentBeatPairInSamples, currentSampleIdx, beatSampleLength), axis=0)
        else:
            if(ht):
                waltzSampleTimeMap = np.append(waltzSampleTimeMap, getStraightBeatQuadTimeMapHT(currentBeatPairInSamples, currentSampleIdx, beatSampleLength), axis=0)
            else:        
                waltzSampleTimeMap = np.append(waltzSampleTimeMap, getStraightBeatPairTimeMap(  currentBeatPairInSamples, currentSampleIdx, beatSampleLength), axis=0)
        #Go to next beat index
        currentBeatPairIdx += 1
        currentSampleIdx = nextBeatSetSampleIdx
    
    #Using the final time map, stretch the whole song at once
    outSamples = pyrb.pyrb.timemap_stretch(inSamples, sr, waltzSampleTimeMap)
    
    sf.write(outFileName, outSamples, sr, format='wav')
    print('Successfully wrote to ' + outFileName)


def main():
    print(sf.__libsndfile_version__)
    args = sys.argv[1:]
    if len(args) < 2:
        print("Usage: walzifier.py infile bpm [sw, ht, beatdelay]\n")
        print("infile: input file name (.ogg)")
        print("bpm: speed of song in beats per minute")
        print("sw: use to indicate the input has a swing rhythm")
        print("ht: use to produce a half-time waltz rhythm (4 beats/measure instead of 2)")
        print("beatdelay: delay in milliseconds before the first beat; use if the timing/rhythm sounds off\n")
        print("Example: waltzifier.py zone_1_3.ogg 140")
        print("Example: waltzifier.py zone_2_3.ogg 150 ht sw 0\n")
        exit()

    inFileName = args[0]
    bpm = int(args[1])
    if(bpm <= 0):
        print("BPM must be greater than 0")
        exit()
    
    sw = False
    ht = False
    beatDelayMS = 0
    for arg in args[2:]:
        if(str(arg) == "sw"):
            sw = True
            print("Swing mode activated!")
        elif(str(arg) == "ht"):
            ht = True
            print("Half-time waltz")
        elif(int(arg) != 0):
            beatDelayMS = int(arg)
            print("Beat delay of " + str(beatDelayMS) + "ms applied")

    fileWaltzifier(inFileName, bpm, sw, ht, beatDelayMS)

    


if __name__=="__main__":
    main()
