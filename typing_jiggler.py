# emulating a mouse and a keyboard: a typing jiggler
import usb_hid
from adafruit_hid.mouse import Mouse
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from time import sleep

mouse = Mouse(usb_hid.devices)
keyboard = Keyboard(usb_hid.devices)

while True:
    sleep(42 / 10)
    mouse.move(-42, 0, 0)    # left
    keyboard.send(Keycode.SPACE, Keycode.L)
    sleep(42 / 100)
    mouse.move(42, 0, 0)    # right
    keyboard.send(Keycode.R)
