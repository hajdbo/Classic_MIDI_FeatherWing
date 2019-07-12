# Classic_MIDI_thru_test.py
# tests byte-by-byte receiving and transmitting via the uart

import digitalio
import board
import busio

# set up red LED activity indicator
led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

# initialize UART MIDI input and output
uart = busio.UART(board.TX, board.RX, baudrate=31250, timeout=0.001)

print("Classic_MIDI_thru_test.py")

while True:
    data = uart.read(1)  # read a bytearray from the RX pin
    if data is not None:
        led.value = True
        uart.write(data)  # send the bytearray out the TX pin
        led.value = False
