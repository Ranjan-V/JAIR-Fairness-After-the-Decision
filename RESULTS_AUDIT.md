# Post-run results and gate audit

Audit date: 2026-09-26  
Kaggle notebook: `ranjanv1/jair-differential-contestability-full-pipeline`  
Final audited run: `352782151`, CPU, Internet disabled  
Run interval: 2026-09-25 18:51:07--19:12:56 UTC  
Downloaded archive: original Kaggle results archive (local filename omitted)  
Archive SHA-256: `AE30CA19BF912DB8FEB1BE33E263C994F73ED3C2556E6EFF6D6EB69747BCBF1A`  
Archive size: 21,451,611 bytes  
Immutable extracted run: `artifacts/kaggle_run_352782151_2026-09-26/`

## Executive decision

Gates E0--E5 pass. Gate E6 receives an honest **PARTIAL PASS**.

The Adult semisynthetic evaluation robustly reproduces post-contestation
equal-opportunity disparity under every unequal-access scenario and all three
models. German Credit shows the predicted signed movement for logistic
regression and gradient boosting, especially under strong asymmetry, but does
not show broad absolute-gap amplification; random forest is effectively null.
The correct claim is therefore cross-dataset evidence for the directional
mechanism, with stable absolute amplification on Adult only.

Status: `RESULTS_VALIDATED_E6_PARTIAL_PASS_NOVELTY_AUDITED`.

## Post-archive proof and reproducibility audit (2026-09-27)

- The theorem-by-theorem audit is a **PASS WITH CORRECTIONS**. It found no
  invalid central theorem, but tightened Theorem 1's domain, corrected the
  target-budget infeasibility boundary, and repaired the zero-mass FNR cases.
- A clean virtual environment installed the declared dependency ranges from
  scratch and passed all 42 tests; the proof-linked subset passed 18/18.
- The immutable archive's 820 standardized CSVs revalidated with zero errors
  and zero warnings. E6 summaries were regenerated from the archived 600 files
  without model retraining.
- A fresh non-E6 rerun regenerated all 220 theorem/synthetic files. Scientific
  content matches at absolute and relative tolerance `1e-6`. Byte identity
  does not hold across Kaggle/Linux and local/Windows because of line endings,
  serialization-only parameter strings/hashes, and optimizer/library
  last-digit differences; the largest numeric deviation is
  `5.3896548557474944e-08`.
- E6 remains a **PARTIAL PASS**. Reproducibility work does not upgrade the
  empirical gate.

## Pipeline and archive integrity

- The archive hash was independently verified before extraction.
- The archive contains 1,848 files and 234,320,450 unpacked bytes.
- Kaggle reports all pipeline commands with return code zero.
- Full validation reports `PASS`, with zero errors and zero warnings.
- Exactly 820 standardized CSVs are present: 220 theorem/synthetic seed files
  and 600 E6 real-data files.
- The E6 factorial is complete: 2 datasets × 3 models × 5 scenarios × 20
  seeds = 600 files, with no missing design cell.
- The emitted `realdata_csv_count: 0` is a bookkeeping bug: the wrapper counted
  the wrong level. The files are present and validated. The launcher now uses
  a recursive `standardized/realdata/**/*.csv` inventory and has a regression
  test. No scientific rerun is needed.

## Gate decisions

| Gate | Decision | Evidence |
|---|---|---|
| E0 unit tests | PASS | Kaggle completed the unit-test stage before all experiments. |
| E1 smoke | PASS | Smoke validation and full validation passed with zero errors/warnings. |
| E2 theory agreement | PASS | All 560 theorem-suite rows across 20 seeds meet the predeclared row-specific tolerance; exact rows have zero error. |
| E3 main phenomenon | PASS | Direction agrees with theory throughout the broad synthetic interior grids, not only at boundaries. |
| E4 intervention | PASS | B6 yields a nontrivial EO-gap/aggregate-loss trade-off and is not dominated everywhere. |
| E5 identification | PASS | Observable-equivalence constructions, sharp bounds, and audit-width contraction behave as predicted. |
| E6 real data | **PARTIAL PASS** | Adult gives stable absolute amplification in 12/12 unequal-access comparisons. German gives the expected signed movement in 7/12 comparisons but absolute amplification in 0/12; random forest is null. |

