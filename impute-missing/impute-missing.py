import numpy as np

def impute_missing(X: list, strategy: str = "mean") -> np.ndarray:
    """
    Returns a NumPy array with the same shape as X.
    """
    #convertimos en matriz
    X_matriz = np.array(X)
    shape = X_matriz.shape #guardamos la forma original, en caso de ser necesario

    #si es un vector de R^n, entonces creamos una matriz n x 1
    if(X_matriz.ndim == 1):
        X_matriz = X_matriz.reshape(-1, 1)
    n, p = np.shape(X_matriz)

    #caso 1: imputación de media
    if(strategy == 'mean'):
        media = np.nanmean(X_matriz, axis = 0)
        media = np.where(np.isnan(media), 0, media)
        print(media)
        for columna in range(p):
            for fila in range(n):
                if(np.isnan(X_matriz[fila][columna])):
                    X_matriz[fila][columna] = media[columna]
                    
    #caso 2: imputación de la mediana
    elif(strategy == 'median'):
        mediana = np.nanmedian(X_matriz, axis = 0)
        mediana = np.where(np.isnan(mediana), 0, mediana)
        for columna in range(p):
            for fila in range(n):
                if(np.isnan(X_matriz[fila][columna])):
                    X_matriz[fila][columna] = mediana[columna]

    #regresamos a la forma original
    return X_matriz.reshape(shape)
    pass