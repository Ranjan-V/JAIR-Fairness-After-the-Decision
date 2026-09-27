"""Compatibility wrapper for the configured semisynthetic real-data stage."""

from __future__ import annotations

import argparse
from pathlib import Path

import yaml

from src.experiments.realdata_semisynthetic import run_configured_realdata


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True, help="YAML containing realdata.datasets paths and schemas")
    parser.add_argument("--output-dir")
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()
    config = yaml.safe_load(Path(args.config).read_text(encoding="utf-8"))
    run_configured_realdata(config, args.output_dir, args.resume, args.force)


if __name__ == "__main__":
    main()
