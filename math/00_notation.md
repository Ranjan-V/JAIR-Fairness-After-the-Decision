# Notation and standing conventions

## Probability space

All random variables are defined on a common probability space.  The group
variable is (G\in\mathcal G), features are (X), the ground-truth label is
(Y\in\{0,1\}), the initial decision is (D_0\in\{0,1\}), the appeal
indicator is (A\in\{0,1\}), the human-review record is (H), and the final
institutional decision is (D_1\in\{0,1\}).  A positive decision is favorable.
Unless stated otherwise, only (D_0=0) is appealable and (D_1=D_0) when
(A=0).

Conditional probabilities are only asserted on conditioning events of
positive probability.  A rate whose conditioning event is null is undefined,
not zero.  For a group (g), write

\[
\pi_g=P(Y=1\mid G=g),\quad
t_g=TPR_g=P(D_0=1\mid Y=1,G=g),\quad
f_g=FPR_g=P(D_0=1\mid Y=0,G=g).
\]

Thus (FNR_g=1-t_g) and (TNR_g=1-f_g).  Primes denote final-decision
quantities.  For adverse initial decisions define

\[
\alpha_g^y=P(A=1\mid D_0=0,Y=y,G=g),\qquad
\rho_g^y=P(D_1=1\mid A=1,D_0=0,Y=y,G=g),
\]

and the effective adverse-to-positive transition probability

\[
\kappa_g^y=\alpha_g^y\rho_g^y,qquad y\in\{0,1\}.
\]

We use (\kappa_g^+=\kappa_g^1) for correction of a false denial and
(\kappa_g^-=\kappa_g^0) for erroneous reversal of a correct denial.  These
are transition probabilities, not proposed fairness metrics.

## Disparities and signs

For two groups (A,B), the signed equal-opportunity gap is
(d=t_A-t_B), the final signed gap is (d'=t'_A-t'_B), and the absolute gaps
are (\Delta_{pre}=|d|), (\Delta_{post}=|d'|).  Analogous notation is used
for FPR.  Keeping the signed gap is essential when discussing reversal.

## Observed-data notation

In the appeal-log model, labels for initially adverse cases are observed only
when an appeal or a random audit reveals them.  With no audit the observable
record is

\[
O=(G,X,D_0,A,H\mathbf 1\{A=1\},Y\mathbf 1\{D_0=1\text{ or }A=1\}),
\]

where inclusion of labels for (D_0=1) is optional and immaterial to the
non-identification result about adverse non-appellants.

## Optimization notation

An assistance allocation is (u=(u_g)_{g\in\mathcal G}\in Usubseteq
\mathbb R_+^{|\mathcal G|}).  Residual false denial is

\[
R_g(u_g)=FNR_g[1-\rho_g^+\alpha_g^+(u_g)].
\]

Resource use is (C(u)=\sum_g c_g(u_g)), with budget (C(u)\le B).
Weights (w_g\ge0) are fixed ex ante and need not equal group prevalence.

## Scope conventions

The core model is associational.  Group differences in costs, appeal, or
review do not by themselves identify causal effects of group membership.
The binary, one-shot model is extended to two-sided appeals in
`01_base_model.md`; all named core theorems state which version they use.

