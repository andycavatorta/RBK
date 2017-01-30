instruments = (
    "_system",
    "_general",
    #"_miscellaneous"
)


mapping = {
    "_general/sound/bass_drum/bang":(
        ("pulse", {"channel":4, "function": "pulse", "pulselength":0.02 })
    ),
    # "_general/sound/bass_drum/off":(
    #     ("digital", {"channel":21, "function": "digital", "bool":1 })
    # ),

    "_general/sound/snare_drum1/bang":(
        ("pulse", {"channel":5, "function": "pulse", "pulselength":0.02 })
    ),
    # "_general/sound/snare_drum1/off":(
    #     ("digital", {"channel":1, "value":38 ,"status":"note_off"})
    # ),

    "_general/sound/snare_drum2/bang":(
        ("digital", {"channel":13, "function": "digital", "bool":1 }),
        ("digital", {"channel":23,"function": "digital", "bool":0})
    ),

    "_general/sound/snare_drum2/off":(
        ("digital", {"channel":23, "function": "digital", "bool":1}),
        ("digital", {"channel":13, "function": "digital", "bool":0 })
    ),

    "_general/sound/high_woodblock/bang":(
        ("pulse", {"channel":9, "function": "pulse", "pulselength":0.02 })
    ),

    "_general/sound/high_bongo/bang":(
        ("pulse", {"channel":7, "function": "pulse", "pulselength":0.02 })
    ),

    "_general/control_change/Main_Volume":(
        ("square_wave_duty", {"channel":3, "function": "square_wave", "frequency":30000})
    ),

    "_general/control_change/start_stop":(
        ("digital", {"channel":1, "function": "digital"})
    ),

    "_general/control_change/int_ext":(
        ("digital", {"channel":0, "function": "digital"})
    ),

    "_general/control_change/clock":(
        ("square_wave", {"channel":2, "function": "square_wave", "frequency":11})
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
