"""
KMK for RP2040 with direct GPIO pins
NDR008
"""
# https://gist.github.com/Corteil/e2297184ec1008230669176f2e1b5249

import board
import sys

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner


def rp2040_pins():
    return [
        board.GP0, board.GP3, board.GP6,
        board.GP1, board.GP4, board.GP7,
        board.GP2, board.GP5, board.GP8,
    ]


def isRP2040():
    return sys.platform == "RP2040"


if isRP2040():
    _KEY_CFG = rp2040_pins()


class RP2040(KMKKeyboard):
    """
    Default keyboard config for the Keybow.
    """

    def __init__(self):
        self.matrix = KeysScanner(_KEY_CFG)
