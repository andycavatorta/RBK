
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
    70:"acetone_bass_off",
    71:"acetone_cymbal_off",
    72:"acetone_cowbell_off",
    73:"acetone_claves_off",
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
    95:"start_stop",
    96:"Data_entry_+1",
    97:"Data_entry_-1",
    98:"Undefined",
    99:"Undefined",
    100:"Undefined",
    101:"Undefined",
    102:"start",
    103:"stop",
    104:"clock",
    105:"int_ext",
    106:"sensitivity",
    107:"pitch",
    108:"decay",
    109:"sweep",
    110:"lfo_rate",
    111:"lfo_depth",
    112:"master_tempo_ub",
    113:"master_tempo_lb",
    114:"Undefined",
    115:"tempo_mod_numerator_ub",
    116:"tempo_mod_numerator_lb",
    117:"tempo_mod_denominator",
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

def tempo_calculation(tempo_list):
    tempo_string = "%s%s" % (tempo_list["upper_byte"],tempo_list["lower_byte"])
    tempo_int = int(tempo_string,2)
    modifier = 1
    tempo_after_formula = tempo_int * 979/16383 + 20
    master_tempo = tempo_after_formula * modifier
    print "Tempo: %s | Modifier: %s | Master Tempo: %s" % (tempo_after_formula, modifier, master_tempo)
    return [float(master_tempo),modifier]

def modifier_calculation(modifier_list):
    # tempo_string = "%s%s" % (modifier_list["numerator"],modifier_list["denominator"])
    # tempo_int = int(tempo_string,2)
    numerator_int = int(modifier_list["numerator"],2)
    print numerator_int
    if numerator_int < 500:
        numerator_after_math = (numerator_int/100.0) + 0.01
    else:
        numerator_after_math = ((numerator_int-500)/20.0)+5.05
    # print tempo_int
    # tempo_modifier = float(pow(tempo_int/16383.0, 4.322)*1999.95+0.05)
    denominator_int = int(modifier_list["denominator"],2)
    tempo_modifier = numerator_after_math/(denominator_int+1)
    print "Numerator: %s | Denominator: %s | Total: %s" % (numerator_after_math,denominator_int+1,tempo_modifier)
    # return float(tempo_modifier/100.0)
    return tempo_modifier

tempo_list = {
    "upper_byte": "0000000",
    "lower_byte": "0000001"
}

modifier_list = {
    "numerator_upper":"0000000",
    "numerator_lower":"0000001",
    "numerator":"00000000000001",
    "denominator":"0000001"
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
        if status == "note_on" and data2 != 0:
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
        if status == "control_change/master_tempo_ub":
            master_tempo_ub = '{0:07b}'.format(data2)
            tempo_list["upper_byte"] = master_tempo_ub
        elif status == "control_change/master_tempo_lb":
            master_tempo_lb = '{0:07b}'.format(data2)
            tempo_list["lower_byte"] = master_tempo_lb
            master_tempo = tempo_calculation(tempo_list)
            status = "control_change/master_tempo"
            params = {
                "channel":channel,
                "type": "master_tempo",
                "value": master_tempo[0],
                "modifier": master_tempo[1]
            }
        elif status == "control_change/tempo_mod_numerator_ub":
            numerator_ub = '{0:07b}'.format(data2)
            modifier_list["numerator_upper"] = numerator_ub
        elif status == "control_change/tempo_mod_numerator_lb":
            # tempo_mod_numerator = int(data2)
            numerator_lb = '{0:07b}'.format(data2)
            modifier_list["numerator_lower"] = numerator_lb
            tempo_mod_numerator = "%s%s" % (modifier_list["numerator_upper"], modifier_list["numerator_lower"])
            print "numerator bits = ", tempo_mod_numerator
            modifier_list["numerator"] = tempo_mod_numerator
            master_tempo = tempo_calculation(tempo_list)
            status = "control_change/master_tempo"
            params = {
                "channel":channel,
                "type": "master_tempo",
                "value": master_tempo[0],
                "modifier": master_tempo[1]
            }
        elif status == "control_change/tempo_mod_denominator":
            # tempo_mod_denominator = int(data2)
            tempo_mod_denominator = '{0:07b}'.format(data2)
            modifier_list["denominator"] = tempo_mod_denominator
            print "denominator bits = ", tempo_mod_denominator
            master_tempo = tempo_calculation(tempo_list)
            status = "control_change/master_tempo"
            params = {
                "channel":channel,
                "type": "master_tempo",
                "value": master_tempo[0],
                "modifier": master_tempo[1]
            }
        else:
            params = {
                "channel":channel,
                "type":data1,
                "value":data2
            }

    params_j = json.dumps(params, separators=(',', ':'))
    return "/%s/%s %s" % (devicename,status, params_j)
