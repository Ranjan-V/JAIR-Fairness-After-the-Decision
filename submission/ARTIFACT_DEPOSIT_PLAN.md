# Permanent artifact deposit plan

No upload was performed. Recommended workflow after the authors select a
repository is: (1) prepare a clean public source repository; (2) freeze a
versioned release; (3) archive that release in Zenodo or another
author-selected archival service; (4) obtain its DOI or permanent identifier;
and (5) insert that identifier in the manuscript and JAIR portal. The archived
release should contain:

- source code and tests;
- exact experiment and Kaggle configurations;
- standardized raw/seed-level generated outputs where licensing permits;
- aggregation, analysis, figure, and table generation scripts;
- dependency/environment files and build instructions;
- a top-level README with exact reproduction and validation commands;
- the proof and reproducibility audits and relevant checksums;
- table-generation scripts, in addition to aggregation and figure scripts.

Exclude credentials, private information, temporary environments and caches,
LaTeX build debris, and third-party datasets whose licenses do not permit
redistribution. Record checksums, repository DOI, release tag, and license
scope in the manuscript and portal only after the deposit is complete.
