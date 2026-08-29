import numpy as np

def zscore_standardize(X: list, axis: int = 0, eps: float = 1e-12) -> np.ndarray:
    """
    Returns population Z-scores as a NumPy array matching the shape of X.
    """
    X_est = np.array(X)
    X_mean = np.mean(X, axis = axis, keepdims = True)
    X_std = np.std(X, axis = axis, keepdims = True)

    X_est = (X_est - X_mean)/np.where(X_std == 0, eps, X_std)
    return X_est
    pass