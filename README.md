# Waltzifier
A set of utilities and command interfaces used for creating a Crypt of the NecroDancer music mod.

The mod turns all in-game songs into waltz rhythms (effectively 1.5x speed rhythms where 2 beats become 3). The aim was to accomplish this for all in-game songs and soundtracks, while preserving decent sound quality with minimal sound artifacts. To accomplish this, Python script utilities were used which leverage PyRubberBand for high-quality audio timestretching:
https://pyrubberband.readthedocs.io/en/stable/index.html

The results were designed to be paired with triplet-time beatmaps which I previously created in a prior mod for the game on the Steam Workshop:
https://steamcommunity.com/sharedfiles/filedetails/?id=2254556266

The Python utilities in this project can also be used to waltzify other audio tracks, provided they have a straight- or swing-time 4/4 rhythm, as well as either a) a known beatmap file (.txt file with newline-separated beat timing in seconds), or b) a known, steady tempo in exact beats per minute.

Some example songs are included under sample_music to demonstrate the effect + functionality.

In-game video demo: https://www.youtube.com/watch?v=boIb7meTRgs

Mod link: https://mod.io/g/crypt/m/ballofthenecrowaltzer
