from pathlib import Path
import argparse


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "input", help="Directory containing files to translate", type=Path
    )
    parser.add_argument(
        "-l", "--language", help="Language to translate to", default="english"
    )
    parser.add_argument(
        "-d",
        "--definitions",
        help="Directory containing word definitions",
        required=True,
        type=Path,
    )
    return parser.parse_args()
