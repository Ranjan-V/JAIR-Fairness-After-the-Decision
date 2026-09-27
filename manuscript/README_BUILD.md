# JAIR manuscript build

This directory uses the official JAIR author kit downloaded from
https://www.jair.org/index.php/jair/formatting on 2026-09-27.

Build with:

```text
pdflatex -interaction=nonstopmode -halt-on-error manuscript_jair.tex
biber manuscript_jair
pdflatex -interaction=nonstopmode -halt-on-error manuscript_jair.tex
pdflatex -interaction=nonstopmode -halt-on-error manuscript_jair.tex
```

The submission version uses `\documentclass[manuscript,screen,review]{jair}`.
Do not replace the official class or modify its margins, fonts, or spacing.
JAIR ordinary submissions include author information. The confirmed author,
affiliation, email, and corresponding-author metadata are present. DOI,
article number, publication date, and Associate Editor are not author-supplied
here; the source suppresses the sample DOI/editor/reference blocks and retains
only the official class-generated footer behavior.

The reproducibility checklist is included after the references and technical
appendix. Public availability and licensing answers reflect the verified
GitHub repository, MIT code license, and CC BY 4.0 artifact license. Remaining
`Partially` answers concern environment disclosure and the absence of a broad
hyperparameter search.
