# SPDX-FileCopyrightText: 2021 Emma Humphries for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys: Brave web browser for Linux


from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                       # REQUIRED dict, must be named 'app'
    'name' : 'Workchat bots', # Application name
    'macros' : [              # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x004000, 'task', ['#fileatask ']),
        (0x004000, 'meet', ['#fileameeting']),
        (0x400000, 'vc', ['#fileavc\n']),
        # 2nd row ----------
        (0x202000, 'shh', ['#silent ']),
        (0x202000, 'room', ['#getmearoom\n']),
        (0x400000, 'ack', ['#ack\n']),
        # 3rd row ----------
        (0x000040, 'R-me', ['#remindme ']),
        (0x000040, 'R-us', ['#remindus ']),
        (0x000040, 'portal', ['#portalme\n']),
        # 4th row ----------
        (0x000040, 'doc', ['#shareadoc\n']),
        (0x101010, 'ty', ['#thanks ']),
        (0x000040, 'til', ['#til']),
        # Encoder button ---
        (0x000000, '', [''])
    ]
}
