"""!
A simple convenience command interface for generating all waltzified soundtracks in full for the Crypt of the Necrodancer.
The interface also allowed a user to specify a single version of the soundtrack, a specific song, or both, to be waltzified (since the full script takes ~45 minutes).
This was made to be run from within "<Steam_install_dir>/steamapps/common/Crypt of the NecroDancer/mods/Ball of the NecroWaltzer"
When run inside this folder, the script automatically waltzified all official versions Crypt of the NecroDancer soundtracks in sequence so they could be played in-game.
However, due to issues with the old modding system/song replacements, I had to create a new (Synchrony) mod to tell the game to use these waltzified songs.
See BalloftheNecroWaltzer.lua for details. I then copied the waltzified songs to the new mod folder so the lua script could access them.
"""

import ARivalSongParams, ChipzelSongParams, DanganronpaSongParams, \
    DannyBSongParams, GirlfriendRecordsSongParams, JulesSongParams, \
    OCRSongParams, SoundsStreamingParams, VirtSongParams

import numpy as np
import sys
import Waltzifier

"""! Dictionary defining parameters for each soundtrack"""
SOUNDTRACK_PARAMS_DICT = dict({
    'DannyB':            DannyBSongParams.DANNYB_SONG_PARAMS,
    'ARival':            ARivalSongParams.ARIVAL_SONG_PARAMS,
    'Jules':             JulesSongParams.JULES_SONG_PARAMS,
    'Virt':              VirtSongParams.VIRT_SONG_PARAMS,
    'GirlfriendRecords': GirlfriendRecordsSongParams.GIRLFRIEND_RECORDS_SONG_PARAMS,
    'Danganronpa':       DanganronpaSongParams.DANGANRONPA_SONG_PARAMS,
    'Chipzel':           ChipzelSongParams.CHIPZEL_SONG_PARAMS,
    'OCR':               OCRSongParams.OCR_SONG_PARAMS,
    'SoundsStreaming':   SoundsStreamingParams.SOUNDS_STREAMING_PARAMS
})

def main():
    """! Main entry point for command interface to convert NecroDancer songs or full soundtrack versions"""

    soundtrackNames = []
    songNames = set()
    #Parse command line arguments for soundtrack and song names
    args = sys.argv[1:]
    i = 0
    while i < len(args):
        arg = args[i]
        if arg == "-soundtrack":
            if i == len(args) - 1:
                print("Error: -soundtrack option must be followed by the name of a soundtrack or song set")
                exit()
            soundtrackNames.append(args[i+1])
            i += 2

        elif arg == "-song":
            if i == len(args) - 1:
                print("Error: -song option must be followed by the name of a song to convert")
                exit()
            songNames.add(args[i+1])
            i += 2
        
        else:
            print("Warning: unrecognized argument: " + args[i])
            i += 1

    if len(soundtrackNames) == 0:
        soundtrackNames = SOUNDTRACK_PARAMS_DICT.keys()
        print("Waltzifying all available soundtracks")
    else:
        print("Waltzifying the following soundtracks:")
        print(soundtrackNames)

    if len(songNames) == 0:
        for soundtrack in SOUNDTRACK_PARAMS_DICT.values():
            for key in soundtrack.keys():
                songNames.add(key)
        print("Waltzifying all songs in each soundtrack")
    else:
        print("Songs to waltzify:")
        print(songNames)

    print("Performing waltzification...")
    for soundtrackName in soundtrackNames:
        if soundtrackName not in SOUNDTRACK_PARAMS_DICT:
            continue
        soundtrackData = SOUNDTRACK_PARAMS_DICT[soundtrackName]
        for songName in songNames:
            if songName not in soundtrackData:
                continue
            songParams = soundtrackData[songName]
            Waltzifier.waltzifyFile(songParams)
    
    print("Waltzification complete!")

if __name__=="__main__":
    main()


