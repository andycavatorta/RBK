
import json
import math

statusMap = {
    128:"note_off",
    144:"note_on",
    160:"polyphonic_aftertouch",
    176:"control_change",
    192:"program_change",
    208:"channel_aftertouch",
    224:"pitch_wheel",
    240:"system_exclusive",
    241:"system_common",
    242:"song_position_pointer",
    243:"song_select",
    244:"system_common",
    245:"system_common",
    246:"tune_request",
    247:"end_of_sysex",
    248:"timing_clock",
    249:"undefined",
    250:"start",
    251:"continue",
    252:"stop",
    253:"undefined",
    254:"active_sensing",
    255:"sys_reset",
}

ccMap = {
    0:"Continuous_controller",
    1:"Modulation_wheel",
    2:"Breath_control",
    3:"Continuous_controller",
    4:"Foot_controller",
    5:"Portamento_time",
    6:"Data_Entry",
    7:"Main_Volume",
    8:"Continuous_controller",
    9:"Continuous_controller",
    10:"Continuous_controller",
    11:"Continuous_controller",
    12:"Continuous_controller",
    13:"Continuous_controller",
    14:"Continuous_controller",
    15:"Continuous_controller",
    16:"Continuous_controller",
    17:"Continuous_controller",
    18:"Continuous_controller",
    19:"Continuous_controller",
    20:"Continuous_controller",
    21:"Continuous_controller",
    22:"Continuous_controller",
    23:"Continuous_controller",
    24:"Continuous_controller",
    25:"Continuous_controller",
    26:"Continuous_controller",
    27:"Continuous_controller",
    28:"Continuous_controller",
    29:"Continuous_controller",
    30:"Continuous_controller",
    31:"Continuous_controller",
    32:"Continuous_controller",
    33:"Modulation_wheel",
    34:"Breath_control",
    35:"Continuous_controller",
    36:"Foot_controller",
    37:"Portamento_time",
    38:"Data_entry",
    39:"Main_volume",
    40:"Continuous_controller",
    41:"Continuous_controller",
    42:"Continuous_controller",
    43:"Continuous_controller",
    44:"Continuous_controller",
    45:"Continuous_controller",
    46:"Continuous_controller",
    47:"Continuous_controller",
    48:"Continuous_controller",
    49:"Continuous_controller",
    50:"Continuous_controller",
    51:"Continuous_controller",
    52:"Continuous_controller",
    53:"Continuous_controller",
    54:"Continuous_controller",
    55:"Continuous_controller",
    56:"Continuous_controller",
    57:"Continuous_controller",
    58:"Continuous_controller",
    59:"Continuous_controller",
    60:"Continuous_controller",
    61:"Continuous_controller",
    62:"Continuous_controller",
    63:"Continuous_controller",
    64:"Damper_pedal_on/off",
    65:"Portamento_on/off",
    66:"Sustenuto_on/off",
    67:"Soft_pedal_on/off",
    68:"Undefined_on/off",
    69:"Undefined_on/off",
    70:"Undefined_on/off",
    71:"Undefined_on/off",
    72:"Undefined_on/off",
    73:"Undefined_on/off",
    74:"Undefined_on/off",
    75:"Undefined_on/off",
    76:"Undefined_on/off",
    77:"Undefined_on/off",
    78:"Undefined_on/off",
    79:"Undefined_on/off",
    80:"Undefined_on/off",
    81:"Undefined_on/off",
    82:"Undefined_on/off",
    83:"Undefined_on/off",
    84:"Undefined_on/off",
    85:"Undefined_on/off",
    86:"Undefined_on/off",
    87:"Undefined_on/off",
    88:"Undefined_on/off",
    89:"Undefined_on/off",
    90:"Undefined_on/off",
    91:"Undefined_on/off",
    92:"Undefined_on/off",
    93:"Undefined_on/off",
    94:"Undefined_on/off",
    95:"Undefined_on/off",
    96:"Data_entry_+1",
    97:"Data_entry_-1",
    98:"Undefined",
    99:"Undefined",
    100:"Undefined",
    101:"Undefined",
    102:"Undefined",
    103:"Undefined",
    104:"Undefined",
    105:"Undefined",
    106:"Undefined",
    107:"Undefined",
    108:"Undefined",
    109:"Undefined",
    110:"Undefined",
    111:"Undefined",
    112:"Undefined",
    113:"Undefined",
    114:"Undefined",
    115:"Undefined",
    116:"Undefined",
    117:"Undefined",
    118:"Undefined",
    119:"Undefined",
    120:"Undefined",
    121:"Undefined",
    122:"Local_control_on/off",
    123:"All_notes_off",
    124:"Omni_mode_off",
    125:"Omni_mode_on",
    126:"Poly_mode_on/off",
    127:"Poly_mode_on",
}

