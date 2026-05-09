# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

import yaml


def load_config(path=None):
    if path is None:
        # return default config instead of trying to open a file
        return {
            "data": {
                "input_path": "inputs",
                "output_path": "outputs",
            },
            "geography": {
                "countries": [],
            },
            "powertrains": ["BEV"],
            "model": {
                "start_year": 1970,
                "end_year": 2050,
            },
        }

    with open(path, "r") as f:
        return yaml.safe_load(f) or {}