# Dataset preparation

No loader downloads data.  Place user-obtained, license-compliant CSV files in
this directory or pass an absolute path outside it.

- Adult: prepare a CSV with a binary label column (default `income`) and group
  column (default `sex`).
- German Credit: prepare a CSV with binary `credit_risk` and explicitly choose
  a documented group column; source schemas differ, so none is guessed.

## Reproducible UCI snapshot used for Gate E6

Retrieved 2026-09-25 from the official UCI Machine Learning Repository:

- Adult: DOI `10.24432/C5XW20`, CC BY 4.0,
  `https://archive.ics.uci.edu/static/public/2/adult.zip`, archive SHA-256
  `7537312DD56C2B98035880805CE99E68183A30EE468AA5329D6DF0FBB3CC21BB`.
- Statlog (German Credit Data): DOI `10.24432/C5NC77`, CC BY 4.0,
  `https://archive.ics.uci.edu/static/public/144/statlog+german+credit+data.zip`,
  archive SHA-256
  `E12D9D5DEF6845C0622634A1CD2AB87FA470668C4298F1EC52A4E403376A435B`.

Run `scripts/prepare_uci_realdata.py` to reproduce `uci/prepared/*.csv` from
the extracted official files. Adult combines the repository's train/test files
before the experiment performs a fresh stratified train/validation/test split.
German Credit maps UCI label 1 (good credit) to favorable outcome 1 and label 2
to 0. Its documented personal-status/sex codes are mapped to `Female` for A92
and A95 and `Male` for A91, A93, and A94; the source field is then removed from
the predictive features. Prepared-file checksums and row counts are recorded in
`uci/prepared/provenance.json`.

These datasets contain no observed appeal behavior. All appeal/review variables
in the experiment are semisynthetic.
