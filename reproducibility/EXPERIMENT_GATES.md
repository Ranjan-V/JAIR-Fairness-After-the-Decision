# Experimental failure gates

These gates are evaluated only after the corresponding stage is run. Kaggle
run `352782151` has now been evaluated. Gates E0--E5 pass and E6 partially
passes. The evidence and claim limits are recorded in `../RESULTS_AUDIT.md`;
the predeclared definitions below are unchanged.

## GATE E0 — Unit tests

PASS: all critical theorem, probability, optimization, identification, and
counterexample tests pass.  FAIL: any core theorem implementation test fails.

On failure: `STOP_EXPERIMENTS`.  Inspect source and mathematics; never relax a
test merely to continue.

## GATE E1 — Smoke

PASS if every EXP-01--EXP-10 smoke job completes, standardized CSVs parse,
probabilities are legal, unexplained NaN/infinity is absent, optimizers report
feasibility, budgets hold within (10^{-7}), and `validate_outputs.py` returns
PASS.  Otherwise: `STOP_EXPERIMENTS`.

## GATE E2 — Theory agreement

For a binomial rate estimate with theoretical value (p) and effective sample
size (N), define

\[
\tau(N,p)=4\sqrt{\max\{p(1-p),10^{-6}\}/N}+2/N.
\]

PASS a closed-form rate row when absolute error is at most this conservative
four-standard-error tolerance.  For a difference of two independent rates,
use the sum of their variance terms under the square root.  Exact algebraic
checks use tolerance (10^{-10}); optimizer/KKT checks use (10^{-5}) unless
the configuration documents a stricter solver tolerance.  Across increasing
sample sizes, median absolute error should show a decreasing trend; monotonicity
of every random realization is not required.

Persistent systematic violation at large (N): `STOP_AND_AUDIT`.

## GATE E3 — Main phenomenon

PASS if a broad interior range—not only zero/universal-appeal boundaries—shows
the signed and absolute disparity predicted by Theorems 5, 7, and 8, with
direction agreeing with theory.  If the phenomenon occurs only in contrived
boundary settings: `WEAK_EMPIRICAL_SUPPORT`.

## GATE E4 — Intervention

PASS if the fairness-aware allocation yields a meaningful, nontrivial
fairness/aggregate-loss trade-off relative to uniform, random, proportional,
and welfare/error-reduction baselines for at least one interior budget region.
It need not dominate every metric.  If it is Pareto-dominated everywhere:
`ALGORITHM_NEEDS_REVISION`.

## GATE E5 — Identification

PASS if EXP-06 produces equal observable signatures with unequal oracle targets,
Theorem 14 intervals contain their constructed truths, and EXP-08 coverage and
width behave consistently with the audit theory.  Otherwise:
`IDENTIFICATION_AUDIT_REQUIRED`.

## GATE E6 — Real data

PASS if the semisynthetic phenomenon appears over plausible, predeclared
parameter ranges on both Adult and German Credit, after validation-set
calibration and frozen test evaluation.  A single cherry-picked configuration
does not pass.  If effects vanish broadly, record that result without changing
the gate post hoc.

**Observed decision: PARTIAL PASS.** Adult shows absolute EO-gap amplification
with paired 95% CIs above zero in 12/12 unequal-access model/scenario cells.
German Credit shows the predicted signed shift in 7/12 cells (logistic 4/4,
gradient boosting 3/4, random forest 0/4) but absolute amplification in 0/12.
This supports a cross-dataset directional mechanism but not broad
cross-dataset absolute amplification. The 600-run factorial is complete and
validated; this decision is not caused by missing outputs.

## Progression rule

Run gates in order.  E0/E1/E2/E5 are correctness gates and block later claims.
E3/E4/E6 assess scientific strength; failure does not license suppression or
parameter fishing, but may require revising the intervention or project claim.
