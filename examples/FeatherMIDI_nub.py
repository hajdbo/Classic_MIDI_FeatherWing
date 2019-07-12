import time
import board
import busio
from digitalio import DigitalInOut, Direction, Pull
import adafruit_midi

uart = busio.UART(board.TX, board.RX, baudrate=31250, timeout=0.001)
midi = adafruit_midi.MIDI(midi_out=uart, midi_in=uart, out_channel=0, debug=False)

button = DigitalInOut(board.A2)
button.direction = Direction.INPUT
button.pull = Pull.UP

arp0 = [45, 48, 52, 55, 57, 55, 52, 48]  # MIDI notes
arp1 = [47, 50, 54, 57, 59, 57, 54, 50]
arp2 = [45, 52, 57, 57, 52]

rest = 0.087

mode = 0  # button state
last_mode = 0

while True:
    if not button.value:  # button pushed (reversed logic due to pull up resistor)
        mode = (mode + 1) % 6
        print(mode)
        #time.sleep(rest)
    #else:
        #print("not pushed")


    if mode is 0:
        for i in range(8):
            midi.note_on(arp0[i], 127)
            time.sleep(rest)
            midi.note_off(arp0[i], 127)
            time.sleep(rest)

    if mode is 1:
        for i in range(8):
            midi.note_on(arp1[i], 127)
            time.sleep(rest)
            midi.note_off(arp1[i], 127)
            time.sleep(rest)

    if mode is 2:
        for i in range(4):
            midi.note_on(arp2[i], 127)
            time.sleep(rest*2)
            midi.note_off(arp2[i], 127)
            time.sleep(rest*2)

    if mode is 3:
        midi.note_on(33, 127)
        time.sleep(rest*4)
        midi.note_off(33, 127)
        time.sleep(rest*4)

    if mode is 4:
        midi.note_on(33, 127)
        time.sleep(rest*16)
        midi.note_off(33, 127)
        time.sleep(rest*16)

    if mode is 5:
        midi.note_on(24, 127)
        time.sleep(rest*16)
        midi.note_off(24, 127)
        time.sleep(rest*16)
