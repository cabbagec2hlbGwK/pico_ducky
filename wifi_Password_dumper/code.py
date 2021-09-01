import usb_hid
import time
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode as K

time.sleep(1)
keyboard = Keyboard(usb_hid.devices)
keyboard.send(K.WINDOWS, K.R)
time.sleep(0.5)
keyboard.send(K.C, K.M, K.D)
time.sleep(0.2)
keyboard.send(K.ENTER)