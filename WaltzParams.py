"""! Definition file for WaltzParams class"""

class WaltzParams:
    """! A set of data fields storing information required to perform waltzification on a specific file."""
    
    def __init__(self, inFilePath, bpm, sw, ht, beatDelayMs, outFilePath):
        self.inFilePath  = inFilePath
        self.bpm         = bpm
        self.sw          = sw
        self.ht          = ht
        self.beatDelayMs = beatDelayMs
        self.outFilePath = outFilePath
    
    inFilePath      = ""    
    bpm             = 0
    sw              = False
    ht              = False
    beatDelayMs     = 0
    outFilePath     = ""

    #TODO (unused for now)
    timeSwitchBeats = []
    deltaBPM        = 0
