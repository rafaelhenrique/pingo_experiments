# -*- coding: utf-8 -*-
import pingo

board = pingo.detect.get_board()
for pin in board.pins.values():
    try:
        pin.mode = pingo.OUT
        pin.hi()
    except:
        pass
