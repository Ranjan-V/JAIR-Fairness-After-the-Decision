# Non-preservation and disparity dynamics

## Minimal counterexample

Let two groups have (TPR_A=TPR_B=1/2), (\kappa_A^+=1), and
(\kappa_B^+=0).  Then (TPR'_A=1) and (TPR'_B=1/2).  Thus an initially
equal-opportunity classifier need not yield a final equal-opportunity system.
Neither reviewer error nor unequal initial prediction is required.

## Theorem 5 (exact signed-gap dynamics)

For arbitrary initial TPRs (t_A,t_B),

\[
d'=d+(1-t_A)\kappa_A^+-(1-t_B)\kappa_B^+.
\tag{1}
\]

Let (c=(1-t_A)\kappa_A^+-(1-t_B)\kappa_B^+).  Then:

1. disparity increases iff (|d+c|>|d|), equivalently (c(2d+c)>0);
2. disparity decreases iff (c(2d+c)<0);
3. it is unchanged iff (c=0) or (c=-2d);
4. direction reverses iff (d(d+c)<0);
5. exact equality after appeal occurs iff (c=-d).

*Proof.* Equation (1) is Proposition 1 after subtraction.  Squaring the two
nonnegative absolute gaps yields
(|d+c|^2-|d|^2=c(2d+c)).  The remaining claims follow from signs. ∎

## Theorem 6 (tight bounds given initial rates)

For (a=1-t_A), (b=1-t_B), and unrestricted
(\kappa_A^+,\kappa_B^+\in[0,1]),

\[
d'\in[d-b,d+a]=[t_A-1,1-t_B].
\]

Consequently

\[
\min_{\kappa}|d'|=
\begin{cases}
0,&0\in[d-b,d+a],\\
\min\{|d-b|,|d+a|\},&\text{otherwise},
\end{cases}
\]

and

\[
\max_{\kappa}|d'|=\max\{|d-b|,|d+a|\}.
\]

All bounds are attained at endpoints or at a feasible solution of (d'=0).

*Proof.* The correction term (a\kappa_A-b\kappa_B) ranges over the full
interval ([-b,a]) by continuity, with extrema at corners.  Distance of that
interval shifted by (d) from zero gives the formulas. ∎

## Corollary 3 (initially fair case)

If (t_A=t_B=t), then

\[
\Delta_{post}=(1-t)|\kappa_A^+-\kappa_B^+|,
\qquad 0\le\Delta_{post}\le1-t,
\]

and the upper bound is tight.  This is the exact amplification from a zero
pre-gap; calling it merely an upper bound would lose information.

## FPR analogue

Every statement above holds after replacing (t_g,\kappa_g^+) by
(f_g,\kappa_g^-).  For equalized odds, the maximum of the absolute TPR and
FPR gaps is controlled by the larger of the two corresponding exact terms.

