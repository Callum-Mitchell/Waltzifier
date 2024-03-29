"""! Provides a lookup dictionary for waltz parameters in the Virt soundtrack"""

import WaltzParams

GIRLFRIEND_RECORDS_SONG_PARAMS = dict({
    'boss_1':   WaltzParams.WaltzParams("../../data/music/boss_1_4.ogg",   120, False, False, 10,  "./music/boss_1_4.ogg"  ),
    'boss_2':   WaltzParams.WaltzParams("../../data/music/boss_2_4.ogg",   175, False, True,  10,  "./music/boss_2_4.ogg"  ),
    'boss_3':   WaltzParams.WaltzParams("../../data/music/boss_3_4.ogg",   123, False, False, 10,  "./music/boss_3_4.ogg"  ),
    'boss_4':   WaltzParams.WaltzParams("../../data/music/boss_4_4.ogg",   126, False, True,  10,  "./music/boss_4_4.ogg"  ),
    'boss_5':   WaltzParams.WaltzParams("../../data/music/boss_5_4.ogg",   140, False, False, 10,  "./music/boss_5_4.ogg"  ),
    'boss_6':   WaltzParams.WaltzParams("../../data/music/boss_6_4.ogg",   140, False, False, 10,  "./music/boss_6_4.ogg"  ),
    'boss_6a':  WaltzParams.WaltzParams("../../data/music/boss_6_4a.ogg",  160, False, False, 10,  "./music/boss_6_4a.ogg" ),
    'boss_7':   WaltzParams.WaltzParams("../../data/music/boss_7_4.ogg",   0,   False, False, -45, "./music/boss_7_4.ogg",  beatmapFile="../../data/music/boss_7.txt"),
    'boss_8':   WaltzParams.WaltzParams("../../data/music/boss_8_4.ogg",   120, False, True,  10,  "./music/boss_8_4.ogg",  timeSwitchBeats=[48]),
    'boss_9':   WaltzParams.WaltzParams("../../data/music/boss_9_4.ogg",   150, False, False, 10,  "./music/boss_9_4.ogg"  ),
    'boss_9a':  WaltzParams.WaltzParams("../../data/music/boss_9_4a.ogg",  150, False, False, 10,  "./music/boss_9_4a.ogg" ),
    'boss_9b':  WaltzParams.WaltzParams("../../data/music/boss_9_4b.ogg",  150, False, False, 10,  "./music/boss_9_4b.ogg" ),
    'lobby':    WaltzParams.WaltzParams("../../data/music/lobby_4.ogg",    130, False, False, 10,  "./music/lobby_4.ogg"   ),
    'training': WaltzParams.WaltzParams("../../data/music/training_4.ogg", 120, False, True,  10,  "./music/training_4.ogg"),
    'zone1_1':  WaltzParams.WaltzParams("../../data/music/zone1_1_4.ogg",  115, False, False, 10,  "./music/zone1_1_4.ogg" ),
    'zone1_2':  WaltzParams.WaltzParams("../../data/music/zone1_2_4.ogg",  130, False, True,  20,  "./music/zone1_2_4.ogg", rhythmSwitchBeats=[108, 112, 228, 232, 236, 240, 244, 248, 252, 268, 300]),
    'zone1_3':  WaltzParams.WaltzParams("../../data/music/zone1_3_4.ogg",  140, False, True,  10,  "./music/zone1_3_4.ogg" ),
    'zone2_1':  WaltzParams.WaltzParams("../../data/music/zone2_1_4.ogg",  130, True,  True,  20,  "./music/zone2_1_4.ogg" ),
    'zone2_2':  WaltzParams.WaltzParams("../../data/music/zone2_2_4.ogg",  140, False, False, 10,  "./music/zone2_2_4.ogg" ),
    'zone2_3':  WaltzParams.WaltzParams("../../data/music/zone2_3_4.ogg",  150, True,  True,  10,  "./music/zone2_3_4.ogg" ),
    'zone3_1c': WaltzParams.WaltzParams("../../data/music/zone3_1_4c.ogg", 135, False, False, 10,  "./music/zone3_1_4c.ogg"),
    'zone3_1h': WaltzParams.WaltzParams("../../data/music/zone3_1_4h.ogg", 135, False, True,  10,  "./music/zone3_1_4h.ogg"),
    'zone3_2c': WaltzParams.WaltzParams("../../data/music/zone3_2_4c.ogg", 145, True,  False, 10,  "./music/zone3_2_4c.ogg"),
    'zone3_2h': WaltzParams.WaltzParams("../../data/music/zone3_2_4h.ogg", 145, True,  True,  10,  "./music/zone3_2_4h.ogg"),
    'zone3_3c': WaltzParams.WaltzParams("../../data/music/zone3_3_4c.ogg", 155, False, False, 10,  "./music/zone3_3_4c.ogg"),
    'zone3_3h': WaltzParams.WaltzParams("../../data/music/zone3_3_4h.ogg", 155, False, True,  10,  "./music/zone3_3_4h.ogg"),
    'zone4_1':  WaltzParams.WaltzParams("../../data/music/zone4_1_4.ogg",  130, False, False, 10,  "./music/zone4_1_4.ogg" ),
    'zone4_2':  WaltzParams.WaltzParams("../../data/music/zone4_2_4.ogg",  145, False, False, 10,  "./music/zone4_2_4.ogg" ),
    'zone4_3':  WaltzParams.WaltzParams("../../data/music/zone4_3_4.ogg",  160, False, True,  10,  "./music/zone4_3_4.ogg" ),
    'zone5_1':  WaltzParams.WaltzParams("../../data/music/zone5_1_4.ogg",  130, False, False, 10,  "./music/zone5_1_4.ogg" ),
    'zone5_2':  WaltzParams.WaltzParams("../../data/music/zone5_2_4.ogg",  140, True,  True,  10,  "./music/zone5_2_4.ogg" ),
    'zone5_3':  WaltzParams.WaltzParams("../../data/music/zone5_3_4.ogg",  155, False, False, 10,  "./music/zone5_3_4.ogg", timeSwitchBeats=[112, 152, 336])
})
