"""Manual wrapper around the aggregation library."""

from __future__ import annotations

import argparse
from pathlib import Path

from src.reporting.aggregation import aggregate_all


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", required=True)
    args = parser.parse_args()
    for path in aggregate_all(Path(args.output_dir)):
        print(path)


if __name__ == "__main__":
    main()

