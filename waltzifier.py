from colorsys import TWO_THIRD
import numpy as np
import pyrubberband as pyrb
import pyogg
import soundfile as sf #For creating output files
import sys
import wave

TWO_THIRDS     = float(2.0/3.0)
THREE_QUARTERS = float(3.0/4.0)
THREE_HALVES   = float(3.0/2.0)
FIVE_THIRDS    = float(5.0/3.0)
EIGHT_THIRDS   = float(8.0/3.0)
ELEVEN_THIRDS  = float(11.0/3.0)

HALFF  = float(0.5)
ONEF   = float(1.0)
TWOF   = float(2.0)
THREEF = float(3.0)

SECONDS_PER_MINUTEF = float(60.0)
MS_PER_SECOND       = float(1000.0)

#Take 2 beats worth of straight-beat input samples and waltzify the rhythm
#inSamples should be of length 2*beatSampleLength, except at the end of a file/channel
def waltzifyStraightBeatPair(inSamples, beatSampleLength, sr):
    numSamples          = len(inSamples)
    halfBeatSmpl        = min(round(beatSampleLength*HALFF       ), numSamples)
    threeHalvesBeatSmpl = min(round(beatSampleLength*THREE_HALVES), numSamples)

    outSamples = np.empty((0, 2), float)
    if(0 < numSamples):
        outSamples = np.append(outSamples, pyrb.pyrb.time_stretch(inSamples[0                  :halfBeatSmpl+1       ], sr, THREE_QUARTERS), axis=0)
    if(halfBeatSmpl < numSamples):
        outSamples = np.append(outSamples, pyrb.pyrb.time_stretch(inSamples[halfBeatSmpl       :threeHalvesBeatSmpl+1], sr, THREE_HALVES  ), axis=0)
    if(threeHalvesBeatSmpl < numSamples):
        outSamples = np.append(outSamples, pyrb.pyrb.time_stretch(inSamples[threeHalvesBeatSmpl:numSamples+1         ], sr, THREE_QUARTERS), axis=0)

    #outSamples = outSamples[0:len(inSamples)]
    return outSamples

#Take 4 beats worth of straight-beat input samples and half-time waltzify the rhythm at
#inSamples should be of length 2*beatSampleLength, except at the end of a file/channel
def waltzifyStraightBeatQuadHT(inSamples, beatSampleLength, sr):
    numSamples    = len(inSamples)
    fullBeatSmpl  = min(round(beatSampleLength       ), numSamples)
    threeBeatSmpl = min(round(beatSampleLength*THREEF), numSamples)

    outSamples = np.empty((0, 2), float)
    if(0 < numSamples):
        outSamples = np.append(outSamples, pyrb.pyrb.time_stretch(inSamples[0            :fullBeatSmpl ], sr, THREE_QUARTERS), axis=0)
    if(fullBeatSmpl < numSamples):
        outSamples = np.append(outSamples, pyrb.pyrb.time_stretch(inSamples[fullBeatSmpl :threeBeatSmpl], sr, THREE_HALVES  ), axis=0)
    if(threeBeatSmpl < numSamples):
        outSamples = np.append(outSamples, pyrb.pyrb.time_stretch(inSamples[threeBeatSmpl:numSamples   ], sr, THREE_QUARTERS), axis=0)

    #outSamples = outSamples[0:len(inSamples)]
    return outSamples

#Take 2 beats worth of swing-beat input samples and waltzify the rhythm
#inSamples should be of length 2*beatSampleLength, except at the end of a file/channel
def waltzifySwingBeatPair(inSamples, beatSampleLength, sr):
    numSamples         = len(inSamples)
    fullBeatSmpl       = min(round(beatSampleLength            ), numSamples)
    fiveThirdsBeatSmpl = min(round(beatSampleLength*FIVE_THIRDS), numSamples)

    outSamples = np.empty((0, 2), float)
    if(0 < numSamples):
        outSamples = np.append(outSamples,                        inSamples[0                 :fullBeatSmpl      ],             axis=0) #rate unchanged
    if(fullBeatSmpl < numSamples):
        outSamples = np.append(outSamples, pyrb.pyrb.time_stretch(inSamples[fullBeatSmpl      :fiveThirdsBeatSmpl], sr, TWOF ), axis=0)
    if(fiveThirdsBeatSmpl < numSamples):
        outSamples = np.append(outSamples, pyrb.pyrb.time_stretch(inSamples[fiveThirdsBeatSmpl:numSamples        ], sr, HALFF), axis=0)

    return outSamples

