# Optional TPU decision

`TPU_EXTENSION_NOT_JUSTIFIED`

The core experiments use analytical sufficient statistics, NumPy/SciPy
optimization, pandas aggregation, and small scikit-learn models.  These are
CPU-first workloads.  Porting them to JAX/TPU would duplicate trusted logic,
add a second numerical stack, and provide little scientific value at the
configured sample sizes.

The stress profile already avoids materializing individual records for the
largest closed-form simulations.  If future research introduces a genuinely
large individual-level mechanism whose CPU implementation is demonstrably the
bottleneck, a separate JAX simulator may be proposed then.  The current paper
and replication pipeline do not depend on TPU, JAX, GPU, or neural hardware.

