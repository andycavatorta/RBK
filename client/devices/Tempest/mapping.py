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
    "_general/sound/bass_drum/bang":(
        ("MIDI", {"channel":1, "pitch":36 ,"status":"note_on"})
    ),
    "_general/sound/bass_drum/off":(
        ("MIDI", {"channel":1, "pitch":36 ,"status":"note_off"})
    ),
    "_general/sound/side_stick/bang":(
        ("MIDI", {"channel":1, "pitch":37 ,"status":"note_on"})
    ),
    "_general/sound/side_stick/off":(
        ("MIDI", {"channel":1, "pitch":37 ,"status":"note_off"})
    ),

    "_general/sound/snare_drum1/bang":(
        ("MIDI", {"channel":1, "pitch":38 ,"status":"note_on"})
    ),
    "_general/sound/snare_drum1/off":(
        ("MIDI", {"channel":1, "pitch":38 ,"status":"note_off"})
    ),

    "_general/sound/hand_clap/bang":(
        ("MIDI", {"channel":1, "pitch":39 ,"status":"note_on"})
    ),
    "_general/sound/hand_clap/off":(
        ("MIDI", {"channel":1, "pitch":39 ,"status":"note_off"})
    ),

    "_general/sound/snare_drum2/bang":(
        ("MIDI", {"channel":1, "pitch":40 ,"status":"note_on"})
    ),
    "_general/sound/snare_drum2/off":(
        ("MIDI", {"channel":1, "pitch":40 ,"status":"note_off"})
    ),

    "_general/sound/closed_hihat/bang":(
        ("MIDI", {"channel":1, "pitch":42 ,"status":"note_on"})
    ),
    "_general/sound/closed_hihat/off":(
        ("MIDI", {"channel":1, "pitch":42 ,"status":"note_off"})
    ),

    "_general/sound/low_tom1/bang":(
        ("MIDI", {"channel":1, "pitch":43 ,"status":"note_on"})
    ),
    "_general/sound/low_tom1/off":(
        ("MIDI", {"channel":1, "pitch":43 ,"status":"note_off"})
    ),

    "_general/sound/open_hihat/bang":(
        ("MIDI", {"channel":1, "pitch":46 ,"status":"note_on"})
    ),
    "_general/sound/open_hihat/off":(
        ("MIDI", {"channel":1, "pitch":46 ,"status":"note_off"})
    ),

    "_general/sound/mid_tom1/bang":(
        ("MIDI", {"channel":1, "pitch":47 ,"status":"note_on"})
    ),
    "_general/sound/mid_tom1/off":(
        ("MIDI", {"channel":1, "pitch":47 ,"status":"note_off"})
    ),

    "_general/sound/crash_cymbal1/bang":(
        ("MIDI", {"channel":1, "pitch":49 ,"status":"note_on"})
    ),
    "_general/sound/crash_cymbal1/off":(
        ("MIDI", {"channel":1, "pitch":49 ,"status":"note_off"})
    ),

    "_general/sound/high_tom1/bang":(
        ("MIDI", {"channel":1, "pitch":50 ,"status":"note_on"})
    ),
    "_general/sound/high_tom1/off":(
        ("MIDI", {"channel":1, "pitch":50 ,"status":"note_off"})
    ),

    "_general/sound/ride_cymbal1/bang":(
        ("MIDI", {"channel":1, "pitch":51 ,"status":"note_on"})
    ),
    "_general/sound/ride_cymbal1/off":(
        ("MIDI", {"channel":1, "pitch":51 ,"status":"note_off"})
    ),

    "_general/sound/tambourine/bang":(
        ("MIDI", {"channel":1, "pitch":54 ,"status":"note_on"})
    ),
    "_general/sound/tambourine/off":(
        ("MIDI", {"channel":1, "pitch":54 ,"status":"note_off"})
    ),

    "_general/sound/splash_cymbal/bang":(
        ("MIDI", {"channel":1, "pitch":55 ,"status":"note_on"})
    ),
    "_general/sound/splash_cymbal/off":(
        ("MIDI", {"channel":1, "pitch":55 ,"status":"note_off"})
    ),

    "_general/sound/cabasa/bang":(
        ("MIDI", {"channel":1, "pitch":69 ,"status":"note_on"})
    ),
    "_general/sound/cabasa/off":(
        ("MIDI", {"channel":1, "pitch":69 ,"status":"note_off"})
    ),

    "_general/sound/low_woodblock/bang":(
        ("MIDI", {"channel":1, "pitch":127 ,"status":"note_on"})
    ),
    "_general/sound/low_woodblock/off":(
        ("MIDI", {"channel":1, "pitch":127 ,"status":"note_off"})
    ),

    "_general/pitch_wheel":(
        ("MIDI", {"status":"pitch_wheel"})
    ),

    ##### KICK ######

    "_kick/sound/kick_1/bang":(
        ("MIDI", {"channel":1, "pitch":79, "status":"note_on"})
    ),
    "_kick/sound/kick_1/off":(
        ("MIDI", {"channel":1, "pitch":79, "status":"note_off"})
    ),

    ##### SNARE ######

    "_snare/sound/snare_1/bang":(
        ("MIDI", {"channel":1, "pitch":79, "status":"note_on"})
    ),
    "_snare/sound/snare_1/off":(
        ("MIDI", {"channel":1, "pitch":79, "status":"note_off"})
    ),

    ##### TOM ######

    "_tom/sound/tom_1/bang":(
        ("MIDI", {"channel":1, "pitch":79, "status":"note_on"})
    ),
    "_tom/sound/tom_1/off":(
        ("MIDI", {"channel":1, "pitch":79, "status":"note_off"})
    ),

    ##### HIHAT ######

    "_hihat/sound/hihat_1/bang":(
        ("MIDI", {"channel":1, "pitch":79, "status":"note_on"})
    ),
    "_hihat/sound/hihat_1/off":(
        ("MIDI", {"channel":1, "pitch":79, "status":"note_off"})
    ),

    ##### CYMBAL ######

    "_cymbal/sound/cymbal_1/bang":(
        ("MIDI", {"channel":1, "pitch":79, "status":"note_on"})
    ),
    "_cymbal/sound/cymbal_1/off":(
        ("MIDI", {"channel":1, "pitch":79, "status":"note_off"})
    ),

    ##### PERCUSSION ######

    "_percussion/sound/percussion_1/bang":(
        ("MIDI", {"channel":1, "pitch":79, "status":"note_on"})
    ),
    "_percussion/sound/percussion_1/off":(
        ("MIDI", {"channel":1, "pitch":79, "status":"note_off"})
    ),

    ##### MISCELLANEOUS ######

    "_miscellaneous/sound/miscellaneous_1/bang":(
        ("MIDI", {"channel":1, "pitch":79, "status":"note_on"})
    ),
    "_miscellaneous/sound/miscellaneous_1/off":(
        ("MIDI", {"channel":1, "pitch":79, "status":"note_off"})
    ),
}
