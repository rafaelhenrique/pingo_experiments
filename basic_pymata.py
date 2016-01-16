# -*- coding: utf-8 -*-

import signal
import sys

from PyMata.pymata import PyMata

# Pin definitions

# Digital Input Pin - D12
PUSH_BUTTON = 12

# Analog Input Pin - A0
POTENTIOMETER = 0

# Indices for data passed to callback function
PIN_MODE = 0  # This is the PyMata Pin MODE = ANALOG = 2 and DIGITAL = 0x20:
PIN_NUMBER = 10
DATA_VALUE = 2


# Control-C signal handler to suppress exceptions if user presses Crtl+C
def signal_handler(sig, frame):
    print('You pressed Ctrl+C')
    if board is not None:
        board.reset()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)


def cb_push_button(data):
    print("Digital Data:",
          " Pin: ", data[PIN_NUMBER],
          " Pin Mode: ", data[PIN_MODE],
          " Data Value: ", data[DATA_VALUE])

# Instantiate PyMata
board = PyMata("/dev/ttyACM0", verbose=True)

# Set up pin modes for both pins with callbacks for each
board.set_pin_mode(PUSH_BUTTON, board.INPUT, board.DIGITAL, cb_push_button)

# A forever loop until user presses Ctrl+C
while 1:
    pass
