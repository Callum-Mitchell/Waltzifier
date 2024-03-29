"""! Provides a lookup dictionary for waltz parameters in the DannyB soundtrack"""

import WaltzParams

DANNYB_SONG_PARAMS = dict({
    'boss_1':    WaltzParams.WaltzParams("../../data/music/boss_1.ogg",    120, False, False, 10,    "./music/boss_1.ogg"   ),
    'boss_2':    WaltzParams.WaltzParams("../../data/music/boss_2.ogg",    175, False, True,  10,    "./music/boss_2.ogg"   ),
    'boss_3':    WaltzParams.WaltzParams("../../data/music/boss_3.ogg",    123, True,  False, 10,    "./music/boss_3.ogg"   ),
    #Not replacing boss_4 for DannyB - it is silent and unused
    'boss_5':    WaltzParams.WaltzParams("../../data/music/boss_5.ogg",    140, False, False, 10,    "./music/boss_5.ogg"   ),
    'boss_6':    WaltzParams.WaltzParams("../../data/music/boss_6.ogg",    140, False, False, 10,    "./music/boss_6.ogg"   ),
    'boss_6a':   WaltzParams.WaltzParams("../../data/music/boss_6a.ogg",   160, False, False, 10,    "./music/boss_6a.ogg"  ),
    'boss_7':    WaltzParams.WaltzParams("../../data/music/boss_7.ogg",    0,   False, False, -45,   "./music/boss_7.ogg",  beatmapFile="../../data/music/boss_7.txt"),
    'boss_8':    WaltzParams.WaltzParams("../../data/music/boss_8.ogg",    120, False, True,  10,    "./music/boss_8.ogg",  timeSwitchBeats=[48]),
    'boss_9':    WaltzParams.WaltzParams("../../data/music/boss_9.ogg",    150, False, False, 10,    "./music/boss_9.ogg"   ),
    'boss_10':   WaltzParams.WaltzParams("../../data/music/boss_10.ogg",   125, False, False, 30,    "./music/boss_10.ogg"  ),
    'boss_11':   WaltzParams.WaltzParams("../../data/music/boss_11.ogg",   145, True,  True,  10,    "./music/boss_11.ogg"  ),
    'credits_1': WaltzParams.WaltzParams("../../data/music/credits_1.ogg", 140, False, True,  30,    "./music/credits_1.ogg"),
    'credits_2': WaltzParams.WaltzParams("../../data/music/credits_2.ogg", 140, False, True,  30,    "./music/credits_2.ogg"),
    'credits_3': WaltzParams.WaltzParams("../../data/music/credits_3.ogg", 140, False, True,  30,    "./music/credits_3.ogg"),
    'credits_4': WaltzParams.WaltzParams("../../data/music/credits_4.ogg", 140, False, True,  30,    "./music/credits_4.ogg"),
    'credits_5': WaltzParams.WaltzParams("../../data/music/credits_5.ogg", 140, False, True,  30,    "./music/credits_5.ogg"),
    'lobby':     WaltzParams.WaltzParams("../../data/music/lobby.ogg",     130, False, False, 10,    "./music/lobby.ogg"    ),
    'training':  WaltzParams.WaltzParams("../../data/music/training.ogg",  120, False, True,  10,    "./music/training.ogg" ),
    'tutorial':  WaltzParams.WaltzParams("../../data/music/tutorial.ogg",  100, False, False, 10,    "./music/tutorial.ogg" ),
    'zone1_1':   WaltzParams.WaltzParams("../../data/music/zone1_1.ogg",   115, False, False, 10,    "./music/zone1_1.ogg"  ),
    'zone1_2':   WaltzParams.WaltzParams("../../data/music/zone1_2.ogg",   130, True,  True,  20,    "./music/zone1_2.ogg"  ),
    'zone1_3':   WaltzParams.WaltzParams("../../data/music/zone1_3.ogg",   140, False, True,  10,    "./music/zone1_3.ogg"  ),
    'zone2_1':   WaltzParams.WaltzParams("../../data/music/zone2_1.ogg",   130, True,  True,  20,    "./music/zone2_1.ogg"  ),
    'zone2_2':   WaltzParams.WaltzParams("../../data/music/zone2_2.ogg",   140, False, False, 10,    "./music/zone2_2.ogg"  ),
    'zone2_3':   WaltzParams.WaltzParams("../../data/music/zone2_3.ogg",   150, True,  True,  10,    "./music/zone2_3.ogg"  ),
    'zone3_1c':  WaltzParams.WaltzParams("../../data/music/zone3_1c.ogg",  135, False, False, 10,    "./music/zone3_1c.ogg" ),
    'zone3_1h':  WaltzParams.WaltzParams("../../data/music/zone3_1h.ogg",  135, False, True,  10,    "./music/zone3_1h.ogg" ),
    'zone3_2c':  WaltzParams.WaltzParams("../../data/music/zone3_2c.ogg",  145, True,  False, 10,    "./music/zone3_2c.ogg" ),
    'zone3_2h':  WaltzParams.WaltzParams("../../data/music/zone3_2h.ogg",  145, True,  True,  10,    "./music/zone3_2h.ogg" ),
    'zone3_3c':  WaltzParams.WaltzParams("../../data/music/zone3_3c.ogg",  155, False, False, 10,    "./music/zone3_3c.ogg" ),
    'zone3_3h':  WaltzParams.WaltzParams("../../data/music/zone3_3h.ogg",  155, False, True,  10,    "./music/zone3_3h.ogg" ),
    'zone4_1':   WaltzParams.WaltzParams("../../data/music/zone4_1.ogg",   130, False, False, 10,    "./music/zone4_1.ogg"  ),
    'zone4_2':   WaltzParams.WaltzParams("../../data/music/zone4_2.ogg",   145, False, False, 10,    "./music/zone4_2.ogg"  ),
    'zone4_3':   WaltzParams.WaltzParams("../../data/music/zone4_3.ogg",   160, False, True,  10,    "./music/zone4_3.ogg"  ),
    'zone5_1':   WaltzParams.WaltzParams("../../data/music/zone5_1.ogg",   130, False, False, 10,    "./music/zone5_1.ogg"  ),
    'zone5_2':   WaltzParams.WaltzParams("../../data/music/zone5_2.ogg",   140, True,  True,  10,    "./music/zone5_2.ogg"  ),
    'zone5_3':   WaltzParams.WaltzParams("../../data/music/zone5_3.ogg",   155, False, False, 10,    "./music/zone5_3.ogg", timeSwitchBeats=[112, 152, 336])
})
