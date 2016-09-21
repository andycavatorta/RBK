instruments = (
    "_system",
    "_general",
    "_kick",
    "_snare",
    "_tom",
    "_hihat",
    "_cymbal",
    "_percussion",
    #"_miscellaneous"
)


mapping = {
    "_general/sound/bass_drum2/bang":(
        ("MIDI", {"channel":1, "pitch":35 ,"status":"note_on"})
    ),
    "_general/sound/bass_drum2/off":(
        ("MIDI", {"channel":1, "pitch":35 ,"status":"note_off"})
    ),

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

    "_general/sound/low_tom2/bang":(
        ("MIDI", {"channel":1, "pitch":41 ,"status":"note_on"})
    ),
    "_general/sound/low_tom2/off":(
        ("MIDI", {"channel":1, "pitch":41 ,"status":"note_off"})
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

    "_general/sound/pedal_hihat/bang":(
        ("MIDI", {"channel":1, "pitch":44 ,"status":"note_on"})
    ),
    "_general/sound/pedal_hihat/off":(
        ("MIDI", {"channel":1, "pitch":44 ,"status":"note_off"})
    ),

    "_general/sound/mid_tom2/bang":(
        ("MIDI", {"channel":1, "pitch":45 ,"status":"note_on"})
    ),
    "_general/sound/mid_tom2/off":(
        ("MIDI", {"channel":1, "pitch":45 ,"status":"note_off"})
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

    "_general/sound/high_tom2/bang":(
        ("MIDI", {"channel":1, "pitch":48 ,"status":"note_on"})
    ),
    "_general/sound/high_tom2/off":(
        ("MIDI", {"channel":1, "pitch":48 ,"status":"note_off"})
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

    "_general/sound/ride_bell/bang":(
        ("MIDI", {"channel":1, "pitch":53 ,"status":"note_on"})
    ),
    "_general/sound/ride_bell/off":(
        ("MIDI", {"channel":1, "pitch":53 ,"status":"note_off"})
    ),

    "_general/sound/tambourine/bang":(
        ("MIDI", {"channel":1, "pitch":54 ,"status":"note_on"})
    ),
    "_general/sound/tambourine/off":(
        ("MIDI", {"channel":1, "pitch":54 ,"status":"note_off"})
    ),

    "_general/sound/cowbell/bang":(
        ("MIDI", {"channel":1, "pitch":56 ,"status":"note_on"})
    ),
    "_general/sound/cowbell/off":(
        ("MIDI", {"channel":1, "pitch":56 ,"status":"note_off"})
    ),

    "_general/sound/crash_cymbal2/bang":(
        ("MIDI", {"channel":1, "pitch":57 ,"status":"note_on"})
    ),
    "_general/sound/crash_cymbal2/off":(
        ("MIDI", {"channel":1, "pitch":57 ,"status":"note_off"})
    ),

    "_general/sound/high_bongo/bang":(
        ("MIDI", {"channel":1, "pitch":60 ,"status":"note_on"})
    ),
    "_general/sound/high_bongo/off":(
        ("MIDI", {"channel":1, "pitch":60 ,"status":"note_off"})
    ),

    "_general/sound/low_bongo/bang":(
        ("MIDI", {"channel":1, "pitch":61 ,"status":"note_on"})
    ),
    "_general/sound/low_bongo/off":(
        ("MIDI", {"channel":1, "pitch":61 ,"status":"note_off"})
    ),

    "_general/sound/mute_high_conga/bang":(
        ("MIDI", {"channel":1, "pitch":62 ,"status":"note_on"})
    ),
    "_general/sound/mute_high_conga/off":(
        ("MIDI", {"channel":1, "pitch":62 ,"status":"note_off"})
    ),

    "_general/sound/open_high_conga/bang":(
        ("MIDI", {"channel":1, "pitch":63 ,"status":"note_on"})
    ),
    "_general/sound/open_high_conga/off":(
        ("MIDI", {"channel":1, "pitch":63 ,"status":"note_off"})
    ),

    "_general/sound/low_conga/bang":(
        ("MIDI", {"channel":1, "pitch":64 ,"status":"note_on"})
    ),
    "_general/sound/low_conga/off":(
        ("MIDI", {"channel":1, "pitch":64 ,"status":"note_off"})
    ),

    "_general/sound/high_timbale/bang":(
        ("MIDI", {"channel":1, "pitch":65 ,"status":"note_on"})
    ),
    "_general/sound/high_timbale/off":(
        ("MIDI", {"channel":1, "pitch":65 ,"status":"note_off"})
    ),

    "_general/sound/low_timbale/bang":(
        ("MIDI", {"channel":1, "pitch":66 ,"status":"note_on"})
    ),
    "_general/sound/low_timbale/off":(
        ("MIDI", {"channel":1, "pitch":66 ,"status":"note_off"})
    ),

    "_general/sound/high_agogo/bang":(
        ("MIDI", {"channel":1, "pitch":67 ,"status":"note_on"})
    ),
    "_general/sound/high_agogo/off":(
        ("MIDI", {"channel":1, "pitch":67 ,"status":"note_off"})
    ),

    "_general/sound/low_agogo/bang":(
        ("MIDI", {"channel":1, "pitch":68 ,"status":"note_on"})
    ),
    "_general/sound/low_agogo/off":(
        ("MIDI", {"channel":1, "pitch":68 ,"status":"note_off"})
    ),

    "_general/sound/cabasa/bang":(
        ("MIDI", {"channel":1, "pitch":69 ,"status":"note_on"})
    ),
    "_general/sound/cabasa/off":(
        ("MIDI", {"channel":1, "pitch":69 ,"status":"note_off"})
    ),

    "_general/sound/claves/bang":(
        ("MIDI", {"channel":1, "pitch":75 ,"status":"note_on"})
    ),
    "_general/sound/claves/off":(
        ("MIDI", {"channel":1, "pitch":75 ,"status":"note_off"})
    ),

    ##### KICK ######

    "_kick/sound/kick_1/bang":(
        ("MIDI", {"channel":1, "pitch":36 ,"status":"note_on"})
    ),
    "_kick/sound/kick_1/off":(
        ("MIDI", {"channel":1, "pitch":36 ,"status":"note_off"})
    ),

    "_kick/sound/kick_2/bang":(
        ("MIDI", {"channel":1, "pitch":35 ,"status":"note_on"})
    ),
    "_kick/sound/kick_2/off":(
        ("MIDI", {"channel":1, "pitch":35 ,"status":"note_off"})
    ),

    "_kick/sound/kick_3/bang":(
        ("MIDI", {"channel":1, "pitch":15 ,"status":"note_on"})
    ),
    "_kick/sound/kick_3/off":(
        ("MIDI", {"channel":1, "pitch":15 ,"status":"note_off"})
    ),

    "_kick/sound/kick_4/bang":(
        ("MIDI", {"channel":1, "pitch":19 ,"status":"note_on"})
    ),
    "_kick/sound/kick_4/off":(
        ("MIDI", {"channel":1, "pitch":19 ,"status":"note_off"})
    ),

    "_kick/sound/kick_5/bang":(
        ("MIDI", {"channel":1, "pitch":23 ,"status":"note_on"})
    ),
    "_kick/sound/kick_5/off":(
        ("MIDI", {"channel":1, "pitch":23 ,"status":"note_off"})
    ),

    ##### SNARE ######

    "_snare/sound/snare_1/bang":(
        ("MIDI", {"channel":1, "pitch":38 ,"status":"note_on"})
    ),
    "_snare/sound/snare_1/off":(
        ("MIDI", {"channel":1, "pitch":38 ,"status":"note_off"})
    ),

    "_snare/sound/snare_2/bang":(
        ("MIDI", {"channel":1, "pitch":40 ,"status":"note_on"})
    ),
    "_snare/sound/snare_2/off":(
        ("MIDI", {"channel":1, "pitch":40 ,"status":"note_off"})
    ),

    "_snare/sound/snare_3/bang":(
        ("MIDI", {"channel":1, "pitch":16 ,"status":"note_on"})
    ),
    "_snare/sound/snare_3/off":(
        ("MIDI", {"channel":1, "pitch":16 ,"status":"note_off"})
    ),

    "_snare/sound/snare_4/bang":(
        ("MIDI", {"channel":1, "pitch":20 ,"status":"note_on"})
    ),
    "_snare/sound/snare_4/off":(
        ("MIDI", {"channel":1, "pitch":20 ,"status":"note_off"})
    ),

    "_snare/sound/snare_5/bang":(
        ("MIDI", {"channel":1, "pitch":24 ,"status":"note_on"})
    ),
    "_snare/sound/snare_5/off":(
        ("MIDI", {"channel":1, "pitch":24 ,"status":"note_off"})
    ),

    "_snare/sound/snare_6/bang":(
        ("MIDI", {"channel":1, "pitch":37 ,"status":"note_on"})
    ),
    "_snare/sound/snare_6/off":(
        ("MIDI", {"channel":1, "pitch":37 ,"status":"note_off"})
    ),

    ##### TOM ######

    "_tom/sound/tom_1/bang":(
        ("MIDI", {"channel":1, "pitch":41 ,"status":"note_on"})
    ),
    "_tom/sound/tom_1/off":(
        ("MIDI", {"channel":1, "pitch":41 ,"status":"note_off"})
    ),

    "_tom/sound/tom_2/bang":(
        ("MIDI", {"channel":1, "pitch":43 ,"status":"note_on"})
    ),
    "_tom/sound/tom_2/off":(
        ("MIDI", {"channel":1, "pitch":43 ,"status":"note_off"})
    ),

    "_tom/sound/tom_3/bang":(
        ("MIDI", {"channel":1, "pitch":45 ,"status":"note_on"})
    ),
    "_tom/sound/tom_3/off":(
        ("MIDI", {"channel":1, "pitch":45 ,"status":"note_off"})
    ),

    "_tom/sound/tom_4/bang":(
        ("MIDI", {"channel":1, "pitch":47 ,"status":"note_on"})
    ),
    "_tom/sound/tom_4/off":(
        ("MIDI", {"channel":1, "pitch":47 ,"status":"note_off"})
    ),

    "_tom/sound/tom_5/bang":(
        ("MIDI", {"channel":1, "pitch":48 ,"status":"note_on"})
    ),
    "_tom/sound/tom_5/off":(
        ("MIDI", {"channel":1, "pitch":48 ,"status":"note_off"})
    ),

    "_tom/sound/tom_6/bang":(
        ("MIDI", {"channel":1, "pitch":50 ,"status":"note_on"})
    ),
    "_tom/sound/tom_6/off":(
        ("MIDI", {"channel":1, "pitch":50 ,"status":"note_off"})
    ),

    "_tom/sound/tom_7/bang":(
        ("MIDI", {"channel":1, "pitch":21 ,"status":"note_on"})
    ),
    "_tom/sound/tom_7/off":(
        ("MIDI", {"channel":1, "pitch":21 ,"status":"note_off"})
    ),

    "_tom/sound/tom_8/bang":(
        ("MIDI", {"channel":1, "pitch":22 ,"status":"note_on"})
    ),
    "_tom/sound/tom_8/off":(
        ("MIDI", {"channel":1, "pitch":22 ,"status":"note_off"})
    ),

    ##### HIHAT ######

    "_hihat/sound/hihat_1/bang":(
        ("MIDI", {"channel":1, "pitch":42 ,"status":"note_on"})
    ),
    "_hihat/sound/hihat_1/off":(
        ("MIDI", {"channel":1, "pitch":42 ,"status":"note_off"})
    ),

    "_hihat/sound/hihat_2/bang":(
        ("MIDI", {"channel":1, "pitch":44 ,"status":"note_on"})
    ),
    "_hihat/sound/hihat_2/off":(
        ("MIDI", {"channel":1, "pitch":44 ,"status":"note_off"})
    ),

    "_hihat/sound/hihat_3/bang":(
        ("MIDI", {"channel":1, "pitch":46 ,"status":"note_on"})
    ),
    "_hihat/sound/hihat_3/off":(
        ("MIDI", {"channel":1, "pitch":46 ,"status":"note_off"})
    ),

    "_hihat/sound/hihat_4/bang":(
        ("MIDI", {"channel":1, "pitch":17 ,"status":"note_on"})
    ),
    "_hihat/sound/hihat_4/off":(
        ("MIDI", {"channel":1, "pitch":17 ,"status":"note_off"})
    ),

    "_hihat/sound/hihat_5/bang":(
        ("MIDI", {"channel":1, "pitch":18 ,"status":"note_on"})
    ),
    "_hihat/sound/hihat_5/off":(
        ("MIDI", {"channel":1, "pitch":18 ,"status":"note_off"})
    ),

    "_hihat/sound/hihat_6/bang":(
        ("MIDI", {"channel":1, "pitch":25 ,"status":"note_on"})
    ),
    "_hihat/sound/hihat_6/off":(
        ("MIDI", {"channel":1, "pitch":25 ,"status":"note_off"})
    ),

    "_hihat/sound/hihat_7/bang":(
        ("MIDI", {"channel":1, "pitch":26 ,"status":"note_on"})
    ),
    "_hihat/sound/hihat_7/off":(
        ("MIDI", {"channel":1, "pitch":26 ,"status":"note_off"})
    ),


    ##### CYMBAL ######

    "_cymbal/sound/cymbal_1/bang":(
        ("MIDI", {"channel":1, "pitch":49 ,"status":"note_on"})
    ),
    "_cymbal/sound/cymbal_1/off":(
        ("MIDI", {"channel":1, "pitch":49 ,"status":"note_off"})
    ),

    "_cymbal/sound/cymbal_2/bang":(
        ("MIDI", {"channel":1, "pitch":51 ,"status":"note_on"})
    ),
    "_cymbal/sound/cymbal_2/off":(
        ("MIDI", {"channel":1, "pitch":51 ,"status":"note_off"})
    ),

    "_cymbal/sound/cymbal_3/bang":(
        ("MIDI", {"channel":1, "pitch":53 ,"status":"note_on"})
    ),
    "_cymbal/sound/cymbal_3/off":(
        ("MIDI", {"channel":1, "pitch":53 ,"status":"note_off"})
    ),

    "_cymbal/sound/cymbal_4/bang":(
        ("MIDI", {"channel":1, "pitch":57 ,"status":"note_on"})
    ),
    "_cymbal/sound/cymbal_4/off":(
        ("MIDI", {"channel":1, "pitch":57 ,"status":"note_off"})
    ),

    ##### PERCUSSION ######

    "_percussion/sound/percussion_1/bang":(
        ("MIDI", {"channel":1, "pitch":54 ,"status":"note_on"})
    ),
    "_percussion/sound/percussion_1/off":(
        ("MIDI", {"channel":1, "pitch":54 ,"status":"note_off"})
    ),

    "_percussion/sound/percussion_2/bang":(
        ("MIDI", {"channel":1, "pitch":56 ,"status":"note_on"})
    ),
    "_percussion/sound/percussion_2/off":(
        ("MIDI", {"channel":1, "pitch":56 ,"status":"note_off"})
    ),

    "_percussion/sound/percussion_3/bang":(
        ("MIDI", {"channel":1, "pitch":60 ,"status":"note_on"})
    ),
    "_percussion/sound/percussion_3/off":(
        ("MIDI", {"channel":1, "pitch":60 ,"status":"note_off"})
    ),

    "_percussion/sound/percussion_4/bang":(
        ("MIDI", {"channel":1, "pitch":61 ,"status":"note_on"})
    ),
    "_percussion/sound/percussion_4/off":(
        ("MIDI", {"channel":1, "pitch":61 ,"status":"note_off"})
    ),

    "_percussion/sound/percussion_5/bang":(
        ("MIDI", {"channel":1, "pitch":62 ,"status":"note_on"})
    ),
    "_percussion/sound/percussion_5/off":(
        ("MIDI", {"channel":1, "pitch":62 ,"status":"note_off"})
    ),

    "_percussion/sound/percussion_6/bang":(
        ("MIDI", {"channel":1, "pitch":63 ,"status":"note_on"})
    ),
    "_percussion/sound/percussion_6/off":(
        ("MIDI", {"channel":1, "pitch":63 ,"status":"note_off"})
    ),

    "_percussion/sound/percussion_7/bang":(
        ("MIDI", {"channel":1, "pitch":64 ,"status":"note_on"})
    ),
    "_percussion/sound/percussion_7/off":(
        ("MIDI", {"channel":1, "pitch":64 ,"status":"note_off"})
    ),

    "_percussion/sound/percussion_8/bang":(
        ("MIDI", {"channel":1, "pitch":65 ,"status":"note_on"})
    ),
    "_percussion/sound/percussion_8/off":(
        ("MIDI", {"channel":1, "pitch":65 ,"status":"note_off"})
    ),

    "_percussion/sound/percussion_9/bang":(
        ("MIDI", {"channel":1, "pitch":66 ,"status":"note_on"})
    ),
    "_percussion/sound/percussion_9/off":(
        ("MIDI", {"channel":1, "pitch":66 ,"status":"note_off"})
    ),

    "_percussion/sound/percussion_10/bang":(
        ("MIDI", {"channel":1, "pitch":67 ,"status":"note_on"})
    ),
    "_percussion/sound/percussion_10/off":(
        ("MIDI", {"channel":1, "pitch":67 ,"status":"note_off"})
    ),

    "_percussion/sound/percussion_11/bang":(
        ("MIDI", {"channel":1, "pitch":68 ,"status":"note_on"})
    ),
    "_percussion/sound/percussion_11/off":(
        ("MIDI", {"channel":1, "pitch":68 ,"status":"note_off"})
    ),

    "_percussion/sound/percussion_12/bang":(
        ("MIDI", {"channel":1, "pitch":69 ,"status":"note_on"})
    ),
    "_percussion/sound/percussion_12/off":(
        ("MIDI", {"channel":1, "pitch":69 ,"status":"note_off"})
    ),

    "_percussion/sound/percussion_13/bang":(
        ("MIDI", {"channel":1, "pitch":75 ,"status":"note_on"})
    ),
    "_percussion/sound/percussion_13/off":(
        ("MIDI", {"channel":1, "pitch":75 ,"status":"note_off"})
    ),

    "_percussion/sound/percussion_14/bang":(
        ("MIDI", {"channel":1, "pitch":27 ,"status":"note_on"})
    ),
    "_percussion/sound/percussion_14/off":(
        ("MIDI", {"channel":1, "pitch":27 ,"status":"note_off"})
    ),

    "_percussion/sound/percussion_15/bang":(
        ("MIDI", {"channel":1, "pitch":28 ,"status":"note_on"})
    ),
    "_percussion/sound/percussion_15/off":(
        ("MIDI", {"channel":1, "pitch":28 ,"status":"note_off"})
    ),

    "_percussion/sound/percussion_16/bang":(
        ("MIDI", {"channel":1, "pitch":29 ,"status":"note_on"})
    ),
    "_percussion/sound/percussion_16/off":(
        ("MIDI", {"channel":1, "pitch":29 ,"status":"note_off"})
    ),

    "_percussion/sound/percussion_17/bang":(
        ("MIDI", {"channel":1, "pitch":30 ,"status":"note_on"})
    ),
    "_percussion/sound/percussion_17/off":(
        ("MIDI", {"channel":1, "pitch":30 ,"status":"note_off"})
    ),


    ##### MISCELLANEOUS ######

    "_miscellaneous/sound/miscellaneous_1/bang":(
        ("MIDI", {"channel":1, "pitch":79, "status":"note_on"})
    ),
    "_miscellaneous/sound/miscellaneous_1/off":(
        ("MIDI", {"channel":1, "pitch":79, "status":"note_off"})
    ),


}
