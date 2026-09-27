# Experimental readiness

## Post-run update (2026-09-26)

Kaggle run `352782151` completed the configured CPU pipeline, including Adult
and German Credit. Gates E0--E5 pass; full validation reports PASS with no
errors or warnings. Gate E6 is a PARTIAL PASS: Adult is robust, while German
Credit supplies qualified directional evidence for two models and a null
random-forest result. The hash-verified outputs are stored under
`artifacts/kaggle_run_352782151_2026-09-26/`, and the detailed decision record
is `RESULTS_AUDIT.md`.

## Code status

The CPU-first package now covers unit-test preparation, smoke runs, theorem
illustrations, core synthetic experiments, robustness, semisynthetic real data,
aggregation, and publication assets. Seed-level jobs write raw and standardized
CSV files plus an atomic manifest and can resume by configuration hash.

Runtime correctness for the configured synthetic and semisynthetic real-data
pipeline is supported by the successful Kaggle run and output validation.

## Theory-code mapping

`code/THEORY_CODE_AUDIT.md` maps every CORE result to its quantity,
implementation, test, and experiment. No mathematical contradiction was found.
Formerly partial numerical links—sampled formula comparisons, the impossibility
illustration, operator compatibility, and KKT diagnostics—now have source-level
coverage.

## Unit-test coverage

Tests cover probability identities and bounds; EO, FPR, equalized-odds and DP
behavior; perfect, zero, universal and harmful-review boundaries; operator
invariance; cost responses; optimizer feasibility and an analytical KKT case;
knapsack; identification bounds; random audits; generator invariants; and the
major computational counterexamples.

```powershell
cd code
$env:PYTHONPATH = (Get-Location).Path
pytest -q
```

## Smoke-run commands

```powershell
python run_experiments.py --stage smoke --resume
python scripts/validate_outputs.py --output-dir outputs/smoke --expected-seeds 1729 1730
```

Stop if Gate E0 or E1 fails.

## Core-run commands

```powershell
python run_experiments.py --stage theorem --resume --n-jobs 2
python run_experiments.py --stage core --resume --n-jobs 2
python run_experiments.py --stage robustness --resume --n-jobs 2
```

Inspect Gate E2 and E5 before interpreting scientific results.

## Full-run commands

After configuring legal local dataset paths in a copy of `configs/full.yaml`:

```powershell
python run_experiments.py --stage realdata --config configs/my_local_full.yaml --resume --n-jobs 2
python scripts/validate_outputs.py --output-dir outputs/full
python run_experiments.py --stage aggregate
python run_experiments.py --stage figures
python scripts/build_results_summary.py --output-dir outputs/full
```

`--stage all` excludes optional stress.

## Expected approximate resource requirements

| Stage | CPU | RAM | Disk | Basis |
|---|---|---|---|---|
| Unit tests | LIGHT | LIGHT | LIGHT | Small arrays and optimizers. |
| Smoke | LIGHT | LIGHT | LIGHT | Two seeds and small grids. |
| Theorem | LIGHT--MODERATE | LIGHT | LIGHT | Binomial sufficient statistics, not (N\)-row tables. |
| Core synthetic | MODERATE | LIGHT--MODERATE | MODERATE | Twenty seeds and bounded grids. |
| Robustness | LIGHT | LIGHT | LIGHT | Structured, not full-factorial. |
| Real data | MODERATE | MODERATE | MODERATE | Dense one-hot small tabular models; two jobs is conservative. |
| Aggregation/figures | LIGHT--MODERATE | MODERATE | MODERATE | Scales with saved CSV rows. |
| Stress | HEAVY | LIGHT--MODERATE | MODERATE | Up to five million sufficient-statistic trials. |

No fabricated runtime is stated. For Adult/German-sized tables, 16 GB RAM
should be adequate with conservative parallelism.

## Kaggle suitability

| Stage | CPU | GPU | TPU |
|---|---|---|---|
| Tests/smoke/theorem | Sufficient | Not useful | Unnecessary |
| Core/robustness | Sufficient | Not useful | Unnecessary |
| Real data | Sufficient | Not required | Unnecessary |
| Aggregation/figures | Sufficient | Not useful | Unnecessary |
| Optional stress | Sufficient but heavier | Not required | Not justified currently |

The Kaggle notebooks are output-free launchers calling the source runner. The
optional TPU notebook records `TPU_EXTENSION_NOT_JUSTIFIED`; JAX was not added.

## Missing requirements

- No required experiment is missing for the present paper scope.
- External validation with observed appeal behavior remains future work, not a
  condition satisfied by these semisynthetic datasets.
- Any future tolerance or gate change requires sampling-model justification;
  it may never be changed merely to improve a result.

## Known risks

- Validation fairness calibration can be noisy for rare groups.
- Dense one-hot encoding may be inefficient for unplanned high-cardinality data.
- Oracle columns in EXP-06 must remain outside observable estimators.
- Experiments may show small effects, baseline dominance, or failed real-data
  reproduction; those outcomes must be preserved.
- Checkpointing is seed-level because configured sufficient-statistic sweeps are
  short; interruption reruns one seed rather than an entire stage.

## Final status

`RESULTS_VALIDATED_E6_PARTIAL_PASS_NOVELTY_AUDITED`

Gates E0--E5 pass, E6 partially passes, and the focused source-based novelty
audit is complete. Manuscript drafting may proceed only with the qualified
German result and the narrow contribution language in
`NOVELTY_LITERATURE_AUDIT.md`.
