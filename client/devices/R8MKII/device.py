import mido
import time
import json
import traceback

oNames = mido.get_output_names()

midi_out = mido.open_output(oNames[1])


# creating OSC endpoint methds
def play_sound(path,params):
    split_path = path.split('/')
    print split_path
    if split_path[4] == "bang":
        midi_out.send(mido.Message('note_on', channel = int(params['channel']), note = int(pathToMethod_d[path]), velocity=int(params["dynamics"]["amplitude"]*127)))
    else:
        pass
def sound_off(params):
    pass

def system_power_on(params):
    pass
def system_power_off(params):
    pass
def system_clock_1(params):
    pass
def system_clock_2(params):
    pass
def system_clock_3(params):
    pass
def system_clock_4(params):
    pass
def system_miditest_start(params):
    for channel in range(16):
        for pitch in range(0,127):
            msg_midi = mido.Message('note_on')
            msg_midi.channel = 9
            msg_midi.note = pitch
            print msg_midi
            midi_out.send(msg_midi)
            time.sleep(0.1)

def system_miditest_stop(params):
    midi_out.panic()
    pass
def system_midipanic(params):
    pass

def ping(params):
    pass

def handleNOSC(nosc_d):
    try:
        category = nosc_d['innerpath'].split('/')
        if category[2] == "sound":
            play_sound(nosc_d["innerpath"],nosc_d["params"])
        # pathToMethod_d[nosc_d["innerpath"]](nosc_d["params"])
    except Exception as e:
        traceback.print_exc()
        print "device: path not found", e

def init():
    pass

pathToMethod_d = {
    "/R8MKII/sound/bass_drum2/bang":35,
    "/R8MKII/sound/bass_drum/bang":36,
    "/R8MKII/sound/side_stick/bang":37,
    "/R8MKII/sound/snare_drum1/bang":38,
    "/R8MKII/sound/hand_clap/bang":39,
    "/R8MKII/sound/snare_drum2/bang":40,
    "/R8MKII/sound/low_tom2/bang":41,
    "/R8MKII/sound/closed_hihat/bang":42,
    "/R8MKII/sound/low_tom1/bang":43,
    "/R8MKII/sound/pedal_hihat/bang":44,
    "/R8MKII/sound/mid_tom2/bang":45,
    "/R8MKII/sound/open_hihat/bang":46,
    "/R8MKII/sound/mid_tom1/bang":47,
    "/R8MKII/sound/high_tom2/bang":48,
    "/R8MKII/sound/crash_cymbal/bang":49,
    "/R8MKII/sound/high_tom1/bang":50,
    "/R8MKII/sound/ride_cymbal1/bang":51,
    "/R8MKII/sound/chinese_cymbal/bang":52,
    "/R8MKII/sound/ride_bell/bang":53,
    "/R8MKII/sound/tambourine/bang":54,
    "/R8MKII/sound/splash_cymbal/bang":55,
    "/R8MKII/sound/cowbell/bang":56,
    "/R8MKII/sound/crash_cymbal2/bang":57,
    "/R8MKII/sound/vibra_slap/bang":58,
    "/R8MKII/sound/ride_cymbal2/bang":59,
    "/R8MKII/sound/high_bongo/bang":60,
    "/R8MKII/sound/low_bongo/bang":61,
    "/R8MKII/sound/mute_high_conga/bang":62,
    "/R8MKII/sound/open_high_conga/bang":63,
    "/R8MKII/sound/low_conga/bang":64,
    "/R8MKII/sound/high_timbale/bang":65,
    "/R8MKII/sound/low_timbale/bang":66,
    "/R8MKII/sound/high_agogo/bang":67,
    "/R8MKII/sound/low_agogo/bang":68,
    "/R8MKII/sound/cabasa/bang":69,
    "/R8MKII/sound/maracas/bang":70,
    "/R8MKII/sound/short_whistle/bang":71,
    "/R8MKII/sound/long_whistle/bang":72,
    "/R8MKII/sound/short_guiro/bang":73,
    "/R8MKII/sound/long_guiro/bang":74,
    "/R8MKII/sound/claves/bang":75,
    "/R8MKII/sound/high_woodblock/bang":76,
    "/R8MKII/sound/low_woodblock/bang":77,
    "/R8MKII/sound/mute_cuica/bang":78,
    "/R8MKII/sound/open_cuica/bang":79,
    "/R8MKII/sound/mute_triangle/bang":80,
    "/R8MKII/sound/open_triangle/bang":81,

    "/R8MKII/sound/bass_drum2/off":35,
    "/R8MKII/sound/bass_drum/off":36,
    "/R8MKII/sound/side_stick/off":37,
    "/R8MKII/sound/snare_drum1/off":38,
    "/R8MKII/sound/hand_clap/off":39,
    "/R8MKII/sound/snare_drum2/off":40,
    "/R8MKII/sound/low_tom2offg":41,
    "/R8MKII/sound/closed_hihat/off":42,
    "/R8MKII/sound/low_tom1/off":43,
    "/R8MKII/sound/pedal_hihat/off":44,
    "/R8MKII/sound/mid_tom2/off":45,
    "/R8MKII/sound/open_hihat/off":46,
    "/R8MKII/sound/mid_tom1/off":47,
    "/R8MKII/sound/high_tom2/off":48,
    "/R8MKII/sound/crash_cymbal/off":49,
    "/R8MKII/sound/high_tom1/off":50,
    "/R8MKII/sound/ride_cymbal1/off":51,
    "/R8MKII/sound/chinese_cymbal/off":52,
    "/R8MKII/sound/ride_bell/off":53,
    "/R8MKII/sound/tambourine/off":54,
    "/R8MKII/sound/splash_cymbal/off":55,
    "/R8MKII/sound/cowbell/off":56,
    "/R8MKII/sound/crash_cymbal2/off":57,
    "/R8MKII/sound/vibra_slap/off":58,
    "/R8MKII/sound/ride_cymbal2/off":59,
    "/R8MKII/sound/high_bongo/off":60,
    "/R8MKII/sound/low_bongo/off":61,
    "/R8MKII/sound/mute_high_conga/off":62,
    "/R8MKII/sound/open_high_conga/off":63,
    "/R8MKII/sound/low_conga/off":64,
    "/R8MKII/sound/high_timbale/off":65,
    "/R8MKII/sound/low_timbale/off":66,
    "/R8MKII/sound/high_agogo/off":67,
    "/R8MKII/sound/low_agogo/off":68,
    "/R8MKII/sound/cabasa/off":69,
    "/R8MKII/sound/maracas/off":70,
    "/R8MKII/sound/short_whistle/off":71,
    "/R8MKII/sound/long_whistle/off":72,
    "/R8MKII/sound/short_guiro/off":73,
    "/R8MKII/sound/long_guiro/off":74,
    "/R8MKII/sound/claves/off":75,
    "/R8MKII/sound/high_woodblock/off":76,
    "/R8MKII/sound/low_woodblock/off":77,
    "/R8MKII/sound/mute_cuica/off":78,
    "/R8MKII/sound/open_cuica/off":79,
    "/R8MKII/sound/mute_triangle/off":80,
    "/R8MKII/sound/open_triangle/off":81
}

#     "/system/power/on/":system_power_on,
#     "/system/power/off":system_power_off,
#     "/system/clock/1/":system_clock_1,
#     "/system/clock/2/":system_clock_2,
#     "/system/clock/3/":system_clock_3,
#     "/system/clock/4/":system_clock_4,
#     "/system/miditest":system_miditest_start,
#     "/system/midipanic":system_midipanic,
#     "/system/ping":ping,
#     "/system/ping/":ping,
#     "/ping":ping,
#     "/ping/":ping,