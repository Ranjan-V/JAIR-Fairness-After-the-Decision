# Research status

Final technical audit: 2026-09-27  
Proof decision: **PASS WITH CORRECTIONS**  
Reproducibility decision: **SCIENTIFIC REPRODUCIBILITY PASS**  
Empirical decision: **E6 PARTIAL PASS**

## 1. Central claim

Fairness of an initial AI decision is generally not invariant to a later,
self-selected human correction process.  In the one-sided binary model, the
entire transformation of group confusion rates is governed by label-specific
effective transitions (\kappa_g^+=\alpha_g^+\rho_g^+) and
(\kappa_g^-=\alpha_g^-\rho_g^-).  This yields exact preservation conditions,
shows how heterogeneous costs defeat formally symmetric access, exposes what
ordinary appeal logs cannot identify, and supports auditable resource
allocation interventions.

## 2. Core theorems

### Fairness-preservation characterization (Theorems 1--4)

Linear fairness constraints are preserved by a fixed stochastic operator
exactly when the transformed constraint factors through the original one.  In
the one-sided model, nondegenerate equal opportunity requires equal
(\kappa^+), FPR parity requires equal (\kappa^-), and equalized odds
requires both.  Demographic parity instead requires equality of base-rate- and
confusion-mass-weighted transition increments.  Status: proved.  Importance:
it prevents invalid transfer of equalized-odds logic to demographic parity.

### Endogenous-cost impossibility (Theorems 7--8)

With an initially equal but imperfect TPR, common positive review accuracy,
common perceived value, group-blind assistance, and strict cost-CDF ordering at
every feasible threshold, no feasible group-blind policy can preserve final
equal opportunity.  Status: proved, conditional.  Importance: it precisely
separates nominal procedural symmetry from effective correction equality and
states all escape routes.

### Non-identification, sharp bounds, and audits (Theorems 13--15)

Two latent worlds can induce the same complete ordinary appeal-log law yet have
different final FNR and fairness disparity.  With appellant labels and known
review success, the remaining one-dimensional latent mass yields sharp
no-assumption and propensity-restricted intervals.  Any positive representative
random-audit rate identifies the mass in the population, with finite-sample
width scaling generically as (O((rN)^{-1/2})).  Status: proved.  Importance:
equal observed reversal statistics cannot certify final fairness.

### Resource allocation (Theorems 9--12, Proposition 6)

Continuous minimax allocation is convex when appeal response is concave and
cost is convex; separable welfare allocation obeys a KKT marginal-return rule.
The exact minimum budget for a residual-risk target is a sum of inverse-CDF
threshold costs.  Indivisible intervention contains 0--1 knapsack and is
weakly NP-complete.  Status: proved under stated regularity.  Importance: this
connects the diagnostic theory to a policy design with exact feasibility and
complexity guarantees.

## 3. Failed conjectures

- Equal effective transition probabilities always preserve demographic parity:
  false because appealable masses differ.
- A uniform subsidy monotonically closes a contestability gap under first-order
  stochastic dominance: false because CDF ordering does not order densities.
- Optimal allocation always equalizes residual risks: false for welfare
  objectives and before lower-risk groups become active.
- Benefit/cost ratio greedy is optimal for indivisible assistance: false by a
  standard knapsack counterexample.
- A verbal monotone-selection assumption alone tightens identification bounds:
  false without observed evidence and a truth link.

## 4. Strongest counterexamples

An equal-opportunity classifier with TPR (1/2) becomes maximally separated
over its correctable mass when one group has (\kappa^+=1) and the other zero.
Equal (\kappa^+,\kappa^-) can destroy demographic parity under unequal
base-rate-weighted adverse masses.  Identical logs with appeal rate and
appellant-positive rate both (1/2) permit final FNR values zero and (2/3)
depending only on the hidden non-appellant labels.  Full details are in
`math/counterexamples.md`.

## 5. Algorithmic contribution

The implementation exposes theorem-linked analytical transformations, cost-CDF
responses and inverses, convex minimax and welfare programs, an exact
target-budget calculation, and pseudo-polynomial dynamic programming for the
discrete welfare case.  It compares B0--B6 policies without claiming an
unproved greedy guarantee.

## 6. Identifiability contribution

Ordinary self-selected appeal logs identify appellant behavior and outcomes but
not latent error prevalence among adverse non-appellants.  Final FNR and group
disparity are therefore not point identified without assumptions.  Sharp
worst-case bounds, bounded-propensity refinements, and representative random
audits give progressively stronger conclusions.  IPW is not treated as a cure
unless missing-at-random and positivity assumptions are independently defended.

