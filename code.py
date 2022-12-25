# NDR008: Macropad
# Based on the example from: https://github.com/adafruit/Adafruit_CircuitPython_HID/blob/main/examples/hid_keyboard_shortcuts.py
# Also from: https://github.com/adafruit/Adafruit_CircuitPython_HID

import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

import digitalio
import board
import neopixel

macro = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(macro)

pixel = neopixel.NeoPixel(board.GP16, 1)
pixel.brightness = 1.0

btn0_pin = board.GP0
btn0 = digitalio.DigitalInOut(btn0_pin)
btn0.direction = digitalio.Direction.INPUT
btn0.pull = digitalio.Pull.UP

btn1_pin = board.GP1
btn1 = digitalio.DigitalInOut(btn1_pin)
btn1.direction = digitalio.Direction.INPUT
btn1.pull = digitalio.Pull.UP

btn2_pin = board.GP2
btn2 = digitalio.DigitalInOut(btn2_pin)
btn2.direction = digitalio.Direction.INPUT
btn2.pull = digitalio.Pull.UP

btn3_pin = board.GP3
btn3 = digitalio.DigitalInOut(btn3_pin)
btn3.direction = digitalio.Direction.INPUT
btn3.pull = digitalio.Pull.UP

btn4_pin = board.GP4
btn4 = digitalio.DigitalInOut(btn4_pin)
btn4.direction = digitalio.Direction.INPUT
btn4.pull = digitalio.Pull.UP

btn5_pin = board.GP5
btn5 = digitalio.DigitalInOut(btn5_pin)
btn5.direction = digitalio.Direction.INPUT
btn5.pull = digitalio.Pull.UP

btn6_pin = board.GP6
btn6 = digitalio.DigitalInOut(btn6_pin)
btn6.direction = digitalio.Direction.INPUT
btn6.pull = digitalio.Pull.UP

btn7_pin = board.GP7
btn7 = digitalio.DigitalInOut(btn7_pin)
btn7.direction = digitalio.Direction.INPUT
btn7.pull = digitalio.Pull.UP

btn8_pin = board.GP8
btn8 = digitalio.DigitalInOut(btn8_pin)
btn8.direction = digitalio.Direction.INPUT
btn8.pull = digitalio.Pull.UP

cc = ConsumerControl(usb_hid.devices)

time.sleep(1)

mode2 = True
counter = 0

colT = (255, 255, 255)
colF = (255, 10, 10)

pixel[0] = colT
pixel.write()

while True:
    #pixel.fill((255, 0, 0))
    if not btn1.value and not btn7.value:
        counter = counter + 1
        time.sleep(0.1)
        if counter > 5:
            mode2 = not mode2
            counter = 0
            if mode2:
                pixel[0] = colT
            else:
                pixel[0] = colF
            pixel.write()
            time.sleep(0.3)

    elif mode2:
        if not btn0.value:
            macro.send(Keycode.F13)
            time.sleep(0.2)
        if not btn1.value:
            macro.send(Keycode.F14)
            time.sleep(0.2)
        if not btn2.value:
            macro.send(Keycode.F15)
            time.sleep(0.2)
        if not btn3.value:
            macro.send(Keycode.F16)
            time.sleep(0.2)
        if not btn4.value:
            macro.send(Keycode.F17)
            time.sleep(0.2)
        if not btn5.value:
            macro.send(Keycode.F18)
            time.sleep(0.2)
        if not btn6.value:
            macro.send(Keycode.F19)
            time.sleep(0.2)
        if not btn7.value:
            macro.send(Keycode.F20)
            time.sleep(0.2)
        if not btn8.value:
            # layout.write("NDR008 was here! ")
            macro.send(Keycode.F21)
            time.sleep(0.2)

    elif not mode2:
        if not btn0.value:
            layout.write("o_O")
            time.sleep(0.2)
        if not btn2.value:
            layout.write("I got no clue about that")
            time.sleep(0.2)
        if not btn3.value:
            layout.write("Please explain...")
            time.sleep(0.2)
        if not btn6.value:
            layout.write("Who knows...")
            time.sleep(0.2)
        if not btn8.value:
            layout.write("cool!")
            time.sleep(0.2)
