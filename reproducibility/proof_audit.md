# Proof audit

Final audit date: 2026-09-27  
Decision: **PASS WITH CORRECTIONS**

Every named theorem, proposition, and corollary was checked against its stated
assumptions, boundary cases, proof steps, code counterpart, and theorem-linked
tests. No central conclusion was invalidated. Three statement-level defects
were corrected: Theorem 1 was moved to the signed perturbation space on which
its proof is valid; Proposition 6 now reports infeasibility instead of clipping
an unattainable appeal probability; and Theorem 14/Proposition 7 now separate
the zero-mass and undefined-FNR boundaries. Theorem 12 was also labelled
weakly, rather than strongly, NP-complete. The proof-linked regression suite
passes 18/18 tests.

## Theorem 1
Status: PROVED. Importance: CORE.  
Assumptions: finite-dimensional signed-perturbation space; fixed stochastic
operator; homogeneous linear fairness map.  
Necessity of assumptions: fixedness and linearity are required for the stated
factorization; probability-only applications require a separately checked
relative-interior spanning condition.  
Proof strategy: kernel factorization through a quotient space.  
Potential hidden gap: CLOSED in the final audit.  The theorem is now stated
directly on the perturbation space; affine constraints must still be
homogenized by adding a constant coordinate.  
Counterexample search: group-dependent arbitrary kernels violate invariance.  
Dependencies: linear algebra only.  Ready: YES.

## Theorems 2--4 and Corollary 2
Status: PROVED. Importance: CORE.  
Assumptions: one-sided appeals; defined conditional rates; stated initial
fairness.  
Necessity: CE-2 handles the nondegenerate exception; CE-3/4 show DP cannot use
the EO condition.  
Proof strategy: exact subtraction of Proposition 1/Corollary 1.  
Potential hidden gap: none beyond null conditioning strata.  
Counterexample search: CE-1--4, CE-19.  
Dependencies: Proposition 1. Ready: YES.

## Theorems 5--6
Status: PROVED. Importance: CORE.  
Assumptions: two groups, one-sided appeals, (\kappa\in[0,1]).  
Necessity: restricting attainable (\kappa) narrows Theorem 6's interval.  
Proof strategy: signed affine update and interval image.  
Potential hidden gap: direction reversal is undefined when the initial gap is
zero; the product criterion correctly excludes it.  
Counterexample search: all four parameter corners checked symbolically.  
Dependencies: Proposition 1. Ready: YES.

## Theorem 7
Status: PROVED. Importance: CORE.  
Assumptions: common threshold value and review quality.  
Necessity: CE-6 and CE-8.  
Proof strategy: threshold CDF substitution.  
Potential hidden gap: cost CDF must be conditional on the false-denial stratum.
Counterexample search: crossing CDFs and zero review.  
Dependencies: Proposition 4. Ready: YES.

## Theorem 8
Status: PROVED. Importance: CORE.  
Assumptions: all five are explicit; especially strict pointwise order over the
entire feasible policy range.  
Necessity: CE-2, CE-6--8 give failures of stronger statements.  
Proof strategy: compose Theorems 2 and 7.  
Potential hidden gap: no claim is made outside feasible (U).  
Counterexample search: perfect classifier, zero reviewer, CDF crossing,
universal appeal, group-specific review.  
Dependencies: Theorems 2, 7. Ready: YES.

## Theorems 9--12
Status: PROVED. Importance: Theorems 9--11 SUPPORTING; Theorem 12 CORE
algorithmic boundary.  
Assumptions: continuity/compactness; convexity and Slater where invoked;
indivisible interventions for knapsack.  
Necessity: noncompact unattained infima, nonconvex disparity composition, and
CE-13/14.  
Proof strategy: Weierstrass, convex composition, KKT, identity reduction.  
Potential hidden gap: CLOSED in the final audit.  The statement now specifies
binary-encoded integer inputs; weak NP-completeness must not be described as
strong, and the FPTAS applies only to welfare knapsack.  
Counterexample search: CE-13/14.  
Dependencies: standard finite-dimensional optimization results. Ready: YES.

## Theorem 13 and Corollary 5
Status: PROVED. Importance: CORE.  
Assumptions: labels absent for adverse non-appellants; unrestricted selection.
Necessity: complete labels or representative positive-rate audits identify.
Proof strategy: explicit observationally equivalent latent worlds.  
Potential hidden gap: exact disparity one is not claimed with positive observed
appealed-positive mass; only arbitrarily close along a sequence.  
Counterexample search: CE-15.  
Dependencies: none. Ready: YES.

