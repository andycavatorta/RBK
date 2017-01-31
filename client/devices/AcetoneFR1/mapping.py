instruments = (
    "_system",
    "_general",
    #"_miscellaneous"
)


mapping = {
    "_general/sound/bass_drum/bang":(
        ("signal", {"channel":4, "function": "pulse", "pulselength":0.2 })
    ),
    "_general/control_change/acetone_bass_off":(
        ("signal", {"channel":14, "function": "digital"})
    ),

    "_general/sound/snare_drum1/bang":(
        ("signal", {"channel":5, "function": "pulse", "pulselength":0.2 })
    ),

    # "_general/sound/snare_drum1/off":(
    #     ("digital", {"channel":1, "value":38 ,"status":"note_off"})
    # ),

    "_general/sound/snare_drum2/bang":(
        ("signal", {"channel":11, "function": "digital", "bool":1 })
    ),
    "_general/sound/snare_drum2/off":(
        ("signal", {"channel":11, "function": "digital" ,"bool":0})
    ),

    "_general/sound/crash_cymbal1/bang":(
        ("signal", {"channel":6, "function": "pulse", "pulselength":0.2 })
    ),
    "_general/control_change/acetone_cymbal_off":(
        ("signal", {"channel":12, "function": "digital"})
    ),

    "_general/sound/cowbell/bang":(
        ("signal", {"channel":19, "function": "pulse", "pulselength":0.2 })
    ),
    "_general/control_change/acetone_cowbell_off":(
        ("signal", {"channel":8, "function": "digital"})
    ),

    "_general/sound/high_bongo/bang":(
        ("signal", {"channel":17, "function": "pulse", "pulselength":0.2 })
    ),

    # "_general/sound/high_bongo/off":(
    #     ("digital", {"channel":1, "value":60 ,"status":"note_off"})
    # ),

    "_general/sound/low_bongo/bang":(
        ("signal", {"channel":15, "function": "pulse", "pulselength":0.2 })
    ),

    # "_general/sound/low_bongo/off":(
    #     ("digital", {"channel":1, "value":61 ,"status":"note_off"})
    # ),

    "_general/sound/low_conga/bang":(
        ("signal", {"channel":13, "function": "pulse", "pulselength":0.2 })
    ),

    # "_general/sound/low_conga/off":(
    #     ("digital", {"channel":1, "value":64 ,"status":"note_off"})
    # ),

    "_general/sound/claves/bang":(
        ("signal", {"channel":21, "function": "pulse", "pulselength":0.2 })
    ),
    "_general/control_change/acetone_claves_off":(
        ("signal", {"channel":10, "function": "digital"})
    ),

    "_general/sound/maracas/bang":(
        ("signal", {"channel":23, "function": "pulse", "pulselength":0.2})
    ),

    # "_general/sound/maracas/off":(
    #     ("digital", {"channel":1, "value":70, "status":"note_off"})
    # ),

    "_general/control_change/Main_Volume":(
        ("signal", {"channel":3, "function": "square_wave", "frequency":30000, "duty_cycle":duty_cycle, "freq_min_max":(1,1), "duty_min_max":(0,100)})
    ),

    "_general/control_change/start_stop":(
        ("signal", {"channel":1, "function": "digital"})
    ),

    "_general/control_change/int_ext":(
        ("signal", {"channel":00, "function": "digital"})
    ),

    "_general/control_change/clock":(
        ("signal", {"channel":02, "function": "square_wave", "frequency":frequency, "duty_cycle":50.0, "freq_min_max":(9,40), "duty_min_max":(1,1)})
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
