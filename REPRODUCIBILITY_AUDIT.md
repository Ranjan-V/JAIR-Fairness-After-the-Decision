# Clean reproducibility audit

Audit date: 2026-09-27  
Archived Kaggle run: `352782151`  
Decision: **SCIENTIFIC REPRODUCIBILITY PASS**

## Immutable input

The downloaded Kaggle archive was verified before extraction. SHA-256:
`AE30CA19BF912DB8FEB1BE33E263C994F73ED3C2556E6EFF6D6EB69747BCBF1A`.
The extracted copy under `artifacts/kaggle_run_352782151_2026-09-26/` was
treated as read-only.

## Clean environment

A new virtual environment at `tmp/repro_env_20260926` was populated solely
from `code/requirements.txt`. Resolved principal versions were Python 3.11,
NumPy 2.4.6, pandas 2.3.3, SciPy 1.17.1, scikit-learn 1.9.1, Matplotlib
3.11.2, statsmodels 0.15.0, PyYAML 6.0.3, and pytest 8.4.2.

Results:

- complete test suite: **42 passed**;
- proof-linked subset: **18 passed**;
- archived 820 standardized CSVs: **PASS**, 0 errors, 0 warnings;
- archived E6 factorial: **600/600 present**, summaries regenerated without
  retraining;
- fresh theorem/core/robustness rerun: **220/220 present**, validation PASS.

## Cross-platform comparison

Byte-for-byte equality was not expected and did not hold between Kaggle/Linux
and local/Windows. Line endings differ; EXP-09 serializes a few parameter
floats differently, changing serialization-only keys; and EXP-04/05 optimizer
outputs differ in final digits across scientific-library builds.

After parsing standardized content, ignoring only `parameter_json` and
`parameter_key`, and applying absolute and relative tolerances of `1e-6`, all
220 fresh files match their archived counterparts. Maximum absolute numeric
difference: `5.3896548557474944e-08`. This is a scientific reproducibility
pass, not a byte-reproducibility claim.

## Evidence files

- `artifacts/reproducibility_audit_2026-09-26/validation_report.json`
- `artifacts/reproducibility_audit_2026-09-26/e6/E6_PAIRED_ANALYSIS.md`
- `artifacts/reproducibility_audit_2026-09-26/synthetic_validation_report.json`
- `artifacts/reproducibility_audit_2026-09-26/synthetic_content_comparison.json`
- `artifacts/reproducibility_audit_2026-09-26/synthetic_scientific_comparison.json`

No new Kaggle experiment and no new E6 model fit was run during this audit.