## Theorems 14--15 and Propositions 7--8
Status: PROVED. Importance: CORE.  
Assumptions: observed appellant labels and review success; representative,
error-free audits for point identification; positive denominators.  
Necessity: CE-16--18.  
Proof strategy: one-dimensional latent mass, monotone rational map, and
Hoeffding concentration.  
Potential hidden gap: uncertainty in (s,m,n,\rho) is omitted from Proposition
8's displayed conditional bound and must be included in full empirical CIs.
Counterexample search: null positive strata and nonrandom audits.  
Dependencies: Theorem 13 notation. Ready: YES WITH STATED CONDITIONAL SCOPE.

## Proposition 9
Status: PROVED. Importance: SUPPORTING.  
Assumptions: independent audited Bernoulli labels within each group.  
Necessity: dependence requires another concentration argument.  
Proof strategy: Hoeffding plus union bound.  
Potential hidden gap: other nuisance estimates need simultaneous intervals in
a complete finite-sample analysis.  
Counterexample search: (M_g=0), adaptive biased audit.  
Dependencies: Proposition 8. Ready: YES WITH STATED CONDITIONAL SCOPE.

---

# Standardized theorem-by-theorem readiness cards

The cards below make readiness explicit for every named theorem; the detailed
grouped discussion above supplies additional context.

## Theorem 1
Theorem: Operator preservation criterion.  
Status: PROVED.  
Importance: CORE.  
Assumptions: Fixed finite-dimensional linear operator and homogeneous fairness
map on a declared signed-perturbation space.  
Necessity of assumptions: Nonlinear/adaptive operators need a different result.  
Proof strategy: Factor through the quotient by the fairness-map kernel.  
Potential hidden gap: Closed by the perturbation-space restatement; affine
constraints still require a constant coordinate.  
Counterexample search: Arbitrary unequal group kernels fail.  
Dependencies: Linear algebra.  
Ready / Not Ready: READY.

## Theorem 2
Theorem: Equal-opportunity preservation.  
Status: PROVED.  
Importance: CORE.  
Assumptions: Initial equal TPR and one-sided appeal.  
Necessity of assumptions: At TPR one, unequal correction is irrelevant.  
Proof strategy: Subtract exact TPR transformations.  
Potential hidden gap: Null positive strata make TPR undefined.  
Counterexample search: CE-1, CE-2.  
Dependencies: Proposition 1.  
Ready / Not Ready: READY.

## Theorem 3
Theorem: FPR-parity preservation.  
Status: PROVED.  
Importance: CORE.  
Assumptions: Initial equal FPR and one-sided appeal.  
Necessity of assumptions: At FPR one, unequal false reversal is irrelevant.  
Proof strategy: Subtract exact FPR transformations.  
Potential hidden gap: Null negative strata make FPR undefined.  
Counterexample search: Boundary (f=1) and CE-11.  
Dependencies: Proposition 1.  
Ready / Not Ready: READY.

## Theorem 4
Theorem: Demographic-parity preservation.  
Status: PROVED.  
Importance: CORE.  
Assumptions: Initial demographic parity and one-sided appeal.  
Necessity of assumptions: Weighted adverse masses cannot be omitted.  
Proof strategy: Subtract final positive-rate identities.  
Potential hidden gap: None after retaining both label strata.  
Counterexample search: CE-3, CE-4.  
Dependencies: Corollary 1.  
Ready / Not Ready: READY.

## Theorem 5
Theorem: Exact signed disparity dynamics.  
Status: PROVED.  
Importance: CORE.  
Assumptions: Two groups and one-sided appeal.  
Necessity of assumptions: Two-sided transitions add removal terms.  
Proof strategy: Affine signed-gap update and squared absolute gaps.  
Potential hidden gap: Direction at zero initial gap is not defined.  
Counterexample search: All sign cases and parameter corners.  
Dependencies: Proposition 1.  
Ready / Not Ready: READY.

## Theorem 6
Theorem: Tight attainable disparity bounds.  
Status: PROVED.  
Importance: CORE.  
Assumptions: Each effective correction ranges independently over ([0,1]).  
Necessity of assumptions: Policy restrictions shrink the attainable interval.  
Proof strategy: Image of a rectangle under an affine functional.  
Potential hidden gap: None; endpoints are constructive.  
Counterexample search: Four rectangle corners.  
Dependencies: Theorem 5.  
Ready / Not Ready: READY.

