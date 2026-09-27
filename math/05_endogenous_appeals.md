# Endogenous appeals and contestation cost

## 1. Threshold behavior

Let perceived appeal value be (V_i=B_iS_i\ge0), private cost be (C_i\), and
group assistance be (u_g\ge0).  The individual appeals exactly when

\[
A_i=\mathbf1\{C_i\le V_i+u_g\}.
\]

Because true-label strata may have different signals or costs, all formulas
may be read conditional on (D_0=0,Y=y,G=g).

## Proposition 4 (appeal response)

If (V_i=v_g^y) is deterministic and the conditional cost CDF is (F_g^y),
then

\[
\alpha_g^y(u)=F_g^y(v_g^y+u).
\]

If (V) is random, then without independence

\[
\alpha_g^y(u)=E[F_{C\mid V,g,y}(V+u\mid V,G=g,Y=y,D_0=0)].
\]

Under conditional independence of (C) and (V) given the stratum this
reduces to (E[F_g^y(V+u)]).

*Proof.* Condition the threshold event first on the stratum and, in the random
case, on (V). ∎

## Proposition 5 (comparative statics)

Every (\alpha_g^y(u)) is nondecreasing and right-continuous in (u).  If the
conditional cost distribution has density (f_g^y) and regularity permits
differentiation under the expectation, then

\[
(\alpha_g^y)'(u)=E[f_{C\mid V,g,y}(V+u\mid V,g,y)]\ge0.
\]

It follows that (R_g(u)=FNR_g[1-\rho_g^+\alpha_g^+(u)]) is nonincreasing when
(\rho_g^+\ge0).  It is strictly decreasing only where the density and review
success are positive; strictness must not be assumed at atoms, gaps, or
saturated tails.

## Theorem 7 (procedural symmetry versus effective equality)

Suppose groups receive a common assistance (u), have common deterministic
perceived value (v), and common review success (\rho>0).  Then

\[
\kappa_A^+(u)-\kappa_B^+(u)
=\rho[F_A^+(v+u)-F_B^+(v+u)].
\]

Therefore, under the stated assumption (\rho>0), formal symmetry
(u_A=u_B) yields effective correction parity at that policy exactly when the
two CDFs coincide at the operative threshold.  If the positivity assumption
is relaxed to (\rho=0), parity is automatic because neither group receives a
successful correction.  If (F_A^+(c)<F_B^+(c)) throughout an interval containing
all operative thresholds, then (\kappa_A^+(u)<\kappa_B^+(u)) throughout the
corresponding assistance interval.

*Proof.* Substitute Proposition 4 into (\kappa=\rho\alpha). ∎

The CDF ordering (F_A<F_B) means costs in group (A) are strictly larger in
the first-order stochastic sense.  Equal policy inputs can therefore generate
unequal effective access.  Equal CDFs are sufficient but not necessary at a
single policy: crossing CDFs may coincide at the operative threshold.

## Observation: equal subsidy can widen or narrow a gap

For common review quality,

\[
\frac{d}{du}(\kappa_A^+-\kappa_B^+)
=\rho[f_A^+(v+u)-f_B^+(v+u)].
\]

Stochastic dominance alone signs the level difference, not its derivative.
Hence the claim that a uniform subsidy must monotonically reduce (or enlarge)
effective-access disparity is false without a density-difference condition.
