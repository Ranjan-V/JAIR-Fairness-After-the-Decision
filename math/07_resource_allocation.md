# Limited-resource allocation

## 1. Objectives

Two defensible objectives answer different questions:

\[
\text{(MM)}\quad \min_{u\in U}\max_g R_g(u_g)
\quad\text{s.t.}\quad \sum_gc_g(u_g)\le B,
\]

minimizes the worst residual false-denial rate, while

\[
\text{(WF)}\quad
\min_{u\in U}\sum_gw_gR_g(u_g)
+\lambda\max_{g,h}|R_g(u_g)-R_h(u_h)|
\quad\text{s.t. the same budget}
\]

trades aggregate residual harm against disparity.  Neither dominates the
other normatively.  The cleanest structural theorem is available for (MM);
the cleanest marginal allocation rule is available for the separable welfare
case (\lambda=0).

## Theorem 9 (existence)

If (U=\prod_g[0,\bar u_g]) is nonempty and compact, each (R_g) and (c_g)
is continuous, (c_g\ge0), and the feasible set is nonempty, then (MM) and
(WF) attain optima.

*Proof.* The budget sublevel set is closed in compact (U), hence compact.
Both objectives are continuous (a finite maximum of continuous functions is
continuous).  Apply Weierstrass. ∎

Compactness can be replaced by coercivity/level-boundedness; without either,
an infimum need not be attained.

## Theorem 10 (convexity conditions)

Suppose each (\alpha_g^+) is concave, (\rho_g^+FNR_g\ge0), each (c_g) is
convex, and (U) is convex.  Then each (R_g) is convex and (MM) is a convex
program in epigraph form.  The separable welfare objective
(\sum w_gR_g) is convex.  The disparity-penalized (WF) objective is convex
provided every pairwise composition (|R_g(u_g)-R_h(u_h)|) is convex; convexity
of the individual (R_g) alone does **not** guarantee this last condition.

*Proof.* A nonpositive multiple of a concave function plus a constant is
convex.  Pointwise maxima preserve convexity.  Budget sublevel sets of convex
functions are convex.  The caution follows because a difference of convex
functions followed by absolute value need not be convex. ∎

A safe convex alternative is (MM), or an affine (R_g) model for (WF), in
which absolute pairwise differences are convex.

## Theorem 11 (KKT marginal rule for separable welfare)

Consider (\min\sum_gw_gR_g(u_g)) subject to
(\sum_gc_g(u_g)\le B) and (0\le u_g\le\bar u_g).  Assume differentiability,
convexity, and Slater's condition.  There exist multipliers
(\eta,\ell_g,h_g\ge0) such that

\[
w_gR'_g(u_g)+\eta c'_g(u_g)-\ell_g+h_g=0,
\]

with the usual complementary-slackness conditions.  If the budget binds and
(0<u_g<\bar u_g), then

\[
-\frac{w_gR'_g(u_g)}{c'_g(u_g)}=\eta
\]

whenever (c'_g(u_g)>0).  Thus active interior groups equalize weighted
marginal harm reduction per marginal resource, not residual risks themselves.

*Proof.* These are the necessary and sufficient KKT conditions for the stated
convex program. ∎

The analogous claim is false for arbitrary nonconvex response curves, and for
(MM) the multipliers weight only worst-risk groups.  A two-group linear example
with unequal starting risks shows that equal marginal returns need not
equalize residual risks before the lower-risk group becomes active.

## Proposition 6 (minimum budget for a residual-risk target)

Suppose (c_g) is increasing and each (R_g) is continuous and strictly
decreasing on its effective range.  To enforce (R_g(u_g)\le\epsilon) for all
groups, define

\[
u_g^{min}(\epsilon)=
\inf\{u\in[0,\bar u_g]:R_g(u)\le\epsilon\}.
\]

The target is feasible iff every set is nonempty and

\[
B\ge B_{min}(\epsilon)=\sum_gc_g(u_g^{min}(\epsilon)).
\]

*Proof.* Componentwise monotonicity makes (u_g^{min}) necessary; choosing
those values is sufficient. ∎

With (FNR_g>0), deterministic value (v_g), review rate (\rho_g>0), and cost
CDF (F_g), define the untruncated required appeal probability

\[
p_g^*(\epsilon)=\frac{1-\epsilon/FNR_g}{\rho_g}.
\]

If (\epsilon\ge FNR_g), no assistance is required.  If
(0<p_g^*(\epsilon)\le1), then
(u_g^{min}=\max\{0,F_g^{-1}(p_g^*)-v_g\}), subject to support and
attainability.  If (p_g^*(\epsilon)>1), equivalently
(\epsilon<FNR_g(1-\rho_g)), the target is infeasible even under universal
appeal.  Clipping (p_g^*) to one would conceal this infeasibility and is
therefore not valid.  When (FNR_g=0), every nonnegative target is already met.
This yields explicit formulas:

- Uniform ([0,L_g]): (F^{-1}(p)=L_gp).
- Exponential rate (\beta_g): (F^{-1}(p)=-\log(1-p)/\beta_g) for (p<1).
- Logistic location (\mu_g), scale (s_g):
  (F^{-1}(p)=\mu_g+s_g\log[p/(1-p)]).
- Pareto scale (x_g), shape (a_g):
  (F^{-1}(p)=x_g(1-p)^{-1/a_g}) on its support.

Endpoint and support constraints must be enforced; exponential, logistic, and
Pareto families do not attain (p=1) at finite assistance.

## Theorem 12 (discrete intervention complexity)

If individual (i) can receive an indivisible intervention of nonnegative
integer cost (c_i) and nonnegative integer expected-benefit encoding (v_i),
maximizing total encoded correction benefit under an integer budget is the
0--1 knapsack optimization problem.  Its threshold decision version, with all
integers represented in binary, is weakly NP-complete even with one group;
hence a polynomial-time universal greedy-by-ratio optimum is impossible unless
(P=NP).

*Proof.* An arbitrary 0--1 knapsack instance maps identically to individuals
with the same costs and values.  Feasible selected sets and objectives are
unchanged. ∎

Integer-cost dynamic programming runs in (O(nB)) pseudo-polynomial time;
standard value scaling gives an FPTAS for the welfare-only version.  A
fairness penalty couples groups and is not covered by that guarantee without a
separate multiobjective state or approximation proof.