## Theorem 7
Theorem: Procedural symmetry versus effective equality.  
Status: PROVED.  
Importance: CORE.  
Assumptions: Common perceived value, subsidy, and positive review success.  
Necessity of assumptions: Unequal review can offset unequal access.  
Proof strategy: Substitute threshold CDFs into effective correction.  
Potential hidden gap: CDFs are conditional on false denial.  
Counterexample search: CE-5, CE-6, CE-8.  
Dependencies: Proposition 4.  
Ready / Not Ready: READY.

## Theorem 8
Theorem: Group-blind policy impossibility.  
Status: PROVED.  
Importance: CORE.  
Assumptions: The five enumerated nondegeneracy, symmetry, and strict-order conditions.  
Necessity of assumptions: CE-2 and CE-6--8 give escape routes.  
Proof strategy: Compose Theorems 2 and 7.  
Potential hidden gap: Claim is only over the declared feasible policy set.  
Counterexample search: Saturation, CDF crossing, unequal review, perfect TPR.  
Dependencies: Theorems 2, 7.  
Ready / Not Ready: READY.

## Theorem 9
Theorem: Existence of continuous allocation optima.  
Status: PROVED.  
Importance: SUPPORTING.  
Assumptions: Nonempty compact feasible domain and continuity.  
Necessity of assumptions: Without compactness/coercivity an infimum can escape.  
Proof strategy: Weierstrass theorem.  
Potential hidden gap: Feasibility must be checked before optimization.  
Counterexample search: Open unbounded feasible intervals.  
Dependencies: None.  
Ready / Not Ready: READY.

## Theorem 10
Theorem: Convexity of minimax allocation.  
Status: PROVED.  
Importance: CORE.  
Assumptions: Concave appeal response, convex cost, convex domain.  
Necessity of assumptions: General disparity penalties can remain nonconvex.  
Proof strategy: Curvature composition and epigraph maximum.  
Potential hidden gap: Convex (R_g) alone does not convexify absolute differences.  
Counterexample search: Difference of nonlinear convex residuals.  
Dependencies: Residual-risk definition.  
Ready / Not Ready: READY.

## Theorem 11
Theorem: KKT marginal allocation rule.  
Status: PROVED.  
Importance: CORE.  
Assumptions: Convex differentiable program, Slater, positive marginal cost.  
Necessity of assumptions: Nonconvex stationary points need not be optimal.  
Proof strategy: KKT stationarity and complementary slackness.  
Potential hidden gap: Boundary groups obey inequalities, not equality.  
Counterexample search: CE-13.  
Dependencies: Theorem 10's separable special case.  
Ready / Not Ready: READY.

## Theorem 12
Theorem: Discrete allocation complexity.  
Status: PROVED.  
Importance: CORE.  
Assumptions: Indivisible interventions with additive costs and benefits.  
Necessity of assumptions: Divisible linear allocation is not knapsack.  
Proof strategy: Identity reduction from 0--1 knapsack.  
Potential hidden gap: Closed by specifying binary-encoded integer inputs;
hardness is weak, not strong.  
Counterexample search: CE-14 refutes ratio greedy.  
Dependencies: Standard knapsack complexity.  
Ready / Not Ready: READY.

## Theorem 13
Theorem: Appeal-log non-identifiability.  
Status: PROVED.  
Importance: CORE.  
Assumptions: Labels missing for adverse non-appellants and unrestricted selection.  
Necessity of assumptions: Representative audits or complete labels identify.  
Proof strategy: Two explicit observationally equivalent latent worlds.  
Potential hidden gap: Exact unit disparity is not claimed with positive appellant-positive mass.  
Counterexample search: CE-15.  
Dependencies: None.  
Ready / Not Ready: READY.

## Theorem 14
Theorem: Sharp no-assumption FNR bounds.  
Status: PROVED.  
Importance: CORE.  
Assumptions: Observed masses and appellant review success are identified.  
Necessity of assumptions: Unknown review success adds another latent dimension.  
Proof strategy: Monotone rational function of one missing mass.  
Potential hidden gap: Closed by explicitly separating the all-zero undefined
case and the singleton ({1}) identified set; Proposition 7 requires (m>0).  
Counterexample search: Both latent-mass endpoints constructed.  
Dependencies: Theorem 13's observed-data decomposition.  
Ready / Not Ready: READY.

## Theorem 15
Theorem: Identification through representative random audits.  
Status: PROVED.  
Importance: CORE.  
Assumptions: Positive-rate independent audit and error-free labels.  
Necessity of assumptions: CE-17 and CE-18.  
Proof strategy: Audit conditional prevalence equals target missing prevalence.  
Potential hidden gap: Population identification does not imply finite-sample precision.  
Counterexample search: Zero and outcome-dependent audit.  
Dependencies: Theorem 14.  
Ready / Not Ready: READY.
