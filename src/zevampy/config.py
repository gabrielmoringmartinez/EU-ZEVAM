"""Load configuration settings for the ZEVAMPY model."""

# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

import yaml


def load_config(path=None):
    """
    Load the model configuration from a YAML file.

    If no configuration file path is provided, a default configuration
    dictionary is returned. The configuration contains default settings
    for input/output paths, selected countries, powertrains, and model
    simulation years.

    Parameters:
        path (str, optional):
            Path to a YAML configuration file. If None, a default
            configuration is used.

    Returns:
        dict:
            Dictionary containing model configuration parameters.

    Notes:
        - YAML files are loaded using `yaml.safe_load`.
        - If the YAML file is empty, an empty dictionary is returned.
        - Command-line arguments may later override some configuration values.
    """
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