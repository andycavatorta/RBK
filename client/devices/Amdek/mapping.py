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
        ("pulse", {"channel":10, "function": "pulse", "pulselength":0.2 })
    ),

    "_general/control_change/sensitivity":(
        ("square_wave", {"channel":12, "function": "square_wave", "frequency":30000})
    ),

    "_general/control_change/pitch":(
        ("square_wave", {"channel":14, "function": "square_wave", "frequency":30000})
    ),

    "_general/control_change/decay":(
        ("square_wave", {"channel":16, "function": "square_wave", "frequency":30000})
    ),

    "_general/control_change/sweep":(
        ("square_wave", {"channel":18, "function": "square_wave", "frequency":30000})
    ),

    "_general/control_change/lfo_rate":(
        ("square_wave", {"channel":20, "function": "square_wave", "frequency":30000})
    ),

    "_general/control_change/lfo_depth":(
        ("square_wave", {"channel":22, "function": "square_wave", "frequency":30000})
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
