# emulating a keyboard: typing 'n42'
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from time import sleep

keyboard = Keyboard(usb_hid.devices)

sleep(42 / 10)
keyboard.send(Keycode.N, Keycode.FOUR, Keycode.TWO)