notesStandardMap = {
    35:"bass_drum2",
    36:"bass_drum",
    37:"side_stick",
    38:"snare_drum1",
    39:"hand_clap",
    40:"snare_drum2",
    41:"low_tom2",
    42:"closed_hihat",
    43:"low_tom1",
    44:"pedal_hihat",
    45:"mid_tom2",
    46:"open_hihat",
    47:"mid_tom1",
    48:"high_tom2",
    49:"crash_cymbal1",
    50:"high_tom1",
    51:"ride_cymbal1",
    52:"chinese_cymbal",
    53:"ride_bell",
    54:"tambourine",
    55:"splash_cymbal",
    56:"cowbell",
    57:"crash_cymbal2",
    58:"vibra_slap",
    59:"ride_cymbal2",
    60:"high_bongo",
    61:"low_bongo",
    62:"mute_high_conga",
    63:"open_high_conga",
    64:"low_conga",
    65:"high_timbale",
    66:"low_timbale",
    67:"high_agogo",
    68:"low_agogo",
    69:"cabasa",
    70:"maracas",
    71:"short_whistle",
    72:"long_whistle",
    73:"short_guiro",
    74:"long_guiro",
    75:"claves",
    76:"high_woodblock",
    77:"low_woodblock",
    78:"mute_cuica",
    79:"open_cuica",
    80:"mute_triangle",
    81:"open_triangle"
}

kickMap = {
    1:"kick_1",
    2:"kick_2",
    3:"kick_3",
    4:"kick_4",
    5:"kick_5",
    6:"kick_6",
    7:"kick_7",
    8:"kick_8",
    9:"kick_9",
    10:"kick_10",
    11:"kick_11",
    12:"kick_12",
    13:"kick_13",
    14:"kick_14",
    15:"kick_15",
    16:"kick_16",
    17:"kick_17",
    18:"kick_18",
    19:"kick_19",
    20:"kick_20",
    21:"kick_21",
    22:"kick_22",
    23:"kick_23",
    24:"kick_24",
    25:"kick_25",
    26:"kick_26",
    27:"kick_27",
    28:"kick_28",
    29:"kick_29",
    30:"kick_30",
    31:"kick_31",
    32:"kick_32",
    33:"kick_33",
}

snareMap = {
    1:"snare_1",
    2:"snare_2",
    3:"snare_3",
    4:"snare_4",
    5:"snare_5",
    6:"snare_6",
    7:"snare_7",
    8:"snare_8",
    9:"snare_9",
    10:"snare_10",
    11:"snare_11",
    12:"snare_12",
    13:"snare_13",
    14:"snare_14",
    15:"snare_15",
    16:"snare_16",
    17:"snare_17",
    18:"snare_18",
    19:"snare_19",
    20:"snare_20",
    21:"snare_21",
    22:"snare_22",
    23:"snare_23",
    24:"snare_24",
    25:"snare_25",
    26:"snare_26",
    27:"snare_27",
    28:"snare_28",
    29:"snare_29",
    30:"snare_30",
    31:"snare_31",
    32:"snare_32",
    33:"snare_33",
}

