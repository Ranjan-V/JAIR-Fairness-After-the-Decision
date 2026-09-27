# Statistical estimation results

The statistical layer is intentionally small.  Its purpose is to support the
identification theory, not to add estimators whose assumptions are unavailable.

## Plug-in estimation under complete labels or random audit

When all confusion-cell and transition quantities are identified, empirical
cell proportions plugged into Proposition 1 are consistent by the law of
large numbers.  Under random audit, estimate the missing non-appellant positive
mass by (\hat z=n\hat q) and substitute it into (2).

## Proposition 9 (simultaneous finite-sample audit bounds)

For (K) groups with (M_g\ge1) audited non-appellants, define

\[
e_g=\sqrt{\frac{\log(2K/\delta)}{2M_g}}.
\]

With probability at least (1-\delta), every (q_g) lies in
([\hat q_g-e_g,\hat q_g+e_g]\cap[0,1]).  Propagating these intervals through
the monotone rate map and interval formulas in `09_partial_identification.md`
gives simultaneous confidence bounds for all group FNRs and pairwise gaps.

*Proof.* Apply Hoeffding within each group and a union bound.  Monotone
transformations preserve coverage of the image set. ∎

## Why IPW and doubly robust estimation are not core results

Inverse-propensity weighting requires positivity and correct identification or
estimation of appeal/audit propensities conditional on variables sufficient
for missing-at-random selection.  Ordinary self-selected appeals do not supply
that assumption.  Doubly robust estimators likewise require at least one of a
selection or outcome model to be correct.  The code includes optional IPW for
declared missing-at-random simulations, but it is not presented as solving the
non-identification problem.

## Bootstrap scope

Stratified nonparametric bootstrap intervals are suitable for regular,
non-boundary plug-in metrics.  For max gaps, rare cells, and partially
identified endpoints, percentile bootstrap behavior may be nonregular; the
finite-sample Hoeffding intervals and sensitivity bounds remain the primary
guaranteed procedures.

