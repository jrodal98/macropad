# SPDX-FileCopyrightText: 2021 Emma Humphries for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys example: Universal Numpad

app = {                # REQUIRED dict, must be named 'app'
    'name' : 'Oncalls', # Application name
    'macros' : [       # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x202000, 'ping', ['#pingoncall ']),
        (0x202000, 'bl', ['oncall ']),
        (0x202000, '', ['']),
        # 2nd row ----------
        (0x202000, 'PCA', ['private_aggregation']),
        (0x202000, 'PSI', ['private_services_infra']),
        (0x202000, 'PID', ['private_id_matching']),
        # 3rd row ----------
        (0x202000, 'AAI', ['conversion_lift']),
        (0x202000, 'PCI', ['privacy_cloud']),
        (0x202000, 'Grow', ['private_computation_growth_oncall']),
        # 4th row ----------
        (0x101010, '', ['']),
        (0x800000, '', ['']),
        (0x101010, '', ['']),
        # Encoder button ---
        (0x000000, '', [''])
    ]
}
