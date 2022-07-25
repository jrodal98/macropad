# SPDX-FileCopyrightText: 2021 Emma Humphries for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys: Brave web browser for Linux

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                       # REQUIRED dict, must be named 'app'
    'name' : 'Mac Brave', # Application name
    'macros' : [              # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x004000, '< Back', [Keycode.COMMAND, Keycode.LEFT_ARROW]),
        (0x004000, 'Fwd >', [Keycode.COMMAND, Keycode.RIGHT_ARROW]),
        (0x400000, 'Up', [Keycode.SHIFT, ' ']),      # Scroll up
        # 2nd row ----------
        (0x202000, '< Tab', [Keycode.COMMAND, Keycode.SHIFT, Keycode.TAB]),
        (0x202000, 'Tab >', [Keycode.COMMAND, Keycode.TAB]),
        (0x400000, 'Down', ' '),                     # Scroll down
        # 3rd row ----------
        (0x000040, 'Private', [Keycode.COMMAND, Keycode.SHIFT, 'n']),
        (0x000040, 'Tab n', [Keycode.COMMAND, 't']),
        (0x000040, 'Tab o', [Keycode.COMMAND, Keycode.SHIFT, 't']),
        # 4th row ----------
        (0x000040, 'Search', [Keycode.COMMAND, Keycode.SHIFT, 'l']),
        (0x101010, 'Pi', [Keycode.COMMAND, 't', -Keycode.COMMAND,
                           '192.168.0.104\n']), # adafruit.com in a new tab
        (0x101010, 'Wiki', [Keycode.COMMAND, 't', -Keycode.COMMAND,
            'https://fburl.com/pcp_wiki\n']), # adafruit.com in a new tab
        # Encoder button ---
        (0x000000, '', [Keycode.COMMAND, 'w']) # Close window/tab
    ]
}
