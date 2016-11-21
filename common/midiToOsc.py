
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
    241:"master_volume",
    242:"song_position_pointer",
    243:"song_select",
    244:"system_common",
    245:"system_common",
    246:"tune_request",
    247:"end_of_sysex",
    248:"timing_clock",
    249:"int_ext",
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
    0:"kick_1",
    1:"kick_2",
    2:"kick_3",
    3:"kick_4",
    4:"kick_5",
    5:"kick_6",
    6:"kick_7",
    7:"kick_8",
    8:"kick_9",
    9:"kick_10",
    10:"kick_11",
    11:"kick_12",
    12:"kick_13",
    13:"kick_14",
    14:"kick_15",
    15:"kick_16",
    16:"kick_17",
    17:"kick_18",
    18:"kick_19",
    19:"kick_20",
    20:"kick_21",
    21:"kick_22",
    22:"kick_23",
    23:"kick_24",
    24:"kick_25",
    25:"kick_26",
    26:"kick_27",
    27:"kick_28",
    28:"kick_29",
    29:"kick_30",
    30:"kick_31",
    31:"kick_32",
    32:"kick_33",
}

snareMap = {
    0:"snare_1",
    1:"snare_2",
    2:"snare_3",
    3:"snare_4",
    4:"snare_5",
    5:"snare_6",
    6:"snare_7",
    7:"snare_8",
    8:"snare_9",
    9:"snare_10",
    10:"snare_11",
    11:"snare_12",
    12:"snare_13",
    13:"snare_14",
    14:"snare_15",
    15:"snare_16",
    16:"snare_17",
    17:"snare_18",
    18:"snare_19",
    19:"snare_20",
    20:"snare_21",
    21:"snare_22",
    22:"snare_23",
    23:"snare_24",
    24:"snare_25",
    25:"snare_26",
    26:"snare_27",
    27:"snare_28",
    28:"snare_29",
    29:"snare_30",
    30:"snare_31",
    31:"snare_32",
    32:"snare_33",
}

tomMap = {
    0:"tom_1",
    1:"tom_2",
    2:"tom_3",
    3:"tom_4",
    4:"tom_5",
    5:"tom_6",
    6:"tom_7",
    7:"tom_8",
    8:"tom_9",
    9:"tom_10",
    10:"tom_11",
    11:"tom_12",
    12:"tom_13",
    13:"tom_14",
    14:"tom_15",
    15:"tom_16",
    16:"tom_17",
    17:"tom_18",
    18:"tom_19",
    19:"tom_20",
    20:"tom_21",
    21:"tom_22",
    22:"tom_23",
    23:"tom_24",
    24:"tom_25",
    25:"tom_26",
    26:"tom_27",
    27:"tom_28",
    28:"tom_29",
    29:"tom_30",
    30:"tom_31",
    31:"tom_32",
    32:"tom_33",
}

hihatMap = {
    0:"hihat_1",
    1:"hihat_2",
    2:"hihat_3",
    3:"hihat_4",
    4:"hihat_5",
    5:"hihat_6",
    6:"hihat_7",
    7:"hihat_8",
    8:"hihat_9",
    9:"hihat_10",
    10:"hihat_11",
    11:"hihat_12",
    12:"hihat_13",
    13:"hihat_14",
    14:"hihat_15",
    15:"hihat_16",
    16:"hihat_17",
    17:"hihat_18",
    18:"hihat_19",
    19:"hihat_20",
    20:"hihat_21",
    21:"hihat_22",
    22:"hihat_23",
    23:"hihat_24",
    24:"hihat_25",
    25:"hihat_26",
    26:"hihat_27",
    27:"hihat_28",
    28:"hihat_29",
    29:"hihat_30",
    30:"hihat_31",
    31:"hihat_32",
    32:"hihat_33",
}

cymbalMap = {
    0:"cymbal_1",
    1:"cymbal_2",
    2:"cymbal_3",
    3:"cymbal_4",
    4:"cymbal_5",
    5:"cymbal_6",
    6:"cymbal_7",
    7:"cymbal_8",
    8:"cymbal_9",
    9:"cymbal_10",
    10:"cymbal_11",
    11:"cymbal_12",
    12:"cymbal_13",
    13:"cymbal_14",
    14:"cymbal_15",
    15:"cymbal_16",
    16:"cymbal_17",
    17:"cymbal_18",
    18:"cymbal_19",
    19:"cymbal_20",
    20:"cymbal_21",
    21:"cymbal_22",
    22:"cymbal_23",
    23:"cymbal_24",
    24:"cymbal_25",
    25:"cymbal_26",
    26:"cymbal_27",
    27:"cymbal_28",
    28:"cymbal_29",
    29:"cymbal_30",
    30:"cymbal_31",
    31:"cymbal_32",
    32:"cymbal_33",
}

percussionMap = {
    0:"percussion_1",
    1:"percussion_2",
    2:"percussion_3",
    3:"percussion_4",
    4:"percussion_5",
    5:"percussion_6",
    6:"percussion_7",
    7:"percussion_8",
    8:"percussion_9",
    9:"percussion_10",
    10:"percussion_11",
    11:"percussion_12",
    12:"percussion_13",
    13:"percussion_14",
    14:"percussion_15",
    15:"percussion_16",
    16:"percussion_17",
    17:"percussion_18",
    18:"percussion_19",
    19:"percussion_20",
    20:"percussion_21",
    21:"percussion_22",
    22:"percussion_23",
    23:"percussion_24",
    24:"percussion_25",
    25:"percussion_26",
    26:"percussion_27",
    27:"percussion_28",
    28:"percussion_29",
    29:"percussion_30",
    30:"percussion_31",
    31:"percussion_32",
    32:"percussion_33",
}

miscellaneousMap = {
    0:"miscellaneous_1",
    1:"miscellaneous_2",
    2:"miscellaneous_3",
    3:"miscellaneous_4",
    4:"miscellaneous_5",
    5:"miscellaneous_6",
    6:"miscellaneous_7",
    7:"miscellaneous_8",
    8:"miscellaneous_9",
    9:"miscellaneous_10",
    10:"miscellaneous_11",
    11:"miscellaneous_12",
    12:"miscellaneous_13",
    13:"miscellaneous_14",
    14:"miscellaneous_15",
    15:"miscellaneous_16",
    16:"miscellaneous_17",
    17:"miscellaneous_18",
    18:"miscellaneous_19",
    19:"miscellaneous_20",
    20:"miscellaneous_21",
    21:"miscellaneous_22",
    22:"miscellaneous_23",
    23:"miscellaneous_24",
    24:"miscellaneous_25",
    25:"miscellaneous_26",
    26:"miscellaneous_27",
    27:"miscellaneous_28",
    28:"miscellaneous_29",
    29:"miscellaneous_30",
    30:"miscellaneous_31",
    31:"miscellaneous_32",
    32:"miscellaneous_33",
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
        status = "control_change/%s" % (ccMap[int(data1[0])])
        params = {
            "channel":channel,
            "type":data1,
            "value":data2
        }

    params_j = json.dumps(params, separators=(',', ':'))
    return "/%s/%s %s" % (devicename,status, params_j)
