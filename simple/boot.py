import usb_hid
import board
import digitalio
import storage

usb_hid.enable(
    (usb_hid.Device.KEYBOARD,
    usb_hid.Device.CONSUMER_CONTROL)
)

btn0_pin = board.GP0
btn0 = digitalio.DigitalInOut(btn0_pin)
btn0.direction = digitalio.Direction.INPUT
btn0.pull = digitalio.Pull.UP

if btn0.value:
    storage.disable_usb_drive()