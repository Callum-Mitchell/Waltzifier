-- Press Shift+F1 to display debug output in-game
print("Ball of the NecroWaltzer reloaded")
local Event        = require "necro.event.Event"
local Music        = require "necro.audio.Music"

--Substitutes custom waltzified music/beatmaps
Event.musicTrack.add("setWaltzMusic", {order="replaySkipMute", sequence=100}, function(ev)
    local modDirectory = "mods/BalloftheNecroWaltzer"

    --Replace the soundtrack's beatmap with the local (triplet/waltz) version
    local ogBeatmapDir = ev.beatmap
    local ogBeatmapDirPieces = {}
    for piece in string.gmatch(ogBeatmapDir, "([^".."/".."]+)") do
        table.insert(ogBeatmapDirPieces, piece)
    end
    local beatmapSubdir = ogBeatmapDirPieces[#ogBeatmapDirPieces - 1]
    local beatmapFileName = ogBeatmapDirPieces[#ogBeatmapDirPieces]
    ev.beatmap = modDirectory .. "/" .. beatmapSubdir .. "/" .. beatmapFileName

    --Replace each soundtrack layer with its local equivalent
    local numLayers = #ev.layers
    for i=1,numLayers,1 do
        local musicLayer = ev.layers[i]
        local ogFileDir = musicLayer.file
        local ogFileDirPieces = {}
        for piece in string.gmatch(ogFileDir, "([^".."/".."]+)") do
            table.insert(ogFileDirPieces, piece)
        end
        local musicFileDir = ogFileDirPieces[#ogFileDirPieces - 1]
        local musicFileName = ogFileDirPieces[#ogFileDirPieces]
        musicLayer.file = modDirectory .. "/" .. musicFileDir .. "/" .. musicFileName
        --If this layer has an additional beatmap (eg. Necrodancer phase 2), replace it
        if(musicLayer.beatmap ~= nil) then
            local layerOgBeatmapDir = musicLayer.beatmap
            local layerOgBeatmapDirPieces = {}
            for piece in string.gmatch(layerOgBeatmapDir, "([^".."/".."]+)") do
                table.insert(layerOgBeatmapDirPieces, piece)
            end
            local layerBeatmapSubdir = layerOgBeatmapDirPieces[#layerOgBeatmapDirPieces - 1]
            local layerBeatmapFileName = layerOgBeatmapDirPieces[#layerOgBeatmapDirPieces]
            musicLayer.beatmap = modDirectory .. "/" .. layerBeatmapSubdir .. "/" .. layerBeatmapFileName
        end
    end
end)
  