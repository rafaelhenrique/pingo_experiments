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

$ groups
rafael dialout cdrom floppy sudo audio dip video plugdev netdev bumblebee

$ ls -la /dev/tty
tty      tty11    tty15    tty19    tty22    tty26    tty3     tty33    tty37    tty40    tty44    tty48    tty51    tty55    tty59    tty62    tty9     ttyS2    
tty0     tty12    tty16    tty2     tty23    tty27    tty30    tty34    tty38    tty41    tty45    tty49    tty52    tty56    tty6     tty63    ttyACM0  ttyS3    
tty1     tty13    tty17    tty20    tty24    tty28    tty31    tty35    tty39    tty42    tty46    tty5     tty53    tty57    tty60    tty7     ttyS0    
tty10    tty14    tty18    tty21    tty25    tty29    tty32    tty36    tty4     tty43    tty47    tty50    tty54    tty58    tty61    tty8     ttyS1    

$ ls -la /dev/ttyACM0 
crw-rw---- 1 root dialout 166, 0 Jan 16 00:21 /dev/ttyACM0
```

Same error on pingo.
Can you help me? :cry:
