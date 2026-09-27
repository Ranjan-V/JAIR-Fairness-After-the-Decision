# Counterexample ledger

Each entry records a tempting stronger claim that is false.  Rates are exact
population probabilities; all unspecified parameters may be chosen identically
across groups.

## CE-1: initial equal opportunity is not preserved

- Assumptions retained: one-sided appeal, valid probabilities.
- Construction: (t_A=t_B=1/2), (\kappa_A^+=1), (\kappa_B^+=0).
- Outcome: (t'_A=1,t'_B=1/2).
- Lesson: Theorem 2 needs equality of effective corrections when (t<1).

## CE-2: necessity fails for a perfect classifier

- Construction: (t_A=t_B=1), arbitrary unequal (\kappa_g^+).
- Outcome: both final TPRs remain one.
- Lesson: nondegeneracy (t<1) is necessary for equality of (\kappa^+) to be
  necessary.

## CE-3: equal correction transitions do not preserve demographic parity

- Construction: group (A): (\pi_A=0.8,t_A=0.5,f_A=0); group (B):
  (\pi_B=0.2,t_B=1,f_B=0.25).  Both initial positive rates equal (0.4).
  Let (\kappa_A^+=\kappa_B^+=0.5) and (\kappa_A^-=\kappa_B^-=0).
- Outcome: increments are (0.2) and (0), so final rates are (0.6) and
  (0.4).
- Lesson: Theorem 4 requires equality of weighted appealable mass.

## CE-4: equal effective transitions are not necessary for demographic parity

- Construction: use equal base rates (1/2), initial (t=f=1/2) in both
  groups.  Choose (\kappa_A^+=1,\kappa_A^-=0) and
  (\kappa_B^+=0,\kappa_B^-=1).
- Outcome: each group receives increment (1/4); demographic parity holds
  despite componentwise inequality.

## CE-5: formal symmetry is not effective equality

- Construction: common (v=u=0), common (\rho=1), costs
  (C_A\sim Uniform[0,2]), (C_B\sim Uniform[0,1]), evaluated at a common
  threshold (v+u=1/2).
- Outcome: (\kappa_A^+=1/4), (\kappa_B^+=1/2).

## CE-6: unequal distributions need not defeat a group-blind policy

- Construction: two distinct crossing cost CDFs with
  (F_A(c_0)=F_B(c_0)=1/2); choose (v+u=c_0) and common review quality.
- Outcome: effective corrections agree at the operative threshold.
- Lesson: global distributional inequality is weaker than the pointwise strict
  order in Theorem 8.

## CE-7: universal appeal breaks the bounded-policy impossibility

- Construction: both cost distributions have bounded support; choose common
  (u) above both maximum costs and common (\rho).
- Outcome: both appeal probabilities equal one, even if distributions differ.

## CE-8: group-dependent review can offset access

- Construction: (\alpha_A^+=1/2,\rho_A^+=1) and
  (\alpha_B^+=1,\rho_B^+=1/2).
- Outcome: both (\kappa^+=1/2).
- Lesson: appeal parity is not necessary; the product is the operative object.

## CE-9: perfect reviewer does not cure unequal access

- Construction: (\rho_A^+=\rho_B^+=1), (t_A=t_B=1/2),
  (\alpha_A^+=1,alpha_B^+=0).
- Outcome: final TPRs are (1) and (1/2).

## CE-10: zero or universal appeals are boundary cases

- Zero appeals: (\alpha_g^y=0) implies (D_1=D_0), preserving every
  initial fairness property.
- Universal appeals: (\alpha_g^y=1) equalizes access but not effective
  transitions if (\rho_g^y) differs.

## CE-11: appeals by correct negatives affect FPR

- Construction: initial (f=0), (\alpha^-\rho^-=0.2).
- Outcome: (FPR'=0.2), not zero.
- Lesson: ignoring (\alpha^-\) or assuming appellants know truth can falsely
  claim equalized-odds preservation.

## CE-12: a uniform subsidy need not monotonically close the access gap

- Construction: crossing densities can satisfy (F_A(c)<F_B(c)) over a
  region while (f_A(c)-f_B(c)) changes sign.
- Outcome: the level gap retains its sign but its magnitude first grows and
  then shrinks.
- Lesson: first-order stochastic dominance does not order density slopes.

## CE-13: marginal water-filling does not universally equalize risk

- Construction: (R_A(u)=0.9-0.1u), (R_B(u)=0.2-0.1u), unit costs and a
  small budget.  In the welfare objective both marginal gains are identical,
  so any allocation is optimal; residual risks need not be equal.
- Lesson: Theorem 11 equalizes marginal return only under its interior KKT
  conditions, not levels.

## CE-14: greedy ratio is not optimal for indivisible assistance

- Construction: budget (50), items ((cost,value)=(10,60),(20,100),(30,120)).
  Ratio-greedy chooses the first two for value (160); the last two yield
  (220).

## CE-15: identical appeal logs hide different fairness

- Construction: Theorem 13 with (a=p=1/2), comparing (q=0) and (q=1).
- Outcome: identical observations; (FNR'=0) versus (2/3).

## CE-16: monotone selection stated verbally gives no numerical bound

- Construction: let an unobserved evidence score be constant.  Every value of
  non-appellant positive prevalence is compatible with a weakly monotone
  appeal rule.
- Lesson: score observability and a link to truth are needed.

## CE-17: no random-audit positivity

- Construction: (r=0).
- Outcome: the two worlds in Theorem 13 remain observationally equivalent.
- Lesson: Theorem 15 requires (r>0) and representative audit selection.

## CE-18: nonrandom audits do not identify

- Construction: auditors select non-appellants using an unobserved signal
  correlated with (Y).
- Outcome: audited label prevalence can differ arbitrarily from unaudited
  prevalence.

## CE-19: two-sided appeals invalidate one-sided identities

- Construction: (t=1, q^1=1/2,\kappa^+=0).
- Outcome: (TPR'=1/2), whereas the one-sided formula would give one.

## CE-20: unequal base rates are not themselves a preservation failure

- Construction: unequal (\pi_A,\pi_B), but zero appeals.
- Outcome: any initially satisfied fairness constraint is unchanged.
- Lesson: base rates enter demographic parity through weighted increments;
  their inequality alone proves nothing.