## E6 design and statistical method

Adult and German Credit are real prediction tasks with a **semisynthetic
post-decision contestation process**. They are not datasets of observed human
appeals. For each dataset, the pipeline fits logistic regression, gradient
boosting, and random forest using train/validation/test separation and freezes
validation-calibrated group thresholds before test evaluation.

The five predeclared scenarios are equal access, moderate/strong first-group
advantage, and moderate/strong second-group advantage. Seeds 1729--1748 give
20 paired pre/post observations per dataset–model–scenario cell. The E6 audit
uses two-sided 95% Student-t intervals for paired seed-level changes. The
reproducible output is in
`artifacts/kaggle_run_352782151_2026-09-26/analysis/`.

## E6 findings

### Adult

- Validation-calibrated pre-contestation EO gaps average 0.031--0.039 across
  models.
- All 12 unequal-access model/scenario cells increase the absolute EO gap,
  and every paired 95% CI excludes zero.
- Mean absolute-gap increases range from 0.0442 to 0.1513.
- All 12 signed changes move in the direction predicted by which group has
  greater false-denial appeal access; every paired CI excludes zero.
- Overall accuracy improves in all 15 model/scenario cells, with all paired
  CIs above zero. This is compatible with the mechanism: review is mostly
  corrective, yet unequal access redistributes who receives that improvement.

### German Credit

- The smaller test strata produce visibly noisier calibration and inference:
  pre-contestation EO gaps average 0.0275 (random forest), 0.0742 (gradient
  boosting), and 0.0945 (logistic).
- The expected signed shift is resolved in 7/12 unequal-access cells: 4/4 for
  logistic, 3/4 for gradient boosting, and 0/4 for random forest.
- Signed mean changes range from -0.0700 to +0.0443. Strong asymmetry is the
  clearest region for logistic and gradient boosting.
- No German cell has a positive paired CI for an increase in the absolute EO
  gap. Existing sampling/calibration gaps are often reduced or crossed rather
  than monotonically amplified.
- Accuracy nevertheless improves in all 15 cells with paired CIs above zero,
  confirming that the null fairness result is not a failed execution.

### Interpretation

German Credit supports Theorem 5's signed-gap dynamics more than the special
initially-fair amplification corollary. This is scientifically informative:
unequal contestability can amplify, reduce, or reverse an existing gap,
depending on its initial direction. The dataset is too small to support a
broad model-agnostic absolute-amplification claim.

## Synthetic quantitative highlights retained

- EXP-01 theoretical signed gaps span -0.24 to 0.24; empirical means track
  them with mean absolute errors of 0.000441--0.001621.
- EXP-02 theoretical signed gaps span -0.15 to 0.15; mean absolute errors are
  0.000640--0.001522.
- EXP-03 mean absolute errors are 0.000379--0.001324.
- At interior budgets, B6 substantially reduces the EO gap relative to
  uniform, random, and proportional baselines; it reaches zero on the reported
  grid from budget 0.75 while retaining the stated welfare trade-off.
- EXP-06 contains four observationally equivalent world pairs with oracle FNR
  differences from 1/3 to 2/3.
- EXP-08 aggregate interval width contracts from 0.1496 at audit rate 0.001 to
  0.0102 at 0.20, with reported coverage 1.0 across the grid.

## Claim discipline

Supported:

- the implemented transformation matches the derived theory;
- self-selected contestation can create, amplify, reduce, or reverse group
  disparity according to the exact signed-gap formula;
- stable absolute amplification occurs across Adult models and access regimes;
- German Credit supplies qualified directional support for two models but not
  broad absolute amplification;
- the allocation and identification mechanisms behave as predicted in the
  synthetic evaluation.

Not supported:

- real observed appeal behavior or institutional cost estimates;
- a universal claim that unequal access always increases absolute disparity;
- a model-robust German Credit effect;
- any “first work” or exhaustive literature-priority claim.

The source-based positioning audit is in `NOVELTY_LITERATURE_AUDIT.md` and must
be reflected in every manuscript claim.
