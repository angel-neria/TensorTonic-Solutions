import numpy as np

def covariance_matrix(X: list) -> np.ndarray:
    """
    Returns the covariance matrix as a NumPy array.
    """
    X_matriz = np.array(X)
    medias = np.mean(X, axis = 0)

    X_centrada = X_matriz - medias

    X_covarianza = np.matmul(np.matrix.transpose(X_centrada), X_centrada)*(1/(X_matriz.shape[0]-1))
    return X_covarianza
    pass