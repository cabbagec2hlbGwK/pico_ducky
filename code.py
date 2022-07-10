import time
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode as K
from typer import typer

keyboard = Keyboard(usb_hid.devices)
t = typer(keyboard)

t.powershell("notepad",True)
t.type("this is a sample string")
t.cmd(" echo 'this is working'", True)
