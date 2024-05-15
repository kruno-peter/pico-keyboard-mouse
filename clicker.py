# emulating a mouse: the left click
import usb_hid
from adafruit_hid.mouse import Mouse
import board
import digitalio
from time import sleep

mouse = Mouse(usb_hid.devices)
button = digitalio.DigitalInOut(board.GP16)
button.switch_to_input(pull=digitalio.Pull.DOWN)    # GP16 -> GND

while True:
    if button.value:                      
        mouse.click(Mouse.LEFT_BUTTON)    # the left click
        sleep(42 / 100)                   # preventing multiple clicks