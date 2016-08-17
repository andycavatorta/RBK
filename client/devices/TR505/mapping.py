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
    "/sound/tom_1/bang":(
        ("MIDI", {"channel":1, "pitch":48 ,"status":"note_on"})
    ),
    "/sound/tom_1/off":(
        ("MIDI", {"channel":1, "pitch":48 ,"status":"note_off"})
    ),

    "/sound/tom_2/bang":(
        ("MIDI", {"channel":1, "pitch":48 ,"status":"note_on"})
    ),
    "/sound/tom_2/off":(
        ("MIDI", {"channel":1, "pitch":48 ,"status":"note_off"})
    ),

    "/sound//bang":(
        ("MIDI", {"channel":1, "pitch":45 ,"status":"note_on"})
    ),
    "/sound//off":(
        ("MIDI", {"channel":1, "pitch":45 ,"status":"note_off"})
    ),

    "/sound/tom_3/bang":(
        ("MIDI", {"channel":1, "pitch":41 ,"status":"note_on"})
    ),
    "/sound/tom_3/off":(
        ("MIDI", {"channel":1, "pitch":41 ,"status":"note_off"})
    ),

    "/sound/tom_4/bang":(
        ("MIDI", {"channel":1, "pitch":63 ,"status":"note_on"})
    ),
    "/sound/tom_4/off":(
        ("MIDI", {"channel":1, "pitch":63 ,"status":"note_off"})
    ),

    "/sound/ride/bang":(
        ("MIDI", {"channel":1, "pitch":51 ,"status":"note_on"})
    ),
    "/sound/ride/off":(
        ("MIDI", {"channel":1, "pitch":51 ,"status":"note_off"})
    ),

    "/sound/crash/bang":(
        ("MIDI", {"channel":1, "pitch":49 ,"status":"note_on"})
    ),
    "/sound/crash/off":(
        ("MIDI", {"channel":1, "pitch":49 ,"status":"note_off"})
    ),

    "/sound/perc_1/bang":(
        ("MIDI", {"channel":1, "pitch":65 ,"status":"note_on"})
    ),
    "/sound/perc_1/off":(
        ("MIDI", {"channel":1, "pitch":65 ,"status":"note_off"})
    ),

    "/sound/perc_2/bang":(
        ("MIDI", {"channel":1, "pitch":62 ,"status":"note_on"})
    ),
    "/sound/perc_2/off":(
        ("MIDI", {"channel":1, "pitch":62 ,"status":"note_off"})
    ),

    "/sound/kick/bang":(
        ("MIDI", {"channel":1, "pitch":35 ,"status":"note_on"})
    ),
    "/sound/kick/off":(
        ("MIDI", {"channel":1, "pitch":35 ,"status":"note_off"})
    ),

    "/sound/snare/bang":(
        ("MIDI", {"channel":1, "pitch":38 ,"status":"note_on"})
    ),
    "/sound/snare/off":(
        ("MIDI", {"channel":1, "pitch":38 ,"status":"note_off"})
    ),

    "/sound/closed_hat/bang":(
        ("MIDI", {"channel":1, "pitch":42 ,"status":"note_on"})
    ),
    "/sound/closed_hat/off":(
        ("MIDI", {"channel":1, "pitch":42 ,"status":"note_off"})
    ),

    "/sound/mid_hat/bang":(
        ("MIDI", {"channel":1, "pitch":44 ,"status":"note_on"})
    ),
    "/sound/mid_hat/off":(
        ("MIDI", {"channel":1, "pitch":44 ,"status":"note_off"})
    ),

    "/sound/open_hat/bang":(
        ("MIDI", {"channel":1, "pitch":46 ,"status":"note_on"})
    ),
    "/sound/open_hat/off":(
        ("MIDI", {"channel":1, "pitch":46 ,"status":"note_off"})
    ),

    "/sound/claps/bang":(
        ("MIDI", {"channel":1, "pitch":39 ,"status":"note_on"})
    ),
    "/sound/clapsperc_3/off":(
        ("MIDI", {"channel":1, "pitch":39 ,"status":"note_off"})
    ),

    "/sound/perc_3/bang":(
        ("MIDI", {"channel":1, "pitch":67 ,"status":"note_on"})
    ),
    "/sound/perc_3/off":(
        ("MIDI", {"channel":1, "pitch":67 ,"status":"note_off"})
    ),

    "/sound/perc_4/bang":(
        ("MIDI", {"channel":1, "pitch":68 ,"status":"note_on"})
    ),
    "/sound/perc_4/off":(
        ("MIDI", {"channel":1, "pitch":68 ,"status":"note_off"})
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
