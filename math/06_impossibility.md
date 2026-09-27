# A conditional impossibility result

## Theorem 8 (group-blind policy impossibility)

Consider two groups under the one-sided model.  Assume:

1. (TPR_A=TPR_B=t<1) initially;
2. assistance is group-blind: (u_A=u_B=u\in U);
3. perceived value is the same deterministic (v) in the false-denial
   stratum;
4. review success is common and positive: (\rho_A^+=\rho_B^+=\rho>0);
5. for every feasible (u\in U),
   (F_A^+(v+u)<F_B^+(v+u)).

Then no feasible group-blind assistance preserves post-contestation equal
opportunity.  In fact,

\[
TPR'_A-TPR'_B=(1-t)\rho[F_A^+(v+u)-F_B^+(v+u)]<0.
\]

*Proof.* Proposition 4 gives the appeal probabilities; Theorem 7 gives strict
inequality of effective transitions; Theorem 2 converts it into strict final
TPR inequality. ∎

This is not an unconditional incompatibility among initial fairness,
procedural symmetry, and final fairness.  It is a pointwise impossibility over
a specified feasible policy set whose operative thresholds remain in a region
of strict cost-CDF order.

## Corollary 4 (why bounded assistance matters)

If (U=[0,\bar u]) and the strict CDF order holds on
([v,v+\bar u]), Theorem 8 applies.  If unbounded assistance makes both CDFs
equal one at a finite saturation threshold (bounded costs), universal appeal
can restore equality, so the impossibility disappears.

## Assumption audit

- If (t=1), there are no false denials to correct and equality is automatic.
- If (\rho=0), appeals do not affect final decisions.
- If CDFs meet at an operative threshold, that group-blind policy preserves
  equal opportunity despite unequal distributions elsewhere.
- If review qualities differ, unequal appeal rates can be exactly offset by
  unequal (\rho_g^+).
- If group-specific assistance is allowed, thresholds may be chosen to match
  (\rho_AF_A(v_A+u_A)=\rho_BF_B(v_B+u_B)), when the ranges overlap.
- If initial TPRs differ, appeals may repair rather than destroy equality.

These are counterexamples to stronger versions, not technical nuisances.

