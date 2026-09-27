# Model interpretation

The model separates three mechanisms that are often conflated:

- initial prediction quality, represented by the group confusion matrix;
- access and self-selection, represented by (\alpha_g^y);
- review behavior conditional on entry, represented by (\rho_g^y).

Only their product changes final confusion rates, but policy interpretation
requires retaining the factors.  A low correction transition can arise from
high barriers, pessimistic beliefs, weak review, or combinations of them.

The one-sided model represents institutions where only adverse decisions are
meaningfully challenged.  It is analytically useful rather than universal.
The two-sided kernel in `math/01_base_model.md` covers challenges to favorable
decisions and shows precisely which simple formulas cease to hold.

Fairness of (D_0) is a property of the classifier output.  Fairness of (D_1)
is a property of the full institution, including who enters review and what
review does.  The latter is the primary estimand.

