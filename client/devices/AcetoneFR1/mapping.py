instruments = (
    "_system",
    "_general",
    #"_miscellaneous"
)


mapping = {
    "_general/sound/bass_drum/bang":(
        ("signal", {"channel":4, "function": "digital", "bool": 1 })
    ),
    "_general/sound/bass_drum/off":(
        ("signal", {"channel":4, "function": "digital", "bool": 0 })
    ),

    "_general/control_change/acetone_bass_off":(
        ("signal", {"channel":14, "function": "digital"})
    ),

    "_general/sound/snare_drum1/bang":(
        ("signal", {"channel":5, "function": "digital", "bool":1 })
    ),

    "_general/sound/snare_drum1/off":(
        ("signal", {"channel":5, "function": "digital", "bool":0 })
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
        ("signal", {"channel":6, "function": "digital", "bool": 1 })
    ),

    "_general/sound/crash_cymbal1/off":(
        ("signal", {"channel":6, "function": "digital", "bool":0 })
    ),

    "_general/control_change/acetone_cymbal_off":(
        ("signal", {"channel":12, "function": "digital"})
    ),

    "_general/sound/cowbell/bang":(
        ("signal", {"channel":19, "function": "digital", "bool": 1 })
    ),

    "_general/sound/cowbell/off":(
        ("signal", {"channel":19, "function": "digital", "bool": 0 })
    ),


    "_general/control_change/acetone_cowbell_off":(
        ("signal", {"channel":8, "function": "digital"})
    ),

    "_general/sound/high_bongo/bang":(
        ("signal", {"channel":17, "function": "digital", "bool": 1 })
    ),

    "_general/sound/high_bongo/off":(
        ("signal", {"channel":17, "function": "digital", "bool": 0 })
    ),

    "_general/sound/low_bongo/bang":(
        ("signal", {"channel":15, "function": "digital", "bool": 1 })
    ),

    "_general/sound/low_bongo/off":(
        ("signal", {"channel":15, "function": "digital", "bool": 0 })
    ),

    # "_general/sound/low_bongo/off":(
    #     ("digital", {"channel":1, "value":61 ,"status":"note_off"})
    # ),

    "_general/sound/low_conga/bang":(
        ("signal", {"channel":13, "function": "digital", "bool": 1 })
    ),

    "_general/sound/low_conga/off":(
        ("signal", {"channel":13, "function": "digital", "bool": 0 })
    ),

    # "_general/sound/low_conga/off":(
    #     ("digital", {"channel":1, "value":64 ,"status":"note_off"})
    # ),

    "_general/sound/claves/bang":(
        ("signal", {"channel":21, "function": "digital", "bool": 1 })
    ),

    "_general/sound/claves/off":(
        ("signal", {"channel":21, "function": "digital", "bool": 0 })
    ),


    "_general/control_change/acetone_claves_off":(
        ("signal", {"channel":10, "function": "digital"})
    ),

    "_general/sound/maracas/bang":(
        ("signal", {"channel":23, "function": "digital", "bool": 1})
    ),

    "_general/sound/maracas/off":(
        ("signal", {"channel":23, "function": "digital", "bool": 0})
    ),

    # "_general/sound/maracas/off":(
    #     ("digital", {"channel":1, "value":70, "status":"note_off"})
    # ),

    "_general/control_change/Main_Volume":(
        ("signal", {"channel":3, "function": "square_wave", "frequency":30000, "duty cycle":0, "freq_min_max":(30000,30000), "duty_min_max":(0,100), "variable_key":"duty_cycle"})
    ),

    "_general/control_change/start_stop":(
        ("signal", {"channel":1, "function": "digital"})
    ),

    "_general/control_change/start":(
        ("signal", {"channel":1, "function": "digital", "bool": 1})
    ),

    "_general/control_change/stop":(
        ("signal", {"channel":1, "function": "digital", "bool": 0})
    ),

    "_general/control_change/int_ext":(
        ("signal", {"channel":0, "function": "digital"})
    ),

    "_general/control_change/clock":(
        ("signal", {"channel":02, "function": "square_wave", "frequency":0, "duty cycle":20.0, "freq_min_max":(9,100), "duty_min_max":(1,1), "variable_key":"frequency"})
    ),

    "_general/control_change/master_tempo":(
        ("signal", {"channel":02, "function": "square_wave", "frequency":0, "duty cycle":20.0, "freq_min_max":(9,100), "duty_min_max":(1,1), "variable_key":"frequency"})
    ),

}
