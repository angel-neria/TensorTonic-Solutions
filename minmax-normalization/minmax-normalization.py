import numpy as np

def minmax_scale(X: list, axis: int = 0, eps: float = 1e-12) -> np.ndarray:
    """
    Returns a floating-point NumPy array matching the shape of X.
    """
    X_matriz = np.array(X)
    X_min = np.min(X, axis = axis, keepdims = True)
    X_max = np.max(X, axis = axis, keepdims = True)

    X_minmax = (X_matriz - X_min)/(X_max - X_min + eps)
    return X_minmax
    
    pass