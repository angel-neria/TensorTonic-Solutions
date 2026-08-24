import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    matriz = np.array(A)
    filas = matriz.shape[0]
    columnas = matriz.shape[1]

    matriz_transpuesta = np.ndarray((columnas, filas))
    for i in range(columnas):
        for j in range(filas):
            matriz_transpuesta[i][j] = matriz[j][i]
    
    return matriz_transpuesta
    pass