#Take 4 beats worth of swing-beat input samples and half-time waltzify the rhythm
#inSamples should be of length 2*beatSampleLength, except at the end of a file/channel
def waltzifySwingBeatQuadHT(inSamples, beatSampleLength, sr):
    numSamples           = len(inSamples) - 1
    twoThirdsBeatSmpl    = min(round(beatSampleLength*TWO_THIRDS   ), numSamples)
    fullBeatSmpl         = min(round(beatSampleLength*ONEF         ), numSamples)
    fiveThirdsBeatSmpl   = min(round(beatSampleLength*FIVE_THIRDS  ), numSamples)
    twoBeatSmpl          = min(round(beatSampleLength*TWOF         ), numSamples)
    eightThirdsBeatSmpl  = min(round(beatSampleLength*EIGHT_THIRDS ), numSamples)
    elevenThirdsBeatSmpl = min(round(beatSampleLength*ELEVEN_THIRDS), numSamples)

    outSamples = np.empty((0, 2), float)
    if(0                    < numSamples):
        outSamples = np.append(outSamples,                        inSamples[0                   :twoThirdsBeatSmpl    ],             axis=0) #rate unchanged
    if(twoThirdsBeatSmpl    < numSamples):
        outSamples = np.append(outSamples, pyrb.pyrb.time_stretch(inSamples[twoThirdsBeatSmpl   :fullBeatSmpl         ], sr, HALFF), axis=0)
    if(fullBeatSmpl         < numSamples):
        outSamples = np.append(outSamples, pyrb.pyrb.time_stretch(inSamples[fullBeatSmpl        :fiveThirdsBeatSmpl   ], sr, TWOF ), axis=0)
    if(fiveThirdsBeatSmpl   < numSamples):
        outSamples = np.append(outSamples,                        inSamples[fiveThirdsBeatSmpl  :twoBeatSmpl          ],             axis=0) #rate unchanged
    if(twoBeatSmpl          < numSamples):
        outSamples = np.append(outSamples, pyrb.pyrb.time_stretch(inSamples[twoBeatSmpl         :eightThirdsBeatSmpl  ], sr, TWOF ), axis=0)
    if(eightThirdsBeatSmpl  < numSamples):
        outSamples = np.append(outSamples,                        inSamples[eightThirdsBeatSmpl :elevenThirdsBeatSmpl ],             axis=0) #rate unchanged
    if(elevenThirdsBeatSmpl < numSamples):
        outSamples = np.append(outSamples, pyrb.pyrb.time_stretch(inSamples[elevenThirdsBeatSmpl:numSamples           ], sr, HALFF), axis=0)

    return outSamples

def fileWaltzifier(inputFileName, bpm, sw, ht, beatDelayMS):

    inSamples, sr = sf.read(inputFileName)
    if(len(inSamples) == 0):
        print("Unable to read audio file: " + inputFileName)
        exit()

    
    currentBeatPairIdx = 0
    beatDelaySamples = round(sr * (beatDelayMS / MS_PER_SECOND))
    currentSampleIdx = beatDelaySamples

    outFileName = 'waltz'
    if ht:
        outFileName += 'ht'
    
    outFileName += '_' + inputFileName

    outSamples =  np.empty((0, 2), float)
    if(currentSampleIdx > 0):
        outSamples = np.append(outSamples, inSamples[0:currentSampleIdx], axis=0)

    beatSampleLength = float(sr * SECONDS_PER_MINUTEF / bpm)
    beatsPerWaltzSegment = 4 if ht else 2
    #TODO: work through the file 2 beats at a time and call waltzifying functions
    while(currentSampleIdx < len(inSamples)):
        
        nextBeatSetSampleIdx = round((currentBeatPairIdx + 1) * beatsPerWaltzSegment * beatSampleLength) + beatDelaySamples
        currentBeatPairInSamples = inSamples[max(0, currentSampleIdx):nextBeatSetSampleIdx]
        if(sw):
            if(ht):
                outSamples = np.append(outSamples, waltzifySwingBeatQuadHT(   currentBeatPairInSamples, beatSampleLength, sr), axis=0)
            else:
                outSamples = np.append(outSamples, waltzifySwingBeatPair(     currentBeatPairInSamples, beatSampleLength, sr), axis=0)
        else:
            if(ht):
                outSamples = np.append(outSamples, waltzifyStraightBeatQuadHT(currentBeatPairInSamples, beatSampleLength, sr), axis=0)
            else:        
                outSamples = np.append(outSamples, waltzifyStraightBeatPair(  currentBeatPairInSamples, beatSampleLength, sr), axis=0)
        #Go to next beat index
        currentBeatPairIdx += 1
        currentSampleIdx = nextBeatSetSampleIdx
        
    print(len(inSamples))
    print(len(outSamples))
    print('Successfully wrote to ' + outFileName)
    sf.write(outFileName, outSamples, sr, format='wav')


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
        print("Example: waltzifier.py zone_2_3.ogg 150 sw ht 0\n")
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
