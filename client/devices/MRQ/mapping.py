instruments = [
    "_system",
    "_general",
    #"_miscellaneous"
]


mapping = {
    "_general/sound/bass_drum/bang":[
        ["signal", {"channel":4, "function": "pulse", "pulselength":0.02 }]
    ],
    "_general/sound/snare_drum1/bang":[
        ["signal", {"channel":5, "function": "pulse", "pulselength":0.02 }]
    ],
    "_general/sound/snare_drum2/bang":[
        ["signal", {"channel":13, "function": "digital", "bool":1 }],
        ["signal", {"channel":23,"function": "digital", "bool":0}]
    ],

    "_general/sound/snare_drum2/off":[
        ["signal", {"channel":23, "function": "digital", "bool":1}],
        ["signal", {"channel":13, "function": "digital", "bool":0}]
    ],

    "_general/sound/high_woodblock/bang":[
        ["signal", {"channel":9, "function": "pulse", "pulselength":0.02 }]
    ],

    "_general/sound/high_bongo/bang":[
        ["signal", {"channel":7, "function": "pulse", "pulselength":0.02 }]
    ],
    "_general/control_change/Main_Volume":[
        ["signal", {"channel":3, "function": "square_wave", "frequency":30000, "duty cycle":0, "freq_min_max":[30000,30000], "duty_min_max":[0,100], "variable_key":"duty_cycle"}]
    ],
    "_general/control_change/start":[
        ["signal", {"channel":1, "function": "digital", "bool":1}],
        ["signal", {"channel":19, "function": "digital", "bool":0}]
    ],
    "_general/control_change/stop":[
        ["signal", {"channel":1, "function": "digital", "bool":0}],
        ["signal", {"channel":19, "function": "digital", "bool":1}]
    ],
    "_general/control_change/int_ext":[
        ["signal", {"channel":0, "function": "digital"}]
    ],
    "_general/control_change/master_tempo":[
        ["signal", {"channel":2, "function": "square_wave", "frequency":0, "duty cycle":50.0, "duty_min_max":[0,100], "variable_key":"frequency", "clock_factor":1.0}]
    ],
    "_system/start":[
            ["digital", {"channel":2,"function": "digital", "bool":1}]
    ],
    "_system/stop":[
        ["digital", {"channel":1, "function": "digital", "bool":0}]
    ],
    "_system/master_volume":[
        ["square_wave", {"channel":3, "function": "square_wave", "frequency":30000, "duty":50.0}]
    ],
    "_system/int_ext":[
        ["digital", {"channel":0, "function": "digital", "bool":1}]
    ],
    "_system/timing_clock":[
        ["square_wave", {"channel":2, "function": "square_wave", "frequency":40, "duty":50.0}]
    ],
}
