# JAIR Submission Artifact v1.0.0

This frozen release accompanies the manuscript *Fairness After the Decision:
Group Fairness Under Selective Human Contestation*, prepared for submission to
the Journal of Artificial Intelligence Research (JAIR). It does not imply
acceptance or publication.

The release includes source code, configurations, tests, mathematical and
theory documentation, manuscript sources, generated figures and tables,
reproducibility audits, and 820 standardized seed-level outputs (220
synthetic/theorem and 600 semisynthetic real-data outputs).

Empirically, Adult resolves all 12 predicted signed directions and all 12
absolute-gap increases. German Credit resolves 7 of 12 signed directions,
supports 0 of 12 broad absolute-gap increases, and random forest resolves 0 of
4 directions. E6 is therefore a partial pass rather than universal support.

A clean-environment run reproduced 220/220 synthetic/theorem outputs at
absolute and relative tolerance `1e-6`, with maximum absolute numerical
difference `5.39e-08`; this is not a byte-equality claim.

- Author-written code: MIT License.
- Author-generated research artifacts: CC BY 4.0.
- Third-party datasets: original source terms; raw/prepared UCI data are not
  redistributed.

