# SPDX-FileCopyrightText: 2021 Emma Humphries for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys: Brave web browser for Linux


from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                       # REQUIRED dict, must be named 'app'
    'name' : 'Macros', # Application name
    'macros' : [              # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x004000, '#m', ['#m ']),
        (0x004000, 'orly', ['test_in_prod_orly']),
        (0x400000, 'lgtm', ['lgtm_from_facebook']),
        # 2nd row ----------
        (0x202000, 'flex', ['flextape']),
        (0x202000, 'zucc', ['zucc_bless_this_diff']),
        (0x400000, 'pto', ['pto_bonk']),
        # 3rd row ----------
        (0x000040, 'sev', ['wild_sev']),
        (0x000040, 'Fri', ['iroh_shipit_friday']),
        (0x000040, 'ship?', ['shipittoday']),
        # 4th row ----------
        (0x000040, 'deep', ['deep_impacc']),
        (0x101010, 'psc', ['psc_impacc']),
        (0x000040, 'pakt', ['impact_meme_man']),
        # Encoder button ---
        (0x000000, 'bl', [Keycode.COMMAND, 't', -Keycode.COMMAND,
            'macro\n'])
    ]
}
