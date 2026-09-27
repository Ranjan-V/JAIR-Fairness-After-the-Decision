# Fairness preservation

All exact statements first treat two groups; pairwise application covers a
finite collection of groups.

## Theorem 2 (equal-opportunity preservation)

If (t_A=t_B=t), then (t'_A=t'_B) if and only if

\[
(1-t)(\kappa_A^+-\kappa_B^+)=0.
\]

Consequently, if (t<1), preservation is equivalent to
(\kappa_A^+=\kappa_B^+); if (t=1), it holds for arbitrary correction
parameters.

*Proof.* Proposition 1 gives
(t'_A-t'_B=(1-t)(\kappa_A^+-\kappa_B^+)). ∎

## Theorem 3 (FPR-parity preservation)

If (f_A=f_B=f), then (f'_A=f'_B) if and only if

\[
(1-f)(\kappa_A^--\kappa_B^-)=0.
\]

For (f<1), preservation is equivalent to equality of (\kappa^-); for the
degenerate (f=1), it is automatic.

*Proof.* Identical to Theorem 2 using the FPR identity. ∎

## Corollary 2 (equalized odds)

Suppose (t_A=t_B=t) and (f_A=f_B=f).  Post-contestation equalized odds
holds exactly when

\[
(1-t)(\kappa_A^+-\kappa_B^+)=0,
\qquad
(1-f)(\kappa_A^--\kappa_B^-)=0.
\]

If (t<1) and (f<1), both effective transitions must be equal across groups.

## Theorem 4 (demographic-parity preservation)

Assume initial demographic parity (r_A=r_B).  It is preserved exactly when

\[
\pi_AFNR_A\kappa_A^+ +(1-\pi_A)TNR_A\kappa_A^-
=\pi_BFNR_B\kappa_B^+ +(1-\pi_B)TNR_B\kappa_B^-.
\tag{DP}
\]

*Proof.* Subtract the two identities in Corollary 1 and use (r_A-r_B=0). ∎

Equality of both (\kappa) values is generally neither sufficient nor
necessary for (DP).  It is sufficient only under additional equality of the
weighted adverse masses, or when the two common transition values happen to
solve (DP).  Different base rates can therefore make demographic parity react
differently from equalized odds.

## Proposition 3 (universal preservation within the one-sided family)

Fix a common initial (t<1).  A pair of group-specific one-sided operators
preserves equal opportunity for every pair of group distributions having that
common TPR if and only if their (Y=1) adverse-to-positive transition
probabilities agree.  The analogous statement holds for FPR parity with
(f<1) and the (Y=0) transitions.  This is the concrete specialization of
Theorem 1.

## More than two groups

For equal opportunity at common (t<1), preservation across all groups is
equivalent to (\kappa_g^+) being constant over (g).  For FPR parity at
common (f<1), it is equivalent to constant (\kappa_g^-).  Demographic
parity requires equality across groups of the full weighted increment in
(DP), not componentwise transition equality.

