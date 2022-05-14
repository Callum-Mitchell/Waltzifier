import pyrubberband as pyrb
import pyogg
import sys

TWO_THIRDS = float(2.0/3.0)
THREE_HALVES = float(3.0/2.0)
HALF = float(0.5)
TWOF = float(2.0)

#Take two beats worth of straight-beat input samples and waltzify the rhythm
#inSamples should be of length 2*beatSampleLength, except at the end of a file/channel
def waltzifyStraightBeatPair(inSamples, beatSampleLength):
    lastSmpl            = len(inSamples) - 1
    halfBeatSmpl        = min(round(beatSampleLength*HALF        ), lastSmpl)
    threeHalvesBeatSmpl = min(round(beatSampleLength*THREE_HALVES), lastSmpl)

    outSamples =      pyrb.pyrb.time_stretch(inSamples[0                  :halfBeatSmpl       ], rate=TWO_THIRDS  )
    outSamples.extend(pyrb.pyrb.time_stretch(inSamples[halfBeatSmpl       :threeHalvesBeatSmpl], rate=THREE_HALVES))
    outSamples.extend(pyrb.pyrb.time_stretch(inSamples[threeHalvesBeatSmpl:lastSmpl           ], rate=TWO_THIRDS  ))

    return outSamples

#Take two beats worth of straight-beat input samples and waltzify the rhythm
#inSamples should be of length 2*beatSampleLength, except at the end of a file/channel
def waltzifySwingBeatPair(inSamples, beatSampleLength):
    lastSmpl            = len(inSamples) - 1
    fullBeatSmpl        = min(round(beatSampleLength             ), lastSmpl)
    threeHalvesBeatSmpl = min(round(beatSampleLength*THREE_HALVES), lastSmpl)

    outSamples =                             inSamples[0                  :fullBeatSmpl       ] #rate=1 (unchanged)
    outSamples.extend(pyrb.pyrb.time_stretch(inSamples[fullBeatSmpl       :threeHalvesBeatSmpl], rate=TWOF))
    outSamples.extend(pyrb.pyrb.time_stretch(inSamples[threeHalvesBeatSmpl:lastSmpl           ], rate=HALF))

    return outSamples

def fileWaltzifier(inBuf, bpm):

    currentBeatPairIdx = 0
    currentSampleIdx = 0
    pyrb.pyrb.time_stretch(y, sr, rate, rbargs=None)

def main():
    args = sys.argv[1:]
    if len(args) < 3:
        print("Usage: walzifier.py --infile --bpm -sw\n")
        print("--infile: input file name (.ogg)")
        print("--bpm: speed of song in beats per minute")
        print("-sw: 1 if the input has a swing rhythm; default 0")
        print("Example: waltzifier.py zone_2_1.ogg 130 -sw\n")

    filename = args[0]
    inputFile = pyogg.VorbisFile(filename)
    inBuf = inputFile.buffer
    if len(inBuf) == 0:
        print("Unable to open file: " + filename)
        exit()
    


if __name__=="__main__":
    main()
