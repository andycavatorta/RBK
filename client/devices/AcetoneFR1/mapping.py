instruments = (
    "_system",
    "_general",
    #"_miscellaneous"
)


mapping = {
    "_general/sound/bass_drum/bang":(
        ("pulse", {"channel":4, "function": "pulse", "pulselength":0.2 })
    ),
    # "_general/sound/bass_drum/off":(
    #     ("digital", {"channel":21, "function": "digital", "bool":1 })
    # ),

    "_general/sound/snare_drum1/bang":(
        ("pulse", {"channel":5, "function": "pulse", "pulselength":0.2 })
    ),
    # "_general/sound/snare_drum1/off":(
    #     ("digital", {"channel":1, "value":38 ,"status":"note_off"})
    # ),

    "_general/sound/snare_drum2/bang":(
        ("pulse", {"channel":11, "function": "pulse", "pulselength":0.2 })
    ),
    # "_general/sound/snare_drum2/off":(
    #     ("digital", {"channel":1, "value":40 ,"status":"note_off"})
    # ),

    "_general/sound/crash_cymbal1/bang":(
        ("pulse", {"channel":6, "function": "pulse", "pulselength":0.2 })
    ),
    # "_general/sound/crash_cymbal1/off":(
    #     ("digital", {"channel":20, "function": "digital", "bool":1 })
    # ),

    "_general/sound/cowbell/bang":(
        ("pulse", {"channel":19, "function": "pulse", "pulselength":0.2 })
    ),
    # "_general/sound/cowbell/off":(
    #     ("digital", {"channel":18, "function": "digital", "bool":1 })
    # ),

    "_general/sound/high_bongo/bang":(
        ("pulse", {"channel":17, "function": "pulse", "pulselength":0.2 })
    ),
    # "_general/sound/high_bongo/off":(
    #     ("digital", {"channel":1, "value":60 ,"status":"note_off"})
    # ),

    "_general/sound/low_bongo/bang":(
        ("pulse", {"channel":15, "function": "pulse", "pulselength":0.2 })
    ),
    # "_general/sound/low_bongo/off":(
    #     ("digital", {"channel":1, "value":61 ,"status":"note_off"})
    # ),

    "_general/sound/low_conga/bang":(
        ("pulse", {"channel":13, "function": "pulse", "pulselength":0.2 })
    ),
    # "_general/sound/low_conga/off":(
    #     ("digital", {"channel":1, "value":64 ,"status":"note_off"})
    # ),

    "_general/sound/claves/bang":(
        ("pulse", {"channel":21, "function": "pulse", "pulselength":0.2 })
    ),
    # "_general/sound/claves/off":(
    #     ("digital", {"channel":19, "function": "digital", "bool":1 })
    # ),

    "_general/sound/maracas/bang":(
        ("pulse", {"channel":23, "function": "pulse", "pulselength":0.2 })
    ),
    # "_general/sound/maracas/off":(
    #     ("digital", {"channel":1, "value":70, "status":"note_off"})
    # ),

    "_general/control_change/Main_Volume":(
        ("square_wave", {"channel":3, "function": "square_wave", "frequency":30000})
    ),

    "_general/control_change/start_stop":(
        ("digital", {"channel":1, "function": "digital"})
    ),

    "_general/control_change/int_ext":(
        ("digital", {"channel":00, "function": "digital"})
    ),

    "_general/control_change/clock":(
        ("square_wave", {"channel":02, "function": "square_wave", "frequency":40})
    ),


    ##### SYSTEM ######

    # "_system/start":(
    #     ("digital", {"channel":2, "function": "digital", "bool":1})
    # ),

    # "_system/start":(
    #     ("digital", {"channel":2, "function": "digital", "bool":0})
    # ),

    # "_system/master_volume":(
    #     ("square_wave", {"channel":3, "function": "square_wave", "frequency":30000, "duty":50.0})
    # ),

    # "_system/int_ext":(
    #     ("digital", {"channel":14, "function": "digital", "bool":1})
    # ),

    # "_system/timing_clock":(
    #     ("square_wave", {"channel":14, "function": "square_wave", "frequency":40, "duty":50.0})
    # ),

}
