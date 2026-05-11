"""Provide the command-line interface for running the ZEVAMPY model."""

# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

import argparse
from zevampy.run_model import run_model


def main():
    """
    Run the command-line interface for the ZEVAMPY model.

    This function parses optional command-line arguments that allow users to:
    - Provide a custom configuration YAML file.
    - Override the default input data directory.
    - Override the default output directory.

    After parsing the arguments, the function executes the full modeling workflow
    through the `run_model` function.

    Command-line arguments:
        --config : str, optional
            Path to a YAML configuration file containing model settings.

        --input : str, optional
            Path to the folder containing input datasets.

        --output : str, optional
            Path to the folder where model outputs will be saved.

    Returns:
        None
    """
    parser = argparse.ArgumentParser(
        description="ZEVAMPY: Zero-Emission Vehicle Adoption Model"
    )

    parser.add_argument(
        "--config",
        default=None,
        help="Path to config YAML file"
    )

    parser.add_argument(
        "--input",
        default=None,
        help="Override input data folder"
    )

    parser.add_argument(
        "--output",
        default=None,
        help="Override output folder"
    )

    args = parser.parse_args()

    run_model(
        config_path=args.config,
        input_path=args.input,
        output_path=args.output,
    )


if __name__ == "__main__":
    main()