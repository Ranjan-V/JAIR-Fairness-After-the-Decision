# Kaggle execution guide

The notebooks in this directory are thin launchers.  All research logic lives
under `code/src/` and `code/run_experiments.py`; notebooks do not duplicate it.
Core execution is CPU-only.  GPU is unnecessary, and TPU/JAX is not justified
for the current scientific workload.

## Upload layout

Upload or unzip the project so Kaggle can find a directory containing
`code/run_experiments.py`.  The notebooks search common locations including
`/kaggle/working/JAIR` and the current directory.

For real data, add legally obtained CSVs as Kaggle input datasets, then create a
local YAML copy of `code/configs/full.yaml` with entries such as:

```yaml
realdata:
  datasets:
    - name: adult
      path: /kaggle/input/YOUR_DATASET/adult.csv
      group_column: sex
      label_column: income
    - name: german
      path: /kaggle/input/YOUR_DATASET/german_credit.csv
      group_column: YOUR_DOCUMENTED_GROUP
      label_column: credit_risk
```

Do not put credentials in notebooks or configuration.  The code never invokes
the Kaggle API or downloads these datasets.

## Required order

1. `00_validate.ipynb`
2. `01_smoke.ipynb`
3. inspect logs, manifest, validation report, and errors
4. `02_theorem_validation.ipynb`
5. inspect theory agreement against Gate E2
6. `03_core_synthetic.ipynb`
7. `04_robustness.ipynb`
8. `05_realdata.ipynb` after configuring dataset paths
9. `06_aggregate_and_figures.ipynb`
10. `OPTIONAL_07_tpu_stress.ipynb` only to read the TPU decision

Do not proceed past a failed correctness gate.  Use `--resume` after a session
interruption.  The `full` launcher deliberately excludes optional stress work.

## Resource expectations

- Validation and smoke: LIGHT CPU/RAM/disk.
- Theorem and core synthetic: LIGHT to MODERATE; sufficient-statistic sampling
  avoids large individual arrays.
- Robustness and aggregation: LIGHT to MODERATE.
- Adult/German Credit models: MODERATE CPU and RAM; two jobs is a conservative
  Kaggle default.
- Stress profile: HEAVY CPU, but bounded memory because configured analytical
  simulations do not materialize (N\)-row tables.

## Outputs

Outputs, manifests, validation reports, tables, and figures remain under the
configured `code/outputs/` path.  Zip them from the Kaggle UI or with a final
user-run archive cell after all gates pass.

