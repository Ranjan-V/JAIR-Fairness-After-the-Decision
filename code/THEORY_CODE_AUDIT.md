# Theory-to-code consistency audit

Audit basis: `math/theorem_index.md`, `math/proof_audit.md`, and the current
source tree.  Mathematics remains authoritative.  No research code was run.

## Theorem 1
Theorem ID: Theorem 1.  
Mathematical quantity: (Lp=0\Rightarrow LT_Kp=0), equivalently kernel
invariance/factorization.  
Implementation file: `src/fairness/operators.py`.  
Function/class: `preserves_linear_constraint`.  
Experiment validating it: theorem stage, static operator scenarios; no
population simulation is scientifically necessary.  
Unit test: `tests/test_operators.py::test_operator_preservation_and_failure`.  
Expected qualitative behavior: common compatible kernels preserve the linear
constraint; unequal incompatible kernels fail the kernel test.  
Status: COMPLETE.

## Theorems 2--3 and Corollary 2
Theorem ID: Theorem 2, Theorem 3, Corollary 2.  
Mathematical quantity: equal-opportunity, FPR-parity, and equalized-odds
preservation under equal effective label-specific transitions.  
Implementation file: `src/contestation/transforms.py`, `src/fairness/metrics.py`.  
Function/class: `post_contestation_rates`, `signed_tpr_gap_after`,
`pairwise_gaps`.  
Experiment validating it: theorem stage; EXP-01; EXP-02; EXP-10.  
Unit test: `test_transforms.py`, `test_fairness_theorems.py`,
`test_counterexamples.py`.  
Expected qualitative behavior: gaps converge to zero under matching effective
transitions and to the exact nonzero formula otherwise.  
Status: COMPLETE.

## Theorem 4
Theorem ID: Theorem 4.  
Mathematical quantity: base-rate-weighted increment governing demographic
parity preservation.  
Implementation file: `src/fairness/metrics.py`.  
Function/class: `demographic_parity_increment`.  
Experiment validating it: theorem stage DP cases; EXP-10 boundary suite.  
Unit test: `test_fairness_theorems.py::test_theorem_4_dp_counterexample`.  
Expected qualitative behavior: equal transitions can break demographic parity
when weighted appealable masses differ.  
Status: COMPLETE.

## Theorems 5--6
Theorem ID: Theorem 5, Theorem 6.  
Mathematical quantity: exact signed gap dynamics and tight attainable range.  
Implementation file: `src/fairness/metrics.py`, `src/fairness/bounds.py`.  
Function/class: `signed_tpr_gap_after`, `attainable_signed_tpr_gap`,
`attainable_absolute_gap`.  
Experiment validating it: theorem stage and EXP-01.  
Unit test: `test_fairness_theorems.py`.  
Expected qualitative behavior: empirical gaps approach the affine prediction;
corner transitions attain the analytical bounds.  
Status: COMPLETE.

## Theorems 7--8
Theorem ID: Theorem 7, Theorem 8.  
Mathematical quantity: common subsidy maps heterogeneous cost CDFs into unequal
effective corrections; strict pointwise order prevents EO preservation.  
Implementation file: `src/contestation/costs.py`.  
Function/class: cost-family CDFs and `appeal_probability`.  
Experiment validating it: theorem-stage impossibility illustration; flagship
EXP-03.  
Unit test: `test_costs_and_allocation.py`, `test_counterexamples.py`.  
Expected qualitative behavior: the formally identical policy yields ordered
appeal rates, correction rates, and post-FNRs at operative thresholds.  
Status: COMPLETE.

## Theorem 10
Theorem ID: Theorem 10.  
Mathematical quantity: convex minimax allocation under concave response and
convex cost.  
Implementation file: `src/optimization/continuous.py`.  
Function/class: `solve_minimax`.  
Experiment validating it: EXP-04 and EXP-05.  
Unit test: `test_costs_and_allocation.py::test_continuous_optimizers_respect_budget_and_bounds`.  
Expected qualitative behavior: feasible allocations respect budget and reduce
the maximum residual risk.  
Status: COMPLETE.

