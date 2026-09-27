# Fairness notions

Equal opportunity compares (P(D=1\mid Y=1,G=g)).  In the one-sided model it
is affected only by correction transitions (\kappa_g^+).  FPR parity compares
(P(D=1\mid Y=0,G=g)) and is affected only by false-reversal transitions
(\kappa_g^-).  Equalized odds requires both.

Demographic parity compares (P(D=1\mid G=g)) and mixes labels.  Its
post-contestation increment is

\[
\pi_gFNR_g\kappa_g^+ +(1-\pi_g)TNR_g\kappa_g^-.
\]

Therefore equal transitions across groups do not generally preserve
demographic parity: the amount and label composition of appealable adverse
mass also matter.  Conversely, unequal transitions can offset one another.

These are descriptive constraints, not a normative ranking.  Selecting a
fairness target requires context about harms, legal obligations, base rates,
and the meaning of labels.  The allocation code exposes alternative objectives
rather than silently choosing one.

