"""Compatibility wrapper for publication asset generation."""

from __future__ import annotations

import argparse
from pathlib import Path

from src.reporting.publication import build_all_figures_and_tables


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", required=True)
    args = parser.parse_args()
    build_all_figures_and_tables(Path(args.output_dir))


if __name__ == "__main__":
    main()

