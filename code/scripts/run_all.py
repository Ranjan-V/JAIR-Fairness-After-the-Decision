"""Manual sequential runner; intentionally never invoked by project creation."""

from __future__ import annotations

import importlib
from pathlib import Path

from run_experiment import MODULES


def main() -> None:
    output = Path("outputs")
    output.mkdir(parents=True, exist_ok=True)
    for experiment, module_name in MODULES.items():
        frame = importlib.import_module(module_name).run()
        frame.to_csv(output / f"{experiment.lower()}.csv", index=False)


if __name__ == "__main__":
    main()

