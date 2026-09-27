# Assumptions and scope

## Substantive assumptions

- A final institutional action (D_1) follows an initial AI decision (D_0).
- Appeal is individual-initiated and may be endogenous.
- Group and outcome definitions are fixed before analysis.
- Review behavior is stable within the modeled policy environment.
- Random audits, when invoked, are representative and reveal valid labels.

## Mathematical conveniences

- Binary decisions and labels.
- One-shot appeal without queues, learning, or repeated interaction.
- Adverse-only appeal in core closed forms.
- Finite groups and continuous assistance in the main optimizer.
- Deterministic perceived value for the cleanest cost-CDF theorem.

The kernel formulation relaxes binary/one-sided structure, but the detailed
fairness identities must then be re-derived.  Random perceived values are
already covered by conditional integration.

## Out of scope

The theory does not model a strategic institution, endogenous classifier
retraining, peer effects, legal entitlement, causal effects of protected-group
membership, or welfare comparisons across incommensurable outcomes.  It does
not assume people know whether the initial decision is wrong.

## Validity threats

Cost distributions conditional on latent error are difficult to estimate;
review outcomes may be biased proxies for truth; protected groups may be
multidimensional; repeated appeals may violate the one-shot kernel; assistance
may alter perceived benefit or reviewer behavior rather than cost alone.

