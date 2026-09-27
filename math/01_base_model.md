# Base post-decision model

## 1. Structural sequence

The baseline sequence is

\[
(G,X,Y)\longrightarrow D_0\longrightarrow A\longrightarrow H\longrightarrow D_1.
\]

This diagram is temporal, not a causal DAG.  The joint law may contain
unobserved variables affecting several nodes.  The operational rules are:

1. (D_0=1\Rightarrow A=0\) in the one-sided model.
2. (A=0\Rightarrow D_1=D_0).
3. (A=1\Rightarrow D_0=0), and (H) determines whether the decision is
   reversed; for rate calculations only (D_1\) is required.

No assumption says that an individual observes (Y).  The two propensities
(\alpha_g^+,\alpha_g^-) are reduced-form conditional probabilities induced
by information, beliefs, costs, and behavior.  In particular,
(\alpha_g^+\ne\alpha_g^-) is compatible with imperfect knowledge of error.

## 2. Contestation kernel

Conditional on (Y=y,G=g), the transition from (D_0) to (D_1) is the
row-stochastic matrix

\[
K_g^y=
\begin{pmatrix}
1-\kappa_g^y&\kappa_g^y\\
0&1
\end{pmatrix},
\]

where rows index (D_0=0,1) and columns index (D_1=0,1).  If
(p_g^y=(P(D_0=0\mid y,g),P(D_0=1\mid y,g))), then
(p_g^{y\prime}=p_g^yK_g^y).  A single label-independent (K_g) exists only
when (\kappa_g^+=\kappa_g^-); forcing that restriction would erase the
distinction between correction and false reversal.

For a stacked vector (p_g=(p_g^0,p_g^1)), define the block-diagonal operator
(K_g=\operatorname{diag}(K_g^0,K_g^1)).  Then (p'_g=p_gK_g) without any
label-independence assumption.

## 3. General finite-state invariance principle

**Theorem 1 (linear operator preservation criterion).**  Let (V) be a
finite-dimensional vector space containing the signed perturbations of the
probability model, let (T_K:V\to V) be the linear map induced by a fixed
collection of stochastic kernels, and let (L:V\to W) encode a homogeneous
linear fairness constraint.  The following are equivalent:

1. (Lv=0) implies (LT_Kv=0) for every (v\in V);
2. (\ker L\subseteq\ker(LT_K));
3. there is a linear map (M:\operatorname{im}L\to W) such that
   (LT_K=ML) on (V).

*Proof.* Conditions 1 and 2 are the same statement.  If condition 2 holds,
define (M(Lv)=LT_Kv).  If (Lv=Lw), then (v-w\in\ker L), so condition 2 gives
(LT_Kv=LT_Kw); hence (M) is well-defined and linear.  Conversely,
(LT_K=ML) implies (LT_Kv=0) whenever (Lv=0).  ∎

To apply the theorem only to probability vectors, take (V) to be the linear
space of feasible signed perturbations (the span of differences of admissible
probability vectors).  The probability-domain statement is equivalent only
when the feasible fair distributions have enough relative-interior variation
to span (\ker L\cap V).  Affine constraints, including normalization when it
is explicitly represented, must be homogenized by adding a constant
coordinate.  This qualification prevents an invalid inference from a thin or
boundary-only probability domain to the whole algebraic kernel.

This theorem is reusable but deliberately modest: it characterizes universal
preservation on the declared perturbation space by a *fixed* operator.  It does not imply that arbitrary
group-specific kernels preserve fairness, nor does it cover demographic
parity unless base-rate weighting is included in (L).

## 4. Two-sided extension

If favorable decisions can also be challenged, define

\[
q_g^y=P(D_1=0\mid D_0=1,Y=y,G=g).
\]

Then

\[
K_g^y=\begin{pmatrix}1-\kappa_g^y&\kappa_g^y\\q_g^y&1-q_g^y\end{pmatrix}.
\]

All operator results continue to hold.  The simple one-sided rate identities
do not: both (\kappa) and (q) enter.  This extension is retained for scope,
but the core results use one-sided appeals because it isolates selective access
to correction and admits transparent necessary-and-sufficient conditions.
