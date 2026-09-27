import importlib.util
import json
from pathlib import Path


def _load_launcher():
    path = Path(__file__).resolve().parents[1] / "scripts" / "run_kaggle_pipeline.py"
    spec = importlib.util.spec_from_file_location("run_kaggle_pipeline", path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_realdata_inventory_is_recursive(tmp_path):
    (tmp_path / "standardized" / "realdata" / "nested").mkdir(parents=True)
    (tmp_path / "standardized" / "exp-01").mkdir(parents=True)
    (tmp_path / "standardized" / "realdata" / "adult.csv").write_text("x\n1\n")
    (tmp_path / "standardized" / "realdata" / "nested" / "german.csv").write_text("x\n1\n")
    (tmp_path / "standardized" / "exp-01" / "seed.csv").write_text("x\n1\n")

    launcher = _load_launcher()
    target = launcher._write_output_inventory(tmp_path)
    inventory = json.loads(target.read_text(encoding="utf-8"))

    assert inventory["standardized_csv_count"] == 3
    assert inventory["realdata_csv_count"] == 2
    assert inventory["counting_rule"] == "recursive"
