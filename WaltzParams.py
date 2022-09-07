"""! Definition file for WaltzParams class"""

class WaltzParams:
    """! A set of data fields storing information required to perform waltzification on a specific file."""
    
    def __init__(self, inFilePath, bpm, sw, ht, beatDelayMs, outFilePath, timeSwitchBeats=[], rhythmSwitchBeats=[], beatmapFile=""):
        """! Initializes all parameters
        @param inFilePath: name/path to input audio file
        @param bpm: tempo of the input audio track in beats per minute
        @param sw: indicates the input audio track has a swing rhythm (False=straight rhythm)
        @param ht: set true to produce a half-time (slower) waltz output track (False=full-time waltz)
        @param beatDelayMs: specify delay in milliseconds before the first "beat" of the input track (useful for rhythm-syncing)
        @param outFilePath: name/path to produce output audio file (default if empty: <input file directory> + "waltz" [+ "ht" if half-time] + "_" + <input file name>)
        @param timeSwitchBeats: specify beats on which to switch between full-time and half-time waltz
        @param rhythmSwitchBeats: specify beats on which the input audio changes between a straight rhythm and swing rhythm
        @param beatmapFile: name/path of beatmap file with newline-separate beat timestamps in seconds to guide waltzification. *This will override bpm.*
        """
        self.inFilePath        = inFilePath
        self.bpm               = bpm
        self.sw                = sw
        self.ht                = ht
        self.beatDelayMs       = beatDelayMs
        self.outFilePath       = outFilePath
        self.timeSwitchBeats   = timeSwitchBeats
        self.rhythmSwitchBeats = rhythmSwitchBeats
        self.beatmapFile       = beatmapFile
    
    inFilePath        = ""
    bpm               = float(0.0)
    sw                = False
    ht                = False
    beatDelayMs       = 0
    outFilePath       = ""
    timeSwitchBeats   = []
    rhythmSwitchBeats = []
    beatmapFile       = ""
