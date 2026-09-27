"""Linear-operator utilities corresponding to Theorem 1."""

from __future__ import annotations

import numpy as np


def preserves_linear_constraint(L: np.ndarray, T: np.ndarray, atol: float = 1e-10) -> bool:
    """Numerically test ker(L) subset ker(LT) via an SVD null-space basis.

    This is a diagnostic implementation, not a floating-point proof.
    """
    L = np.asarray(L, dtype=float)
    T = np.asarray(T, dtype=float)
    _, singular, vh = np.linalg.svd(L, full_matrices=True)
    rank = int(np.sum(singular > atol))
    null_basis = vh[rank:].T
    return bool(np.allclose(L @ T @ null_basis, 0.0, atol=atol, rtol=0.0))

