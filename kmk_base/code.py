# RP2040 based basic KMK setup
import board
from kmk.modules.layers import Layers as _Layers
from kmk.extensions.rgb import RGB, AnimationModes
from kmk.keys import KC
from kmk.handlers.sequences import send_string

STRINGS = [
            send_string("NDR008 - PSX, Cars and Pizza!"),
            send_string("PSX lives forever"),
            send_string("PCSX-Redux is a cool emulator"),
            send_string("GRRRR"),
            send_string("That's cool thanks!"),
            send_string("That is awesome!")
        ]

from rp2040 import RP2040


keyboard = RP2040()
rgb = RGB(pixel_pin=board.GP16, num_pixels=1,
          animation_mode=AnimationModes.STATIC)

keyboard.extensions.append(rgb)


class Layers(_Layers):
    last_top_layer = 0
    hues = ((255, 0, 0), (0, 0, 255), (0, 255, 0))

    def after_hid_send(self, keyboard):
        if keyboard.active_layers[0] != self.last_top_layer:
            self.last_top_layer = keyboard.active_layers[0]
            rgb.set_rgb_fill(self.hues[self.last_top_layer])

keyboard.modules.append(Layers())
keyboard.keymap = [
    # Base layer
    [
        KC.F13, KC.F16, KC.F18,
        KC.F14, KC.F17, KC.F19,
        KC.F15, KC.TO(1), KC.F20,
    ],

    # Function Layer
    [
        KC.Q,  KC.W,  KC.T,
        KC.A,  KC.S,  KC.N,
        KC.LEFT, KC.TO(2), KC.RIGHT,
    ],
    [
        STRINGS[0],  STRINGS[1],  STRINGS[2],
        STRINGS[3],  STRINGS[4],  STRINGS[5],
        KC.LEFT, KC.TO(0), KC.RIGHT,
    ],
]
# fmt: on

print("NDR008 PSX Style Macro Pad Keyboard running KMK firmware")

if __name__ == '__main__':
    keyboard.go()
