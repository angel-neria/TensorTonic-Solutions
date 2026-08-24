import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    matriz = np.array(A) #matriz de dimensión (m,n)
    m = matriz.shape[0]
    n = matriz.shape[1]

    matriz_transpuesta = np.ndarray((n, m)) #matriz de dimensión (n,m)
    for i in range(n):
        for j in range(m):
            matriz_transpuesta[i][j] = matriz[j][i]
    
    return matriz_transpuesta
    pass
