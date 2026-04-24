import argparse
from src.zevampy.run_model import run_model


def main():
    parser = argparse.ArgumentParser(description="ZEVAMPY: Zero-Emission Vehicle Adoption Model in Python")

    parser.add_argument(
        "--input",
        default="inputs",
        help="Path to input data folder"
    )

    parser.add_argument(
        "--output",
        default="outputs",
        help="Path to output folder"
    )

    args = parser.parse_args()

    run_model(input_path=args.input, output_path=args.output)


if __name__ == "__main__":
    main()
