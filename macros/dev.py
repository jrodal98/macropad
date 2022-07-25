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

TMUX_LEADER_DELAY = 0
TMUX_LEADER = [Keycode.CONTROL, ' ', -Keycode.CONTROL, TMUX_LEADER_DELAY]

app = {                       # REQUIRED dict, must be named 'app'
    'name' : 'Tmux', # Application name
    'macros' : [              # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x004000, 'N Tab', TMUX_LEADER + ['c']),
        (0x004000, 'V spl', TMUX_LEADER + ['|']),
        (0x004000, 'H spl', TMUX_LEADER + ['-']),      # Scroll up
        # 2nd row ----------
        (0x400000, '< Tab', TMUX_LEADER + ['p']),
        (0x000040, 'Up', TMUX_LEADER + ['k']),
        (0x400000, 'Tab >', TMUX_LEADER + ['n']),                     # Scroll down
        # 3rd row ----------
        (0x000040, 'Left', TMUX_LEADER + ['h']),
        (0x000040, 'Down', TMUX_LEADER + ['j']),
        (0x000040, 'Right', TMUX_LEADER + ['l']),
        # 4th row ----------
        (0x101010, 'Help', TMUX_LEADER + ['?']),
        (0x101010, 'Copy', TMUX_LEADER + ['[']), # adafruit.com in a new tab
        (0x000000, '', ['']),     # dev mode
        # Encoder button ---
        (0x000000, '', TMUX_LEADER + ['x', 'y']) # Close window/tab
    ]
}
