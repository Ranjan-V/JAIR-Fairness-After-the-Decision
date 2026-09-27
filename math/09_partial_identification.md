# Partial identification and random audits

## 1. Sharp no-assumption bounds

Within group (g), normalize masses by (P(G=g)) and define

\[
s=P(D_0=1,Y=1\mid g),\quad
m=P(D_0=0,A=1,Y=1\mid g),\quad
n=P(D_0=0,A=0\mid g).
\]

Assume the mean successful-reversal probability among appealed positives,
(\rho), is known or identified from their outcomes.  Let the unknown positive
mass among adverse non-appellants be (z\in[0,n]).  Then

\[
FNR'(z)=\frac{m(1-\rho)+z}{s+m+z}.
\tag{2}
\]

## Theorem 14 (sharp bounds)

If (s+m>0) and (s+\rho m>0), (2) is increasing in (z), so the sharp identified set is

\[
\left[
\frac{m(1-\rho)}{s+m},
\frac{m(1-\rho)+n}{s+m+n}
\right].
\]

If (s+m>0) but (s+\rho m=0), (2) equals one for every (z\in[0,n]).
If (s=m=0<n), the rate is undefined at (z=0) and equals one for every
(z>0), so its identified set over laws in which the positive stratum exists is
the singleton ({1}).  If (s=m=n=0), the FNR is undefined under every
compatible law.  The bounds are sharp because every feasible (z\in[0,n]) can be
realized by assigning that positive mass within the unobserved stratum without
altering the observed law.

*Proof.* Differentiate (2):

\[
\frac{dFNR'}{dz}=\frac{s+\rho m}{(s+m+z)^2}\ge0.
\]

Endpoint substitution gives the bounds, and the construction gives sharpness.
∎

Pairwise disparity has a sharp interval obtained by interval arithmetic:
if group rates lie in ([L_A,U_A]), ([L_B,U_B]), then the signed gap lies in
([L_A-U_B,U_A-L_B]).  The absolute-gap identified set has lower endpoint
zero when the intervals overlap and otherwise their distance, and upper
endpoint (\max(|L_A-U_B|,|U_A-L_B|)).

## Proposition 7 (bounded error-stratum appeal propensity)

Assume (m>0), so the false-denial appeal propensity is defined and positive.
The true appeal propensity among false denials is
(\alpha=m/(m+z)).  If (0<\underline\alpha\le\alpha\le
\overline\alpha\le1), then

\[
z\in\left[
m\frac{1-\overline\alpha}{\overline\alpha},
m\frac{1-\underline\alpha}{\underline\alpha}
\right]\cap[0,n].
\]

Substitution of the two endpoints into (2) yields sharp bounds under exactly
this restriction.  Empty intersection falsifies the assumed propensity range.
When (m=0), the displayed inversion is not valid: a positive lower propensity
is incompatible with any positive false-denial mass, while a zero total
false-denial mass leaves the conditional propensity undefined.

## Monotone selection

An ordering such as “stronger evidence of error weakly increases appeal” does
not alone bound (z) unless evidence is observed and linked to (Y).  With an
observed score (S), a specified monotone response, and calibration bounds
for (P(Y=1\mid S,D_0=0,g)), one can integrate score-specific bounds.  A bare
verbal monotonicity assumption is therefore recorded as insufficient rather
than promoted to a theorem.

## Theorem 15 (random audits identify the missing mass)

Suppose each adverse non-appellant is independently audited with probability
(r>0), audit selection is independent of (Y) conditional on the recorded
stratum, and audit reveals (Y) without error.  Then
(q=P(Y=1\mid D_0=0,A=0,g)), hence (z=nq), is identified from the audited
law.  Consequently (2) and the post-contestation disparity are identified.

*Proof.* Conditional independence gives
(P(Y=1\mid audit=1,D_0=0,A=0,g)=q).  All other terms in (2) are observed. ∎

Identification is a population property: any positive (r) suffices.  Precision
does depend strongly on (r).

## Proposition 8 (finite-audit uncertainty contraction)

Let (M_g\ge1) non-appellants in group (g) actually be audited and
(\hat q_g) be their positive fraction.  Hoeffding's inequality gives, with
probability at least (1-\delta),

\[
|\hat q_g-q_g|\le
e_g=\sqrt{\frac{\log(2/\delta)}{2M_g}}.
\]

Intersecting ([\hat q_g-e_g,\hat q_g+e_g]) with ([0,1]), multiplying by
(n_g), and applying monotone map (2) gives a valid confidence interval.
Its width is at most

\[
\frac{n_g(s_g+\rho_gm_g)}{(s_g+m_g)^2}\,2e_g,
\]

when (s_g+m_g>0).  Since (M_g\) is approximately (rN_g^0), the generic
rate is (O((rN_g^0)^{-1/2})).  This is a bound, not an equality; near-zero
denominators can make fairness estimation intrinsically unstable.
