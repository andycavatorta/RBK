instruments = (
    "_system",
    "_general",
    # "_kick",
    # "_snare",
    # "_tom",
    # "_hihat",
    # "_cymbal",
    # "_percussion",
    # "_miscellaneous"
)

mapping = {
    "_general/sound/bass_drum2/bang":(
        ("MIDI", {"channel":0, "pitch":35 ,"status":"note_on"})
    ),
    "_general/sound/bass_drum2/off":(
        ("MIDI", {"channel":0, "pitch":35 ,"status":"note_off"})
    ),

    "_general/sound/snare_drum1/bang":(
        ("MIDI", {"channel":0, "pitch":38 ,"status":"note_on"})
    ),
    "_general/sound/snare_drum1/off":(
        ("MIDI", {"channel":0, "pitch":38 ,"status":"note_off"})
    ),

    "_general/sound/hand_clap/bang":(
        ("MIDI", {"channel":0, "pitch":39 ,"status":"note_on"})
    ),
    "_general/sound/hand_clap/off":(
        ("MIDI", {"channel":0, "pitch":39 ,"status":"note_off"})
    ),

    "_general/sound/low_tom2/bang":(
        ("MIDI", {"channel":0, "pitch":41 ,"status":"note_on"})
    ),
    "_general/sound/low_tom2/off":(
        ("MIDI", {"channel":0, "pitch":41 ,"status":"note_off"})
    ),

    "_general/sound/closed_hihat/bang":(
        ("MIDI", {"channel":0, "pitch":42 ,"status":"note_on"})
    ),
    "_general/sound/closed_hihat/off":(
        ("MIDI", {"channel":0, "pitch":42 ,"status":"note_off"})
    ),

    "_general/sound/pedal_hihat/bang":(
        ("MIDI", {"channel":0, "pitch":44 ,"status":"note_on"})
    ),
    "_general/sound/pedal_hihat/off":(
        ("MIDI", {"channel":0, "pitch":44 ,"status":"note_off"})
    ),

    "_general/sound/mid_tom2/bang":(
        ("MIDI", {"channel":0, "pitch":45 ,"status":"note_on"})
    ),
    "_general/sound/mid_tom2/off":(
        ("MIDI", {"channel":0, "pitch":45 ,"status":"note_off"})
    ),

    "_general/sound/open_hihat/bang":(
        ("MIDI", {"channel":0, "pitch":46 ,"status":"note_on"})
    ),
    "_general/sound/open_hihat/off":(
        ("MIDI", {"channel":0, "pitch":46 ,"status":"note_off"})
    ),

    "_general/sound/high_tom2/bang":(
        ("MIDI", {"channel":0, "pitch":48 ,"status":"note_on"})
    ),
    "_general/sound/high_tom2/off":(
        ("MIDI", {"channel":0, "pitch":48 ,"status":"note_off"})
    ),

    "_general/sound/crash_cymbal1/bang":(
        ("MIDI", {"channel":0, "pitch":49 ,"status":"note_on"})
    ),
    "_general/sound/crash_cymbal1/off":(
        ("MIDI", {"channel":0, "pitch":49 ,"status":"note_off"})
    ),

    "_general/sound/ride_cymbal1/bang":(
        ("MIDI", {"channel":0, "pitch":51 ,"status":"note_on"})
    ),
    "_general/sound/ride_cymbal1/off":(
        ("MIDI", {"channel":0, "pitch":51 ,"status":"note_off"})
    ),

    "_general/sound/mute_high_conga/bang":(
        ("MIDI", {"channel":0, "pitch":62 ,"status":"note_on"})
    ),
    "_general/sound/mute_high_conga/off":(
        ("MIDI", {"channel":0, "pitch":62 ,"status":"note_off"})
    ),

    "_general/sound/open_high_conga/bang":(
        ("MIDI", {"channel":0, "pitch":63 ,"status":"note_on"})
    ),
    "_general/sound/open_high_conga/off":(
        ("MIDI", {"channel":0, "pitch":63 ,"status":"note_off"})
    ),

    "_general/sound/high_timbale/bang":(
        ("MIDI", {"channel":0, "pitch":65 ,"status":"note_on"})
    ),
    "_general/sound/high_timbale/off":(
        ("MIDI", {"channel":0, "pitch":65 ,"status":"note_off"})
    ),

    "_general/sound/high_agogo/bang":(
        ("MIDI", {"channel":0, "pitch":67 ,"status":"note_on"})
    ),
    "_general/sound/high_agogo/off":(
        ("MIDI", {"channel":0, "pitch":67 ,"status":"note_off"})
    ),

    "_general/sound/low_agogo/bang":(
        ("MIDI", {"channel":0, "pitch":68 ,"status":"note_on"})
    ),
    "_general/sound/low_agogo/off":(
        ("MIDI", {"channel":0, "pitch":68 ,"status":"note_off"})
    ),

        ##### KICK ######

    "_kick/sound/kick_1/bang":(
        ("MIDI", {"channel":0, "pitch":79, "status":"note_on"})
    ),
    "_kick/sound/kick_1/off":(
        ("MIDI", {"channel":0, "pitch":79, "status":"note_off"})
    ),

    ##### SNARE ######

    "_snare/sound/snare_1/bang":(
        ("MIDI", {"channel":0, "pitch":79, "status":"note_on"})
    ),
    "_snare/sound/snare_1/off":(
        ("MIDI", {"channel":0, "pitch":79, "status":"note_off"})
    ),

    ##### TOM ######

    "_tom/sound/tom_1/bang":(
        ("MIDI", {"channel":0, "pitch":79, "status":"note_on"})
    ),
    "_tom/sound/tom_1/off":(
        ("MIDI", {"channel":0, "pitch":79, "status":"note_off"})
    ),

    ##### HIHAT ######

    "_hihat/sound/hihat_1/bang":(
        ("MIDI", {"channel":0, "pitch":79, "status":"note_on"})
    ),
    "_hihat/sound/hihat_1/off":(
        ("MIDI", {"channel":0, "pitch":79, "status":"note_off"})
    ),

    ##### CYMBAL ######

    "_cymbal/sound/cymbal_1/bang":(
        ("MIDI", {"channel":0, "pitch":79, "status":"note_on"})
    ),
    "_cymbal/sound/cymbal_1/off":(
        ("MIDI", {"channel":0, "pitch":79, "status":"note_off"})
    ),

    ##### PERCUSSION ######

    "_percussion/sound/percussion_1/bang":(
        ("MIDI", {"channel":0, "pitch":79, "status":"note_on"})
    ),
    "_percussion/sound/percussion_1/off":(
        ("MIDI", {"channel":0, "pitch":79, "status":"note_off"})
    ),

    ##### MISCELLANEOUS ######

    "_miscellaneous/sound/miscellaneous_1/bang":(
        ("MIDI", {"channel":0, "pitch":79, "status":"note_on"})
    ),
    "_miscellaneous/sound/miscellaneous_1/off":(
        ("MIDI", {"channel":0, "pitch":79, "status":"note_off"})
    ),
}