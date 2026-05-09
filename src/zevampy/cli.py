# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

import argparse
from zevampy.run_model import run_model


def main():
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