import WaltzParams

"""! Lookup dictionary for all songs within the data/sounds_streaming directory.
These include Coral Riff instrument layers, Fortissimole's vocals, and all shopkeeper songs
"""
SOUNDS_STREAMING_PARAMS = dict({
    'boss_4_inst0':           WaltzParams.WaltzParams("../../data/sounds_streaming/boss_4_inst0.ogg",           126, False, True,  10, "./sounds_streaming/boss_4_inst0.ogg"          ),
    'boss_4_inst1':           WaltzParams.WaltzParams("../../data/sounds_streaming/boss_4_inst1.ogg",           126, False, True,  10, "./sounds_streaming/boss_4_inst1.ogg"          ),
    'boss_4_inst2':           WaltzParams.WaltzParams("../../data/sounds_streaming/boss_4_inst2.ogg",           126, False, True,  10, "./sounds_streaming/boss_4_inst2.ogg"          ),
    'boss_4_inst3':           WaltzParams.WaltzParams("../../data/sounds_streaming/boss_4_inst3.ogg",           126, False, True,  10, "./sounds_streaming/boss_4_inst3.ogg"          ),
    'boss_4_inst4':           WaltzParams.WaltzParams("../../data/sounds_streaming/boss_4_inst4.ogg",           126, False, True,  10, "./sounds_streaming/boss_4_inst4.ogg"          ),
    'boss_9_vocal':           WaltzParams.WaltzParams("../../data/sounds_streaming/boss_4_inst4.ogg",           150, False, False, 10, "./sounds_streaming/boss_4_inst4.ogg"          ),
    'zone1_1_shopkeeper':     WaltzParams.WaltzParams("../../data/sounds_streaming/zone1_1_shopkeeper.ogg",     115, False, False, 10, "./sounds_streaming/zone1_1_shopkeeper.ogg"    ),
    'zone1_1_shopkeeper_m':   WaltzParams.WaltzParams("../../data/sounds_streaming/zone1_1_shopkeeper_m.ogg",   115, False, False, 10, "./sounds_streaming/zone1_1_shopkeeper_m.ogg"  ),
    'zone1_1_shopkeeper_nd':  WaltzParams.WaltzParams("../../data/sounds_streaming/zone1_1_shopkeeper_nd.ogg",  115, False, False, 10, "./sounds_streaming/zone1_1_shopkeeper_nd.ogg" ),
    'zone1_2_shopkeeper':     WaltzParams.WaltzParams("../../data/sounds_streaming/zone1_2_shopkeeper.ogg",     130, True,  False, 10, "./sounds_streaming/zone1_2_shopkeeper.ogg"    ),
    'zone1_2_shopkeeper_m':   WaltzParams.WaltzParams("../../data/sounds_streaming/zone1_2_shopkeeper_m.ogg",   130, True,  False, 10, "./sounds_streaming/zone1_2_shopkeeper_m.ogg"  ),
    'zone1_2_shopkeeper_nd':  WaltzParams.WaltzParams("../../data/sounds_streaming/zone1_2_shopkeeper_nd.ogg",  130, True,  False, 10, "./sounds_streaming/zone1_2_shopkeeper_nd.ogg" ),
    'zone1_3_shopkeeper':     WaltzParams.WaltzParams("../../data/sounds_streaming/zone1_3_shopkeeper.ogg",     140, False, True,  10, "./sounds_streaming/zone1_3_shopkeeper.ogg"    ),
    'zone1_3_shopkeeper_m':   WaltzParams.WaltzParams("../../data/sounds_streaming/zone1_3_shopkeeper_m.ogg",   140, False, True,  10, "./sounds_streaming/zone1_3_shopkeeper_m.ogg"  ),
    'zone1_3_shopkeeper_nd':  WaltzParams.WaltzParams("../../data/sounds_streaming/zone1_3_shopkeeper_nd.ogg",  140, False, True,  10, "./sounds_streaming/zone1_3_shopkeeper_nd.ogg" ),
    'zone2_1_shopkeeper':     WaltzParams.WaltzParams("../../data/sounds_streaming/zone2_1_shopkeeper.ogg",     130, True,  True,  10, "./sounds_streaming/zone2_1_shopkeeper.ogg"    ),
    'zone2_1_shopkeeper_m':   WaltzParams.WaltzParams("../../data/sounds_streaming/zone2_1_shopkeeper_m.ogg",   130, True,  True,  10, "./sounds_streaming/zone2_1_shopkeeper_m.ogg"  ),
    'zone2_1_shopkeeper_nd':  WaltzParams.WaltzParams("../../data/sounds_streaming/zone2_1_shopkeeper_nd.ogg",  130, True,  True,  10, "./sounds_streaming/zone2_1_shopkeeper_nd.ogg" ),
    'zone2_2_shopkeeper':     WaltzParams.WaltzParams("../../data/sounds_streaming/zone2_2_shopkeeper.ogg",     140, False, False, 10, "./sounds_streaming/zone2_2_shopkeeper.ogg"    ),
    'zone2_2_shopkeeper_m':   WaltzParams.WaltzParams("../../data/sounds_streaming/zone2_2_shopkeeper_m.ogg",   140, False, False, 10, "./sounds_streaming/zone2_2_shopkeeper_m.ogg"  ),
    'zone2_2_shopkeeper_nd':  WaltzParams.WaltzParams("../../data/sounds_streaming/zone2_2_shopkeeper_nd.ogg",  140, False, False, 10, "./sounds_streaming/zone2_2_shopkeeper_nd.ogg" ),
    'zone2_3_shopkeeper':     WaltzParams.WaltzParams("../../data/sounds_streaming/zone2_3_shopkeeper.ogg",     150, True,  True,  10, "./sounds_streaming/zone2_3_shopkeeper.ogg"    ),
    'zone2_3_shopkeeper_m':   WaltzParams.WaltzParams("../../data/sounds_streaming/zone2_3_shopkeeper_m.ogg",   150, True,  True,  10, "./sounds_streaming/zone2_3_shopkeeper_m.ogg"  ),
    'zone2_3_shopkeeper_nd':  WaltzParams.WaltzParams("../../data/sounds_streaming/zone2_3_shopkeeper_nd.ogg",  150, True,  True,  10, "./sounds_streaming/zone2_3_shopkeeper_nd.ogg" ),
    'zone3_1c_shopkeeper':    WaltzParams.WaltzParams("../../data/sounds_streaming/zone3_1c_shopkeeper.ogg",    135, False, False, 10, "./sounds_streaming/zone3_1c_shopkeeper.ogg"   ),
    'zone3_1c_shopkeeper_m':  WaltzParams.WaltzParams("../../data/sounds_streaming/zone3_1c_shopkeeper_m.ogg",  135, False, False, 10, "./sounds_streaming/zone3_1c_shopkeeper_m.ogg" ),
    'zone3_1c_shopkeeper_nd': WaltzParams.WaltzParams("../../data/sounds_streaming/zone3_1c_shopkeeper_nd.ogg", 135, False, False, 10, "./sounds_streaming/zone3_1c_shopkeeper_nd.ogg"),
    'zone3_2c_shopkeeper':    WaltzParams.WaltzParams("../../data/sounds_streaming/zone3_2c_shopkeeper.ogg",    145, True,  False, 10, "./sounds_streaming/zone3_2c_shopkeeper.ogg"   ),
    'zone3_2c_shopkeeper_m':  WaltzParams.WaltzParams("../../data/sounds_streaming/zone3_2c_shopkeeper_m.ogg",  145, True,  False, 10, "./sounds_streaming/zone3_2c_shopkeeper_m.ogg" ),
    'zone3_2c_shopkeeper_nd': WaltzParams.WaltzParams("../../data/sounds_streaming/zone3_2c_shopkeeper_nd.ogg", 145, True,  False, 10, "./sounds_streaming/zone3_2c_shopkeeper_nd.ogg"),
    'zone3_3c_shopkeeper':    WaltzParams.WaltzParams("../../data/sounds_streaming/zone3_3c_shopkeeper.ogg",    155, False, True,  10, "./sounds_streaming/zone3_3c_shopkeeper.ogg"   ),
    'zone3_3c_shopkeeper_m':  WaltzParams.WaltzParams("../../data/sounds_streaming/zone3_3c_shopkeeper_m.ogg",  155, False, True,  10, "./sounds_streaming/zone3_3c_shopkeeper_m.ogg" ),
    'zone3_3c_shopkeeper_nd': WaltzParams.WaltzParams("../../data/sounds_streaming/zone3_3c_shopkeeper_nd.ogg", 155, False, True,  10, "./sounds_streaming/zone3_3c_shopkeeper_nd.ogg"),
    'zone3_1h_shopkeeper':    WaltzParams.WaltzParams("../../data/sounds_streaming/zone3_1h_shopkeeper.ogg",    135, False, True,  10, "./sounds_streaming/zone3_1h_shopkeeper.ogg"   ),
    'zone3_1h_shopkeeper_m':  WaltzParams.WaltzParams("../../data/sounds_streaming/zone3_1h_shopkeeper_m.ogg",  135, False, True,  10, "./sounds_streaming/zone3_1h_shopkeeper_m.ogg" ),
    'zone3_1h_shopkeeper_nd': WaltzParams.WaltzParams("../../data/sounds_streaming/zone3_1h_shopkeeper_nd.ogg", 135, False, True,  10, "./sounds_streaming/zone3_1h_shopkeeper_nd.ogg"),
    'zone3_2h_shopkeeper':    WaltzParams.WaltzParams("../../data/sounds_streaming/zone3_2h_shopkeeper.ogg",    145, True,  True,  10, "./sounds_streaming/zone3_2h_shopkeeper.ogg"   ),
    'zone3_2h_shopkeeper_m':  WaltzParams.WaltzParams("../../data/sounds_streaming/zone3_2h_shopkeeper_m.ogg",  145, True,  True,  10, "./sounds_streaming/zone3_2h_shopkeeper_m.ogg" ),
    'zone3_2h_shopkeeper_nd': WaltzParams.WaltzParams("../../data/sounds_streaming/zone3_2h_shopkeeper_nd.ogg", 145, True,  True,  10, "./sounds_streaming/zone3_2h_shopkeeper_nd.ogg"),
    'zone3_3h_shopkeeper':    WaltzParams.WaltzParams("../../data/sounds_streaming/zone3_3h_shopkeeper.ogg",    155, False, True,  10, "./sounds_streaming/zone3_3h_shopkeeper.ogg"   ),
    'zone3_3h_shopkeeper_m':  WaltzParams.WaltzParams("../../data/sounds_streaming/zone3_3h_shopkeeper_m.ogg",  155, False, True,  10, "./sounds_streaming/zone3_3h_shopkeeper_m.ogg" ),
    'zone3_3h_shopkeeper_nd': WaltzParams.WaltzParams("../../data/sounds_streaming/zone3_3h_shopkeeper_nd.ogg", 155, False, True,  10, "./sounds_streaming/zone3_3h_shopkeeper_nd.ogg"),
    'zone4_1_shopkeeper':     WaltzParams.WaltzParams("../../data/sounds_streaming/zone4_1_shopkeeper.ogg",     130, False, False, 10, "./sounds_streaming/zone4_1_shopkeeper.ogg"    ),
    'zone4_1_shopkeeper_m':   WaltzParams.WaltzParams("../../data/sounds_streaming/zone4_1_shopkeeper_m.ogg",   130, False, False, 10, "./sounds_streaming/zone4_1_shopkeeper_m.ogg"  ),
    'zone4_1_shopkeeper_nd':  WaltzParams.WaltzParams("../../data/sounds_streaming/zone4_1_shopkeeper_nd.ogg",  130, False, False, 10, "./sounds_streaming/zone4_1_shopkeeper_nd.ogg" ),
    'zone4_2_shopkeeper':     WaltzParams.WaltzParams("../../data/sounds_streaming/zone4_2_shopkeeper.ogg",     145, False, False, 10, "./sounds_streaming/zone4_2_shopkeeper.ogg"    ),
    'zone4_2_shopkeeper_m':   WaltzParams.WaltzParams("../../data/sounds_streaming/zone4_2_shopkeeper_m.ogg",   145, False, False, 10, "./sounds_streaming/zone4_2_shopkeeper_m.ogg"  ),
    'zone4_2_shopkeeper_nd':  WaltzParams.WaltzParams("../../data/sounds_streaming/zone4_2_shopkeeper_nd.ogg",  145, False, False, 10, "./sounds_streaming/zone4_2_shopkeeper_nd.ogg" ),
    'zone4_3_shopkeeper':     WaltzParams.WaltzParams("../../data/sounds_streaming/zone4_3_shopkeeper.ogg",     160, False, True,  10, "./sounds_streaming/zone4_3_shopkeeper.ogg"    ),
    'zone4_3_shopkeeper_m':   WaltzParams.WaltzParams("../../data/sounds_streaming/zone4_3_shopkeeper_m.ogg",   160, False, True,  10, "./sounds_streaming/zone4_3_shopkeeper_m.ogg"  ),
    'zone4_3_shopkeeper_nd':  WaltzParams.WaltzParams("../../data/sounds_streaming/zone4_3_shopkeeper_nd.ogg",  160, False, True,  10, "./sounds_streaming/zone4_3_shopkeeper_nd.ogg" ),
    'zone5_1_shopkeeper':     WaltzParams.WaltzParams("../../data/sounds_streaming/zone5_1_shopkeeper.ogg",     130, False, False, 10, "./sounds_streaming/zone5_1_shopkeeper.ogg"    ),
    'zone5_1_shopkeeper_m':   WaltzParams.WaltzParams("../../data/sounds_streaming/zone5_1_shopkeeper_m.ogg",   130, False, False, 10, "./sounds_streaming/zone5_1_shopkeeper_m.ogg"  ),
    'zone5_1_shopkeeper_nd':  WaltzParams.WaltzParams("../../data/sounds_streaming/zone5_1_shopkeeper_nd.ogg",  130, False, False, 10, "./sounds_streaming/zone5_1_shopkeeper_nd.ogg" ),
    'zone5_2_shopkeeper':     WaltzParams.WaltzParams("../../data/sounds_streaming/zone5_2_shopkeeper.ogg",     140, True,  True,  10, "./sounds_streaming/zone5_2_shopkeeper.ogg"    ),
    'zone5_2_shopkeeper_m':   WaltzParams.WaltzParams("../../data/sounds_streaming/zone5_2_shopkeeper_m.ogg",   140, True,  True,  10, "./sounds_streaming/zone5_2_shopkeeper_m.ogg"  ),
    'zone5_2_shopkeeper_nd':  WaltzParams.WaltzParams("../../data/sounds_streaming/zone5_2_shopkeeper_nd.ogg",  140, True,  True,  10, "./sounds_streaming/zone5_2_shopkeeper_nd.ogg" ),
    'zone5_3_shopkeeper':     WaltzParams.WaltzParams("../../data/sounds_streaming/zone5_3_shopkeeper.ogg",     155, False, False, 10, "./sounds_streaming/zone5_3_shopkeeper.ogg"    ),
    'zone5_3_shopkeeper_m':   WaltzParams.WaltzParams("../../data/sounds_streaming/zone5_3_shopkeeper_m.ogg",   155, False, False, 10, "./sounds_streaming/zone5_3_shopkeeper_m.ogg"  ),
    'zone5_3_shopkeeper_nd':  WaltzParams.WaltzParams("../../data/sounds_streaming/zone5_3_shopkeeper_nd.ogg",  155, False, False, 10, "./sounds_streaming/zone5_3_shopkeeper_nd.ogg" )
})