## Theorem 11
Theorem ID: Theorem 11.  
Mathematical quantity: equality of weighted marginal harm reduction per unit
resource for active interior groups.  
Implementation file: `src/optimization/continuous.py`.  
Function/class: `solve_weighted_residual`.  
Experiment validating it: EXP-04 KKT diagnostics.  
Unit test: `tests/test_optimization_kkt.py`.  
Expected qualitative behavior: analytical and numerical interior allocations
agree within declared tolerance.  
Status: COMPLETE.

## Proposition 6
Theorem ID: Proposition 6.  
Mathematical quantity: exact minimum assistance and budget for a common
residual-risk target.  
Implementation file: `src/optimization/closed_form.py`.  
Function/class: `required_appeal_probability`, `minimum_subsidy`,
`minimum_budget`.  
Experiment validating it: theorem stage and EXP-04.  
Unit test: `test_costs_and_allocation.py::test_minimum_subsidy_hits_target`.  
Expected qualitative behavior: the inverse-CDF allocation hits the target;
any componentwise smaller assistance misses it when the response is strict.  
Status: COMPLETE.

## Theorem 12
Theorem ID: Theorem 12.  
Mathematical quantity: indivisible welfare allocation is 0--1 knapsack.  
Implementation file: `src/optimization/discrete.py`.  
Function/class: `knapsack_dynamic_program`.  
Experiment validating it: theorem stage exact instance; optional discrete
substudy within EXP-04.  
Unit test: `test_costs_and_allocation.py::test_knapsack_regression_against_ratio_greedy`.  
Expected qualitative behavior: dynamic programming finds value 220 where
ratio greedy finds 160 in CE-14.  
Status: COMPLETE.

## Theorem 13 and Corollary 5
Theorem ID: Theorem 13, Corollary 5.  
Mathematical quantity: identical observed appeal laws with different latent
final FNR/fairness.  
Implementation file: `src/identification/worlds.py`.  
Function/class: `LatentWorld`, `equivalent_world_pair`.  
Experiment validating it: theorem stage and flagship EXP-06, with oracle and
observable columns separated by name.  
Unit test: `test_identification.py::test_theorem_13_observational_equivalence`.  
Expected qualitative behavior: observable signatures match exactly while
oracle FNRs differ.  
Status: COMPLETE.

## Theorem 14 and Proposition 7
Theorem ID: Theorem 14, Proposition 7.  
Mathematical quantity: sharp no-assumption and propensity-restricted FNR
intervals.  
Implementation file: `src/identification/bounds.py`.  
Function/class: `fnr_identification_interval`,
`propensity_bounded_interval`, gap interval functions.  
Experiment validating it: theorem stage and EXP-07.  
Unit test: `test_identification.py`, `test_counterexamples.py`.  
Expected qualitative behavior: valid intervals contain oracle truth and valid
propensity information weakly narrows them.  
Status: COMPLETE.

## Theorem 15 and Propositions 8--9
Theorem ID: Theorem 15, Proposition 8, Proposition 9.  
Mathematical quantity: representative random audits identify missing label
prevalence; uncertainty contracts at (O((rN)^{-1/2})).  
Implementation file: `src/estimation/audit.py`.  
Function/class: `hoeffding_audit_interval`,
`simultaneous_audit_intervals`, `propagate_q_interval_to_fnr`.  
Experiment validating it: EXP-08 and theorem stage.  
Unit test: `test_audits.py`.  
Expected qualitative behavior: coverage is controlled and interval width
decreases with audited sample size, subject to random variation.  
Status: COMPLETE.

## Audit conclusion

No mathematical contradiction was found, so `MATH_CODE_CONFLICTS.md` is not
needed. Previously partial links were experimental: sampled theorem
comparisons, the exact impossibility illustration, and KKT diagnostics. Those
are represented in source and tests. Kaggle notebook version 4 subsequently
completed the configured pipeline; Gates E0--E5 pass. Gate E6 remains
unevaluated because Adult and German Credit inputs were absent. See
`../RESULTS_AUDIT.md`.
