# Manuscript consistency audit

Audit date: 2026-09-27  
Decision: **PASS WITH QUALIFICATIONS**

| Manuscript claim | Formal support | Empirical support | Figure/table | Citation status | Disposition |
|---|---|---|---|---|---|
| Fixed contestation can change fairness | Proposition 1; Theorems 2--6 | EXP-01/02; E6 | Figures 1 and 7 | Related work cited | Retain |
| Equal formal assistance need not equalize access | Proposition 4; Theorems 7--8 | EXP-03 | Figure 2 | Contestability/recourse work cited | Retain with strict-CDF-order qualification |
| Allocation has a convex tractable regime | Theorems 9--11 | EXP-04/05 | Figure 3 | Standard tools not claimed novel | Retain; KKT sentence narrowed to differentiable convex separable, Slater, binding-budget, interior case |
| Exact target budget is available | Proposition 6 | Theorem-linked tests | Appendix | No priority claim | Retain with infeasibility boundary |
| Indivisible allocation contains knapsack | Theorem 12 | Exact algorithm tests | Appendix | Classical result acknowledged | Retain as weak NP-completeness only |
| Ordinary appeal logs do not identify final FNR | Theorems 13--14; Corollary 5 | EXP-06/07 | Figures 4--5 | Selective-label literature cited | Retain with zero-mass cases |
| Representative audits identify missing mass | Theorem 15; Propositions 8--9 | EXP-08 | Figure 5 | Supporting claim | Retain; nuisance uncertainty noted |
| Adult supports stable absolute EO-gap amplification | Theorem 5 special regime | 12/12 cells, paired CIs exclude zero | Table 1; Figure 7 | Dataset cited | Retain |
| German supports the signed mechanism | Theorem 5 | 7/12 cells; RF 0/4 | Table 1; Figure 7 | Dataset cited | Retain as qualified support |
| Unequal access universally amplifies absolute disparity | Not implied | German 0/12 absolute cells | Figure 7 | N/A | Rejected |
| Experiments observe real appeal behavior | None | Contestation is simulated | Design | N/A | Rejected; call semisynthetic |
| Integrated framework is first of its kind | Priority not established | N/A | N/A | Adjacent work exists | Rejected |

## Cross-reference checks

- Every formal claim in the index has a full statement and proof in
  `paper/technical_appendix.tex`.
- Every principal figure cited in text exists in `paper/figures/` and is
  generated from audited outputs.
- The E6 table matches the paired analysis: Adult 12/12 signed and absolute;
  German 7/12 signed and 0/12 absolute.
- Dataset citations and CC BY 4.0 status were added for Adult and German
  Credit.
- The reproducibility statement records the final run, interval, and hash.

## Remaining author-controlled items

The paper cannot truthfully be called submitted or publication-ready until
the authors supply identity/affiliations, prior-publication and simultaneous-
review declarations, a code/artifact license, a permanent public archive, and
an independent human proofread. These do not change the mathematical or
empirical gate decisions.
