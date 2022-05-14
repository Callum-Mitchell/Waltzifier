import numpy as np
import pyrubberband as pyrb
import pyogg
import soundfile as sf #For creating output files
import sys
import wave

TWO_THIRDS = float(2.0/3.0)
THREE_HALVES = float(3.0/2.0)
FIVE_THIRDS = float(5.0/3.0)
HALF = float(0.5)
TWOF = float(2.0)

SECONDS_PER_MINUTEF = float(60.0)

#Take two beats worth of straight-beat input samples and waltzify the rhythm
#inSamples should be of length 2*beatSampleLength, except at the end of a file/channel
def waltzifyStraightBeatPair(inSamples, beatSampleLength, sr):
    lastSmpl            = len(inSamples) - 1
    halfBeatSmpl        = min(round(beatSampleLength*HALF        ), lastSmpl)
    threeHalvesBeatSmpl = min(round(beatSampleLength*THREE_HALVES), lastSmpl)

    outSamples = np.empty((0, 2), float)
    if(0 != lastSmpl):
        outSamples = np.append(outSamples, pyrb.pyrb.time_stretch(inSamples[0                  :halfBeatSmpl       ], sr, TWO_THIRDS  ), axis=0)
    if(halfBeatSmpl != lastSmpl):
        outSamples = np.append(outSamples, pyrb.pyrb.time_stretch(inSamples[halfBeatSmpl       :threeHalvesBeatSmpl], sr, THREE_HALVES), axis=0)
    if(threeHalvesBeatSmpl != lastSmpl):
        outSamples = np.append(outSamples, pyrb.pyrb.time_stretch(inSamples[threeHalvesBeatSmpl:lastSmpl           ], sr, TWO_THIRDS  ), axis=0)

    return outSamples

#Take two beats worth of straight-beat input samples and waltzify the rhythm
#inSamples should be of length 2*beatSampleLength, except at the end of a file/channel
def waltzifySwingBeatPair(inSamples, beatSampleLength, sr):
    lastSmpl           = len(inSamples) - 1
    fullBeatSmpl       = min(round(beatSampleLength            ), lastSmpl)
    fiveThirdsBeatSmpl = min(round(beatSampleLength*FIVE_THIRDS), lastSmpl)

    outSamples = np.empty((0, 2), float)
    if(0 != lastSmpl):
        outSamples = np.append(outSamples,                        inSamples[0                 :fullBeatSmpl      ],            axis=0) #rate unchanged
    if(fullBeatSmpl != lastSmpl):
        outSamples = np.append(outSamples, pyrb.pyrb.time_stretch(inSamples[fullBeatSmpl      :fiveThirdsBeatSmpl], sr, TWOF), axis=0)
    if(fiveThirdsBeatSmpl != lastSmpl):
        outSamples = np.append(outSamples, pyrb.pyrb.time_stretch(inSamples[fiveThirdsBeatSmpl:lastSmpl          ], sr, HALF), axis=0)

    return outSamples

def fileWaltzifier(inputFileName, bpm, sw):

    inSamples, sr = sf.read(inputFileName)
    if(len(inSamples) == 0):
        print("Unable to read audio file: " + inputFileName)
        exit()

    currentBeatPairIdx = 0
    currentSampleIdx = 0

    outFileName = 'waltz_' + inputFileName

    outSamples =  np.empty((0, 2), float)
    beatSampleLength = float(sr * SECONDS_PER_MINUTEF / bpm)
    #TODO: work through the file 2 beats at a time and call waltzifying functions
    while(currentSampleIdx < len(inSamples)):
        
        nextBeatPairSampleIdx = round((currentBeatPairIdx + 1) * 2 * beatSampleLength)
        currentBeatPairInSamples = inSamples[currentSampleIdx:nextBeatPairSampleIdx]

        if(sw):
            outSamples = np.append(outSamples, waltzifySwingBeatPair(   currentBeatPairInSamples, beatSampleLength, sr), axis=0)
        else:
            outSamples = np.append(outSamples, waltzifyStraightBeatPair(currentBeatPairInSamples, beatSampleLength, sr), axis=0)
            
        #Go to next beat index
        currentBeatPairIdx += 1
        currentSampleIdx = nextBeatPairSampleIdx

    print('Successfully wrote to ' + outFileName)
    sf.write(outFileName, outSamples, sr, format='wav')


def main():
    print(sf.__libsndfile_version__)
    args = sys.argv[1:]
    if len(args) < 2:
        print("Usage: walzifier.py infile bpm sw\n")
        print("infile: input file name (.ogg)")
        print("bpm: speed of song in beats per minute")
        print("sw: 1 if the input has a swing rhythm; 0 for straight rhythm (default 0)")
        print("Example: waltzifier.py zone_2_1.ogg 130 1\n")
        exit()

    inFileName = args[0]
    bpm = int(args[1])
    if(bpm <= 0):
        print("BPM must be greater than 0")
        exit()
    
    sw = False
    if len(args) >= 3 and int(args[2]) == 1:
        sw = True
        print("Swing mode activated!")

    fileWaltzifier(inFileName, bpm, sw)

    


if __name__=="__main__":
    main()
