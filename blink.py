# -*- coding: utf-8 -*-
import pingo
from time import sleep

board = pingo.detect.get_board()
led_pin = board.pins[11]
led_pin.mode = pingo.OUT

while True:
    led_pin.hi()
    sleep(1)
    led_pin.lo()
    sleep(1)
