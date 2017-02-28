instruments = (
    "_system",
    "_general",
    # "_trigger",
    # "_sensitivity",
    # "_pitch",
    # "_decay",
    # "_sweep",
    # "_lforate",
    # "_lfodepth",
)


mapping = {
    "_general/sound/bass_drum/bang":(
        ("signal", {"channel":10, "function": "digital", "bool":1 })
    ),

    "_general/sound/bass_drum/off":(
        ("signal", {"channel":10, "function": "digital", "bool":0 })
    ),

    "_general/control_change/sensitivity":(
        ("signal", {"channel":12, "function": "square_wave", "frequency":30000, "duty cycle":0, "freq_min_max":(1,1), "duty_min_max":(0,100), "variable_key":"duty_cycle"})
    ),

    "_general/control_change/pitch":(
        ("signal", {"channel":14, "function": "square_wave", "frequency":30000, "duty cycle":0, "freq_min_max":(1,1), "duty_min_max":(0,100), "variable_key":"duty_cycle"})
    ),

    "_general/control_change/decay":(
        ("signal", {"channel":16, "function": "square_wave", "frequency":30000, "duty cycle":0, "freq_min_max":(1,1), "duty_min_max":(0,100), "variable_key":"duty_cycle"})
    ),

    "_general/control_change/sweep":(
        ("signal", {"channel":18, "function": "square_wave", "frequency":30000, "duty cycle":0, "freq_min_max":(1,1), "duty_min_max":(0,100), "variable_key":"duty_cycle"})
    ),

    "_general/control_change/lfo_rate":(
        ("signal", {"channel":20, "function": "square_wave", "frequency":30000, "duty cycle":0, "freq_min_max":(1,1), "duty_min_max":(0,100), "variable_key":"duty_cycle"})
    ),

    "_general/control_change/lfo_depth":(
        ("signal", {"channel":22, "function": "square_wave", "frequency":30000, "duty cycle":0, "freq_min_max":(1,1), "duty_min_max":(0,100), "variable_key":"duty_cycle"})
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
