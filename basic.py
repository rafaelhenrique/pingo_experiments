# -*- coding: utf-8 -*-
import pingo

try:
    board = pingo.detect.get_board()
except Exception as err:
    print("Previous exception: {}".format(err))
    board = pingo.detect.MyBoard()

