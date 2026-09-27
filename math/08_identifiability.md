# Observational non-identifiability

## Observed-data model

Focus on the initially adverse stratum.  Appeal logs reveal (A), review
records and final decisions for appellants, and (in the strongest convenient
version) the true label (Y) for appellants.  They do not reveal (Y) for
non-appellants.  Giving the analyst appellant labels only strengthens the
negative result.

## Theorem 13 (appeal-log non-identifiability)

Without restrictions on selection into appeal, (FNR'_g) is not identified
from ordinary appeal logs, even when review is perfect and appellant labels
are observed.

*Proof by observational equivalence.*  Fix one group and let every case have
(D_0=0).  Fix (a\in(0,1)) and (p\in(0,1)).  In every latent world,
(P(A=1)=a), (P(Y=1\mid A=1)=p), and perfect review sets (D_1=Y) for
appellants; non-appellants retain (D_1=0).  Let
(q=P(Y=1\mid A=0)).  The entire observable law is the same for every
(q\in[0,1]), because (Y) is missing exactly when (A=0).  Yet

\[
FNR'(q)=\frac{(1-a)q}{ap+(1-a)q},
\]

which is strictly increasing in (q).  Taking two distinct values of (q)
produces identical observable laws and different final false-negative rates.
∎

## Corollary 5 (fairness disparity is not identified)

Apply the construction independently to two groups with the same observable
law and choose different latent (q_g).  Post-contestation equal-opportunity
disparity differs across observationally equivalent joint laws.  Moreover,
over a sequence with (a p\downarrow0), one world can have disparity zero and
another disparity arbitrarily close to one.  Exact disparity one is excluded
when the fixed observed appellant-positive mass (ap) is strictly positive.

## What is and is not learned

Appeal logs identify appeal frequency, reversal frequency among appellants,
and their product on the observed population.  They do not generally identify
the prevalence of erroneous denials among non-appellants.  Equal reversal
rates among appellants therefore do not imply equal residual error.  This is a
specific selection failure tied to the correction channel, though its formal
logic is a missing-data argument.