## 7. Code completeness

Implemented scripts/modules cover EXP-01 fairness destruction, EXP-02 review
disparity, EXP-03 cost heterogeneity, EXP-04 budget allocation, EXP-05 frontier,
EXP-06 non-identification, EXP-07 partial identification, EXP-08 random audits,
EXP-09 robustness, and EXP-10 boundaries.  Local-only Adult and German Credit
adapters, three lightweight classifiers, deterministic plotting, bootstrap and
audit intervals, B0--B6 policies, and theorem-linked tests are included.

The experimental package was subsequently hardened with smoke/full/stress
profiles, a resumable staged master runner, a dedicated theorem-illustration
suite, standardized outputs, validation gates, train/validation/test
semisynthetic evaluation, aggregation/table/figure generators, and thin Kaggle
launchers. Final Kaggle run `352782151` completed unit tests, smoke, theorem,
core, robustness, Adult/German E6, validation, aggregation, figures, and
summary on 2026-09-25. Full validation returned PASS with no errors or
warnings. Its hash-verified immutable extraction is under
`artifacts/kaggle_run_352782151_2026-09-26/`.

## 8. Execution record

The initial construction phase was source-only. At the user's later explicit
request, the pipeline was uploaded to and executed on Kaggle using CPU with no
accelerator and Internet disabled. The final E6 run executed from
2026-09-25 18:51:07 to 19:12:56 UTC. Its 21,451,611-byte archive was downloaded,
verified at SHA-256
`AE30CA19BF912DB8FEB1BE33E263C994F73ED3C2556E6EFF6D6EB69747BCBF1A`,
and extracted locally. See `RESULTS_AUDIT.md` for provenance, paired confidence
intervals, gate calculations, and claim limits.

Adult and German Credit produced the complete predeclared 600-run factorial.
E6 is a PARTIAL PASS: Adult robustly shows absolute amplification, while German
supports signed movement for logistic and gradient boosting but not broad
absolute amplification or a random-forest effect.

## 9. Remaining risks

- The focused source-based novelty audit found a defensible narrow wedge but
  substantial adjacent work on contestability, human-assisted fairness,
  recourse costs, and selective labels. No priority claim is justified;
  operator invariance, missing-data bounds, and allocation tools are
  individually classical.
- The impossibility theorem is clean but conditional on pointwise cost-CDF
  ordering throughout the feasible policy range.
- Cost distributions conditional on latent false denial may be difficult to
  estimate empirically.
- Reviewer accuracy can change with selected case mix, violating fixed (\rho).
- The displayed finite-audit bound conditions on other masses and review
  accuracy; complete finite-sample inference must propagate their uncertainty.
- Semisynthetic datasets may demonstrate mechanisms without validating real
  appeal behavior.
- Convexity can fail for the disparity-penalized objective when residual risks
  are nonlinear; the minimax formulation is the safer guaranteed program.
- Rare groups and near-zero positive strata may make empirical intervals too
  wide for useful conclusions.
- The aggregate EXP-07 sensitivity rows using propensity bounds (0.4, 0.6)
  exclude the constructed truth because the constructed propensity is about
  0.3846. They must be labeled as assumption-misspecification sensitivity
  checks, not failures of the valid-bounds theorem.
- German Credit has small test strata, imperfect validation calibration, and
  noisy paired changes; its random-forest result is null and must remain so in
  the manuscript.

## 10. Research readiness decision

`RESULTS_VALIDATED_E6_PARTIAL_PASS_NOVELTY_AUDITED`

Gates E0--E5 pass and E6 partially passes. The synthetic results support the
exact fairness-transformation, heterogeneous-cost, intervention, and
identification claims over broad grids. Adult supplies stable semisynthetic
real-data replication; German Credit bounds the empirical claim to signed
effects for two models. The literature audit supports cautious positioning of
the integrated contestation-specific theory, not a broad novelty claim.

## 11. Submission-stage result

The complete mathematical appendix now contains proofs for every named formal
claim. Manuscript wording has been narrowed where theorems require
nondegeneracy, interiority, or Slater conditions, and the public UCI datasets
are explicitly cited. A clean environment passes all 42 tests, the immutable
820-file archive validates, and a fresh 220-file synthetic/theorem rerun agrees
scientifically with the archive at `1e-6` tolerance. The anonymous paper has
been migrated to the current JAIR author-kit class and includes the required
reproducibility checklist. Author identity, declarations, artifact licensing,
and a permanent public archive remain author-controlled submission items;
their absence must not be described as a completed submission.
