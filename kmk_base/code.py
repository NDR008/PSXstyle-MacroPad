from kmk.modules.layers import Layers as Layers
from kmk.extensions.rgb import RGB, AnimationModes
from kmk.keys import KC
from rp2040 import RP2040

import board

rgb = RGB(pixel_pin=board.GP16, num_pixels=1,
          animation_mode=AnimationModes.RAINBOW)

keyboard = RP2040()
keyboard.extensions = [rgb]

keyboard.modules.append(Layers())
keyboard.keymap = [
    # Base layer
    [
        KC.F13, KC.F14, KC.F15,
        KC.F16, KC.F16, KC.F17,
        KC.TG(1), KC.HOME, KC.END,
    ],

    # Function Layer
    [
        KC.Q,  KC.W,  KC.R,
        KC.A,  KC.S,  KC.D,
        KC.LEFT, KC.Z, KC.X,
    ],
]
# fmt: on

print("NDR008 PSX Style Macro Pad Keyboard running KMK firmware")

if __name__ == '__main__':
    keyboard.go()
