# Fairness After the Decision:
# Group Fairness Under Selective Human Contestation

## Overview

This project studies how a self-selected human appeal or review process after
an AI decision can transform standard group-fairness properties. It separates
the fairness of the initial classifier from the fairness of the final decision
and analyzes the access, review-quality, identification, and resource-allocation
conditions connecting them.

## Authors

- Ranjan Veerabhadraswamy
- Ajith Jubilson Emerson — corresponding author

School of Computer Science and Engineering, Vellore Institute of Technology,
Andhra Pradesh, Amaravati, Andhra Pradesh 522241, India.

Correspondence: Ajith Jubilson Emerson, ajith.jubilson@vitap.ac.in.

## Paper

This repository accompanies *Fairness After the Decision: Group Fairness Under
Selective Human Contestation*, a manuscript prepared for submission to the
Journal of Artificial Intelligence Research (JAIR). It does not imply
acceptance or publication.

## Main contributions

- A post-decision contestation operator linking initial and final decisions.
- An exact characterization of when standard group-fairness properties are
  preserved by selective review.
- Signed-disparity dynamics that distinguish reinforcement, attenuation,
  crossing, and reversal.
- Endogenous access under heterogeneous appeal costs.
- Non-identification from ordinary appeal logs and sharp bounds under stated
  information restrictions.
- Budget-constrained analysis of appeal assistance.
- Synthetic and semisynthetic validation of the formal claims and their
  empirical limits.

## Repository contents

- `code/`: implementation, configurations, orchestration, aggregation, figure
  scripts, and tests.
- `math/` and `theory/`: theorem statements, proofs, assumptions, and scope.
- `kaggle/`: the audited CPU-oriented Kaggle workflow.
- `manuscript/`: JAIR LaTeX source, bibliography, required style files,
  figures, and submission checklist.
- `results/`: all 820 standardized seed-level outputs, compact aggregate
  summaries, manuscript tables, and run manifests from the validated study.
- `figures/`: publication figures generated from the validated outputs.

## Reproduction

The validated workflow is CPU-first. From the repository root:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
Set-Location code
$env:PYTHONPATH = (Get-Location).Path
pytest -q
python run_experiments.py --stage theorem --config configs/full.yaml --resume
python run_experiments.py --stage core --config configs/full.yaml --resume --n-jobs 2
python run_experiments.py --stage robustness --config configs/full.yaml --resume --n-jobs 2
python run_experiments.py --stage aggregate --config configs/full.yaml
python run_experiments.py --stage figures --config configs/full.yaml
```

On Linux or macOS, activate with `source .venv/bin/activate` and run
`export PYTHONPATH="$PWD"`. The semisynthetic real-data stage additionally
requires legally obtained and locally prepared Adult and German Credit files;
follow `code/data/README.md`, then use the portable configuration pattern in
`code/configs/uci_realdata_kaggle.yaml` or a local copy with explicit paths.
The exact audited Kaggle notebook sequence is documented in
`kaggle/README_KAGGLE.md`. These commands are provided for reproduction; this
release freeze did not rerun scientific experiments.

## Experimental status

For Adult, all 12 of 12 unequal-access cells resolve the predicted signed
direction and all 12 of 12 increase the absolute equal-opportunity gap. For
German Credit, 7 of 12 cells resolve the predicted signed direction, 0 of 12
support broad absolute-gap amplification, and random forest resolves 0 of 4.
The empirical evidence is therefore partial rather than universal, and the E6
gate is a **partial pass**.

## Reproducibility

The validated study comprised 220 synthetic/theorem runs and 600
semisynthetic real-data runs. A clean-environment reproduction regenerated all
220 synthetic/theorem outputs; every output matched the archived numerical
content at absolute and relative tolerance `1e-6`, with maximum absolute
difference `5.39e-08`. The repository retains all 820 standardized seed-level
outputs alongside aggregate summaries, tables, manifests, source code,
configurations, and manuscript sources. Compiled submission packages remain
outside version control.

## Data

Adult and German Credit originate from the UCI Machine Learning Repository.
Raw and prepared third-party data are deliberately not included here. Obtain
them from their official UCI dataset pages and follow the mappings and
preparation notes in `code/data/README.md`. The authors do not relicense these
datasets; their original source terms apply.

## Licenses

- Original source code: MIT License (`LICENSE`).
- Author-generated outputs, figures, tables, configurations, documentation,
  and reports: CC BY 4.0 (`ARTIFACT_LICENSE.md`).
- Third-party datasets and software: their original licenses.

## Citation

Citation metadata are provided in `CITATION.cff`. No archival DOI has been
assigned at this stage.

## Contact

Ajith Jubilson Emerson (corresponding author): ajith.jubilson@vitap.ac.in

