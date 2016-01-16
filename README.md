# Try Pingo

[https://github.com/pingo-io/pingo-py](https://github.com/pingo-io/pingo-py)

Its cool project :D

My serial/usb dont work now :disappointed:...

```
$ python basic_pymata.py 

Python Version 2.7.7 (default, Jan  6 2016, 19:56:29) 
[GCC 4.9.2]

PyMata version 2.11  Copyright(C) 2013-15 Alan Yorinks    All rights reserved.

Opening Arduino Serial port /dev/ttyACM0 

Please wait while Arduino is being detected. This can take up to 30 seconds ...
Board Auto Discovery Failed!, Shutting Down
Traceback (most recent call last):
  File "basic_pymata.py", line 43, in <module>
    board.set_pin_mode(PUSH_BUTTON, board.INPUT, board.DIGITAL, cb_push_button)
  File "/home/rafael/.virtualenvs/pymata/lib/python2.7/site-packages/PyMata/pymata.py", line 733, in set_pin_mode
    self._command_handler.send_command(command)
  File "/home/rafael/.virtualenvs/pymata/lib/python2.7/site-packages/PyMata/pymata_command_handler.py", line 633, in send_command
    self.pymata.transport.write(data)
  File "/home/rafael/.virtualenvs/pymata/lib/python2.7/site-packages/PyMata/pymata_serial.py", line 107, in write
    self.arduino.write(data)
  File "/home/rafael/.virtualenvs/pymata/lib/python2.7/site-packages/serial/serialposix.py", line 490, in write
    if not self._isOpen: raise portNotOpenError
serial.serialutil.SerialException: Attempting to use a port that is not open
```

Same error on pingo.
Can you help me? :cry:
