# Experiment results summary

> Generated only from files present on disk. Missing stages are labeled NOT_RUN or MISSING.

## Successful and failed runs

Standardized seed/configuration files present: 820 (220 theorem/synthetic +
600 semisynthetic real-data). Full validation: PASS, with zero errors and zero
warnings.

Failed run IDs: none recorded

## Theorem agreement

MISSING

## Primary synthetic metrics

MISSING

## Resource-allocation comparisons

MISSING

## Identification and auditing

MISSING

MISSING

## Robustness

MISSING

## Semisynthetic real-data results

- Complete factorial: 2 datasets × 3 models × 5 scenarios × 20 seeds.
- Adult: absolute EO-gap amplification has a positive paired 95% CI in 12/12
  unequal-access cells; mean changes range from +0.0442 to +0.1513.
- German Credit: expected signed movement is resolved in 7/12 unequal-access
  cells (logistic 4/4, gradient boosting 3/4, random forest 0/4), but absolute
  amplification is resolved in 0/12.
- Overall accuracy improves with a positive paired 95% CI in all 30
  dataset/model/scenario cells.
- Gate E6: PARTIAL PASS. See `RESULTS_AUDIT.md` and the paired-seed outputs
  under `artifacts/kaggle_run_352782151_2026-09-26/analysis/`.

## Validation warnings

Status: PASS

Errors: []

Warnings: []

## Interpretation guardrails

- Numerical theorem illustrations are not proofs.
- Real-data contestation is semisynthetic, not observed appeal behavior.
- Ranges above are descriptive inventory summaries, not claims of superiority.
- Consult seed-level outputs and confidence intervals before drawing conclusions.
