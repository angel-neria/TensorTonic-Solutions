import numpy as np

def make_diagonal(v: list) -> np.ndarray:
    """
    Returns a NumPy array with shape (N, N).
    """
    n = len(v)
    matriz = np.zeros((n,n), dtype = float)

    for i in range(n):
        matriz[i][i] = v[i]
    return matriz
    pass