tomMap = {
    1:"tom_1",
    2:"tom_2",
    3:"tom_3",
    4:"tom_4",
    5:"tom_5",
    6:"tom_6",
    7:"tom_7",
    8:"tom_8",
    9:"tom_9",
    10:"tom_10",
    11:"tom_11",
    12:"tom_12",
    13:"tom_13",
    14:"tom_14",
    15:"tom_15",
    16:"tom_16",
    17:"tom_17",
    18:"tom_18",
    19:"tom_19",
    20:"tom_20",
    21:"tom_21",
    22:"tom_22",
    23:"tom_23",
    24:"tom_24",
    25:"tom_25",
    26:"tom_26",
    27:"tom_27",
    28:"tom_28",
    29:"tom_29",
    30:"tom_30",
    31:"tom_31",
    32:"tom_32",
    33:"tom_33",
}

hihatMap = {
    1:"hihat_1",
    2:"hihat_2",
    3:"hihat_3",
    4:"hihat_4",
    5:"hihat_5",
    6:"hihat_6",
    7:"hihat_7",
    8:"hihat_8",
    9:"hihat_9",
    10:"hihat_10",
    11:"hihat_11",
    12:"hihat_12",
    13:"hihat_13",
    14:"hihat_14",
    15:"hihat_15",
    16:"hihat_16",
    17:"hihat_17",
    18:"hihat_18",
    19:"hihat_19",
    20:"hihat_20",
    21:"hihat_21",
    22:"hihat_22",
    23:"hihat_23",
    24:"hihat_24",
    25:"hihat_25",
    26:"hihat_26",
    27:"hihat_27",
    28:"hihat_28",
    29:"hihat_29",
    30:"hihat_30",
    31:"hihat_31",
    32:"hihat_32",
    33:"hihat_33",
}

cymbalMap = {
    1:"cymbal_1",
    2:"cymbal_2",
    3:"cymbal_3",
    4:"cymbal_4",
    5:"cymbal_5",
    6:"cymbal_6",
    7:"cymbal_7",
    8:"cymbal_8",
    9:"cymbal_9",
    10:"cymbal_10",
    11:"cymbal_11",
    12:"cymbal_12",
    13:"cymbal_13",
    14:"cymbal_14",
    15:"cymbal_15",
    16:"cymbal_16",
    17:"cymbal_17",
    18:"cymbal_18",
    19:"cymbal_19",
    20:"cymbal_20",
    21:"cymbal_21",
    22:"cymbal_22",
    23:"cymbal_23",
    24:"cymbal_24",
    25:"cymbal_25",
    26:"cymbal_26",
    27:"cymbal_27",
    28:"cymbal_28",
    29:"cymbal_29",
    30:"cymbal_30",
    31:"cymbal_31",
    32:"cymbal_32",
    33:"cymbal_33",
}

percussionMap = {
    1:"percussion_1",
    2:"percussion_2",
    3:"percussion_3",
    4:"percussion_4",
    5:"percussion_5",
    6:"percussion_6",
    7:"percussion_7",
    8:"percussion_8",
    9:"percussion_9",
    10:"percussion_10",
    11:"percussion_11",
    12:"percussion_12",
    13:"percussion_13",
    14:"percussion_14",
    15:"percussion_15",
    16:"percussion_16",
    17:"percussion_17",
    18:"percussion_18",
    19:"percussion_19",
    20:"percussion_20",
    21:"percussion_21",
    22:"percussion_22",
    23:"percussion_23",
    24:"percussion_24",
    25:"percussion_25",
    26:"percussion_26",
    27:"percussion_27",
    28:"percussion_28",
    29:"percussion_29",
    30:"percussion_30",
    31:"percussion_31",
    32:"percussion_32",
    33:"percussion_33",
}

miscellaneousMap = {
    1:"miscellaneous_1",
    2:"miscellaneous_2",
    3:"miscellaneous_3",
    4:"miscellaneous_4",
    5:"miscellaneous_5",
    6:"miscellaneous_6",
    7:"miscellaneous_7",
    8:"miscellaneous_8",
    9:"miscellaneous_9",
    10:"miscellaneous_10",
    11:"miscellaneous_11",
    12:"miscellaneous_12",
    13:"miscellaneous_13",
    14:"miscellaneous_14",
    15:"miscellaneous_15",
    16:"miscellaneous_16",
    17:"miscellaneous_17",
    18:"miscellaneous_18",
    19:"miscellaneous_19",
    20:"miscellaneous_20",
    21:"miscellaneous_21",
    22:"miscellaneous_22",
    23:"miscellaneous_23",
    24:"miscellaneous_24",
    25:"miscellaneous_25",
    26:"miscellaneous_26",
    27:"miscellaneous_27",
    28:"miscellaneous_28",
    29:"miscellaneous_29",
    30:"miscellaneous_30",
    31:"miscellaneous_31",
    32:"miscellaneous_32",
    33:"miscellaneous_33",
}

