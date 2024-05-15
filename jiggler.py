# emulating a mouse: a mouse jiggler
import usb_hid
from adafruit_hid.mouse import Mouse
from time import sleep

mouse = Mouse(usb_hid.devices)

while True:
    sleep(42 / 10)
    mouse.move(-42, 0, 0)    # left
    sleep(42 / 100)
    mouse.move(42, 0, 0)     # right


