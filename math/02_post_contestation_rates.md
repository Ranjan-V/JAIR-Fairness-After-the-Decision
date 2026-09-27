# Exact post-contestation rates

## Proposition 1 (confusion-rate transformation)

In the one-sided model, for every group with defined conditional rates,

\[
\begin{aligned}
TPR'_g&=TPR_g+FNR_g\kappa_g^+, &
FNR'_g&=FNR_g(1-\kappa_g^+),\\
FPR'_g&=FPR_g+TNR_g\kappa_g^-, &
TNR'_g&=TNR_g(1-\kappa_g^-).
\end{aligned}
\]

*Proof.* Conditional on (Y=1,G=g), a final positive is either an initial
positive, or an initial negative followed by appeal and reversal.  These
events are disjoint.  The chain rule gives

\[
P(D_0=0,A=1,D_1=1\mid Y=1,g)
=FNR_g\alpha_g^+\rho_g^+=FNR_g\kappa_g^+.
\]

This proves the TPR identity; complementation proves FNR.  Replacing (Y=1)
by (Y=0) gives the FPR identity, and complementation gives TNR.  No
conditional independence assumption is used.  ∎

## Corollary 1 (positive-decision rate)

Let (r_g=P(D_0=1\mid G=g)=\pi_gt_g+(1-\pi_g)f_g).  Then

\[
\begin{aligned}
r'_g
&=\pi_g[t_g+(1-t_g)\kappa_g^+]
 +(1-\pi_g)[f_g+(1-f_g)\kappa_g^-]\\
&=r_g+\pi_gFNR_g\kappa_g^+
 +(1-\pi_g)TNR_g\kappa_g^-.
\end{aligned}
\]

Thus appeals weakly increase the favorable-decision rate in the one-sided
model, but the increase mixes beneficial corrections and erroneous reversals.

## Proposition 2 (two-sided transformation)

Under the extension in `01_base_model.md`,

\[
TPR'_g=t_g(1-q_g^1)+(1-t_g)\kappa_g^+,
\qquad
FPR'_g=f_g(1-q_g^0)+(1-f_g)\kappa_g^-.
\]

*Proof.* Partition on (D_0) and apply the two rows of (K_g^y). ∎

## Interpretation

(\alpha_g^y) measures entry into review among a latent stratum, (\rho_g^y)
measures reversal conditional on entry, and (\kappa_g^y) measures the net
transition from adverse to favorable.  Final confusion rates depend on
(\alpha) and (\rho) only through their product; ordinary final-decision
data cannot separate access from review quality without observing appeals.

