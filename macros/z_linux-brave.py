# SPDX-FileCopyrightText: 2021 Emma Humphries for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys: Brave web browser for Linux


"""
Note to self: we can add delays like this:

DELAY_AFTER_SLASH = 0.80 # required so minecraft has time to bring up command screen
DELAY_BEFORE_RETURN = 0.10

...

        (0x101010, 'bed', [
            '/', DELAY_AFTER_SLASH,
            'msg @a Time for bed!',
            DELAY_BEFORE_RETURN, Keycode.RETURN, -Keycode.RETURN]),
"""

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                       # REQUIRED dict, must be named 'app'
    'name' : 'Linux Brave', # Application name
    'macros' : [              # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x004000, '< Back', [Keycode.ALT, Keycode.LEFT_ARROW]),
        (0x004000, 'Fwd >', [Keycode.ALT, Keycode.RIGHT_ARROW]),
        (0x400000, 'Up', [Keycode.SHIFT, ' ']),      # Scroll up
        # 2nd row ----------
        (0x202000, '< Tab', [Keycode.CONTROL, Keycode.SHIFT, Keycode.TAB]),
        (0x202000, 'Tab >', [Keycode.CONTROL, Keycode.TAB]),
        (0x400000, 'Down', ' '),                     # Scroll down
        # 3rd row ----------
        (0x000040, 'Private', [Keycode.CONTROL, Keycode.SHIFT, 'n']),
        (0x000040, 'Tab n', [Keycode.CONTROL, 't']),
        (0x000040, 'Tab o', [Keycode.CONTROL, Keycode.SHIFT, 't']),
        # 4th row ----------
        (0x000040, 'Search', [Keycode.CONTROL, 'k']),
        (0x101010, 'Pi', [Keycode.CONTROL, 't', -Keycode.CONTROL,
                           '192.168.0.104\n']), # adafruit.com in a new tab
        (0x000040, 'Dev', [Keycode.F12]),     # dev mode
        # Encoder button ---
        (0x000000, '', [Keycode.CONTROL, 'w']) # Close window/tab
    ]
}
