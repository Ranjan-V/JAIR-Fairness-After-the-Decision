# Differential Contestability research code

## Staged master workflow

The authoritative runner is `run_experiments.py`. Run from `JAIR/code/` with
that directory on `PYTHONPATH`:

```powershell
python run_experiments.py --stage smoke --resume
python run_experiments.py --stage theorem --resume
python run_experiments.py --stage core --resume --n-jobs 2
python run_experiments.py --stage robustness --resume --n-jobs 2
python run_experiments.py --stage realdata --config configs/my_local_full.yaml --resume
python run_experiments.py --stage aggregate
python run_experiments.py --stage figures
```

The runner supports `--config`, `--seed`, `--output-dir`, `--n-jobs`,
`--resume`, and `--force`. Resume skips seed-level jobs already marked COMPLETE
under the same configuration hash. Writes use temporary CSVs, and
`run_manifest.json` records actual run metadata; no manifest is prepopulated.

Profiles are `configs/smoke.yaml` (small grids and two seeds),
`configs/full.yaml` (20 seeds and primary research grids), and
`configs/stress.yaml` (coarse large-(N) checks). Large closed-form experiments
sample sufficient statistics instead of allocating (N\)-row data frames, so
CPU execution is the intended path.

Apply the objective gates in `EXPERIMENT_GATES.md`. The theorem stage is always
labeled `THEOREM ILLUSTRATION`; numerical agreement is not proof.

This directory implements the mathematical results in `../math/` and prepares
experiments EXP-01--EXP-10.  No result files are bundled, and project creation
did not execute any command below.

The package is CPU-first and uses only lightweight tabular/scientific Python
dependencies.  Real-data runs combine a real classification task with a
**semisynthetic contestation mechanism**; they do not estimate historical
appeal behavior.

## Installation

From `JAIR/code/`, the user may create an environment and install dependencies:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
$env:PYTHONPATH = (Get-Location).Path
```

On Linux/macOS, activate with `source .venv/bin/activate` and export
`PYTHONPATH="$PWD"`.

## Dataset preparation

No automated downloader is present.  Follow `data/README.md`, place legally
obtained CSVs locally, document provenance and mappings, and pass paths
explicitly.  The default adapters are:

- `src.datasets.adult.load_adult`
- `src.datasets.german_credit.load_german_credit`

## Synthetic experiments

Run one registered experiment:

```powershell
python scripts/run_experiment.py EXP-01 --output-dir outputs
```

Run all registered experiments:

```powershell
python scripts/run_all.py
```

Stable experiment IDs are:

| ID | Purpose | Main theorem link | Default output |
|---|---|---|---|
| EXP-01 | Fairness destruction from access gaps | Theorems 2, 5 | `outputs/exp-01.csv` |
| EXP-02 | Correction-quality disparity | Theorems 2, 7 | `outputs/exp-02.csv` |
| EXP-03 | Heterogeneous costs under common policy | Theorems 7, 8 | `outputs/exp-03.csv` |
| EXP-04 | Budget-allocation baselines B0--B6 | Theorems 9--11 | `outputs/exp-04.csv` |
| EXP-05 | Fairness--utility frontier | Proposition 6 | `outputs/exp-05.csv` |
| EXP-06 | Observationally equivalent worlds | Theorem 13 | `outputs/exp-06.csv` |
| EXP-07 | Partial-identification bounds | Theorem 14, Proposition 7 | `outputs/exp-07.csv` |
| EXP-08 | Random-audit contraction | Theorem 15, Proposition 8 | `outputs/exp-08.csv` |
| EXP-09 | Robustness grid | Theorems 5--8 | `outputs/exp-09.csv` |
| EXP-10 | Boundary cases | Propositions 1--2 | `outputs/exp-10.csv` |

The default YAML file records canonical seeds and sweep values.  Experiment
modules expose `run(...)` so a user can build expanded configuration-driven
runs without changing theorem implementations.

## Real-data experiments

Copy `configs/full.yaml`, add legal local paths under `realdata.datasets`, and
run `python scripts/run_real_data.py --config configs/my_local_full.yaml
--resume`. The harness supports logistic regression, gradient boosting, and
random forest with train/validation/test separation. Optional equal-opportunity
thresholds are selected only on validation data and frozen for test evaluation.

## Ablations

Use the public `run` arguments and `configs/default.yaml` to vary one mechanism
at a time:

- access only: EXP-01;
- review only: EXP-02;
- cost family and common subsidy: EXP-03;
- budget and policy: EXP-04;
- fairness penalty: EXP-05;
- propensity restrictions: EXP-07;
- audit rate and sample size: EXP-08;
- prevalence, classifier quality, review quality, and group count: EXP-09;
- degenerate cases: EXP-10.

For stochastic extensions, run every declared seed and preserve every output,
including null and adverse findings.

## Statistical analysis

`src/estimation/audit.py` provides finite-sample Hoeffding intervals and
simultaneous group coverage.  `src/estimation/bootstrap.py` provides a seeded
stratified bootstrap for regular plug-in estimands.  Bootstrap intervals should
not replace the guaranteed audit bounds at rare-cell or max-gap boundaries.

Report means, standard deviations, confidence intervals, and effect sizes
across seeds.  Do not infer identifiability from stable simulation averages.

## Figures

After aggregating actual full outputs:

```powershell
python scripts/aggregate_results.py --output-dir outputs/full
python scripts/make_figures.py --output-dir outputs/full
```

This creates deterministic tables and figures under the configured output tree:

1. EO gap versus appeal-access gap;
2. fairness versus assistance budget by policy;
3. fairness--utility frontier;
4. identification-interval width versus audit rate.

Additional planned views (residual group error, theoretical-versus-sampled
rates, and the cost-heterogeneity/review-accuracy heatmap) should be added only
after inspecting real outputs, without changing or suppressing runs.

## Tests

The tests statically correspond to theorem identities, counterexamples,
probability bounds, optimizer subproblems, random-audit intervals, and generator
invariants.  The user may run:

```powershell
pytest -q
```

No tests were run during repository construction.

## Reproducing each future paper table

No paper or table currently exists.  Reserve stable mappings after manual
inspection of outputs:

- TABLE-T1: theorem-verification errors from EXP-01/02/10;
- TABLE-T2: allocation-policy metrics from EXP-04;
- TABLE-T3: non-identification and bound coverage from EXP-06/07/08;
- TABLE-T4: semisynthetic real-data metrics across classifiers and seeds.

Until experiments are run, every cell is `TO_BE_MEASURED`; do not create a
table from these labels alone.

## Reproducing each future paper figure

Provisional stable mappings are:

- FIG-F1: `outputs/figures/fig01_gap_vs_access.png` from EXP-01;
- FIG-F2: `outputs/figures/fig02_fairness_budget.png` from EXP-04;
- FIG-F3: `outputs/figures/fig03_frontier.png` from EXP-05;
- FIG-F4: `outputs/figures/fig04_audit_width.png` from EXP-08.

These are mappings, not generated artifacts.  The `outputs/` directory is
empty except for `.gitkeep` until the user runs experiments.

## Baselines

- B0: no appeal assistance;
- B1: universal assistance when capacity permits;
- B2: equal subsidy;
- B3: random allocation;
- B4: allocation by expected correction need;
- B5: welfare/error-reduction optimum;
- B6: fairness-aware minimax allocation.

B5 and B6 expose optimizer success flags.  Failed convergence must be reported,
not silently replaced with a preferred policy.
