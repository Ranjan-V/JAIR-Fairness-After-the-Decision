# Theorem index

| ID | One-line statement | Status | Importance | Proof file | Main assumptions | Code counterpart |
|---|---|---|---|---|---|---|
| Theorem 1 | Linear fairness is universally preserved on a declared perturbation space iff the post-operator factors through the fairness map. | PROVED | CORE | `01_base_model.md` | fixed linear stochastic operator; homogeneous constraint | `fairness/operators.py` |
| Proposition 1 | Exact one-sided confusion-rate transformation. | PROVED | SUPPORTING | `02_post_contestation_rates.md` | one-sided appeals | `contestation/transforms.py` |
| Corollary 1 | Exact post-contestation positive-decision rate. | PROVED | SUPPORTING | `02_post_contestation_rates.md` | one-sided appeals | `contestation/transforms.py` |
| Proposition 2 | Exact two-sided transformation. | PROVED | OPTIONAL | `02_post_contestation_rates.md` | two-sided kernel | `contestation/transforms.py` |
| Theorem 2 | EO preservation iff ((1-t)(\kappa_A^+-\kappa_B^+)=0). | PROVED | CORE | `03_fairness_preservation.md` | initial EO | `fairness/metrics.py` |
| Theorem 3 | FPR-parity preservation has the analogous (\kappa^-\) condition. | PROVED | CORE | `03_fairness_preservation.md` | initial FPR parity | `fairness/metrics.py` |
| Corollary 2 | EO plus FPR conditions exactly characterize post equalized odds. | PROVED | CORE | `03_fairness_preservation.md` | initial EO | `fairness/metrics.py` |
| Theorem 4 | DP is preserved iff weighted appealable-mass increments agree. | PROVED | CORE | `03_fairness_preservation.md` | initial DP | `fairness/metrics.py` |
| Proposition 3 | Common effective transitions characterize universal nondegenerate EO/FPR preservation. | PROVED | SUPPORTING | `03_fairness_preservation.md` | fixed common initial rate | `fairness/operators.py` |
| Theorem 5 | Exact signed-gap formula characterizes amplification, reduction, equality, and reversal. | PROVED | CORE | `04_non_preservation.md` | two groups | `fairness/metrics.py` |
| Theorem 6 | Attainable post-gap interval and absolute bounds are tight. | PROVED | CORE | `04_non_preservation.md` | unrestricted unit-interval transitions | `fairness/bounds.py` |
| Corollary 3 | Initially fair EO gap equals ((1-t)|\Delta\kappa^+|). | PROVED | SUPPORTING | `04_non_preservation.md` | initial EO | `fairness/metrics.py` |
| Proposition 4 | Threshold appeal equals a cost CDF or its conditional expectation. | PROVED | SUPPORTING | `05_endogenous_appeals.md` | rational threshold rule | `contestation/costs.py` |
| Proposition 5 | Appeal is monotone in assistance, with density derivative when regular. | PROVED | SUPPORTING | `05_endogenous_appeals.md` | regular conditional CDF | `contestation/costs.py` |
| Theorem 7 | Equal assistance yields equal correction only at equal operative CDF values (under common review). | PROVED | CORE | `05_endogenous_appeals.md` | common value/review | `contestation/costs.py` |
| Theorem 8 | Strict cost-CDF ordering over feasible thresholds makes group-blind EO preservation impossible. | PROVED | CORE | `06_impossibility.md` | five stated conditions | `experiments/exp03_cost_heterogeneity.py` |
| Theorem 9 | Compact continuous allocation programs attain optima. | PROVED | SUPPORTING | `07_resource_allocation.md` | compactness/continuity | `optimization/continuous.py` |
| Theorem 10 | Concave appeal response gives convex residual risk and convex minimax allocation. | PROVED | CORE | `07_resource_allocation.md` | curvature conditions | `optimization/continuous.py` |
| Theorem 11 | Interior welfare allocations equalize weighted marginal return per resource. | PROVED | CORE | `07_resource_allocation.md` | convexity, Slater, differentiability | `optimization/continuous.py` |
| Proposition 6 | Exact minimum budget for a common residual-risk target. | PROVED | CORE | `07_resource_allocation.md` | monotone invertible risks | `optimization/closed_form.py` |
| Theorem 12 | Discrete correction allocation contains 0--1 knapsack and is weakly NP-complete. | PROVED | CORE | `07_resource_allocation.md` | indivisible interventions | `optimization/discrete.py` |
| Theorem 13 | Ordinary self-selected appeal logs do not identify final FNR. | PROVED | CORE | `08_identifiability.md` | non-appellant labels missing | `identification/worlds.py` |
| Corollary 5 | Post-contestation fairness disparity is observationally non-identified. | PROVED | CORE | `08_identifiability.md` | two groups | `identification/worlds.py` |
| Theorem 14 | No-assumption FNR bounds are sharp. | PROVED | CORE | `09_partial_identification.md` | known observed masses/review | `identification/bounds.py` |
| Proposition 7 | Propensity bounds sharpen the latent-mass interval exactly when appealed-positive mass is nonzero. | PROVED | CORE | `09_partial_identification.md` | bounded error appeal propensity; (m>0) | `identification/bounds.py` |
| Theorem 15 | Any positive representative random-audit rate identifies missing prevalence. | PROVED | CORE | `09_partial_identification.md` | MCAR audit, accurate labels | `estimation/audit.py` |
| Proposition 8 | Audit uncertainty contracts at (O((rN)^{-1/2})). | PROVED | SUPPORTING | `09_partial_identification.md` | realized independent audits | `estimation/audit.py` |
| Proposition 9 | Union-bounded Hoeffding intervals cover all groups simultaneously. | PROVED | SUPPORTING | `10_statistical_results.md` | independent audited labels | `estimation/audit.py` |

## Disproved candidate claims

- Equal (\kappa^+,\kappa^-\) always preserve demographic parity: DISPROVED
  by CE-3.
- A uniform subsidy monotonically closes contestability gaps under stochastic
  dominance: DISPROVED by CE-12.
- The allocation optimum always equalizes residual risks: DISPROVED by CE-13.
- Ratio-greedy is optimal for discrete assistance: DISPROVED by CE-14.
- Verbal monotone selection alone tightens bounds: DISPROVED by CE-16.

## Headline contributions (not inflated)

1. Theorems 1--4: operator view plus exact, fairness-specific preservation
   conditions, including the distinct demographic-parity condition.
2. Theorems 7--8: endogenous heterogeneous costs produce a conditional but
   genuine impossibility for group-blind contestation policy.
3. Theorems 13--15: appeal-specific observational equivalence, sharp bounds,
   and identification through randomized auditing.
4. Theorems 10--12 and Proposition 6: convex continuous allocation structure,
   an exact target-budget formula, and the discrete complexity boundary.
5. Theorems 5--6: exact disparity dynamics and tight attainable bounds.
