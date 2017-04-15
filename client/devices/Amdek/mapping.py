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

    # 00 - int/ext
    "_system/int_ext":(
        ("digital", {"channel":0, "function": "digital", "bool":1})
    ),
    #02 - clock
    "_system/timing_clock":(
        ("square_wave", {"channel":14, "function": "square_wave", "frequency":40, "duty":50.0})
    ),

    #03 - master vol
    "_system/master_volume":(
        ("square_wave", {"channel":3, "function": "square_wave", "frequency":30000, "duty":50.0})
    ),

    #04 - kick
    "_general/sound/bass_drum/bang":(
        ("signal", {"channel":4, "function": "digital", "bool":1 })
    ),

    "_general/sound/bass_drum/off":(
        ("signal", {"channel":4, "function": "digital", "bool":0 })
    ),

    #05 - snare
    "_general/sound/snare/bang":(
        ("signal", {"channel":5, "function": "digital", "bool":1 })
    ),

    "_general/sound/snare/off":(
        ("signal", {"channel":5, "function": "digital", "bool":0 })
    ),

    #06 - hi hat
    "_general/sound/hi_hat/bang":(
        ("signal", {"channel":6, "function": "digital", "bool":1 })
    ),

    "_general/sound/hi_hat/off":(
        ("signal", {"channel":6, "function": "digital", "bool":0 })
    ),
    #07 - sensitivity
    "_general/control_change/sensitivity":(
        ("signal", {"channel":7, "function": "square_wave", "frequency":30000, "duty cycle":0, "freq_min_max":(1,1), "duty_min_max":(0,100), "variable_key":"duty_cycle"})
    ),
  
    #08 - pitch

    "_general/control_change/pitch":(
        ("signal", {"channel":8, "function": "square_wave", "frequency":30000, "duty cycle":0, "freq_min_max":(1,1), "duty_min_max":(0,100), "variable_key":"duty_cycle"})
    ),

    #09 - decay
    "_general/control_change/decay":(
        ("signal", {"channel":9, "function": "square_wave", "frequency":30000, "duty cycle":0, "freq_min_max":(1,1), "duty_min_max":(0,100), "variable_key":"duty_cycle"})
    ),

    #10 - sweep
    "_general/control_change/sweep":(
        ("signal", {"channel":10, "function": "square_wave", "frequency":30000, "duty cycle":0, "freq_min_max":(1,1), "duty_min_max":(0,100), "variable_key":"duty_cycle"})
    ),


    #11 - lfo rate
    "_general/control_change/lfo_rate":(
        ("signal", {"channel":11, "function": "square_wave", "frequency":30000, "duty cycle":0, "freq_min_max":(1,1), "duty_min_max":(0,100), "variable_key":"duty_cycle"})
    ),

    #12 - lfo depth
    "_general/control_change/lfo_depth":(
        ("signal", {"channel":12, "function": "square_wave", "frequency":30000, "duty cycle":0, "freq_min_max":(1,1), "duty_min_max":(0,100), "variable_key":"duty_cycle"})
    ),


    #14 - trig 1
    "_general/sound/trigger_1/bang":(
        ("signal", {"channel":14, "function": "digital", "bool":1 })
    ),

    "_general/sound/trigger_1/off":(
        ("signal", {"channel":14, "function": "digital", "bool":0 })
    ),

    # 16 - trig 2
    "_general/sound/trigger_2/bang":(
        ("signal", {"channel":16, "function": "digital", "bool":1 })
    ),

    "_general/sound/trigger_2/off":(
        ("signal", {"channel":16, "function": "digital", "bool":0 })
    ),

    #18 - trig 3
    "_general/sound/trigger_3/bang":(
        ("signal", {"channel":18, "function": "digital", "bool":1 })
    ),

    "_general/sound/trigger_3/off":(
        ("signal", {"channel":18, "function": "digital", "bool":0 })
    ),

    #20 - trig 4
    "_general/sound/trigger_4/bang":(
        ("signal", {"channel":20, "function": "digital", "bool":1 })
    ),

    "_general/sound/trigger_4/off":(
        ("signal", {"channel":20, "function": "digital", "bool":0 })
    ),
}



  
