# JAIR pre-submission checklist

Prepared: 2026-09-27

## Completed

- Official post-spring-2025 JAIR `jair.cls`/ACM-based format used.
- Ordinary review mode enabled; confirmed author metadata and correspondence
  details are inserted.
- Seventeen-page PDF compiles with no LaTeX errors, undefined references,
  overfull boxes, or missing figure descriptions.
- Complete technical appendix included.
- Official JAIR reproducibility checklist included and answered honestly.
- Adult and German Credit dataset citations and CC BY 4.0 status added.
- Proof audit, manuscript consistency audit, literature audit, and clean
  reproducibility audit completed.
- Color figures were visually inspected; legends and geometric marks carry
  meaning in addition to color.

## Author must complete before upload

- Optionally provide ORCID identifiers; none were supplied or invented.
- Confirm originality, prior publication, and concurrent-review status.
- Select a code and generated-artifact license.
- Designate a permanent artifact repository or remove any promise
  that code/data accompanies the submission.
- Arrange an independent human proofread.
- Confirm acknowledgments, funding, and conflict declarations.
- Paste the three submission-question answers below into the JAIR system after
  author review.

## Submission question 1: importance and use (under 150 words)

This work shows that fairness measured at an algorithm's initial decision need
not survive a later, self-selected human appeal process. It gives exact
conditions for preserving equal opportunity, false-positive parity, equalized
odds, and demographic parity; explains how heterogeneous appeal costs defeat
formally symmetric policies; derives constrained assistance rules; and proves
what ordinary appeal logs cannot identify without representative audits. The
results are useful to researchers and institutions designing or auditing
human--AI decision systems in lending, benefits, hiring, and related settings.
They identify which access and review-quality quantities must be measured,
when fairness can worsen despite improved accuracy, and how to target audits
or assistance. Synthetic experiments verify the formal results, while 600
semisynthetic Adult/German Credit runs delimit the empirical claim rather than
presenting simulated appeal behavior as institutional evidence.

## Submission question 2: closest prior JAIR papers and distinction (under 150 words)

Yu, Xi, and Shetty, "Differential Parity: Relative Fairness Between Two Sets
of Decisions" (JAIR 86, 2026), study a relative-fairness metric comparing
decision sets, including human/model comparisons and bridge estimation. Wang,
Huang, Tang, and Yao, "Procedural Fairness in Machine Learning" (JAIR 85,
2026), formalize fairness of the model decision process using feature
attributions. This submission proposes neither another relative-fairness
metric nor a model-process criterion. It specifies a claimant-initiated
transition from an adverse initial decision through selective appeal and human
review to a final decision. It derives how this mechanism transforms standard
group-fairness quantities, when formally symmetric policies fail under
heterogeneous participation, what final error disparities appeal logs identify,
and how assistance can be allocated. It makes no generic novelty claim for
appeal costs, procedural fairness, selective labels, or partial identification.

## Submission question 3: prior publication/review status

**AUTHOR_CONFIRMATION_REQUIRED.** Complete this only after checking JAIR's
disclosure rules and all substantially overlapping versions.
