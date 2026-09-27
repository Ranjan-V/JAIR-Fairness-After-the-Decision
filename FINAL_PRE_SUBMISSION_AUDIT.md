# Final pre-submission audit

Date: 2026-09-27

## 1. Decision

**SUBMISSION_BLOCKERS_REMAIN**

The scientific manuscript is revised and auditable, but author metadata,
author declarations, license choices, and a permanent artifact repository are
not authoritatively available and cannot be invented.

## 2. Scope observed

No experiment, model fit, simulation, bootstrap, dataset download, literature
search, or Kaggle job was run. Only existing validated outputs were analyzed;
source, documentation, bibliography, figure-generation code, and LaTeX were
revised.

## 3. Title and framing

The title is now *Fairness After the Decision: Group Fairness Under Selective
Human Contestation*. Claims center on a claimant-initiated correction channel,
not a new fairness metric.

## 4. Abstract

The abstract uses the JAIR template's Background, Objectives, Methods, Results,
and Conclusions fields. Adult and German Credit qualifications are explicit.

## 5. Novelty positioning

The supplied external novelty audit was incorporated. No independent
literature verification is claimed. Generic novelty claims for contestability,
procedural fairness, costs, selective labels, partial identification, auditing,
KKT, and knapsack were removed or expressly disclaimed.

## 6. Related work

The section now covers contestability/correctability, procedural fairness,
machine-assisted human decisions, relative decision-set fairness, recourse and
appeal costs, and selective labels/partial identification. It explicitly
distinguishes the six required 2026 works.

## 7. Theoretical claims

The headline claims are limited to exact post-contestation fairness
transformation and preservation, signed disparity dynamics, endogenous-access
consequences, appeal-log-specific sharp bounds, and assistance within the same
mechanism. The prior proof audit remains PASS WITH CORRECTIONS.

## 8. Empirical claims

E6 remains PARTIAL PASS. Adult resolves 12/12 signed directions and 12/12
absolute-gap increases. German Credit resolves 7/12 signed directions, 0/12
absolute-gap increases, and 0/4 random-forest signed directions. No result was
changed or hidden.

## 9. Figure 5

Figure 5 was regenerated only from the audited paired-summary CSV. It shows
signed pre/post change and 95% paired intervals in separate Adult and German
Credit panels, with shapes and grayscale styling that do not rely on color.
The absolute-gap result is stated in its caption and table.

## 10. Dataset and protocol record

A compact data card now records sources/licenses, raw and prepared counts,
targets, group mappings, feature exclusion, missing-value treatment, encoding,
scaling, split seeds, validation calibration, models, regimes, correction
parameters, paired seeds, and empirical versus semisynthetic quantities.

## 11. Reproducibility

The manuscript records the audited Kaggle run and SHA-256, 820/820 validated
files, and the clean-environment 220/220 numerical reproduction at tolerance
1e-6 with maximum difference 5.39e-08. It does not claim byte equality or
independent replication.

## 12. JAIR metadata

Anonymous mode and invented publication metadata were removed. The source has
one obvious author insertion block. The official class may still render its
own submission defaults; no volume, DOI, publication date, article number, or
Associate Editor was supplied by this revision.

## 13. Checklist

Preprocessing/splitting and implementation-detail items are now truthfully
`Yes` because the data card is complete. License and permanent-repository items
remain unresolved and were not upgraded.

## 14. Portal material

Draft answers use the two supplied 2026 JAIR papers as the closest primary
comparators. The prior-publication answer is marked
AUTHOR_CONFIRMATION_REQUIRED.

## 15. Packaging

The final versioned package contains manuscript source, bibliography, class
support files, figures, checklist, final PDF, portal responses, and audit and
decision documents. It excludes caches, environments, build debris, and large
third-party data. The compiled PDF is 17 pages, produced with no matched LaTeX
warnings, undefined references, or overfull boxes, and has SHA-256
`0E7E42D98D7A7FB13C3FE9E666D532A11362300128C5F228A11BCE9F49267658`.
Every rendered page was visually inspected. The deliverables are
`output/pdf/fairness_after_decision_JAIR_presubmission.pdf` and
`output/JAIR_final_presubmission_package.zip`.

## 16. Required author actions

Before submission, authors must (1) insert and verify complete author metadata,
(2) confirm prior-publication/concurrent-review and any funding/conflict
declarations, (3) select licenses and add notices, and (4) select and complete
a permanent artifact deposit, then update its DOI and availability statement.