def makePitch(midiNoteNumber, cents_int=0):
    pitch = ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"][midiNoteNumber%12]
    octave = int(math.floor(midiNoteNumber/12)-1)
    

    return {
        'pitch':pitch,
        'octave':octave,
        'cents':cents_int,
        '12tet':"%s%d"%(pitch,octave),
        'freq':round(440.0 * (2.0**((midiNoteNumber-69+cents_int)/12.0)),3),
        'midi':midiNoteNumber
    }

def convert(devicename, status, channel, data1=None, data2=None):
    print devicename
    if "_general" in devicename:
        mapper = notesStandardMap
    elif "_kick" in devicename:
        mapper = kickMap
    elif "_snare" in devicename:
        mapper = snareMap
    elif "_tom" in devicename:
        mapper = tomMap
    elif "_hihat" in devicename:
        mapper = hihatMap
    elif "_cymbal" in devicename:
        mapper = cymbalMap
    elif "_percussion" in devicename:
        mapper = percussionMap
    elif "_miscellaneous" in devicename:
        mapper = miscellaneousMap
    #### PARSE MIDI ####
    """
    if event[0] < 0xF0:
        channel = (event[0] & 0xF) + 1
        status_int = event[0] & 0xF0
    else:
        status_int = event[0]
        channel = None
    status = statusMap[int(status_int)]
    data1 = data2 = None
    num_bytes = len(event)
    if num_bytes >= 2:
        data1 = event[1]
    if num_bytes >= 3:
        data2 = event[2]
    """

    if status in ["note_off","note_on","polyphonic_aftertouch","channel_aftertouch"]:
        data1 = makePitch(data1)
    if status == "control_change":
        data1 = [data1, ccMap[data1]]

    channel = str(channel)
    #data1 = str(data1)
    #data2 = str(data2)
    #### CREATE OSC ####
    params = {
        "channel":channel, 
        "data1":data1,
        "data2":data2
    }
    if status in ["note_off","note_on"]:
        if status == "note_on":
            if data1['midi'] not in mapper:
                pass
            else:
                status = "sound/%s/bang" % (mapper[int(data1['midi'])])
        else:
            if data1['midi'] not in mapper:
                pass
            else:
                status = "sound/%s/off" % (mapper[int(data1['midi'])])
        params = {
            "channel":channel,
            "pitch":data1,
            "dynamics":{"amplitude":data2/127.0},
            "timbre":None
        }
    if status =="polyphonic_aftertouch":
        params = {
            "channel":channel,
            "pitch":data1,
            "pressure":data2
        }
    if status =="program_change":
        params = {
            "channel":channel,
            "program":data1
        }
    if status =="channel_aftertouch":
        params = {
            "channel":channel,
            "pressure":data1
        }
    if status in ["system_common","tune_request","end_of_sysex","timing_clock","start","continue","stop","undefined","active_sensing","sys_reset"]:
        params = {
            "channel":channel
        }
    if status =="pitch_wheel":
        params = {
            "channel":channel,
            "value":int(data1) + int(data2)<<7
        }
    if status =="song_select":
        params = {
            "channel":channel,
            "value":data1
        }
    if status =="song_position_pointer":
        params = {
            "channel":channel,
            "value":int(data1) + int(data2)<<7
        }
    if status =="system_exclusive":
        params = {
            "channel":channel,
            "vendorID":data1,
            "value":data2
        }
    if status =="system_common":
        params = {
            "channel":channel
        }
    if status =="control_change":
        params = {
            "channel":channel,
            "type":data1,
            "value":data2
        }

    params_j = json.dumps(params, separators=(',', ':'))
    return "/%s/%s %s" % (devicename,status, params_j)
